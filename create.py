import os

# Указываем путь к директории, в которой будут созданы файлы HTML
directory = "C:/Users/HP-PC/Desktop/study/4 семестр/вэб/лаб2"  # Укажите свой путь к директории

# в скобках указываешь количество от 1 до сколько хочешь
for i in range(1, 25):
    # вместо слова primer прописываешь название своего файла которое нужно создать вместо html расширение которое тебе нужно
    file_path = os.path.join(directory, f"primer{i}.html")
    with open(file_path, "w") as file:
        file.write("<!DOCTYPE html>\n<html>\n<head>\n<title>File Title</title>\n</head>\n<body>\n<h1>File Content</h1>\n</body>\n</html>")
