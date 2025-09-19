from src.view.first_view import introduction_page
from .constructor.song_register_constructor import song_register_process
from .constructor.song_all_constructor import song_all_process

def start() -> None:
    while True:

        command = introduction_page()

        if command == "1": song_register_process()
        elif command == "2": song_all_process()
        elif command == "5": exit()
        else: print("Invalid command, please try again.")