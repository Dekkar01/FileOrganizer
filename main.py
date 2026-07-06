import os
import shutil
from tkinter import filedialog, Tk
from tkinter import *
import datetime

log_messages = []



def log_and_print(message):
    print(message)
    log_messages.append(message)



log_and_print("*"*30)
now = datetime.datetime.now()
log_and_print(now.strftime("%Y-%m-%d %H:%M:%S"))

root = Tk()
root.title("Сортировка")
#root.withdraw()

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")



def clicked():
    
    folder_path = filedialog.askdirectory(
        title = 'Выберите папку для сортировки'
    )
    if not folder_path:
        log_and_print("Вы не выбрали папку. Программа завершена")
        log_and_print("*"*30)
        root.destroy()
        return
        # exit()

    
    confirm = Toplevel(root)
    confirm.title("Потверждение")

    confirm.geometry('200x50')
    confirm.transient(root)
    confirm.grab_set()
    
    center_window(confirm)
        
    lbl2 = Label(confirm, text = 'Этот скрипт переместит все файлы в папке. Вы уверены?', font = ('Arial', 21))

    lbl.grid(column = 0, row = 0)

    def cancel_btn():
        log_and_print('Отмена')
        log_and_print('*'*30)
        root.destroy()
        return

    def confirm_btn():
        
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
        root.destroy()
        return
        # input("Нажмите Enter, чтобы выйти...")


    btn_confirm = Button(confirm, text = 'Да', command = confirm_btn)
    btn_confirm.grid(column = 0, row = 1)
    btn_cancel = Button(confirm, text = 'Нет', command = cancel_btn)
    btn_cancel.grid(column = 1, row = 1)



    log_and_print(f'Вы выбрали папку: {folder_path}')  
    log_and_print(f'Начинаю сортировку папки: {folder_path}')
    log_and_print("Библиотеки загружены, все работает!")

root.geometry('400x250')
lbl = Label(root, text = 'Выберите папку:', font = ('Arial Bold', 21))
lbl.grid(column = 0, row = 0)

btn = Button(root, text = 'Выбрать', command = clicked)
btn.grid(column = 1, row = 0)



rules = {
    "images": ['.jpg', '.jpeg', '.png', '.gif'],
    "documents": ['.txt', '.doc', '.docx', '.xlsx', '.pdf'],
    'archives': ['.zip', '.rar', '.7z'],
    "music": ['.mp3', '.wav'],
    "scripts": ['.py', '.js', '.html'],
    'video': ['.mp4']
    }

center_window(root)

root.mainloop() #не позволяет окну прятаться
































# confirm = input("Этот скрипт переместит все файлы в папке. Вы уверены? y/n \n")
# if confirm.lower() != 'y':
#     log_and_print('Отмена')
#     log_and_print('*'*30)
#     exit()

# moved_count = 0
# skipped_count = 0
# undefined_count = 0

# for file in os.listdir(folder_path):
#     file_path = os.path.join(folder_path, file)

#     if os.path.isfile(file_path):
#         _, extension = os.path.splitext(file)
#         extension = extension.lower()

#         moved = False

#         for folder_name, extension_list in rules.items():
#             if extension in extension_list:
#                 dest_folder = os.path.join(folder_path, folder_name)
#                 os.makedirs(dest_folder, exist_ok = True)

#                 shutil.move(file_path, os.path.join(dest_folder, file))
#                 dest_path = os.path.join(dest_folder, file)
#                 if os.path.exists(dest_path):
#                     log_and_print(f'Файл {file} уже есть в {folder_name}, пропускаем.')
#                     moved = True
#                     skipped_count  += 1
#                     break
#                 log_and_print(f'Переместил {file} -> {folder_name}')
#                 moved = True
#                 moved_count += 1 
#                 break

#         if not moved:
#             log_and_print(f'Не знаю что делать с {file}, оставил на месте')
#             undefined_count += 1
# log_and_print('*'*30 + '\n')

# report_path = os.path.join(os.getcwd(), 'Отчёт о сортировке.txt')
# with open(report_path, 'a', encoding = 'utf-8') as report_file:
#     report_file.write("=== ОТЧЁТ О СОРТИРОВКЕ ФАЙЛОВ ===\n")
#     report_file.write(f"Папка: {folder_path}\n")
#     report_file.write(f"Перемещено: {moved_count} файлов\n")
#     report_file.write(f"Пропущено (уже были): {skipped_count} файлов\n")
#     report_file.write(f"Не определено: {undefined_count} файлов\n")
#     report_file.write("=" * 40 + "\n\n")

#     report_file.write('\n'.join(log_messages))

# log_and_print(f"\nОтчет сохранен в файл: {report_path}")
# log_and_print('сортировка завершена')

# input("Нажмите Enter, чтобы выйти...")
# root.mainloop() #не позволяет окну прятаться