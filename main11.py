import colorama
from colorama import Fore, Back, Style

print("Что есть в colorama:")
print(dir(colorama))

print("\nЧто есть в Fore (цвет текста):")
print(dir(Fore))

print("\nЧто есть в Back (цвет фона):")
print(dir(Back))

print("\nЧто есть в Style (стиль текста):")
print(dir(Style))

colorama.init(autoreset=True)

print("\nПримеры работы:\n")
print(Fore.RED + "Красный текст")
print(Fore.GREEN + "Зелёный текст")
print(Fore.BLUE + "Синий текст")
print(Back.YELLOW + "Жёлтый фон")
print(Back.CYAN + "Голубой фон")

print(Style.BRIGHT + "Яркий текст")
print(Style.DIM + "Тусклый текст")

print(Fore.WHITE + Back.RED + Style.BRIGHT + "Комбинированный текст")

print(Fore.RED + "Красный текст" + Style.RESET_ALL)
print("Обычный текст")