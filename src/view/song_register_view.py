import os

class SongRegisterView:
    def registry_song_initial(self) -> dict:
        self.__clear()
        print("Implementing New Song")

        title = input("Title: ")
        artist = input("Artist: ")
        year = input("Year: ")

        new_song_informations = {
            "title": title,
            "artist": artist,
            "year": year
        }

        return new_song_informations
    
    def __clear(self):
        os.system('cls||clear')