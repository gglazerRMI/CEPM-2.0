# validation / update check for Grant -- RMI example from Christine Phan
# ------------
# test code for SHA256 hash and then url download 
# if you can feed this hash check and then download into your model, this could
# help you speed up the data update check part 
# run from Terminal: python test.py

import os
import sys
import subprocess
import re
import urllib2


def url_download():
	print "URL Download example. "
	print "Getting username ... "
	username = subprocess.check_output(['whoami']).strip()
	
	
	# GTFS Example 
	# -------
	url = "http://gtfs.s3.amazonaws.com/abq-ride_20150802_0107.zip"
	filename = '/Users/' + username + '/Downloads/feed_example.zip'
	# -------
	
	# Google Example 
	# --------------
	# url = "http://www.google.com"
	# filename = '/Users/' + username + '/Downloads/test'

	# ---------------
	
	print "Opening file ... "
	filedata = urllib2.urlopen(url)  
	datatowrite = filedata.read()

	print "Downloading to local ... "
	with open(filename, 'wb') as f:
		f.write(datatowrite)
	
	print "Done."
	print "End URL Download example."

def hashvalue ():
	print "Hash Test running."
	# google example 
	# --------------
	# basic terminal command: Echo -n "enter text here" | shasum -a 256
	cmd = "curl www.google.com | shasum -a 256"
	# --------------
	# GTFS example 
	# if zip file, GTFS feed source
	cmd = "curl http://gtfs.s3.amazonaws.com/abq-ride_20150802_0107.zip --output - | shasum -a 256"
	# --------------
	print "Getting SHA256 from source ..."
	ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	output = ps.communicate()[0]

	print "Using regular expression to parse string ... "
	hash_val = re.search('[\w]{64}', output)
	if hash_val:
		print "SHA256 is: ", hash_val.group(0)
		# whatever else you want to do, the same data will generate the same SHA256
		# use if-equals statements to check similarity 

	print "End hash test."

def main():
	testMode = input("Test Mode: 0 for hash value, 1 for url download: ")
	if testMode == 0: 
		hashvalue() 
	else: 
		url_download()

if __name__ == "__main__":
	main()

