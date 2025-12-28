from django.db import models
from django.conf import settings

class BlogPost(models.Model):
    # 19-1要求的基本字段
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    # 19-5要求的用户关联
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    
    class Meta:
        ordering = ['-date_added']  # 按时间倒序
    
    def __str__(self):
        return self.title
