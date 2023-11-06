import os
import ctypes
import sys
import vk_api

# Получаем привилегии администратора
def run_as_admin():
    try:
        # Проверяем, запущен ли скрипт с административными правами
        if ctypes.windll.shell32.IsUserAnAdmin():
            return
        # Запускаем скрипт от имени администратора
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        sys.exit(0)
    except Exception as e:
        print(e)
        sys.exit(1)

# Вводим sha256
sha256 = '$SHA$3989e11a4e38e9fb$7c5370696d20750ae520e820706f29bd05aacaa5c2fc03befc90d0e37d32e5e9'#input("Введите sha256: ")
dicta = "slovar foxkeys.txt" # тут словарь (ДОЛЖЕН БЫТЬ В КОРНЕ)
# Первая команда
command1 = r'cd C:\Users\marcus\Documents\hashcat-6.2.6' # тут путь к hashcat

# Вторая команда
command2 = f'hashcat.exe -a 0 -m 20711 -w 3 --status --status-timer=60 --potfile-disable -p : -O -r "rules\\best64.rule" {sha256} "{dicta}"'

# Объединяем две команды и выполняем их в одном экземпляре командной строки
os.system(f'cmd /k "{command1} && {command2}"')

# Запускаем скрипт с привилегиями администратора
run_as_admin()

