def generate_story_prompt(theme, use_case, tone="Default"):
    templates = {
        "Personal & Narrative Based": f"""Write a short creative story (max 300 words) inspired by the theme: "{theme}". 
Focus on personal emotions or experiences, with vivid imagery and a poetic or reflective twist. 
It should feel relatable or introspective, ending with a surprising or emotional note.""",

        "🧸 Kids & Family": f"""Write a short, engaging story for children based on the theme: "{theme}". 
Use simple language, fun characters, and a gentle moral. 
The tone should be imaginative and family-friendly with a magical or happy ending.""",

        "🎮 Fantasy, Worldbuilding & RPG": f"""Create a detailed and imaginative world-building piece based on the theme: "{theme}". 
Focus on lore, setting, or magic systems — something fit for a fantasy novel or RPG. 
Include unique creatures, cultures, or rules of the world.""",

        "🎬 Film, Script & Visual Storytelling": f"""Write a cinematic {use_case.lower()} idea based on the theme: "{theme}". 
Use scene-setting, dialogue, and dramatic beats to build visual intensity. Think like a director or screenwriter.""",

        "🖼️ Visual & Inspirational Concepts": f"""Create a highly visual and metaphorical narrative inspired by the theme: "{theme}". 
Focus on mood, symbolism, and abstract storytelling. 
It should spark emotion and imagination rather than follow a strict plot.""",

        "📦 Brand, Marketing & Business": f"""Write a short branded story or ad concept based on the theme: "{theme}". 
It should convey a message or brand identity with emotional impact, storytelling, and clarity. 
Make it catchy and suitable for modern audiences.""",

        "🧪 Experimental, Meta & Thoughtful": f"""Write a creative, unconventional piece based on the theme: "{theme}". 
It could break the fourth wall, use metafiction, or be philosophically abstract. 
Feel free to play with logic, timelines, or formats.""",

        "📚 Education & Edutainment": f"""Turn the concept of "{theme}" into a fun, educational short story or explanation. 
Make it understandable, imaginative, and ideally suitable for students or young learners."""
    }

    # Default fallback
    prompt = templates.get(use_case, f"""Write a short creative story (max 300 words) inspired by the theme: "{theme}". 
Make it vivid, imaginative, and emotionally resonant, with a clear beginning, middle, and end.""")

    if tone != "Default":
        prompt += f"\nWrite it in a {tone.lower()} tone to match the mood."

    return prompt

