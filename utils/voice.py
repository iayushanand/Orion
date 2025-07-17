import whisper
model = whisper.load_model("tiny")


def speech_to_text(path_to_audio):
    result = model.transcribe("audio2.mp3")
    return result["text"] 