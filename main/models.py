from django.db import models

class Products(models.Model):

    CHOICE_TYPE = (
        ('Pizza', 'Пицца'),
        ('Another', 'Другое'),
    )

    name = models.CharField(max_length=50, verbose_name="Имя")
    type = models.CharField(max_length=50, choices=CHOICE_TYPE, default='Pizza', verbose_name="Тип")
    character = models.TextField(max_length=100, verbose_name="Характеристика")
    price = models.IntegerField(max_length=50, verbose_name="Цена")
    image = models.ImageField(null=True, blank=True, upload_to="image/")

    class Meta:
        
        verbose_name = 'товар'
        verbose_name_plural = 'список товаров'
        

    def __str__(self):
        return self.name
    
class record(models.Model):
    name = models.CharField(max_length=150, verbose_name='ФИО')
    number = models.CharField(max_length=150, verbose_name='Номер телефона')
    message = models.CharField(max_length=200, verbose_name='Сообщение')
    
    class Meta:
#        managed = False
        db_table = 'record'
        verbose_name = 'запись'
        verbose_name_plural = 'Записи'
        
    def __str__(self):
        return self.message
    
class completedrecord(models.Model):
    record = models.ForeignKey(record, on_delete=models.CASCADE, null=True, blank=True,verbose_name = 'Выберите клиента')
    completed_work = models.TextField('Назначенное время и доп. условия', default="")

    class Meta:
#        managed = False
        db_table = 'completedrecord'
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи Выполненые'
        
    def __str__(self):
        return self.completed_work
