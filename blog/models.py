from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)  #포스트 제목
    content = models.TextField()             #포스트 내용

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    #Y: 2022, #y:22
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)  #시간
    updated_at = models.DateTimeField(auto_now=True)

    # 추후 author

    def __str__(self):
        return f'[{self.pk}]{self.title}   {self.created_at}'


    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
