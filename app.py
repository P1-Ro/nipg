import os
import logging

from lib.GenerationHandler import GenerationHandler

CWD = os.path.dirname(__file__)

PAGE_TEMPLATE = os.path.join(CWD, "templates", "page_template.html")
LINK_TEMPLATE = os.path.join(CWD, "templates", "link_template.html")

SERVICES_FILE = "/etc/nginx/sites-available/services.conf"
OUTPUT_FILE = "/var/www/html/index.html"

LOG_FILE = "/var/log/nipg.log"
LOG_FORMAT = "%(asctime)s - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT, filename=LOG_FILE)
    handler = GenerationHandler(SERVICES_FILE, OUTPUT_FILE, PAGE_TEMPLATE, LINK_TEMPLATE)
    handler.generate()
