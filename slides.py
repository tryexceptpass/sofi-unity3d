import random
import tweepy
import yaml

from sofi.app import Sofi


consumer_key = "CONSUMER_KEY"
consumer_secret = "CONSUMER_SECRET"
access_token = "ACCESS_TOKEN"
access_token_secret = "ACCESS_TOKEN_SECRET"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

twitter = tweepy.API(auth)

current_slide = -1

with open('slides.yml', 'rb') as f:
    slides = yaml.safe_load(f.read())
    ordered_slides = list()
    for i, slide in enumerate(slides):
        for item in slide['slide']['display']:
            ordered_slides.append({"display": item, "parent": i})

class TwitterListener(tweepy.StreamListener):
    def on_status(self, status):
        text = status.text.encode('ascii', errors='ignore').decode()
        color = (0.5, 0.5, 0.5, 1)

        if text.startswith("RT "):
            color = (1, 0, 0, 1)

        # print(text.encode('ascii', errors='ignore'))
        app.dispatch({
            "command": "unity.spawn",
            "obj": "cube",
            "text": text,
            "position_on": "SpawnPoint",
            "rotation": (random.randint(0, 90), random.randint(0, 90), random.randint(0, 90)),
            # "scale": (5, 5, 5),
            # "position": (-8, 15, -10),
            "color": color,
            "rigidbody": True,
            "collider": True,
            # "look_at": "camera"
        })
        app.dispatch({
            "command": "unity.update",
            "name": "tweet_info",
            "obj": "guitext",
            "text": text,
            # "position_on": "SpawnPoint",
            # "rotation": (random.randint(0, 90), random.randint(0, 90), random.randint(0, 90)),
            # "scale": (5, 5, 5),
            "position": (-1, 20),
            "color": color,
            # "text_font_size": 20,
            # "rigidbody": True,
            # "collider": True,
            # "look_at": "camera"
        })

    def on_error(self, code):
        # Disconnect if we reached the rate limit
        if code == 420:
            return False

def displayslide():
    global current_slide

    if current_slide == -1:
        cmd = 'unity.spawn'
        current_slide = 0
    else:
        cmd = 'unity.update'

    app.dispatch({
        "command": cmd,
        "name": "slide_text",
        "obj": "guitext",
        "text": ordered_slides[current_slide]['display'],
        # "position_on": "SpawnPoint",
        # "rotation": (random.randint(0, 90), random.randint(0, 90), random.randint(0, 90)),
        # "scale": (5, 5, 5),
        # "position": (-8, 15, -10),
        "color": (1, 1, 1, 1),
        "text_font_size": 24,
        # "rigidbody": True,
        # "collider": True,
        # "look_at": "camera"
    })

    print(chr(27) + "[2J")
    print(f"=== {slides[ordered_slides[current_slide]['parent']]['slide']['title']} ===\n")

    print("Display:")
    for item in slides[ordered_slides[current_slide]['parent']]['slide']['display']:
        words = item.split()
        line = "*"
        for i, word in enumerate(words):
            line = f"{line} {word}"

            if len(line) > 120:
                print(f"\t{line}")
                line = " "

        if line != ' ':
            print(f"\t{line}")

    print("\nNotes:")
    if 'notes' in slides[ordered_slides[current_slide]['parent']]['slide']:
        for item in slides[ordered_slides[current_slide]['parent']]['slide']['notes']:
            words = item.split()
            line = "*"
            for i, word in enumerate(words):
                line = f"{line} {word}"

                if len(line) > 120:
                    print(f"\t{line}")
                    line = " "

            if line != ' ':
                print(f"\t{line}")

async def oninit(event):
    print(event)

    app.dispatch({"command": "init", "data": "ABC"})

    displayslide()

    app.dispatch({
        "command": "unity.spawn",
        "name": "tweet_info",
        "obj": "guitext",
        "text": "",
        # "position_on": "SpawnPoint",
        # "rotation": (random.randint(0, 90), random.randint(0, 90), random.randint(0, 90)),
        # "scale": (5, 5, 5),
        "position": (-1, 10),
        # "color": (1, 1, 1, 1),
        # "text_font_size": 20,
        # "rigidbody": True,
        # "collider": True,
        # "look_at": "camera"
    })

    app.dispatch({
        "command": "unity.subscribe",
        "name": "keyboard",
        "data": "up,left,down,right,space,backspace,return,enter"
    })


async def onkeyboard(event):
    global current_slide

    print(event)

    if event['key'] in ['space', 'return', 'enter', 'right', 'down']:
        current_slide = min(current_slide + 1, len(ordered_slides) - 1)
    elif event['key'] in ['up', 'left', 'backspace']:
        current_slide = max(current_slide - 1, 0)

    displayslide()


app = Sofi()
app.register('init', oninit)
app.register('unity.keyboard', onkeyboard)

stream = tweepy.Stream(auth=twitter.auth, listener=TwitterListener())
stream.filter(track=["python"], async=True)

app.start(desktop=False)
