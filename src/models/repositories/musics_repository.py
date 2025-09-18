from src.models.entities.music import Music

class __MusicsRepository:
    def __init__(self):
        self.__music_list = []


    def insert_music(self, music: Music) -> None:
        self.__music_list.append(music)


    def find_music(self, music_title: str) -> Music | None:
        for music in self.__music_list:
            if music.title == music_title:
                return music
        return None


    def get_all_songs(self) -> list[Music]:
        return self.__music_list

# Singleton - Design Pattern
# Ele garante que apenas um objeto dessa minha classe sera instanciado
# Nesse caso eh util porque eu nao quero dois objetos dessa classe, se nao eu iria formar duas listas diferentes
# E eu quero que todas as musicas fiquem na mesma lista
musics_repository = __MusicsRepository()