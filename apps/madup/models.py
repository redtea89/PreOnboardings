from django.db import models


class Advertiser(models.Model):
    """
    광고주 데이터
    """
    name = models.CharField(max_length=30)
    email = models.EmailField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'advertiser_info'


class AdvertisingData(models.Model):
    """
    광고주를 FK로 설정한 광고데이터
    """
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)
    uid = models.CharField(max_length=100)
    media = models.CharField(max_length=30)
    date = models.DateField()
    cost = models.IntegerField()
    impression = models.IntegerField()
    click = models.IntegerField()
    conversion = models.IntegerField()
    cv = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'advertising_data'