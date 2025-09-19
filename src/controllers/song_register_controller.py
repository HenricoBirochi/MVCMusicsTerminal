from src.models.entities.music import Music
from src.models.repositories.musics_repository import musics_repository

class SongRegisterController:
    def insert(self, new_song_informations: dict) -> dict:
        # Principio de Responsabilidade Única
        try:
            self.__verify_songs_infos(new_song_informations)
            self.__verify_if_song_already_registered(new_song_informations)
            self.__insert_song(new_song_informations)
            return self.__format_response(new_song_informations)
        except Exception as e:
            return self.__format_error_response(e)


    def __verify_songs_infos(self, new_song_informations: dict) -> None:
        if len(new_song_informations["title"]) > 100:
            raise Exception("O título da música deve ter no máximo 100 caracteres.")
        try:
            year = int(new_song_informations["year"])
        except Exception:
            raise Exception("O ano da música deve ser um número inteiro.")
        if year > 2025:
            raise Exception("O ano da música não pode ser maior que 2025.")


    def __verify_if_song_already_registered(self, new_song_informations: dict) -> None:
        music = musics_repository.find_music(new_song_informations["title"])
        if music:
            raise Exception("Música já cadastrada.")


    def __insert_song(self, new_song_informations: dict) -> None:
        music = Music(
            title=new_song_informations["title"],
            artist=new_song_informations["artist"],
            year=int(new_song_informations["year"])
        )
        musics_repository.insert_music(music)


    def __format_response(self, new_song_informations: dict) -> dict:
        return {
            "success": True,
            "count": 1,
            "attributes": {
                "title": new_song_informations["title"],
            }
        }


    def __format_error_response(self, err: Exception) -> dict:
        return {
            "success": False,
            "error": str(err)
        }