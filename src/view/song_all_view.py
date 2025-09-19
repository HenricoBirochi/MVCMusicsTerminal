from src.models.entities.music import Music
import os

class SongAllView:
    def show_songs_success(self, controller_response: dict) -> None:
        self.__clear()
        print("       Todas as Músicas Cadastradas:")
        for song in controller_response["songs"]:
            print(f"   Título: {song.title}, Artista: {song.artist}, Ano: {song.year}")

    def show_songs_error(self, controller_message: dict) -> None:
        self.__clear()
        print(f"Erro ao buscar músicas: {controller_message['error']}")


    def __clear(self):
        os.system('cls||clear')