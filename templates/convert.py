from moviepy.editor import *
clip = VideoFileClip("review2.mp4")
clip = clip.subclip(0,5)
clip = clip.cutout(0,3)
clip.write_gif("review2.gif")

shot = VideoFileClip("review2.mp4")
shot = shot.save_frame("review2bg.png")
print("Success")