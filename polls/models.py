import datetime
from django.db import models

# timezone: https://docs.djangoproject.com/ja/4.0/topics/i18n/timezones/
# DBにはUTCを登録し、APP側で特定のtimezoneに変換する場合に利用するライブラリ
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        """直近24時間で公開されている場合はTrue"""
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text