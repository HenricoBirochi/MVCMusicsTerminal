def introduction_page() -> str:
    message = """
        Music System
    1. Insert new music - 1
    2. Create playlist - 2
    5. Exit - 5
    """

    print(message)
    command = input("Comando: \n")

    return command