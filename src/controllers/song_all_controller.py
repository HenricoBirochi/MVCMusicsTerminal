from src.models.entities.music import Music
from src.models.repositories.musics_repository import musics_repository

class SongAllController:
    def get_all_songs(self) -> dict:
        try:
            songs = musics_repository.get_all_songs()
            return self.__format_response(songs)
        except Exception as e:
            return self.__format_error_response(e)


    def __format_response(self, songs: list[Music]) -> dict:
        return {
            "success": True,
            "count": len(songs),
            "songs": songs
        }


    def __format_error_response(self, err: Exception) -> dict:
        return {
            "success": False,
            "error": str(err)
        }