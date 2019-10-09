import xml.etree.ElementTree as ET

class XmlWriter:

    def __init__(self, output_loc, file_name):
        self.aiml_file = open(output_loc + file_name + ".aiml", "w")

    def write_body(self):
        template_content = "ola mundo"
        pattern_text = "ola"
        self.aiml_file.write("\n\t<category>")
        self.aiml_file.write("\n\t\t<pattern>")
        self.aiml_file.write(pattern_text.upper())
        self.aiml_file.write("</pattern>")
        self.aiml_file.write("\n\t\t<template>")
        self.aiml_file.write(template_content)
        self.aiml_file.write("\n\t\t</template>")
        self.aiml_file.write("\n\t</category>")

    def open_file(self):
        self.aiml_file.write("<?xml version='1.0' encoding='ISO-8859-1'?>")
        self.aiml_file.write("\n<aiml version=\"1.0.1\">")

    def close_file(self):
        self.aiml_file.write("\n</aiml>\n")
        self.aiml_file.close()



class BpmnFlow(object):
    def execute(self):

        tree = ET.parse('./input/congratulacoes.bpmn')

        root = tree.getroot()

        for child in root:
            print(child.tag)
            #if str(child.tag).find("process"):
            #    print(child.tag)
            #    print(child.attrib)
        for child in root:
            print(child.attrib)

        print(type(child.attrib))

        print(child.attrib['id'])

        input_path = "./input"
        outpu_path = "./output/"
        xmlWriter = XmlWriter(outpu_path, "saida")
        xmlWriter.open_file()
        xmlWriter.write_body()
        xmlWriter.close_file()

if __name__ == "__main__":
    b = BpmnFlow()
    b.execute()