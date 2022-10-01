from django.db import models

class Category(models.Model):
    categ = models.CharField(max_length=36)
    subcategory = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        if self.subcategory:
            return f"{self.categ}-->{self.subcategory}"
        return f"{self.categ}"