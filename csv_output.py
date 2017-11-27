import io
import os
import xlsxwriter
from operator import itemgetter,attrgetter


# Imports the Google Cloud client library
from google.cloud import vision

# Instantiates a client
vision_client = vision.Client()


workbook=xlsxwriter.Workbook('SUNNY3.xlsx')
worksheet = workbook.add_worksheet()

result=[]

path = "./nice day/DAY3"
files=os.listdir(path)

# The name of the image file to annotate
count1=0
for file in files:
	if not os.path.isdir(file):
		with io.open(path+"/"+file,'rb') as image_file:
			content = image_file.read()
			image = vision_client.image(content=content)
		# Performs label detection on the image file
		labels = image.detect_labels()
   		file_name=os.path.basename(file)
		print file_name
		
		for label in labels:
			if(label.description=="sunny"):
				result.append([file_name,label.description,label.score])
			if(label.description=="snow"):
				result.append([file_name,label.description,label.score])
			if(label.description=="fog"):
				result.append([file_name,label.description,label.score])

count=0
for i in result:
	
	worksheet.write(count,0,i[0])
	worksheet.write(count,1,i[1])
	worksheet.write(count,2,i[2])
	count+=1
