from django.contrib import admin
from django.http import HttpResponseRedirect
from customers.models import Customer, CustomerSaveMonth

from django.http import FileResponse
import io
from reportlab import pdfgen
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from datetime import datetime
# Register your models here.

class CreateCustomer(admin.ModelAdmin):
     list_display = ['id','name','lastname','identification','phone_number','email','address','create_date']
     list_filter = ['create_date']
     search_fields = ["identification"]


class CustomerInvoice(admin.ModelAdmin):
    model = CustomerSaveMonth
    list_display = ['id','name_customer','description','amount_save_money']
    change_form_template = 'invoice/invoice_button.html'
    list_filter = ['create_date']
    search_fields = ["name_customer"]
    
    def response_change(self, request, obj):
        #if "_make-unique" in request.POST:
       
        return create_invoice(obj=obj)
       


admin.site.register(CustomerSaveMonth,CustomerInvoice)
admin.site.register(Customer,CreateCustomer)


def create_invoice(obj):

    #Create byteStream buffer
    buf = io.BytesIO()
    #create a canvas
    c = canvas.Canvas(buf,pagesize=letter,bottomup=0)
    #create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica",14)


    lines =[
        "COOPERATIVA UNIDOS PODEMOS\nDirección: Calle Duarte #2 KM 18 Villa Mella Republica Dominicana\nRNC: 4-30-38208-6\nTelefono: 809-748-5652\n\n\nNo. Socio: {}\n\nNombre del Socio: {}\n\nLa suma de: {} pesos por concepto de ahorro mensual\n\nFecha recibo: {}\n\n\n\n\n\n\n\nEntregado Por:-------------------         Recibido Por:-------------------".format(obj.id,obj.id_customer,obj.amount_save_money,datetime.today().strftime('%m-%d-%Y'))
    
    ]

    for line in lines:
        textob.textLines(line,trim=2)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf,as_attachment=True,filename= 'Test_PDF.pdf')