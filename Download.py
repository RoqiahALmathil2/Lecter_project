import pytube
print("Download vid from web by python")
url = input('Enter vid url : ')
pytube.YouTube(url).stream.get_highest_resolution().Download("Desktop")