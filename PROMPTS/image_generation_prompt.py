
def generate_image_prompt(theme, style="Default"):
    base_prompt = f"Generate a high-quality, vivid illustration based on the theme: '{theme}', without any text, words, or captions in the image."

    if style != "Default":
        base_prompt += f" Use the art style: {style.lower()}."

    return base_prompt
