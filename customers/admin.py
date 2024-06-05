from django.contrib import admin
from django.http import HttpResponseRedirect
from customers.models import Customer, CustomerSaveMonth

from django.http import FileResponse
import io
from reportlab import pdfgen
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
# Register your models here.

class CreateCustomer(admin.ModelAdmin):
     list_display = ['id','name','lastname','identification','phone_number','email','address','create_date']


class CustomerInvoice(admin.ModelAdmin):
    list_display = ['id','name_customer','description','amount_save_money']
    change_form_template = 'invoice/invoice_button.html'
    
    def response_change(self, request, obj):
        #if "_make-unique" in request.POST:
        return create_invoice()
       


admin.site.register(CustomerSaveMonth,CustomerInvoice)
admin.site.register(Customer,CreateCustomer)


def create_invoice():
    #Create byteStream buffer
    buf = io.BytesIO()
    #create a canvas
    c = canvas.Canvas(buf,pagesize=letter,bottomup=0)
    #create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica",14)

    lines =[
        "COOPERATIVA UNIDOS PODEMOS\nDirección: Villa Mella Republica Domoinicana\nTelefono: 8093457654\n\n\nNo. Socio: 2245\n\nNombre del Socio: Manuel Montolio\n\nLa suma de: 800 pesos por concepto de ahorro mensual\n\nFecha recibo: 01/01/2024\n\n\n\n\n\n\n\nEntregado Por:-------------------         Recibido Por:-------------------"
    
    ]

    for line in lines:
        textob.textLines(line,trim=2)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf,as_attachment=True,filename= 'Test_PDF.pdf')