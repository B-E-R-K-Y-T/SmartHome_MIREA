import os

path_to_shm = 'berkyt/SmartHome_MIREA/'

if not os.path.exists(path_to_shm):
    print('Ты читаешь Библию, а я Коран')
    os.system('cd && cd berkyt/ && rm -r SmartHome_MIREA/')
    os.rmdir('berkyt/SmartHome_MIREA/')

os.system("cd && cd berkyt/ && git clone https://github.com/B-E-R-K-Y-T/SmartHome_MIREA && cd && cd berkyt/SmartHome_MIREA/ && python3 generate_sensors.py")
