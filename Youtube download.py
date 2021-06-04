from pytube import YouTube

video = YouTube("https://www.youtube.com/watch?v=opy8D9xO40Q&ab_channel=BERTDELASPEED")
print(video.title)
print(video.views)
print(video.author)
print('\n\n')
print(video.streams.all)
print(video.streams.get_lowest_resolution())
print(video.streams.get_highest_resolution())

# Quality = video.streams.get_by_resolution("360p").download()
# if Quality:
#     print("Video downloaded !")



