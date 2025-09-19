from src.controllers.song_all_controller import SongAllController
from src.view.song_all_view import SongAllView

def song_all_process():
    song_all_view = SongAllView()
    song_all_controller = SongAllController()
    # instancia do controller

    response = song_all_controller.get_all_songs()

    if response["success"]:
        song_all_view.show_songs_success(response)
    else:
        song_all_view.show_songs_error(response)

    # enviar new_song_informations para o controller