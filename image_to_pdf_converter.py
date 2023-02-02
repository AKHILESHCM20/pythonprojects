from fpdf import FPDF
pdf=FPDF()
img=["1.jpeg"]
for i in img:
     pdf.add_page()
     pdf.image(i,x,y,h,w)
pdf.output("1.pdf","F")
