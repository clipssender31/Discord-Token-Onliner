import websocket, threading, random, json, time, pyfiglet, sys
tokens=open('Tokens.txt','r').read().splitlines()
randomstatus=['online','idle','dnd']
AmountOnlined=0
count=0
def countdown(t): #this function was taken from cugeon.
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f"Time Until Re-Online: {timer}", end="\r")  
        time.sleep(1)
        t -= 1 
    print('Trying To Online Tokens')
    print(pyfiglet.figlet_format(f"Clips Token Onliner"))
t = input("How often you'd like Re-online your tokens (500 - 600s recommended): ")
def websocket_token(token):
    ws=websocket.WebSocket();ws.connect('wss://gateway.discord.gg/?encoding=json&v=9');response=ws.recv();event=json.loads(response);heartbeat_interval=event['d']['heartbeat_interval']/1000;ws.send(json.dumps({"op": 2,"d": {"token": token,"properties": {    "$os": sys.platform,    "$browser": "RTB",    "$device": f"{sys.platform} Device"},"presence": {    "game": {        "name": 'github.com/clipssender31 - Token Onliner',        "type": 0,        "details": "Join Here! https://discord.gg/wrNbhMeQeW",        "state": "https://github.com/clipssender31/Discord-Token-Onliner"    },    "status": random.choice(randomstatus),    "since": 0,    'activities':[],    "afk": False}},"s": None,"t": None}))
    while True:
        heartbeatJSON={'op':1,'token':token,'d':'null'};ws.send(json.dumps(heartbeatJSON));time.sleep(heartbeat_interval)
for token in tokens:threading.Thread(target=websocket_token,args=(token,)).start();AmountOnlined+=1;print(f"{AmountOnlined} Tokens onlined")
print(f"{AmountOnlined} Tokens Are Now Online")
for token in tokens:
        countdown(int(t))
        AmountOnlined=0
        for token in tokens:threading.Thread(target=websocket_token,args=(token,)).start();AmountOnlined+=1;print(f"{AmountOnlined} Tokens Are Now Online")
        print(f"{AmountOnlined} Tokens Are Now Online")
