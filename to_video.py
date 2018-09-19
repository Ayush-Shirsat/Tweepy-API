import os

#os.popen"cat images/* | ffmpeg -f image2pipe -i - out.mp4 -vf 'scale=trunc(iw/2)*2:trunc(ih/2)*2'"
try:
	command = "ffmpeg -r 1/1 -i img%04d.jpg -vcodec mpeg4 -y output.mp4"
	os.system(command)
except Exception as e:
	print(e)
	exit()