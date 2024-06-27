from pytube import YouTube

def download(link):
    TubeObject = YouTube(link)
    TubeObject = TubeObject.streams.get_highest_resolution()
    try:
        TubeObject.download()
    except:
        ValueError
        print("ERROR. ERROR. ERROR")
    
link = input("Enter the URL: ")
download(link)
