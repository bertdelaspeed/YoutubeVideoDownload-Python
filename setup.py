import sys
from cx_Freeze import setup, Executable

company_name = 'Laspeed Corp'
product_name = 'YT Downloader'

bdist_msi_options = {
    'add_to_path': False,
    'initial_target_dir': r'[ProgramFilesFolder]\%s\%s' % (company_name, product_name),
    }

path = sys.path
base = None
if sys.platform == "win32":
    base = "Win32GUI"

exe = Executable(
        script="YT Downloader.py",
        icon="viral.ico",
        targetName="LaspeedYTDownloader.exe",
        base=base
        )

build_exe_options = {'packages':['pytube', 'tkinter','PIL','pyautogui'], 'include_files': ['gobtn2', 'download1.png','YoungMe.ico','cleaner.png'], 'icon': ['viral.ico']}


setup(
  name='LaspeedYtDownloader',
  version='1.0',
  description='Software by Bertdelaspeed to download youtube videos',
  author="Wilfried Bertrand Aka LASPEED",
  author_email="bertdelaspeed@gmail.com",
  options={'build.exe': build_exe_options,'bdist_msi': bdist_msi_options},
  executables=[exe]
  )
