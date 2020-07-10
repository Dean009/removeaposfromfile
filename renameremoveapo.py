import os, string
location = os.getcwd()
for root, dirs, files in os.walk(location):
	for filename in files:
		strcurfile = str(filename)
		filename_without_extension = strcurfile[:-1]
		print(filename_without_extension)
		path = os.path.join(location, filename)
		os.rename(filename, filename_without_extension)

