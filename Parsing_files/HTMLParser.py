from html.parser import HTMLParser
import codecs

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

parser = MyHTMLParser()

f = codecs.open("AFDX_VL_Detail.htm", 'r')

for i in f:
    print(i)
