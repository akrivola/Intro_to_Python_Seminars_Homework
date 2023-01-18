"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet

ping_resource = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]
for ping in ping_resource:
    ping_process = subprocess.Popen(ping, stdout=subprocess.PIPE)
    for line in ping_process.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))