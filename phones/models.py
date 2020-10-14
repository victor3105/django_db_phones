from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    price = models.DecimalField(max_length=6)
    image = models.CharField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        # Check if it is a newly created object
        if not self.id:
            self.slug = slugify(self.name)

        super(Phone, self).save(*args, **kwargs)
