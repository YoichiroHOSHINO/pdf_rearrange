import sys
import math
from pypdf import PdfReader, PdfWriter

page_rearrange = [1,4,5,8,3,2,7,6]

file = sys.argv[1].strip()

reader = PdfReader(file)
writer = PdfWriter()

term = len(page_rearrange)
all_pages = len(reader.pages)

c = math.ceil(all_pages / term)

for n in range(c):
    for i in range(term):
        p = n * term + page_rearrange[i]
        if p > all_pages:
            writer.add_blank_page()
        else:
            writer.add_page(reader.pages[p - 1])

with open(file + '_RA.pdf', 'wb') as fp:
    writer.write(fp)



