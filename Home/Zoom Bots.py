import requests
import asyncio
import websockets
import random
import json
import sys
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
requests.packages.urllib3.disable_warnings()
def testCode(code):
	instanceEndpoint = "https://russianschool.zoom.us/j/"+code
	r=requests.get(instanceEndpoint,verify=False)
	return("\"total\":0" not in r.text)
def getToken():
	tokenEndpoint="https://zoom.us/join"
	r=requests.get(tokenEndpoint,verify=False)
	return(r.text[r.text.find("\"multiplayerToken\":\""):r.text.find(",\"personId\""):].split(":")[1][1:-1])
def getSession(code,token):
	sidEndpoint = "https://russianschool.zoom.us/j/"+code
	r=requests.get(sidEndpoint,verify=False)
	return(r.text[r.text.find("\"sid\":\""):r.text.find(",\"upgrades\"")].split(":")[1][1:-1])
def getAnswers(code,token,sid):
	termsEndpoint = "https://russianschool.zoom.us/j/"+code+sid
	r=requests.get(termsEndpoint,verify=False)
	plain=r.text[r.text.find("[")::]
	return(json.loads(plain))
async def join(code,token,sid,name):
	wsUri="https://russianschool.zoom.us/j/"+code+sid
	async with websockets.connect(wsUri) as websocket:
		await websocket.send("2probe")
		await websocket.recv()
		await websocket.send("5")
		await websocket.send("42[\"player-join\",{\"username\":\""+name+"\",\"image\":\"https://p0.piqsels.com/preview/998/626/353/imagination-brain-key-head.jpg\"}]")
		data=await websocket.recv()
print("Enter PIN:")
code=str(input())
if(testCode(code)):
		print(colors.OKGREEN,"[+]Code is valid:",code,colors.ENDC)
else:
		print(colors.FAIL,"[-]Code is invalid:",code,colors.ENDC)
		sys.exit()
print(colors.OKBLUE,"[i]Starting spam, press CTRL+C to stop",colors.ENDC)
while(1):
	token=getToken()
	sid=getSession(code,token)
	name="Call me @3399997636  bot#"+str(random.randint(0,999999))
	asyncio.get_event_loop().run_until_complete(join(code,token,sid,name))
	print(colors.OKGREEN,"[+]Joined as:",name,colors.ENDC)