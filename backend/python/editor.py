from pypdf import PdfReader, PdfWriter
import math
import sys
importedDocumentPath = sys.argv[1]
exportedDocumentPath = sys.argv[2]
#[editorFile, importedDocument, exportedDocumentFolder]
pageIndex = -1
currentHeading = ""
headings = []
def findHeadingVisitor(text, cm, tm, font_dict, font_size):
    global currentHeading
    heading = ""
    if(tm[4] != 0 or tm[5] != 0):
        size = abs(int(tm[3]))#font size
        if(size >= 40):
            currentHeading += text
    
    
    

def makeHeadingList(documentPath):#stores headings in title, page format in glob headings
    global currentHeading
    global pageIndex
    reader = PdfReader(documentPath)
    totalpageLength = len(reader.pages)
    
    for i in range(7, totalpageLength):
        pageIndex = i
        page = reader.pages[pageIndex]
        #move all fragments of a heading on a pageIndex into current Heading
        parts = page.extract_text(extraction_mode='plain', visitor_text=findHeadingVisitor);
        
        #add final heading and pageIndex into headings
        if(currentHeading != ""):
            headings.append({"title":currentHeading, "pageIndex": pageIndex})
        currentHeading = ""
def writeToTableOfContent(importDocumentPath, exportDocumentPath):
    writer = PdfWriter(clone_from=importDocumentPath)
    makeHeadingList(documentPath=importDocumentPath)
    for heading in headings:
        writer.add_outline_item(title=heading["title"], page_number=int(heading["pageIndex"]))
    writer.write(exportedDocumentPath)
    print("aaaaaa")
    sys.stdout.flush()
writeToTableOfContent(importDocumentPath=importedDocumentPath, exportDocumentPath=exportedDocumentPath)
# print("aaaa")
sys.stdout.flush()        

