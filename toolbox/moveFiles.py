import os
try:
	os.mkdir("/usr/local/nagiosxi/html/config/uploads")
except:
	print("Folder already exists")
try:
 	os.popen("cp /env/lib/python3.6/site-packages/handle_file_upload.php /usr/local/nagiosxi/html/config/handle_file_upload.php")
except:
	print("Error")


