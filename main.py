from pydocx import docx2html, Docx2Html, docx2latex
from bs4 import BeautifulSoup
from pydocx.tests import document_builder
import xml.etree.ElementTree as ElementTree

print docx2latex('/Users/samportnow/Documents/Nosek Articles/NHF2012.docx')

with open('test.tex', 'w') as f:
    f.write(docx2latex('/Users/samportnow/Documents/Nosek Articles/NHF2012.docx').encode('utf8'))
#print BeautifulSoup(
#    ElementTree.tostring(
#        Docx2Html('./pydocx/fixtures/simple.docx').root,
#    ),
#).prettify()

