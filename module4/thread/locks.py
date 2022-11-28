import threading

total = 0
lock = threading.Lock()

def update_total(number):
    """
    Updates the total by the given amount
    """
    global total
    lock.acquire()
    try:
        total += number
    finally:
        lock.release()
    print(total)

def update_total_context(number):
    global total
    with lock:
        total += number
    print(total)

if __name__ == '__main__':
    for i in range(10):
        thread = threading.Thread(target=update_total_context,args=(i,))
        thread.start()