from django.db import models,connection
from math import ceil
# Create your models here.


class MediaDate(models.Model):
    class Meta:
        db_table='media_dict'
    filename = models.CharField(max_length=255,default=None)
    majortype= models.CharField(max_length=255,default=None)
    minortype = models.CharField(max_length=255,default=None)
    value = models.CharField(max_length=500,default=None)
    domain = models.CharField(max_length=200,default=None)

    def save_all(self,data_list):
        insert_list = list()
        for data in data_list:
            cur_list = list()
            cur_list.append(data.get('filename'),None)
            cur_list.append(data.get('majortype'),None)
            cur_list.append(data.get('minortype'),None)
            cur_list.append(data.get('value'),None)
            cur_list.append(data.get('domain'),None)
            insert_list.append(cur_list)
        with connection.cursor() as cursor:
            for num in range(ceil(len(insert_list)/5000)):
                cur_list = insert_list[num*5000,(num+1)*5000]
                insert_sql = "insert into media_dict values %s"
                cursor.excute(insert_sql,cur_list)















