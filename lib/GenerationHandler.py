import logging
import re

from lib.Service import Service


class GenerationHandler:

    def __init__(self, services_file, output_file, page_template, item_template):
        self.page_template = page_template
        self.item_template = item_template
        self.output_file = output_file
        self.services_file = services_file

    def generate(self):
        services = []
        with open(self.services_file, "r") as text_file:
            lines = text_file.readlines()
            for line in lines:
                if re.match(r'location .* #', line):
                    try:
                        name = re.search("/[^{]*", line).group(0).replace("/", "").strip()
                        description = re.search("#.*", line).group(0).replace("#", "").strip().capitalize()
                        services.append(Service(name, description))
                    except:
                        logging.error("Can't parse line: %s", line)

        self.update_file(self.generate_html(services))

    def generate_links(self, services):
        result = ""
        link_template = open(self.item_template, "r").read()

        for service in services:
            result += link_template.replace("{{link}}", service.link)\
                        .replace("{{name}}", service.name)\
                        .replace("{{description}}", service.description)
        return result

    def generate_html(self, services):
        links = self.generate_links(services)
        with open(self.page_template, "r") as text_file:
            return text_file.read().replace("{{links}}", links)

    def update_file(self, content):
        with open(self.output_file, "w") as text_file:
            text_file.write(content)
        logging.info("file updated successfully")
