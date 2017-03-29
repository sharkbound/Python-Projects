import os
import re
import zipfile


def entry():
    folder_path = '../files/channel/'
    files = next(os.walk(folder_path))[2]  # grab all files
    file_number_prefix = 90052
    all_text_from_files = []

    cfile = open('anwser_challenge_6.txt', 'w')
    zip_file = zipfile.ZipFile(r"C:\Users\owner\Desktop\channel.zip")

    while True:
        fpath = f'{folder_path}{file_number_prefix}.txt'

        if os.path.exists(fpath):
            with open(fpath) as f:
                file_contents = f.read()

                if 'Next nothing is' in file_contents:
                    file_number_prefix = re.sub(r'[^\d]', '', file_contents)
                else:
                    file_number_prefix = file_contents

                all_text_from_files.append(file_contents)

                cut_file_path = fpath[fpath.rfind('/')+1:]
                zip_inner_file_comment = zip_file.getinfo(cut_file_path).comment.decode('UTF-8')
                cfile.write(zip_inner_file_comment)
                print(zip_inner_file_comment, end='')  #prints HOCKEY
        else:
            break
    cfile.close()

# channels folder is from http://www.pythonchallenge.com/pc/def/channel.zip
if __name__ == '__main__':
    entry()
