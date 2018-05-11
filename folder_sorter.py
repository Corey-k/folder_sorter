# Had a very dirty downloads folder, and using the windows sorting by type was taking too long
# This small script moves all files into folders of their respective types
# Features that might be added down the road:
#		-ignore certain file types
#		-group certain file types together (mainly for packaging cod4 maps)
#
#	Author : Corey Koelewyn
# Email  : Corey.Koelewyn@gmail.com
# 

import os

def files_in_dir(directory_to_scan):
	return os.listdir(directory_to_scan)

def extensions_of_files(list_of_files):
	list_of_extensions = []
	for files in list_of_files:
		if files[0] == '.' or os.path.isdir(files):
			continue #ignores hidden files and folders
		ext = files.split('.', 1)[1] # split(char, X) does a max of X splits
		if ext not in list_of_extensions
			list_of_extensions.append(ext) 
	return list(set(list_of_extensions))

def make_extension_folders(list_of_extensions):
	for extension in list_of_extensions:
		try:
			os.mkdir(extension)
		except:
			print(extension + " folder already exists")
	return

def move_to_folders(list_of_files):
	for files in list_of_files:
		if files[0] == '.' or os.path.isdir(files): or files[0] == "folder_sorter"
			continue #ignores hidden files and folders
		os.rename(files , files.split('.', 1)[1] + '/' + files)

def main():
	try:
		file_list = files_in_dir(os.getcwd())
	except:
		print("problem with getting files in current directory")
	try:
		extens = extensions_of_files(file_list)
	except:
		print("problems building a list of the extensions")
	try:
		make_extension_folders(extens)
	except:
		print("error making folders")
	try:
		move_to_folders(file_list)
	except:
		print("error moving files")


if __name__ == '__main__':
	main()