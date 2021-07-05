from django.db import models

class Libro(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=99)
    Autor = models.CharField(max_length=99)
    Sinopsis = models.TextField
    Precio = models.IntegerField(default=0)
    Stock = models.IntegerField(default=0)
    Publicacion = models.DateField()
    
    def __str__(self):
        return 'Id= %s, Nombre= %s, Autor= %s, Sinopsis= %s, Precio= %i, Stock= %i, Publicacion = %s' % (
            self.Id, self.Nombre, self.Autor, self.Sinopsis, self.Precio, self.Stock, self.Publicacion
            )

