import os, django, csv
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

"""매드업용"""
# from apps.madup.models import AdvertisingData, Advertiser
# CSV_PATH= 'apps/madup/source_data/Madup_Wanted_Data_set.csv'

"""베어로보틱스용"""
from apps.bear.models import Group, Restaurant, Pos
CSV_PATH= 'apps/bear/source_data/bear_pos_example.csv'


"""
베어로보틱스 csv데이터 업로드용
"""
with open(CSV_PATH) as in_file:
    """
    Group과 Restaurant는 수동으로 입력하였음. ( 총 6개의 Rows )
    Pos 입력
    """
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        timestamp = row[1]
        restaurant_id = row[2]
        price = row[3]
        number_of_party = row[4]
        payment = row[5]
        Pos.objects.create(
            timestamp=timestamp,
            restaurant_id=restaurant_id,
            price=price,
            number_of_party=number_of_party,
            payment=payment
        )





"""
Madup csv데이터 업로드용
"""

# with open(CSV_PATH) as in_file:
#     """
#     Advertiser 입력
#     """
#     data_reader = csv.reader(in_file)
#     next(data_reader, None)
#     for row in data_reader:
#         id = row[0]
#         try:
#             Advertiser.objects.create(id = id)
#         except:
#             pass


# date_format = '%Y.%m.%d'
# with open(CSV_PATH) as in_file:
#     """
#     AdvertingData 입력
#     """
#     data_reader = csv.reader(in_file)
#     next(data_reader, None)
#     for row in data_reader:
#         uid = row[1]
#         media = row[2]
#         # date 포멧변환하여 넣기
#         date = datetime.strptime(row[3], date_format)
#         date = date.date()

#         cost = row[4]
#         impression = row[5]
#         click = row[6]
#         conversion = row[7]
#         cv = row[8]
#         advertiser_id = row[0]
#         AdvertisingData.objects.create(
#             uid = uid,
#             media = media,
#             date = date,
#             cost = cost,
#             impression = impression,
#             click = click,
#             conversion = conversion,
#             cv = cv,
#             advertiser_id = advertiser_id
#             )

