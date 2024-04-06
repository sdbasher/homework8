import random

def generate_random_number():
    return random.randint(1, 10)

def guess_number(secret_number, attempts):
    for attempt in range(attempts):
        guess = int(input("Вгадайте число (від 1 до 10): "))
        if guess == secret_number:
            print("Вітаємо! Ви вгадали число!")
            return True
        elif guess < secret_number:
            print("Секретне число вище!")
        else:
            print("Секретне число нижче!")
    print(f"Вибачте, ви використали всі {attempts} спроби. Секретним номером було {secret_number}")
    return False

def play_game():
    secret_number = generate_random_number()
    max_attempts = 3
    while True:
        if not guess_number(secret_number, max_attempts):
            break
        play_again = input("Хочеш зіграти знову? (y/n)").lower()
        if play_again != 'y':
            break
        secret_number = generate_random_number()


play_game()





