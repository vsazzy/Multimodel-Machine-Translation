from transformers import pipeline, M2M100ForConditionalGeneration, M2M100Tokenizer

def speech_to_translation(audio_path, src_lang="fr", tgt_lang="en"):
    # Step 1: Speech → Text
    asr = pipeline("automatic-speech-recognition", model="openai/whisper-small")
    asr_output = asr(audio_path)
    text = asr_output["text"]
    print(f"Detected ({src_lang}):", text)

    # Step 2: Text → Text translation
    model_name = "facebook/m2m100_418M"
    tokenizer = M2M100Tokenizer.from_pretrained(model_name)
    model = M2M100ForConditionalGeneration.from_pretrained(model_name)

    tokenizer.src_lang = src_lang
    encoded = tokenizer(text, return_tensors="pt")
    generated_tokens = model.generate(**encoded, forced_bos_token_id=tokenizer.get_lang_id(tgt_lang))

    translation = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
    print(f"Translated ({src_lang} → {tgt_lang}):", translation)
    return translation

# Example usage:
if __name__ == "__main__":
    speech_to_translation("french.mp3", src_lang="fr", tgt_lang="hi")



