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


    def registry_song_success(self, controller_response: dict) -> None:
        self.__clear()

        message = """
            Music Registered Successfully!

            * Title: {}
            * Quantidade: {}
        """.format(
            controller_response["attributes"]["title"],
            controller_response["count"]
        )
        print(message)


    def registry_song_error(self, controller_message: dict) -> None:
        self.__clear()
        
        message = """
            Music Registration Failed!

            * Error: {}
        """.format(
            controller_message["error"]
        )
        print(message)


    def __clear(self):
        os.system('cls||clear')