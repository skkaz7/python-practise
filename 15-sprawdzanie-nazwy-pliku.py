# Pytanie 15 - napisz funkcję, która sprawdzi czy podany string
# zaczyna się słowem "python" i kończy rozszerzeniem ".py"
# Przetestuj nią stringi:

a = "python_moj_kod.py"
b = "python_notatki.txt"


def check_if_python_file(file):
    return True if file[:6] == 'python' and file[-3:] == '.py' else False


print(check_if_python_file(a))
print(check_if_python_file(b))
