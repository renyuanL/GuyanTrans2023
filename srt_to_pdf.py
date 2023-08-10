#%%
import os
import glob
import tqdm

#%%


mp4Path= '.'


# get mp4Path from command line
import sys
if len(sys.argv) > 1:
    mp4Path= sys.argv[1]


mp4Path= 'srt_短_tmp'

fList= glob.glob(f'{mp4Path}/**/*.srt', recursive= True)

#%%
f= fList[0]
f

# Python program to convert
# text file to pdf file


from fpdf import FPDF

# save FPDF() class into
# a variable pdf
pdf= FPDF()

# Add a page
pdf.add_page()

# set style and size of font
# that you want in the pdf

#pdf.set_font("Arial", size = 12)

# open the text file in read mode
with open(f, encoding= 'utf-8') as fp:
    # insert the texts in pdf
    for x in fp:
        pdf.cell(w=200, h=10, txt= x, ln = 1, align = 'L')

    # save the pdf with name .pdf
    pdf.output(f"{f[:-4]}.pdf")


# %%
# AttributeError: 'FPDF' object has no attribute 'unifontsubset'
# https://stackoverflow.com/questions/62492664/attributeerror-fpdf-object-has-no-attribute-unifontsubset
