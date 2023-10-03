import datetime
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, ValidationError, HyperlinkedRelatedField

from reserva.models import Petshop, Reserva, CategoriaPet
from base.models import Contato

class CategoriaPetRelatedFieldCustomSerializer(PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = CategoriaPetNestedModelSerializer
        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False
    
    def to_representation(self, value):
        return self.serializer(value, context=self.context).data

class CategoriaPetModelSerializer(ModelSerializer):
    reservas = HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='api:reserva-detail'
    )

class CategoriaPetNestedModelSerializer(ModelSerializer):
    class Meta:
        model = CategoriaPet
        fields = '__all__'

class PetShopRelatedFieldCustomSerializer(PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = PetshopNestedModelSerializer
        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False
    
    def to_representation(self, value):
        return self.serializer(value, context=self.context).data

class PetshopModelSerializer(ModelSerializer):
    reservas = HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='api:reserva-detail'
    )

class PetshopNestedModelSerializer(ModelSerializer):
    class Meta:
        model = Petshop
        fields = '__all__'

class AgendamentoModelSerializer(ModelSerializer):
    petshop = PetShopRelatedFieldCustomSerializer(
        queryset=Petshop.objects.all(),
        read_only=False
    )

    categoria = CategoriaPetRelatedFieldCustomSerializer(
        queryset=CategoriaPet.objects.all(),
        read_only=False
    )

    def validate_data(self, value):
        hoje = datetime.date.today()
        if value.date() < hoje:
            raise ValidationError('Não é possível realizar um agendamento para o passado!')
        return value

    class Meta:
        model = Reserva
        fields = '__all__'

class ContatoModelSerializer(ModelSerializer):
    class Meta:
        model = Contato
        fields = '__all__'