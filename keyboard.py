from pynput.keyboard import Key

listen_to_keys = False
last_key = Key.enter


def on_release(key):
    global last_key
    if listen_to_keys:
        last_key = key


def reset_key_listener():
    global listen_to_keys, last_key
    listen_to_keys = False
    last_key = Key.enter


async def ask_user() -> bool:
    global listen_to_keys
    listen_to_keys = True
    while True:
        if last_key == Key.space:
            reset_key_listener()
            return True
        elif last_key == Key.esc:
            reset_key_listener()
            return False
