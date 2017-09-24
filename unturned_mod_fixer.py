import os

TAGS = 'Size_X', 'Size_Y', 'Fuel_Max', 'Fuel_Min'
count = 0

print('Starting search for files to fix...')

for root, folders, files in os.walk(os.getcwd()):
    for file in filter(lambda x: x.endswith('.dat'), files):
        with open(os.path.join(os.getcwd(), root, file), 'r+') as f:
            text = f.read()
            if 'Bypass_Hash_Verification' not in text and any(s in text for s in TAGS):
                count += 1
                f.write('\n\nBypass_Hash_Verification')
                print(f'Fixing #{count} {file}')
print('Done!')
input('Press any key to exit...')
