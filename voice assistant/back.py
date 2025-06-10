from reply import whats_up_reply, hello_reply, fine_reply

commands = {
    "open tiktok": ["https://www.tiktok.com", "Opening TikTok"],
    "open youtube": ["https://www.youtube.com", "Opening YouTube"],
    "open google": ["https://www.google.com", "Opening Google"],
    "open chatgpt": ["https://chatgpt.com", "Opening ChatGPT"],
    "open my website": ["https://prasoonkandel.netlify.app", "Opening your website"],
    "open facebook": ["https://facebook.com", "Opening Facebook"],
    "open instagram": ["https://www.instagram.com", "Opening Instagram"],
    "open twitter": ["https://twitter.com", "Opening Twitter"],
    "open reddit": ["https://www.reddit.com", "Opening Reddit"],
    "open linkedin": ["https://www.linkedin.com", "Opening LinkedIn"],
    "open github": ["https://github.com", "Opening GitHub"],
    
    # Hindi Songs
    "play o rangrez": ["https://www.youtube.com/watch?v=6hPB3tQnw9A", "Playing 'O Rangrez'"],
    "play kesariya": ["https://www.youtube.com/watch?v=BddP6PYo2gs", "Playing 'Kesariya'"],
    "play tum hi ho": ["https://www.youtube.com/watch?v=Umqb9KENgmk", "Playing 'Tum Hi Ho'"],
    "play apna bana le": ["https://www.youtube.com/watch?v=Htaj3o3JD8I", "Playing 'Apna Bana Le'"],
    "play tere hawale": ["https://www.youtube.com/watch?v=x8Xk5vU-JdQ", "Playing 'Tere Hawale'"],
    "play shayad": ["https://www.youtube.com/watch?v=IvUU8joBb1Q", "Playing 'Shayad'"],
    "play raatan lambiyan": ["https://www.youtube.com/watch?v=gvyUuxdRdR4", "Playing 'Raataan Lambiyan'"],
    "play jeena jeena": ["https://www.youtube.com/watch?v=09R8_2nJtjg", "Playing 'Jeena Jeena'"],
    "play agar tum saath ho": ["https://www.youtube.com/watch?v=sK7riqg2mr4", "Playing 'Agar Tum Saath Ho'"],

    # English Songs
    "play perfect": ["https://www.youtube.com/watch?v=2Vv-BfVoq4g", "Playing 'Perfect' by Ed Sheeran"],
    "play shape of you": ["https://www.youtube.com/watch?v=JGwWNGJdvx8", "Playing 'Shape of You' by Ed Sheeran"],
    "play love me like you do": ["https://www.youtube.com/watch?v=AJtDXIazrMo", "Playing 'Love Me Like You Do'"],
    "play faded": ["https://www.youtube.com/watch?v=60ItHLz5WEA", "Playing 'Faded' by Alan Walker"],
    "play night changes": ["https://www.youtube.com/watch?v=syFZfO_wfMQ", "Playing 'Night Changes' by One Direction"],
    "play let me down slowly": ["https://www.youtube.com/watch?v=50VNCymT-Cs", "Playing 'Let Me Down Slowly' by Alec Benjamin"],
    "play something just like this": ["https://www.youtube.com/watch?v=FM7MFYoylVs", "Playing 'Something Just Like This'"],
    "play stay": ["https://www.youtube.com/watch?v=kTJczUoc26U", "Playing 'Stay' by The Kid LAROI & Justin Bieber"],
    "play baby": ["https://www.youtube.com/watch?v=kffacxfA7G4", "Playing 'Baby' by Justin Bieber"],
    "play eenie meenie": ["https://www.youtube.com/watch?v=prmmCg5bKxA", "Playing 'Eenie Meenie' by Sean Kingston & Justin Bieber"],
    


    #greeting
    "how are you": [None, whats_up_reply],
    "how r u": [None, whats_up_reply],
    "how r you": [None, whats_up_reply],
    "how": [None, whats_up_reply],
    "what's up": [None, whats_up_reply],
    "hello": [None, hello_reply],
    "hi": [None, hello_reply],
    "hey": [None, hello_reply],
    "i am fine": [None, fine_reply],

    #identity
    "your name": [None, "I am a simple Voice assistant made by Prasoon Kandel."],
    "who are you": [None, "I am a simple Voice assistant made by Prasoon Kandel."],
    "your creator": [None, "This Voice Assistant is created by Prasoon Kandel. Visit his website: https://prasoonkandel.netlify.app/"],

    "bye": ["bye", "Bye, have a nice day!"]
}

def answer(command):
    for key in commands:
        if key in command:
            url, message = commands[key]
            if callable(message):
                message = message()
            return url, message
    query = command
    url = f"https://www.google.com/search?q={query}"
    message = "I found these results on the web."
    return url, message
