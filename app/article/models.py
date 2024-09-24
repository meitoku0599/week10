import uuid

from django.db import models

from markdownx.models import MarkdownxField

# Create your models here.


class Article(models.Model):

    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False, unique=True)
    image = models.ImageField('イメージ写真', upload_to='article/images', null=True, blank=True)
    meta_keywords = models.CharField('メタキーワード', max_length=155)
    meta_description = models.TextField('メタ説明文')
    title = models.CharField('タイトル', max_length=100)
    body = MarkdownxField('本文')
    views = models.PositiveIntegerField('閲覧数', default=0)
    is_published = models.BooleanField('公開済', default=False)
    created = models.DateTimeField('作成日時', auto_now=True)
    update = models.DateTimeField('更新日時', auto_now_add=True)

    #def get_absolute_url(self):

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = '記事'