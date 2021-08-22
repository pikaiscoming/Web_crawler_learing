# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 11:57:18 2021

@author: User
"""

from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open

def readpdf(pdffile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    
    process_pdf(rsrcmgr, device, pdffile)
    device.close()
    
    content = retstr.getvalue()
    retstr.close()
    return content

pdffile = urlopen('http://pythonscraping.com/pages/warandpeace/chapter1.pdf')

outputString = readpdf(pdffile)
print(outputString[0:10])
pdffile.close()
