"""Game's Views."""
import cv2
import numpy as np
from .models import (
    Game,
    Board,
    GameCard,
)
from deck.models import Card
from django.views.generic import (
    DetailView,
)
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from sklearn.tree import DecisionTreeClassifier
from skimage import io
from skimage.color import rgb2gray


def start_game(request):
    """Create a new game."""
    game = Game.objects.create()
    user_board = Board.objects.create(
        game=game,
        player='jugador',
    )
    computer_board = Board.objects.create(
        game=game,
        player='computadora',
    )
    count = 1
    for user_card in Card.objects.order_by('?')[:16]:
        user_game_card = GameCard(
            board=user_board,
            position=count,
            card=user_card,
        )
        user_game_card.save()
        count += 1
    count = 1
    for computer_card in Card.objects.order_by('?')[:16]:
        computer_game_card = GameCard(
            board=computer_board,
            position=count,
            card=computer_card,
        )
        computer_game_card.save()
        count += 1
    return HttpResponseRedirect(game.get_absolute_url())


class GameDetailView(DetailView):
    """Show the boards of two players."""

    model = Game
    pk_url_kwarg = "game_id"
    template_name = "game.html"
    context_object_game = "game"

    def get_context_data(self, **kwargs):
        """Get the context for the view."""
        context = super(GameDetailView, self).get_context_data(**kwargs)
        for board in self.object.boards.all():
            if board.player == 'jugador':
                context['player_board'] = board
            else:
                context['computer_board'] = board
        return context


def new_card(request, game_id):
    """Take a photo of a new card and detect if is in a board."""
    game = get_object_or_404(Game, pk=game_id)
    webcam = cv2.VideoCapture(0)
    check, frame = webcam.read()
    cv2.imwrite(filename='saved_img.jpg', img=frame)
    webcam.release()
    cv2.destroyAllWindows()

    image_saved = io.imread('saved_img.jpg')
    gray_saved = rgb2gray(image_saved)
    gray_saved = (gray_saved * 255) // 1
    [rows_saved, columns_saved] = gray_saved.shape
    for row in range(rows_saved):
        for column in range(columns_saved):
            if gray_saved[row, column] > 100:
                gray_saved[row, column] = 0
            else:
                gray_saved[row, column] = 255

    number1 = gray_saved[20:65, 200:240]
    number2 = gray_saved[20:65, 245:285]

    data = []
    labels = []

    for i in range(12):
        for j in '0123456789':
            image_name = 'data/{}-{}.jpg'.format(i, j)
            image = io.imread(image_name)
            gray = rgb2gray(image)
            gray = (gray * 255) // 1
            [rows, columns] = gray.shape

            for row in range(rows):
                for column in range(columns):
                    if gray[row, column] > 100:
                        gray[row, column] = 0
                    else:
                        gray[row, column] = 255

            for k in range(100):
                data.append(gray.reshape(1800))
                labels.append(j)

    data = np.array(data)
    labels = np.array(labels)

    clf = DecisionTreeClassifier()
    clf.fit(data, labels)

    test = np.array([number1.reshape(1800), number2.reshape(1800)])
    predictions = clf.predict(test)

    number = int(str(predictions[0]) + str(predictions[1]))
    try:
        card = Card.objects.get(name=number)
        text = card.name
        print(card.number)
    except:
        print('No card')

    for board in game.boards.all():
        if text in board.not_checked_cards:
            game_card = GameCard.objects.get(board=board, card__name=text)
            game_card.checked = True
            game_card.save()

    return HttpResponseRedirect(game.get_absolute_url())
