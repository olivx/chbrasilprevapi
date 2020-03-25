import pytest
from django.contrib.auth import get_user_model
from model_mommy import mommy


@pytest.mark.django_db
def user_has_fields():
    fileds = ('nome', 'rua', 'bairro', 'cidade', 'cep', 'is_admin', 'date_joined', 'email', 'id',)
    user =  mommy.make(get_user_model())
    for field in user._meta.fields: 
        assert field.name in fileds
