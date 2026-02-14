import time

def slow_drip_response():
    yield "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n"
    yield "Beginning Data Stream...\n"
    while True:
        # Every 30 seconds, send 10 bytes of junk. 
        # Keeps the attacker's socket open and their resources tied up.
        time.sleep(30)
        yield "0x90 0x90 0x90 0x90\n" 
