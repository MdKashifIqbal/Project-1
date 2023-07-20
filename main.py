choose=int(input("Press 1 for download profile pic from instagram or press 2 for download video from youtube : "))


if(choose==1):   
    import instaloader
    inp=(input("Enter username : "))
    loader = instaloader.Instaloader()
    loader.download_profile(inp, profile_pic_only=True)
    print("Download completed")

elif(choose==2):
    from pytube import YouTube
    url = input("Give URL : ")
    print("Downloading")
    yt = YouTube(url)
    path="YouTube"
    stream = yt.streams
    # print(yt.title)
    # video = stream.filter(progressive = True, file_extension = "mp4").order_by('resolution').desc().first().download()
    video = stream.filter(progressive = True, file_extension = "mp4").first().download()
    # video.download()
    print("--------------")
    print("Download completed")

else:
    print("Please choose 1 or 2 for proceed")