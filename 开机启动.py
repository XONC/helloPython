import os
import shutil
import winshell

if __name__ == "__main__":
    your_program_path = "G:\aDrive\aDrive.exe"

    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

    shortcut_name = "YourProgram.lnk"

    with winshell.shortcut(os.path.join(startup_folder, shortcut_name)) as shortcut:
        shortcut.path = your_program_path
        shortcut.description = "Your Program Shortcut"

    print(f"已在开机自启动目录创建快捷方式：{os.path.join(startup_folder, shortcut_name)}")