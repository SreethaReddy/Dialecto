import assemblyai as aai
from deep_translator import GoogleTranslator
from datetime import timedelta

aai.settings.api_key = "a00b1c97b4d14896ab21f61deb6d25bd"

def generate_subtitles(audio_path, language='hi'):
    """Generate translated subtitles"""
    try:
        # Transcribe with speaker diarization
        transcriber = aai.Transcriber()
        transcript = transcriber.transcribe(
            audio_path,
            config=aai.TranscriptionConfig(
                speaker_labels=True,
                speakers_expected=2
            )
        )
        
        if transcript.error:
            raise RuntimeError(transcript.error)
        
        # Generate SRT content
        srt_path = "subtitles.srt"
        with open(srt_path, "w", encoding="utf-8") as f:
            for i, utterance in enumerate(transcript.utterances, 1):
                # Translate text
                translated = GoogleTranslator(
                    source='auto', 
                    target=language
                ).translate(utterance.text)
                
                f.write(
                    f"{i}\n"
                    f"{_format_time(utterance.start)} --> {_format_time(utterance.end)}\n"
                    f"[Speaker {utterance.speaker}] {translated}\n\n"
                )
        
        return srt_path
        
    except Exception as e:
        raise RuntimeError(f"Subtitle generation failed: {str(e)}")

def _format_time(ms):
    """Convert milliseconds to SRT time format"""
    td = timedelta(milliseconds=ms)
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02},{td.microseconds//1000:03}"