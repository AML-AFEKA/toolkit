import os
import shutil
import configparser
import glob

directory = [
    {"name": "invalid", "key": "0"},
    {"name": "valid", "key": "1"},
    {"name": "unknown", "key": "2"},
             ]

for folder in directory:
    print(f'mkdir: {folder["name"]}')
    if not os.path.exists(folder["name"]):
        os.makedirs(folder["name"])

def sort(_input):
    for folder in directory:
        if _input == folder["key"]:
            return folder["name"]

    return "unknown"

folders = glob.glob('*')
for folder in folders:
    configFile = f'./{folder}/Exam.ini'
    isExist = os.path.exists(configFile)

    if isExist:
        config = configparser.ConfigParser()
        config.read(configFile)
        config.sections()

        PatID = config["ExamData"]["PatID"]
        PatFirstName = config["ExamData"]["PatFirstName"]
        PatLastName = config["ExamData"]["PatLastName"]
        ExamDate = config["ExamData"]["ExamDate"]

        print(folder)
        print(f"PatID: {PatID}, PatFirstName: {PatFirstName}, PatLastName: {PatLastName}, ExamDate: {ExamDate}")

        for folder in directory:
            print(f'key: {folder["key"]} : {folder["name"]}', end=' , ')

        print()

        classy = sort(input())
        print(classy)

        files = glob.glob(f'./{folder}/Images/*.jpg') 
        for src in files:
            shutil.move(src, f'./{classy}')

