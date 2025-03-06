from tortoise.models import Model
from tortoise.fields import BigIntField, CharField, IntField

from backend.utils.constants import MAX_LEN_CHARFIELD


class User(Model):
    """Класс пользователя."""

    id = IntField(pk=True)
    telegram_id = BigIntField(unique=True)
    username = CharField(max_length=MAX_LEN_CHARFIELD, null=True)
    first_name = CharField(max_length=MAX_LEN_CHARFIELD)
    last_name = CharField(max_length=MAX_LEN_CHARFIELD)
