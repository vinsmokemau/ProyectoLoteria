"""Game's Models."""
from django.db import models
from django.urls import reverse


class Game(models.Model):

    class Meta:
        verbose_name = "Juego"
        verbose_name_plural = "Juegos"

    def get_absolute_url(self):
        return reverse('game:game_detail', kwargs={'game_id': self.pk})


class Board(models.Model):

    game = models.ForeignKey(
        'Game',
        related_name='boards',
        on_delete=models.CASCADE,
    )
    player = models.CharField(
        'jugador',
        max_length=50,
    )

    class Meta:
        verbose_name = "Tablero"
        verbose_name_plural = "Tableros"

    def __str__(self):
        return self.player

    @property
    def not_checked_cards(self):
        list_cards = []
        for card in self.cards.all():
            if not (card.checked):
                list_cards.append(card.card.name)
        return list_cards

    def winner(self):
        cards = {}
        for card in self.cards.order_by('position'):
            cards[card.position] = card
        # Vertical Wins
        if cards[1].checked and cards[5].checked and cards[9].checked and cards[13].checked:
            return True
        elif cards[2].checked and cards[6].checked and cards[10].checked and cards[14].checked:
            return True
        elif cards[3].checked and cards[7].checked and cards[11].checked and cards[15].checked:
            return True
        elif cards[4].checked and cards[8].checked and cards[12].checked and cards[16].checked:
            return True
        # Horizontal Wins
        elif cards[1].checked and cards[2].checked and cards[3].checked and cards[4].checked:
            return True
        elif cards[5].checked and cards[6].checked and cards[7].checked and cards[8].checked:
            return True
        elif cards[9].checked and cards[10].checked and cards[11].checked and cards[12].checked:
            return True
        elif cards[13].checked and cards[14].checked and cards[15].checked and cards[16].checked:
            return True
        # Diagonal Wins
        elif cards[1].checked and cards[6].checked and cards[11].checked and cards[16].checked:
            return True
        elif cards[4].checked and cards[7].checked and cards[10].checked and cards[13].checked:
            return True
        else:
            return False


class GameCard(models.Model):

    board = models.ForeignKey(
        'Board',
        related_name='cards',
        on_delete=models.CASCADE,
    )
    position = models.IntegerField(
        'posicion',
    )
    card = models.ForeignKey(
        'deck.Card',
        on_delete=models.CASCADE,
    )
    checked = models.BooleanField(
        default=False,
    )

    class Meta:
        verbose_name = "Carta de Juego"
        verbose_name_plural = "Carta de Juegos"

    def __str__(self):
        return str(self.position)
