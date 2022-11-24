from django.db import models


class Makeup(models.Model):
    name = models.CharField(max_length=20, verbose_name="Название")
    opisanie = models.TextField(verbose_name="Описание")
    stoimost = models.IntegerField(verbose_name="Стоимость")
    foto = models.ImageField(upload_to='makeup/')

    def __str__(self):
        return self.name

class Pricheski(models.Model):
    name = models.CharField(max_length=20, verbose_name="Название")
    opisanie = models.TextField(verbose_name="Описание")
    stoimost = models.IntegerField(verbose_name="Стоимость")
    foto = models.ImageField(upload_to='pricheski/')

    def __str__(self):
        return self.name


class Kvalifikaciya(models.Model):
    opyt = models.CharField(max_length=20, verbose_name="Опыт")
    procent = models.FloatField(verbose_name="Процент")

    def __str__(self):
        return self.opyt


class Vizajisti(models.Model):
    fam = models.CharField(max_length=45, verbose_name="Фамилия")
    name = models.CharField(max_length=20, verbose_name="Имя")
    kvalifikaciya = models.ForeignKey(Kvalifikaciya, on_delete=models.PROTECT, verbose_name="Квалификация")
    foto = models.ImageField(upload_to='vizajisti/')

    def __str__(self):
        return f"{self.fam}  {self.name}"


class Zayavki(models.Model):
    name_klient = models.CharField(max_length=20, verbose_name='Имя')
    telephon = models.CharField(max_length=18, verbose_name='Телефон')
    data_sozd = models.DateTimeField(auto_now=True)
    data_vypoln = models.DateTimeField(verbose_name="Дата и время")
    pricheski = models.ForeignKey(Pricheski, on_delete=models.PROTECT, verbose_name="Причёска")
    makeup = models.ForeignKey(Makeup, on_delete=models.PROTECT, verbose_name="Макияж")
    vizajist = models.ForeignKey(Vizajisti, on_delete=models.PROTECT, verbose_name="Визажист")

    def __str__(self):
        return self.name_klient
