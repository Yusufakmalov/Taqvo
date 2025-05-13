from django.db import models



class Category(models.Model):

    objects = models.Manager()

    title = models.CharField(max_length=25)
    slug = models.SlugField(max_length=50)

    class Meta:
        db_table = 'Main_category'  # Use exact PostgreSQL table name if different

    def __str__(self):
        return self.title


class Meat(models.Model):

    objects = models.Manager()

    class Status(models.TextChoices):
        AVAILABLE = 'AV', 'Available'
        NOT_AVAILABLE = 'NV', 'Not Available'

    title = models.CharField(max_length=25)
    price = models.IntegerField(default=0)
    numeration = models.IntegerField(blank=True, null=True, default=0)
    slug = models.SlugField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='meats')
    amount_kg = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.AVAILABLE)
    photo = models.ImageField(upload_to='posts/', null=True, blank=True)
    body = models.TextField(blank=True, null=True)
    arrival_date = models.DateTimeField(null=True, blank=True)
    sold_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'Main_meat'  # Use exact PostgreSQL table name if different

    def __str__(self):
        return self.title



