from pytube  import YouTube

link = "https://www.youtube.com/watch?v=nhUZdZ1uMq0"

you_1 = YouTube(link)
videos = you_1.streams.all()
vid = list(enumerate(videos))

for i in vid:
    print (i)
print ()

strm = int (input("Enter: "))
videos[strm].download()
print ("Successfull")



