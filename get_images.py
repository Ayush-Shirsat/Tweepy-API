#Step-2: Extract Media URLs from tweets(in json format) and download images.

import wget

#Access file that contains tweets
filename = "fetched_tweets.json"
file = open(filename)

tweets = ['']
count = 0

substring = "media_url"
for lines in file:
	if substring in lines:
		# Print Yes if tweet contains Media URL
		print("Yes")
		line_new = lines.split('"')
		num = line_new.index('media_url')
		media_url = line_new[num+2]
		media_url = media_url.replace("\\", "")
		
		# Save downloaded images in format (imgXXXX.jpg)
		img_name = "img" + str(count).zfill(4) + ".jpg"	
		count = int(count) + 1
		
		# Download the images
		wget.download(media_url, out=img_name)
	else:
		# Prints No if tweet does not contain Media URL
		print("No")





