# coding=utf-8

import os


def delete_gap_dir(dir):
    if os.path.isdir(dir):
        for d in os.listdir(dir):
            delete_gap_dir(os.path.join(dir, d))

        if not os.listdir(dir):
            os.rmdir(dir)
            print('Delete Gap Dir: ' + dir)


delete_gap_dir(input("Delete Gap Dir Folder Location:"))
print(u'Delete Gap Dir Complete')
input(u'Press Any Key To Exit')
