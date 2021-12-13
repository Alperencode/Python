from pygame import mixer

mixer.init()
mp3file = input("Please enter the mp3 path (example: bloodontheleaves.mp3):\n>")

mixer.music.load(mp3file)
mixer.music.set_volume(0.7)
mixer.music.play()

while True:
    print("Press 'p' to stop and 'r' to resume")
    print("Press 'e' to end the program")
    query = input("\n>")
    if query == 'p':
        mixer.music.pause()
    elif query == 'r':
        mixer.music.unpause()
    elif query == 'e':
        mixer.music.stop()
        break