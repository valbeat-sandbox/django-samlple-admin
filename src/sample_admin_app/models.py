from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from sample_admin_app.managers import PersonManager

class Person(AbstractBaseUser):
    """
    人
     * 人の情報を格納する。
     - name: 名前
     - birthday: 誕生日
     - sex: 性別
     - email: メールアドレス
    """
    # sex
    MAN = 0
    WOMAN = 1

    objects = PersonManager()

    identifier = models.CharField(max_length=64, unique=True, blank=False)
    name = models.CharField(max_length=128)
    birthday = models.DateTimeField()
    sex = models.IntegerField(editable=False)
    email = models.EmailField()

    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'identifier'

class Manager(models.Model):
    """
    マネージャー
     * マネージャー
     - person: 人
     - joined_at: 着任日
     - quited_ad: 辞任日
    """
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    joined_at = models.DateTimeField()
    quited_at = models.DateTimeField(null=True, blank=True)

class Member(models.Model):
    """
    メンバー
     * メンバー
     - person: 人
     - joined_at: 着任日
     - quited_ad: 辞任日
     - manager: 上長
    """
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    joined_at = models.DateTimeField()
    quited_at = models.DateTimeField(null=True, blank=True)
    manager = models.ForeignKey(Manager, on_delete=models.PROTECT)