import os

dirs=[
os.path.join('data','raw'),
os.path.join('data','processed'),
'notebooks',
'saved_models',
'src']

for dir_ in dirs:
    os.makedirs(dir_,exist_ok=True)
for dir_ in dirs:
    gitkeep_file = os.path.join(dir_, '.gitkeep')
    with open(gitkeep_file, 'w'):
        pass

files =[
    'dvc.yaml',
    'params.yaml',
    '.gitignore',
    os.path.join('src','__init__.py')

]

for file_ in files:
    with open(file_,'w') as f:
        pass