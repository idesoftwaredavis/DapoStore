from django.db import models

# Create your models here.
class ModelAdministrador(models.Model):
    username = models.CharField(
            verbose_name="nombre usuario",
            max_length=50,
            null=False,
            blank=False
            )

    password = models.CharField(
            verbose_name="Contraseña",
            max_length=20,
            null=False,
            blank=False
            )
    security_question = models.CharField(
            verbose_name="Pregunta Seguridad",
            max_length = 50,
            )
    answer_question = models.CharField(
            verbose_name = "Respuesta Seguridad",
            max_length = 100,
            null= False,
            default = "Respuesta"
    )


    def __str__(self):
        return self.username + ' | pregunta seguridad : |' +  self.security_question


class Product(models.Model):
    name = models.CharField(
            verbose_name= "Nombre Producto",
            max_length = 50,
            null = False,
            blank = False
    )

    short_description = models.CharField(
            verbose_name = "Descripcion Corta",
            max_length = 100,
            null = False,
            blank = False
    )

    description = models.CharField(
            verbose_name = "Descripcion",
            max_length = 200,
            null = False,
            blank = False
    )

    mg = models.IntegerField()

    quantity = models.IntegerField(verbose_name="Cantidad")

    price = models.CharField(verbose_name="precio", max_length=50, null=False,blank=False)

    stock = models.BooleanField(verbose_name="Disponibilidad")

    def __str__(self):
        resultado = ''
        if self.stock == True:
            resultado = "Disponible"
        else:
            resultado = "No disponible"
        return self.name + ' Disponibilidad : ' + resultado
