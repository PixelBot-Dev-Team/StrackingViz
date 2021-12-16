import sys
import json
import time

def doError(message,id = -1):
	print(f"""AN ERROR OCCURED!
Error Message: {message}
Error ID: {id}
Closing in 5 Seconds
	"""
	)
	time.sleep(5)
	exit(id)

def parsedata(Data):
	print(Data)

while True:
	try:
		File = sys.argv[1] 
	except IndexError:
		doError("Drop a Save-Tracking File onto this executable to generate a corresponding Video",1)
	else:
		try:
			with open(File,"r") as JsonFile:			
				Data = json.load(JsonFile)
		except json.decoder.JSONDecodeError:
			pass
			doError("Json File is corrupted",2)
		else:
			parsedata(Data)
