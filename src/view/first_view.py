def introduction_page() -> str:
    message = """
        Music System
    1. Insert new music - 1
    2. View musics registered - 2
    5. Exit - 5
    """

    print(message)
    command = input("Comando: ")
    print("\n")  # pular linha

    return command