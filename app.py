import os
import sys
import time
import logging
from watchdog.observers import Observer

from lib.GeneratingEventHandler import GeneratingEventHandler

CWD = os.path.dirname(__file__)

PAGE_TEMPLATE = os.path.join(CWD, 'templates', "page_template.html")
LINK_TEMPLATE = os.path.join(CWD, 'templates', "link_template.html")

FOLDER_TO_WATCH = "/etc/nginx/sites-available/"
OUTPUT_FILE = "/var/www/html/index.html"
LOG_FILE = "/var/log/nipg.log"

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S', filename=LOG_FILE)
    event_handler = GeneratingEventHandler(OUTPUT_FILE, PAGE_TEMPLATE, LINK_TEMPLATE)
    observer = Observer()
    running = True
    if sys.argv[1] == 'start':
        observer.schedule(event_handler, FOLDER_TO_WATCH, recursive=True)
        observer.start()
        while running:
            time.sleep(1)
    elif sys.argv[1] == 'stop':
        if running:
            running = False
            observer.stop()
            observer.join()
    elif sys.argv[1] == 'reload':
        handler = GeneratingEventHandler(OUTPUT_FILE, PAGE_TEMPLATE, LINK_TEMPLATE)
        handler.on_modified({
            "is_directory": False,
            "event.src_path": os.path.join(FOLDER_TO_WATCH, "services.conf")
        })
