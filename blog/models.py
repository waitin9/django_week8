# blog/models.py
from django.db import models
from django.urls import reverse # new
class Post(models.Model):
 title = models.CharField(max_length=200)
 author = models.ForeignKey(
 "auth.User",
 on_delete=models.CASCADE,
 )
 body = models.TextField()
 def __str__(self):
    return self.title
 def get_absolute_url(self): # new
    return reverse("post_detail", kwargs={"pk": self.pk})

# blog/models.py
from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    
    # 這個 ForeignKey 會自動對接 Django 內建的 User 表 (對應圖片右半邊)
    # 並在資料庫底層將 author 連結到 user_id
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})