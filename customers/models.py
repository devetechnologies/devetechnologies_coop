from django.db import models

from base.models import BaseModel
# Create your models here.
class Customer(BaseModel):
    """Model definition for customer."""

    # TODO: Define fields here
    name = models.CharField('Nombre', max_length=25, blank=False, null=False)
    lastname = models.CharField('Apellido', max_length=25, blank=False, null=False)
    address = models.CharField('Dirección', max_length=70, blank=False, null=False)
    phone_number = models.CharField('Telefono', max_length=16, blank=False, null=False)
    email = models.EmailField('Correo Electrónico', max_length=100, unique=True,blank=False, null=False)
    cell_number = models.CharField('Celular', max_length=16, blank=False, null=False)
    identification = models.BigIntegerField('Cedula', unique=True, blank=False, null=False)
    name_wife =models.CharField('Nombre Conyugue', max_length=25, blank=True, null=False)
    cell_number_wife = models.CharField('Celular Conyugue', max_length=11, blank=True, null=False)
    email_wife = models.EmailField('Correo Electrónico Conyugue',max_length=100,blank=True,null=True)
    name_children_1 = models.CharField('Nombre Hijo 1', max_length=50, blank=True, null=True)
    name_children_2 = models.CharField('Nombre Hijo 2', max_length=50, blank=True, null=True)
    name_children_3 = models.CharField('Nombre Hijo 3', max_length=50, blank=True, null=True)
    admition_amount = models.IntegerField('Cuota de Admision',blank=False,null=False,default= 700)
    aportation_certify_amount = models.IntegerField('Cuota de Aportación',blank=False,null=False,default=500)
    amount_save_money = models.IntegerField("Cuota Mensual",blank=False,null=False,default=500)

    class Meta:
        """Meta definition for customers."""

        verbose_name = 'Crear Socio'
        verbose_name_plural = 'Crear Socios'

    def __str__(self):
        """Unicode representation of customers."""
        return self.name +" "+ self.lastname
    
class CustomerSaveMonth(BaseModel):
    amount_save_money = models.IntegerField("Cuota Mensual",blank=False,null=False,)
    description = models.CharField('Comentario', max_length=50, blank=False, null=False,default='Ahorro mensual')
    id_customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, verbose_name='Customer', null=False, blank=False)
    name_customer = models.CharField('Nombre Socio',max_length=50,blank=True,null=False)
    
    class Meta:
        """Meta definition for Customer Save."""

        verbose_name = 'Ahorro Socio'
        verbose_name_plural = 'Ahorro Socios'
        

    def __str__(self):
        """Unicode representation of customers save."""
        return self.id_customer.name
