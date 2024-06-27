import moviepy.editor as mp
clip = mp.VideoFileClip(r"C:\\Users\mri\Python Programs\Knock Yourself Out XD.mp4")
clip.audio.write_audiofile(r"C:\\Users\mri\Python Programs\Knock Yourself Out XD.mp3")