from django.db import models


class CUserName(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)

    def __str__(self):
        return self.user_name
    