import typing
from console_progress_bar import next_line, progress_bar
from pytube import YouTube

# Script improvement idea: Accept an argument which will allow you to download n-amount of videos with x hashtag
# Also add a feature to be able to set your own file with links. Example: python main.py --file hello.txt
# E.g. python main.py --tag music --amount 5

# File with links
file = 'links.txt'

def remove_new_line_escape_character(string: str) -> str:
	if string[-1] == '\n':
		# Remove escape character and return the string
		return string[:-1]
	else:
		return string

def read_links(file: str) -> list:
	# List of links
	links = []
	
	# Catch exception in case file doesn't exist
	try:
		# Open file for reading
		with open(file, 'r') as f:
			
			# Read file lines
			lines = f.readlines()
			# Check if there are no lines
			if not lines:
				# Print warning about the empty file
				print('WARNING: {} is empty.'.format(file))

			# Iterate through all the lines in the file
			for i in lines:
				# if current line's text has new line escape character at the end then remove it and append in the list
				links.append(remove_new_line_escape_character(i))
	except:
		print('File {} doesn\'t exist. Try creating the file in the folder with main.py script'.format(file))
		exit(1)
	
	return links

# Read links from the file
links = read_links(file)
# Index of the current link
link_indx = 0

def on_progress(stream, data_chunk, bytes_remaining):
	# Get variables from the outer scope
	global links, link_indx

	# Get the size of downloading video
	filesize = stream.filesize

	# Translate remaining bytes and file size into (from 0 to 100) range
	current = (1 - round((bytes_remaining / filesize), 1)) * 100

	# Remove new line escape character from the link and add colon
	front = remove_new_line_escape_character(links[link_indx]) + ': '

	# Show the progress bar
	progress_bar(int(current), front_text=front)

def on_complete(stream, file_path):
	# Get variables from the outer scope
	global links, link_indx
	
	# Remove new line escape character from the link and add colon
	front = remove_new_line_escape_character(links[link_indx]) + ': '

	# When download is complete show 100% progress
	progress_bar(100, front_text=front)

	# Go to the next line
	next_line()

# Iterate through all the links
for i in links:
	# Catch exception in case parsed link is incorrect or doesn't exist
	try:
		# Create a youtube object with current link and set on_progress, on_complete callbacks to custom functions
		yt = YouTube(i, on_progress_callback=on_progress, on_complete_callback=on_complete)
		# Get a video with .mp4 file extension and lowest quality
		stream = yt.streams.filter(file_extension='mp4').get_lowest_resolution()
		# Download video in videos folder and name it: 'video {index}.mp4'
		stream.download(filename='videos/video {}.mp4'.format(link_indx + 1))
	except:
		print('Wrong link:', i)
		exit(1)
	# Increment link index
	link_indx += 1
	