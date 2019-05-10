import uuid as uuid
from django.db import models

# Create your models here.
class Subscriptions(models.Model):

    uuid = models.UUIDField(primary_key=False, default= uuid.uuid4, editable= False)
    name = models.CharField('nome',max_length= 250)
    cpf = models.CharField('CPF',max_length= 11)
    email = models.EmailField('e-mail')
    phone = models.CharField('telefone',max_length= 20)
    created_at = models.DateTimeField('criado em',auto_now_add= True)
    paid = models.BooleanField('pago',default= False)

    class Meta:
        verbose_name = 'inscrição'
        verbose_name_plural = 'inscrições'

    def __str__(self):

        return self.name