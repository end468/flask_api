from model.base_model import base_model, EnumField
from peewee import  PrimaryKeyField ,CharField,IntegerField


class course(base_model):
    id = PrimaryKeyField()
    presentation = EnumField(choices=['practical' , 'theoric'])
    type =EnumField(choices=['prpfessional','basic','prime','public'])
    status_prerequisite=EnumField(choices=['yes','no'])
    name = CharField(30)
    unit_number = IntegerField(30)
    price = IntegerField(30)
    list_prerequisite = CharField()
    class Meta:
        db_table = 'course'

