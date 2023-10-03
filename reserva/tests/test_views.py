from pytest_django.asserts import assertTemplateUsed

import pytest
from datetime import timedelta, date
from reserva.models import Reserva

@pytest.fixture
def dados_validos():
    amanha = date.today() + timedelta(days=1)
    dados = {
        'nome': 'João',
        'email': 'joao@email.com',
        'nome_pet': 'Tom',
        'data_apenas': amanha,
        'turno': 'tarde',
        'tamanho': 0,
        'observacoes': 'O tom esta bem fedorento'
    }
    return dados

@pytest.mark.django_db
def test_reserva_view_deve_retornar_template(client):
    response = client.get('/reserva/criar/')

    assert response.status_code == 200
    assertTemplateUsed(response, 'criar_reserva.html')

@pytest.mark.django_db
def test_reserva_view_deve_retornar_sucesso(client, dados_validos):

    response = client.post('/reserva/criar/', dados_validos)

    assert response.status_code == 200
    assert 'Reserva realizada com sucesso' in str(response.content)

@pytest.mark.django_db
def test_reserva_view_deve_criar_sucesso(client, dados_validos):
    client.post('/reserva/criar/', dados_validos)

    assert Reserva.objects.all().count() == 1
    reserva = Reserva.objects.first()

    assert reserva.nome == dados_validos['nome']    
    assert reserva.nome_pet == dados_validos['nome_pet']    

# Testes da tarefa da semana.

@pytest.mark.django_db
def test_resgatar_agendamento(dados_validos):
    reserva = Reserva.objects.create(**dados_validos)
    agendamento_resgatado = Reserva.objects.get(id=reserva.id)

    assert agendamento_resgatado.nome == dados_validos['nome']
    assert agendamento_resgatado.email == dados_validos['email']
    assert agendamento_resgatado.nome_pet == dados_validos['nome_pet']
    assert agendamento_resgatado.data_apenas == dados_validos['data_apenas']
    assert agendamento_resgatado.turno == dados_validos['turno']
    assert agendamento_resgatado.tamanho == dados_validos['tamanho']
    assert agendamento_resgatado.observacoes == dados_validos['observacoes']

@pytest.mark.django_db
def test_atualizar_agendamento(dados_validos):
    reserva = Reserva.objects.create(**dados_validos)

    novo_nome_pet = 'Rex'
    reserva.nome_pet = novo_nome_pet
    reserva.save()

    agendamento_atualizado = Reserva.objects.get(id=reserva.id)
    assert agendamento_atualizado.nome_pet == novo_nome_pet

@pytest.mark.django_db
def test_remover_agendamento(dados_validos):

    reserva = Reserva.objects.create(**dados_validos)

    reserva.delete()

    with pytest.raises(Reserva.DoesNotExist):
        Reserva.objects.get(id=reserva.id)