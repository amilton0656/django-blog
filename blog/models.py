from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field

class Post(models.Model):
    autor = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    resumo = CKEditor5Field('Texto', config_name='default', blank=True, null=True)
    conteudo = CKEditor5Field('Texto', config_name='default', blank=True, null=True)
    # IMPORTANTE: gravar em MEDIA_ROOT/blog/, NÃO em static/
    imagem_capa = models.ImageField(upload_to='blog/', blank=True, null=True)
    data_publicacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo
