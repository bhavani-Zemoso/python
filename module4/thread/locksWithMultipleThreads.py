import threading

lock = threading.RLock()

def do_something():
    with lock:
        print('Lock acquired in do_something block')
    print('Lock released in do something block')
    return 'do_something'

def do_something_else():
    with lock:
        print('Lock acquired in do_something_else block')
    print('Lock released in do_something_else block')
    return 'do_something_else'

def call_two_functions():
    with lock:
        result1 = do_something()
        result2 = do_something_else()
    print(result1)
    print(result2)

if __name__ == '__main__':
    for i in range(1, 10):
        thread = threading.Thread(target=call_two_functions)
        thread.start()