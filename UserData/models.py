from django.db import models

# Create your models here.

class UserInfo(models.Model):
    email=models.EmailField(null=False,blank=False)
    username=models.CharField(primary_key=True,null=False,blank=False,max_length=20)
    
    class Meta:
        verbose_name="User Information"
    
    def __str__(self) -> str:
        return self.username