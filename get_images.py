import wget

filename = "fetched_tweets.json"
file = open(filename)

tweets = ['']
count = 0

substring = "media_url"
for lines in file:
	if substring in lines:
		print("Yes")
		line_new = lines.split('"')
		num = line_new.index('media_url')
		media_url = line_new[num+2]
		media_url = media_url.replace("\\", "")
		img_name = "img" + str(count).zfill(4) + ".jpg"	
		count = int(count) + 1
		wget.download(media_url, out=img_name)
	else:
		print("No")





