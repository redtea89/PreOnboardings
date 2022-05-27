import os, django, csv
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from apps.madup.models import AdvertisingData, Advertiser
CSV_PATH= 'apps/madup/source_data/Madup_Wanted_Data_set.csv'

with open(CSV_PATH) as in_file:
    """
    Advertiser 입력
    """
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        id = row[0]
        try:
            Advertiser.objects.create(id = id)
        except:
            pass


date_format = '%Y.%m.%d'
with open(CSV_PATH) as in_file:
    """
    AdvertingData 입력
    """
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        uid = row[1]
        media = row[2]
        # date 포멧변환하여 넣기
        date = datetime.strptime(row[3], date_format)
        date = date.date()

        cost = row[4]
        impression = row[5]
        click = row[6]
        conversion = row[7]
        cv = row[8]
        advertiser_id = row[0]
        AdvertisingData.objects.create(
            uid = uid,
            media = media,
            date = date,
            cost = cost,
            impression = impression,
            click = click,
            conversion = conversion,
            cv = cv,
            advertiser_id = advertiser_id
            )

