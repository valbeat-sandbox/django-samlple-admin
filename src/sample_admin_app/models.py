from django.db import models

class Person(models.Model):
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

    name = models.CharField(max_length=128)
    birthday = models.DateTimeField()
    sex = models.IntegerField(editable=False)
    email = models.EmailField()

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