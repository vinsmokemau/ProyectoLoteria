"""CMS urls."""
from django.urls import path
from . import views

app_name = 'game'

urlpatterns = [

    path(
        '',
        views.start_game,
        name='start-game'
    ),
    path(
        'juego/<int:game_id>/',
        views.GameDetailView.as_view(),
        name='game_detail'
    ),
    path(
        'juego/<int:game_id>/nueva_carta',
        views.new_card,
        name='new_card',
    ),

]
