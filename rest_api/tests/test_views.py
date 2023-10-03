import pytest 
from rest_framework.test import APIClient
from datetime import date
from reserva.models import Petshop, Reserva, CategoriaPet
from rest_api.serializers import PetshopModelSerializer
from model_bakery import baker

@pytest.fixture
def dados_agendamento():
    hoje = date.today()
    petshop = baker.make(Petshop)
    categoria = baker.make(CategoriaPet)
    print(petshop.pk)
    return {
        'petshop': petshop.pk,
        'categoria': categoria.pk,
        'nome': 'Maria da Silva',
        'email': 'maria@email.com',
        'nome_pet': 'Mel',
        'data_apenas': hoje,
        'turno': 'tarde',
        'tamanho': 0,
        'observacoes': 'Observação'}
    
@pytest.fixture
def usuario():
    return baker.make('auth.User')

@pytest.mark.django_db
def test_criar_agendamento(usuario, dados_agendamento):
    cliente = APIClient()
    cliente.force_authenticate(usuario)
    resposta = cliente.post('/api/agendamento', dados_agendamento, format="json")
    print(resposta.json())
    print(dados_agendamento)
    assert resposta.status_code == 201

@pytest.fixture
def agendamento():
    return baker.make(Reserva)

@pytest.mark.django_db
def test_todos_agendamentos(agendamento):
    cliente = APIClient()
    resposta = cliente.get('/api/agendamento')
    assert len(resposta.data['results']) == 1

@pytest.fixture
def petshops():
    return baker.make(Petshop, _quantity=3)

@pytest.mark.django_db
def test_todos_petshops():
    cliente = APIClient()
    resposta = cliente.get('/api/petshop',)
    assert len(resposta.data['results']) == 0