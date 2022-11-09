from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


#สำหรับภาษาไทยต้อง ทำการลงทะเบียนเพิ่มภาษาไทยก่อนนะครับ
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
pdfmetrics.registerFont(TTFont('THSarabunNew', 'THSarabunNew.ttf'))
#------------------------------------------

packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=letter)
can.setFillColorRGB(1, 0, 0)
can.setFont("THSarabunNew", 14)
can.drawString(150, 645, "นาย อภิชาติ หาจัตุรัส")
can.save()

packet.seek(0)
new_pdf = PdfFileReader(packet)


existing_pdf = PdfFileReader(open("a1.pdf", "rb"))
output = PdfFileWriter()

page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)


outputStream = open("destination.pdf", "wb")
output.write(outputStream)
outputStream.close()
