import websockets
import anyio
from rich.pretty import pprint as print
import os
import json
from pocketoptionapi.constants import REGION

# How to get SSID from Pocket Options
# https://www.youtube.com/watch?v=YpM5BeNFvaI&ab_channel=tradingbots
# 1) go to pocket options in your chrome - select the desired market - real/demo
# 2) go to chrome devtools, network tab, WS tab
# 3) click on any request and in messages tab filter for "auth"
# example SSID begins like: 42["auth",{"session":"a:4:{s:10:\"session_id\";s:32:\"10951......

# Read SSID from env variable (or use dotenv to read from local files if you have more environments)
ssid = os.getenv("SSID")

async def websocket_client(url, pro):
    for i in REGION.get_regions(REGION):
        print(f"Trying {i}...")
        try:
            async with websockets.connect(
                i, #teoria de los issues
                extra_headers={
                    #"Origin": "https://pocket-link19.co",
                    "Origin": "https://po.trade/"
                },
            ) as websocket:
                async for message in websocket:
                    await pro(message, websocket, url)
        except KeyboardInterrupt:
            exit()
        except Exception as e:
            print(e)
            print("Connection lost... reconnecting")
            # await anyio.sleep(5)
    return True


async def pro(message, websocket, url):
    # if byte data
    if type(message) == type(b""):
        # cut 100 first symbols of byte date to prevent spam
        print(str(message)[:100])
        return
    else:
        print(message)

    # Code to make order
    # data = r'42["openOrder",{"asset":"#AXP_otc","amount":1,"action":"call","isDemo":1,"requestId":14680035,"optionType":100,"time":20}]'
    # await websocket.send(data)

    if message.startswith('0{"sid":"'):
        print(f"{url.split('/')[2]} got 0 sid send 40 ")
        await websocket.send("40")
    elif message == "2":
        # ping-pong thing
        print(f"{url.split('/')[2]} got 2 send 3")
        await websocket.send("3")

    if message.startswith('40{"sid":"'):
        print(f"{url.split('/')[2]} got 40 sid send session")
        await websocket.send(ssid)
        print("message sent! We are logged in!!!")


async def main():
    url = "wss://api-l.po.market/socket.io/?EIO=4&transport=websocket"
    await websocket_client(url, pro)


if __name__ == "__main__":
    anyio.run(main)