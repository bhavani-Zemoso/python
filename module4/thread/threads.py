import threading
import logging

def get_logger():
    logger = logging.getLogger("Threading example")
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("threading.log")
    fmt = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger

def doubler(number, logger):
    """
    A function that can be used by a thread
    """
    logger.debug('Doubler function executing')
    result = number * 2
    logger.debug('Doubler function ended with: {}'.format(result))

if __name__ == '__main__':
    logger = get_logger()
    thread_names = ['Mike', 'George', 'Wanda', 'Dingbat', 'Nina']
    for i in range(5):
        my_thread = threading.Thread(target=doubler,name=thread_names[i], args=(i,logger))
        my_thread.start()
        print(thread_names[i])