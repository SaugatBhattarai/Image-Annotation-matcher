import os
import sys
# import cv2
image_folder = '/home/saggi/Desktop/annotation_remover/images/'
label_folder = '/home/saggi/Desktop/annotation_remover/label/'
count = 1
label_list = [labelname[:-4] for labelname in os.listdir(label_folder)]
image_list = [imagename[:-4] for imagename in os.listdir(image_folder)]

common_list = set(label_list) & set(image_list)

for imagename in os.listdir(image_folder):
	path = image_folder+imagename
 	if imagename[:-4] not in common_list:
 		if os.path.exists(path):
	 		print(imagename + ' has been removed.')
	 		os.remove(image_folder + imagename)
	 	else:
	 		print('The file doesnot exists.')
	else:
		print(imagename + ' has labelled in the file.')