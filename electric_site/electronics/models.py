from django.db import models


class Electronics(models.Model):
    title = models.CharField(max_length=254)
    content = models.TextField(unique=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    


"""
dt = Electronics(title="Samsung S4", content="modificato")
dt.save()

dt.id # id oggetto
dt.pk # id oggetto ..

# lista delle querry fatte al db
>>> from django.db import connection
>>> connection.queries

# inserisce direttamente i dati nella tabella
quer = Electronics.objects.create(title="Samsung S4", content="modificato")

# CERCA i/il dati che hanno title='Samsung S3'
>>> lst = Electronics.objects.filter(title='Samsung S3')
>>> lst
<QuerySet [<Electronics: Electronics object (1)>]>

#ESCLUDE i dati che hanno l`id = 2
>>> quer = Electronics.objects.exclude(pk=2)
>>> quer
<QuerySet [<Electronics: Electronics object (1)>, <Electronics: Electronics object (3)>]>

            MODIFICARE un dato

>>> lst = Electronics.objects.get(title='Samsung S3')
>>> lst.title = lst.title.uper() # modificato in uppercase
>>> lst.save

             RIMUOVERE un dato
lst = Electronics.objects.get(title='Samsung S3')
lst.delete()



"""


"""CharField(
    verbose_name: str | bytes | None = ...,
    name: str | None = ..., 
    primary_key: bool = ..., 
    max_length: int | None = ...,
    unique: bool = ..., 
    blank: bool = ..., null: bool = ..., 
    db_index: bool = ..., 
    default: Any = ..., 
    editable: bool = ..., 
    auto_created: bool = ..., 
    serialize: bool = ..., 
    unique_for_date: str | None = ..., 
    unique_for_month: str | None = ..., 
    unique_for_year: str | None = ..., 
    choices: _FieldChoices | None = ..., 
    help_text: str = ..., 
    db_column: str | None = ..., 
    db_tablespace: str | None = ..., 
    validators: Iterable[_ValidatorCallable] = ..., 
    error_messages: _ErrorMessagesToOverride | None = ..., 
    db_collation: str | None = ...
) -> None"""