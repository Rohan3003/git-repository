# code to move files into specific folder
import os

path = 'D:/test_folder'

images_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.psd', '.bmp', '.ico', '.svg', '.ai', '.webp', '.eps', '.raw', '.cr2', '.nef', '.orf', '.sr2', '.tif']
videos_extensions = ['.avi', '.flv', '.m4v']
audio_extensions = ['.aac', '.aif', '.aiff','.flac','.m4a','.ogg','.wav','.wma']

# print(os.listdir(path))
# print(os.path.isfile(path))
# print(os.path.join(path, 'file.extension'))

'''
for filename in os.listdir(path):
    if os.path.isfile(os.path.join(path, filename)):
        print(filename)  
'''

for root, dirs, files in os.walk(path):
    print(root, dirs, files)