import websocket
import json


def on_message(ws, message):
    print(message, end="")
    if "Completed" in message:
        print("\nReceived 'Completed' message. Closing WebSocket.")
        ws.close()


def on_error(ws, error):
    print("WebSocket error:", error)


def on_close(ws, a, b):
    print("WebSocket connection closed")


def on_open(ws):
    print("WebSocket connection opened")
    print()
    request = {
        "action": "stream",
        "sys_instruct": "Helpful AI Model",
        "user_request": "What is the reason I am Obese????",
    }
    ws.send(json.dumps(request))


if __name__ == "__main__":
    # fill this wis the approperiate wss://
    ws_url = ""
    ws = websocket.WebSocketApp(
        ws_url, on_message=on_message, on_error=on_error, on_close=on_close
    )
    ws.on_open = on_open
    ws.run_forever()
