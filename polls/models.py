
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(verbose_name='date published')

    def __str__(self):
        return "%s" %self.question_text 

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class User(models.Model):
    last_name = models.CharField(max_length=64,blank=True)

    class Meta:
        abstract = True # wont saved in db
             
class Author(User):
    first_name = models.CharField(max_length=64)

    class Meta: # additional sets
        verbose_name = 'Author' # for admin
        verbose_name_plural = 'Authors' #for admin
        ordering = ['-first_name'] # sort by field (- is down)
        db_table = 'Test Table' # name table in db
        unique_together = ('first_name','last_name') # complex key 

class UaAuthor:
    
    class Meta:
        proxy = True # proxy it is proxy..whou


class Ganre(models.Model):
    name = models.CharField(max_length=64)

class BookManager(models.Manager):
    def author1(self):
        return self.get_queryset().filter(first_name='author')

class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='books')
    ganres = models.ManyToManyField(Ganre,related_name='books',through='BookGanre',default=[])

    objects=BookManager()
    man = BookManager()

    comments = GenericRelation('Comment',related_query_name='book')



class BookGanre(models.Model):

    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    ganre = models.ForeignKey(Ganre,on_delete=models.CASCADE)   
    date_add = models.DateField(auto_now_add=True)


class Comment(models.Model):
    text = models.CharField(max_length=150)
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id = models.IntegerField()

    content_object = GenericForeignKey('content_type','object_id')

def FillDB():
    a1 = Author.objects.create(first_name='A',last_name='B')
    a2 = Author.objects.create(first_name='B',last_name='C')
    a3 = Author.objects.create(first_name='C',last_name='A')

    ga = Ganre.objects.create(name='ganre A')
    gb = Ganre.objects.create(name='ganre B')
    gc = Ganre.objects.create(name='ganre C')

    ba = Book.objects.create(title='Book A',author=a1)
    bb = Book.objects.create(title='Book B',author=a1)
    bc = Book.objects.create(title='Book C',author=a1)
    models.JSONField(encoder="")
    a1.save()
    a2.save()
    a3.save()
    ga.save()
    gb.save()
    gc.save()
    ba.save()
    bb.save()
    bc.save()