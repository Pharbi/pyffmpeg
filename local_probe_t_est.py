from pyffmpeg import FFprobe

f = FFprobe("H:/GitHub/pyffmpeg/_test/asem.mp3")
# ret = f.get_album_art('cover.png')


print(f.duration)
for x in f.metadata:
    print(x, '\n')
