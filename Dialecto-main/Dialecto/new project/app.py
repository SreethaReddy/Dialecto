import os
import subprocess
from flask import Flask, request, render_template, send_from_directory
import assemblyai as aai
from datetime import timedelta
from deep_translator import GoogleTranslator

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'static/processed'

aai.settings.api_key = "a00b1c97b4d14896ab21f61deb6d25bd"

def extract_audio(video_path, audio_output="extracted_audio.mp3"):
    command = ["ffmpeg", "-i", video_path, "-q:a", "0", "-map", "a", audio_output, "-y"]
    subprocess.run(command, check=True)
    return audio_output

def translate_text(text, target_lang='hi'):
    if target_lang == 'en':
        return text  
    try:
        return GoogleTranslator(source='auto', target=target_lang).translate(text)
    except Exception as e:
        print(f"Translation failed: {e}")
        return text

def generate_translated_subtitles(audio_path, output_srt="subtitles.srt", words_per_line=6, language='hi'):
    config = aai.TranscriptionConfig(speaker_labels=True, speakers_expected=2)
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(audio_path, config)

    if transcript.error:
        raise RuntimeError(f"Transcription failed: {transcript.error}")

    srt_content = []
    subtitle_index = 1

    for utterance in transcript.utterances:
        speaker = utterance.speaker
        words = utterance.words

        for i in range(0, len(words), words_per_line):
            chunk = words[i:i + words_per_line]
            start = chunk[0].start
            end = chunk[-1].end
            original_text = " ".join(word.text for word in chunk)
            
            
            translated_text = translate_text(original_text, language)
            speaker_label = f"Speaker {speaker}"

            srt_content.append(
                f"{subtitle_index}\n"
                f"{format_time(start)} --> {format_time(end)}\n"
                f"[{speaker_label}] {translated_text}\n"
            )
            subtitle_index += 1

    with open(output_srt, "w", encoding="utf-8") as f:
        f.write("\n".join(srt_content))

    return output_srt

def embed_subtitles(video_path, srt_path, output_video):
    command = [
        "ffmpeg", "-i", video_path,
        "-vf", f"subtitles={srt_path}:force_style='Fontsize=24'",
        "-c:a", "copy", output_video, "-y"
    ]
    subprocess.run(command, check=True)
    return output_video

def format_time(ms):
    td = timedelta(milliseconds=ms)
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02},{td.microseconds//1000:03}"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["video"]
        language = request.form.get("language", "hi")

        if file:
            filename = file.filename
            upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            video_filename = f"translated_{filename.rsplit('.', 1)[0]}.mp4"
            output_path = os.path.join(app.config['OUTPUT_FOLDER'], video_filename)
            file.save(upload_path)

            try:
                audio_path = extract_audio(upload_path)
                srt_path = generate_translated_subtitles(audio_path, language=language)
                embed_subtitles(upload_path, srt_path, output_path)
                os.remove(audio_path)
                return render_template("result.html", video_url=output_path, filename=video_filename)
            except Exception as e:
                return f"<h2>Error: {e}</h2>"

    return render_template("index.html")

@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(app.config["OUTPUT_FOLDER"], filename, as_attachment=True)

if __name__ == "__main__":
    os.makedirs("uploads", exist_ok=True)
    os.makedirs("static/processed", exist_ok=True)
    app.run(debug=True)