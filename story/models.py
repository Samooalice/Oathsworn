from django.db import models

class TranslatedLine(models.Model):
    chap = models.CharField(max_length=100)
    eng = models.TextField()
    kor = models.TextField()

    class Meta:
        managed = False 
        db_table = 'translated_lines' 