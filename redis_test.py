import redis
import threading
import time

r = redis.Redis(host='localhost', port=6379, db=0)

def subscriber():
    pubsub = r.pubsub()
    pubsub.subscribe('test_channel')
    for message in pubsub.listen():
        if message['type'] == 'message':
            print("Received:", message['data'].decode())

threading.Thread(target=subscriber, daemon=True).start()
time.sleep(1)
r.publish('test_channel', 'Hello Redis!')
r.publish('test_channel', 'Pub/Sub works!')
time.sleep(1)

