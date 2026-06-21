import os
import shutil
from tkinter import filedialog, Tk
import datetime

log_messages = []

def log_and_print(message):
    print(message)
    log_messages.append(message)

log_and_print("*"*30)
now = datetime.datetime.now()
log_and_print(now.strftime("%Y-%m-%d %H:%M:%S"))
root = Tk()
root.withdraw()

folder_path = filedialog.askdirectory(
    title = 'Выберите папку для сортировки'
)
if not folder_path:
    log_and_print("Вы не выбрали папку. Программа завершена")
    log_and_print("*"*30)
    exit()

log_and_print(f'Вы выбрали папку: {folder_path}')  
log_and_print(f'Начинаю сортировку папки: {folder_path}')
log_and_print("Библиотеки загружены, все работает!")

rules = {
    "images": ['.jpg', '.jpeg', '.png', '.gif'],
    "documents": ['.txt', '.doc', '.docx', '.xlsx', '.pdf'],
    'archives': ['.zip', '.rar', '.7z'],
    "music": ['.mp3', '.wav'],
    "scripts": ['.py', '.js', '.html'],
    'video': ['.mp4']
    }

confirm = input("Этот скрипт переместит все файлы в папке. Вы уверены? y/n \n")
if confirm.lower() != 'y':
    log_and_print('Отмена')
    log_and_print('*'*30)
    exit()

moved_count = 0
skipped_count = 0
undefined_count = 0

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        _, extension = os.path.splitext(file)
        extension = extension.lower()

        moved = False

        for folder_name, extension_list in rules.items():
            if extension in extension_list:
                dest_folder = os.path.join(folder_path, folder_name)
                os.makedirs(dest_folder, exist_ok = True)

                shutil.move(file_path, os.path.join(dest_folder, file))
                dest_path = os.path.join(dest_folder, file)
                if os.path.exists(dest_path):
                    log_and_print(f'Файл {file} уже есть в {folder_name}, пропускаем.')
                    moved = True
                    skipped_count  += 1
                    break
                log_and_print(f'Переместил {file} -> {folder_name}')
                moved = True
                moved_count += 1 
                break

        if not moved:
            log_and_print(f'Не знаю что делать с {file}, оставил на месте')
            undefined_count += 1
log_and_print('*'*30 + '\n')

report_path = os.path.join(os.getcwd(), 'Отчёт о сортировке.txt')
with open(report_path, 'a', encoding = 'utf-8') as report_file:
    report_file.write("=== ОТЧЁТ О СОРТИРОВКЕ ФАЙЛОВ ===\n")
    report_file.write(f"Папка: {folder_path}\n")
    report_file.write(f"Перемещено: {moved_count} файлов\n")
    report_file.write(f"Пропущено (уже были): {skipped_count} файлов\n")
    report_file.write(f"Не определено: {undefined_count} файлов\n")
    report_file.write("=" * 40 + "\n\n")

    report_file.write('\n'.join(log_messages))

log_and_print(f"\nОтчет сохранен в файл: {report_path}")
log_and_print('сортировка завершена')

input("Нажмите Enter, чтобы выйти...")