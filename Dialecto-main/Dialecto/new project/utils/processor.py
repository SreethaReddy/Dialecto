import os
import subprocess
import assemblyai as aai
from datetime import timedelta
from deep_translator import GoogleTranslator

aai.settings.api_key = "a00b1c97b4d14896ab21f61deb6d25bd"  # Move to config later

def process_video(input_path, language='hi', session_id=None):
    """Adapted version of your processing pipeline"""
    try:
        # 1. Extract audio
        audio_path = f"temp/audio_{session_id}.mp3"
        subprocess.run([
            "ffmpeg", "-i", input_path,
            "-q:a", "0", "-map", "a",
            audio_path, "-y"
        ], check=True)
        
        # 2. Generate subtitles
        srt_path = generate_translated_subtitles(audio_path, language, session_id)
        
        # 3. Embed subtitles
        output_filename = f"output_{session_id}.mp4"
        output_path = os.path.join("static", "outputs", output_filename)
        
        subprocess.run([
            "ffmpeg", "-i", input_path,
            "-vf", f"subtitles={srt_path}:force_style='Fontsize=24'",
            "-c:a", "copy", output_path, "-y"
        ], check=True)
        
        return output_path
        
    finally:
        # Cleanup temp files
        for f in [input_path, audio_path, srt_path]:
            if f and os.path.exists(f):
                os.remove(f)

def generate_translated_subtitles(audio_path, language, session_id):
    """Your existing subtitle generation code"""
    srt_path = f"temp/subs_{session_id}.srt"
    
    config = aai.TranscriptionConfig(speaker_labels=True, speakers_expected=2)
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(audio_path, config)
    
    if transcript.error:
        raise RuntimeError(transcript.error)
    
    with open(srt_path, "w", encoding="utf-8") as f:
        for i, utterance in enumerate(transcript.utterances, 1):
            translated = GoogleTranslator(source='auto', target=language).translate(utterance.text)
            f.write(
                f"{i}\n"
                f"{_format_time(utterance.start)} --> {_format_time(utterance.end)}\n"
                f"[Speaker {utterance.speaker}] {translated}\n\n"
            )
    
    return srt_path

def _format_time(ms):
    """Your existing time formatter"""
    td = timedelta(milliseconds=ms)
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02},{td.microseconds//1000:03}"