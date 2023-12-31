# tebakangka/game.py
import random

class TebakAngka:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

    def guess(self, number):
        self.attempts += 1

        if number == self.secret_number:
            return f"Selamat! Anda menebak dengan benar dalam {self.attempts} percobaan."
        elif number < self.secret_number:
            return "Tebakan terlalu rendah. Coba lagi."
        else:
            return "Tebakan terlalu tinggi. Coba lagi."
