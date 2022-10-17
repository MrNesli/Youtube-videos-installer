# <link> [===>---------------------------] 10%
# [===============================] Downloaded
# [=====================>---------] 71%


#[>---------------------------------] 0%
#[============>---------------------]
# 100 / 30 = 3

# [>-------------------------]
# 20 chunks so 5 % per chunk (100 / 20)
# [>------------------------------]
# 25 chunks so 4 % per chunk (100 / 25)
# [>---------------------------------]
# 30 chunks so 3.3 % per chunk (100 / 30)

def next_line():
	# Print new line character
	print('\n')

def progress_bar(current_progress, end_progress=100, chunks=25, front_text=''):
	# Catch exception if raised
	try:
		# Get amount of percents 1 chunk holds depending on end_progress
		per_chunk = end_progress // chunks
		# Current amount of filled chunks
		progress_chunks = current_progress // per_chunk
		# Print progress bar
		print(front_text + '[' + ('=' * progress_chunks)  + ('>' if progress_chunks < chunks else '') + ('-' * (chunks - progress_chunks)) + '] ' + str(current_progress) + '%', end='\r')
	except Exception as e:
		print(e)