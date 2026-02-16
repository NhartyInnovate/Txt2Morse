








while True:
    print("\nMorse Code Converter")
    print("1. Text to Morse")
    print("2. Morse to Text")
    print("3. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        user_input = input("Enter text: ")
        morse_code = text_to_morse(user_input)
        print(morse_code)
        play_morse(morse_code)

    elif choice == "2":
        user_input = input('Enter Morse code: ')
        print(morse_to_text(user_input))

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
