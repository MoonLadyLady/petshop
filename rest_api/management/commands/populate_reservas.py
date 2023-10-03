from django.core.management.base import BaseCommand
from model_bakery import baker
from reserva.models import Reserva

class Command(BaseCommand):
    help = 'Cria dados fakes para testar a API de agendamentos'

    def handle(self, *args, **options):
        total = 50
        self.stdout.write(
            self.style.WARNING(f'Criando {total} agendamentos')
        )
        for 1 in range(total):
            reserva = baker.make(Reserva)
            reserva.save()

        self.stdout.write(
            self.style.SUCCESS('Agendamentos criados')
        )