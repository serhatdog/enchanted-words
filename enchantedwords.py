from os import remove
from pdfkit import from_file

def processingwords(text):
	fullText = ""
	originalText = text.split()
	for word in originalText:
		if len(word) <= 4: fullText += '<b style="color:black">' + word + "</b>" + "   "; continue
		fullText += '<b style="color:black">' + word[:(len(word)//2)] + "</b>" + word[(len(word)//2):] + "   "
	return fullText

def enchant(text, title, settings = False):
	if not settings:
		settings = {
	"font-size":	"20px",
	"font-family": 	"Segoe UI",
	"font-weight": 	"light",
		}
	HTML_HEAD = f'<!DOCTYPE html><html><head><meta charset="utf-8"><title>Enchanted Words</title></head><body style="font-size: {settings["font-size"]}; font-family: {settings["font-family"]}; color: rgb(80,80,80); font-weight: {settings["font-weight"]}"><h1 style="text-align: center; color:black; font-weight: lighter">{title}</h1><hr>'
	HTML_END = '<hr><h5 style="text-align: center; color:black; font-weight: lighter">Enchanted Words (Developing)<br>  Author: Serhat Dogan, <a href="https://github.com/serhatdog/">Github</a>, <a href="https://pastebin.pl/view/raw/9b798fb5">Discord</a></h3></body></html>'

	with open(title + ".html", "w", encoding='utf-8') as file:
		file.write(HTML_HEAD + processingwords(text) + HTML_END)
	from_file(title + ".html", f"{title}.pdf")
	remove(title + ".html")

#Author: Serhat Dogan
#github.com/serhatdog