from selenium import webdriver
from threading import Thread
from subprocess import run
import sys, os
import index

def kill_server():
    process = run("netstat -ano | findstr :8080", shell=True, capture_output=True, text=True)
    if process.stdout:
        pid = process.stdout.split()[-1]
        run(f"taskkill /PID {pid} /f")


def start_app():
    index.main()


def open_app():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    path = ""
    if getattr(sys, 'frozen', False):
        path = sys._MEIPASS + "/chromedriver.exe"
    else:
        path = os.path.dirname(os.path.abspath(__file__)) + "/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=path, options=options)
    process = run("ipconfig", shell=True, capture_output=True, text=True)
    ip_address = process.stdout.split("\n")[-5].split()[-1]
    print(ip_address)
    url = f"http://{ip_address}:8080/"
    driver.get(url)


def main():
    kill_server()
    thread = Thread(target=start_app)
    thread.start()
    open_app()


if __name__ == '__main__':
    main()

# dash app
# pyinstaller .\main.py --add-data "C:\Users\allan\OneDrive\Desktop\repos\personal-projects\volt_bench_dash\data\easy_bench.txt;./data"
# --add-data "C:\Users\allan\OneDrive\Desktop\repos\personal-projects\volt_bench_dash\data\hard_bench.txt;./data"
# --add-binary "C:\Users\allan\OneDrive\Desktop\repos\personal-projects\volt_bench_dash\;./" 
# --add-data "C:\Users\allan\.virtualenvs\volt_bench_dash-fL3qpXuH\Lib\site-packages\dash; dash"
