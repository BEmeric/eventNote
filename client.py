import requests
import sys

BASE_URL = 'http://127.0.0.1:5000'

def add_event(start, tag, stop=None):
    url = f"{BASE_URL}/add_event"
    data = {"Start": start, "Tag": tag}
    if stop:
        data["Stop"] = stop
    response = requests.post(url, json=data)
    print(response.json())

def list_events():
    url = f"{BASE_URL}/list_events"
    response = requests.get(url)
    for event in response.json():
        print(event)

def remove_event(event_id):
    url = f"{BASE_URL}/remove_event/{event_id}"
    response = requests.delete(url)
    print(response.json())

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: client.py [add|list|remove] [arguments...]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 4:
            print("Usage: client.py add <start> <tag> [stop]")
        else:
            start = sys.argv[2]
            tag = sys.argv[3]
            stop = sys.argv[4] if len(sys.argv) > 4 else None
            add_event(start, tag, stop)
    elif command == "list":
        list_events()
    elif command == "remove":
        if len(sys.argv) < 3:
            print("Usage: client.py remove <event_id>")
        else:
            event_id = sys.argv[2]
            remove_event(event_id)
    else:
        print("Unknown command")
