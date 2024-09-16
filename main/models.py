from django.db import models
import uuid

class ProductEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1) 
    quantity = models.IntegerField()
    
    @property
    def is_out_of_stock(self):
        return self.quantity == 0