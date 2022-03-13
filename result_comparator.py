RESULT_PATH_CPP = 'result_cpp.txt'
RESULT_PATH_PYTHON_CUSTOM = 'result_python_custom.txt'
RESULT_PATH_PYTHON_ORGINAL = 'result_python_orginal.txt'

result_cpp = []
result_python_custom = []
result_python_orginal = []

with open(RESULT_PATH_CPP) as file:
    result_cpp = file.readlines()

with open(RESULT_PATH_PYTHON_CUSTOM) as file:
    result_python_custom = file.readlines()

with open(RESULT_PATH_PYTHON_ORGINAL) as file:
    result_python_orginal = file.readlines()

for line_number in range(len(result_cpp)):
    if result_cpp[line_number] != result_python_custom[line_number] \
        or result_cpp[line_number] != result_python_orginal[line_number] \
        or result_python_custom[line_number] != result_python_orginal[line_number]:
        print(f'Błąd w linii: {line_number}')
        print(f'result_cpp: {result_cpp[line_number]}')
        print(f'result_python_custom: {result_python_custom[line_number]}')
        print(f'result_python_orginal: {result_python_orginal[line_number]}')
        exit(0)

print('OK')

