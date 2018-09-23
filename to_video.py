import os

try:
	# Frame rate is 1 fps and video is of format .mp4
	command = "ffmpeg -r 1/1 -i img%04d.jpg -vcodec mpeg4 -y output.mp4"
	os.system(command)
except Exception as e:
	# Throws error (if any)
	print(e)
	exit()
