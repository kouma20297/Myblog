from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="カテゴリ名")

    def __str__(self):
        return self.name

    class meta:
        verbose_name = "カテゴリ"


class Article(models.Model):
    title = models.CharField(max_length=70, verbose_name="タイトル")
    body = models.TextField(verbose_name="本文")
    creator = models.CharField(max_length=70, verbose_name="投稿者")
    modifier = models.CharField(max_length=70, verbose_name="更新者")
    created = models.DateTimeField(verbose_name="投稿日時")
    modified = models.DateTimeField(verbose_name="更新日")
    liked = models.IntegerField(default=0, verbose_name="いいね数")

    def __str__(self):
        return self.title

    class meta:
        verbose_name = "記事"


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="記事", related_name="comment")
    commenter = models.CharField(max_length=30, verbose_name="コメント作者")
    body = models.TextField(verbose_name="コメント")
    created = models.DateTimeField(auto_now_add=True, verbose_name="コメント投稿日時")

    def __str__(self):
        return self.article.title + ":{}のコメント".format(self.commenter)

    class meta:
        verbose_name = "コメント"
