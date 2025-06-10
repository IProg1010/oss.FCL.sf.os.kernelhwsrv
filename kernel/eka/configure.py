import os
import sys
import glob

# Получение списка поддиректорий в текущем каталоге, исключая 'epoc32'
rootdirs = []
for entry in os.listdir('.'):
    if os.path.isdir(entry) and entry.lower() != 'epoc32':
        print(os.path.join('./', entry, '*.bld'));        
        rootdirs.append(os.path.join('./', entry, '*.bld'))

# Словарь для хранения информации о build-файлах
bldfiles = {}

# Обработка каждого пути
for pattern in rootdirs:
    print(pattern)
    for filepath in glob.glob(os.path.join(os.getcwd(), pattern)):
        print("Found")
        fullpath = os.path.normcase(os.path.abspath(filepath))
        filename = os.path.basename(fullpath).lower()
        name = filename[:-4]  # удаляем '.bld'
        if name in bldfiles:
            raise Exception(f"Duplicate build file name {name}")
        bldfiles[name] = {
            'fullname': fullpath,
            'name': name
        }

# Анализ содержимого файлов
for bld_name, ref in bldfiles.items():
    filename = ref['fullname']
    options = []
    components = []
    explicit = False
    compulsory = False

    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.rstrip('\n')
                if line.startswith('!'):
                    key = line[1:].strip().lower()
                    if key == 'explicit':
                        explicit = True
                    elif key == 'compulsory':
                        compulsory = True
                elif line.lstrip().lower().startswith('<option'):
                    options.append(line)
                elif line.strip() != '':
                    components.append(line)
    except Exception as e:
        raise Exception(f"Could not open file {filename}: {e}")

    ref['options'] = options
    ref['components'] = components
    ref['explicit'] = explicit
    ref['compulsory'] = compulsory
    ref['incremental'] = False  # Изначально предполагается False, можно изменить при необходимости

# Обработка аргументов командной строки
args = sys.argv[1:]
defaults = []
compulsory_list = []

if not args:
    todo_temp = list(bldfiles.keys())
else:
    todo_temp = list(bldfiles.keys())  # изначально все
    for arg in args:
        arg_lower = arg.lower()
        if arg == '+':
            for bld in defaults:
                if bld not in todo_temp:
                    todo_temp.append(bld)
        elif arg.startswith('-'):
            name = arg[1:].lower()
            if name in bldfiles:
                ref = bldfiles[name]
                if ref.get('compulsory'):
                    raise Exception(f"Cannot omit {name}")
                if name not in ['omit_list']:  # добавьте сюда, если есть список omit
                    if name not in []:
                        # Добавим в omit список
                        pass
            else:
                raise Exception(f"Unrecognized build {name}")
        else:
            if arg_lower in bldfiles:
                if arg_lower not in todo_temp:
                    todo_temp.append(arg_lower)
            else:
                raise Exception(f"Unrecognized build {arg}")

# Формируем финальный список
todo = [b for b in todo_temp if b not in []]  # добавьте сюда список omit, если нужен

# Подсчет вариантов
nvariants = 0
for bld in todo:
    ref = bldfiles[bld]
    if not ref.get('explicit', False):
        defaults.append(bld)
    if not ref.get('incremental', False):
        nvariants += 1

if nvariants == 0:
    raise Exception("No variants specified for building")

# Формируем списки опций и компонентов
output1 = []
output2 = []

for bld in todo:
    ref = bldfiles[bld]
    if sys.argv[1:] and ref.get('explicit', False):
        continue
    for option in ref['options']:
        opt_s = ' '.join(option.split())
        if opt_s not in output1:
            output1.append(opt_s)
    for component in ref['components']:
        comp_s = ' '.join(component.split())
        if comp_s not in output2:
            output2.append(comp_s)

if nvariants == 0:
    raise Exception("No variants specified for building")

output1.sort()
output2.sort()

# Формируем финальный вывод
output = ''.join(output1) + '\n' + ''.join(output2) + '\n'

print("\n\n" + output)