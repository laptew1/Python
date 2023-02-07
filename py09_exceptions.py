import shutil
from datetime import datetime
import sys

IN_FILE = "data/nums.txt"
RESULT_FILE = "data/results.txt"
ERROR_FILE = "data/errors.txt"
PROCESSED_FOLDER = "data/processed"

# x = 1024
# y = 0
# try:
#     z = x / y
#     print(z)
# except:
#     pass # проглоченная ошибка - это антипаттерн
#     print("ERROR!")
# print("Program proceeds...")
try:
    with open(IN_FILE) as f:
        text = f.read()
except Exception as e:
    message = f"{datetime.now()}\t{e}\n"
    with open(ERROR_FILE, "a") as errors:
        errors.write(message)
    sys.exit(0)

lines = text.split("\n")

with open(RESULT_FILE, "a") as results:
    with open(ERROR_FILE, "a") as errors:
        for line in lines:
            try:
                splitted = line.split(";")
                x = int(splitted[0])
                y = int(splitted[1])
                z = x / y
                print(f"{x}:{y}={z}")
                results.write(f"{x}:{y}={z}\n")
            except ZeroDivisionError:
                print(f"{x}:{y}=999999")
            except Exception as e:
                # pass
                print(f"ERROR IN LINE {line}\n{e}")
                errors.write(f"ERROR IN LINE {line}\n{e}\n")
            # finally:
            #     print("Proceeeds...")
            # print("Proceeeds...")
# 20221001_105200
output_file = f"data{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
shutil.move(IN_FILE, f"{PROCESSED_FOLDER}/{output_file}")