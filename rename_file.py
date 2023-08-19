import os

source_path = 'path from which file should be picked'
destination_path = 'path to which file should be placed after the name change'

prefix = 'what should be the changed name?'
#eg. if file name is test.csv and we want to convert it to final_test.csv prefix should be 'final_'

files = os.listdir(source_path)

for filename in files:
        source = os.path.join(source_path, filename)

        if os.path.isfile(source):
            # Generate the new filename with the constant prefix
            new_filename = prefix + filename
            destination = os.path.join(destination_path, new_filename)

            # Rename and move the file
            os.rename(source, destination)

            print(f'Renamed {filename} to {new_filename} and moved to {destination_path}')
print('Done!')
