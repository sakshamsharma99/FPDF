#Virtal Environment: py -m venv myworld
#Activate Environment: myworld\Script\activate.bat
#pip install fpdf2

from fpdf import FPDF
#create FPDF object
#Layout ('P','L')
#Unit ('mm','cm','in')
#forma('A3','A4'(default),'A5','Letter','Legal',(100,150)
pdf = FPDF('p','mm','Letter')

#Add a page
pdf.add_page()

#Specify font
#fonts('times','courier','helvetica','Symbol','zpfdingbats')
#'B' (bold), 'U' (underline), 'I' (italics), '' (regular),combination(i.e.,('BU'))
pdf.set_font('times','',16)
pdf.set_text_color(220,50,50)

#Add text
# w = Width
# h = Height
# txt = your text
# ln (0 False; 1 True - for next line)
# border (0 False; 1 True)
pdf.cell(40,30,'Saksham Sharma',ln=True,border=True)
pdf.cell(80,10,'2135000047')

pdf.output('s1.pdf')