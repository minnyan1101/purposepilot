import shutil
import os
import subprocess as sp


def init():
    shutil.rmtree("build")
    os.makedirs("build/static", exist_ok=True)


def build_frontend():
    sp.run(["npm", "run", "build"], shell=True, cwd="./frontend")


def copy_frontend():
    shutil.copytree("frontend/dist", "build/static", dirs_exist_ok=True)


def build_backend():
    sp.run(["pip", "install", "./backend", "-t", "build/python"])


def make_archive():
    shutil.make_archive("purpose_pilot", format="zip", root_dir="build")


def download_embedded_python():
    url = "https://www.python.org/ftp/python/3.12.1/python-3.12.1-embed-amd64.zip"
    sp.run(["curl.exe", url, "-o", "build/python.zip"])
    shutil.unpack_archive("build/python.zip", "build/python")
    os.remove("build/python.zip")


def copy_scripts():
    shutil.copy("run.bat", "build")


def main():
    init()

    build_backend()

    build_frontend()
    copy_frontend()

    download_embedded_python()

    copy_scripts()

    make_archive()


if __name__ == "__main__":
    main()
