import os

try:
	command = "ffmpeg -r 1/1 -i img%04d.jpg -vcodec mpeg4 -y output.mp4"
	os.system(command)
except Exception as e:
	print(e)
	exit()
