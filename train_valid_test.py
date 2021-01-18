import os
import shutil
import random
import glob
import sys
from tqdm import tqdm

cli_input = sys.argv[1:]

cli_data = '''\nPlease provide the required argument after python train_valid_test.py
              1. Provide the extension for image
              2. Keep a classes.txt file to store the name of image class in small letter
              eg. python train_valid_test.py jpg classes.txt
'''
print('''
████████╗██████╗░░█████╗░██╗███╗░░██╗  ████████╗███████╗░██████╗████████╗
╚══██╔══╝██╔══██╗██╔══██╗██║████╗░██║  ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
░░░██║░░░██████╔╝███████║██║██╔██╗██║  ░░░██║░░░█████╗░░╚█████╗░░░░██║░░░
░░░██║░░░██╔══██╗██╔══██║██║██║╚████║  ░░░██║░░░██╔══╝░░░╚═══██╗░░░██║░░░
░░░██║░░░██║░░██║██║░░██║██║██║░╚███║  ░░░██║░░░███████╗██████╔╝░░░██║░░░
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝  ░░░╚═╝░░░╚══════╝╚═════╝░░░░╚═╝░░░

██╗░░░██╗░█████╗░██╗░░░░░██╗██████╗░
██║░░░██║██╔══██╗██║░░░░░██║██╔══██╗
╚██╗░██╔╝███████║██║░░░░░██║██║░░██║
░╚████╔╝░██╔══██║██║░░░░░██║██║░░██║
░░╚██╔╝░░██║░░██║███████╗██║██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝╚═════╝░''')
print("\n")
def form_dir(classes,train,test,valid,extension):
    try:
        if os.path.isdir('train'):
            print("The directory already exist! or delete it to proceeds")
        else:
            test_valid_train = ['train','test','valid']
            for j in test_valid_train:
                for i in classes:
                    if os.path.isdir(f'{j}/{i}') is False:
                        os.makedirs(f'{j}/{i}')
                    if j=='train':
                        for c in tqdm(random.sample(glob.glob(f'{i}/*.{extension}'),train)):
                            shutil.copy(c,f'{j}/{i}')
                    if j=="test":
                        for c in tqdm(random.sample(glob.glob(f'{i}/*.{extension}'),test)):
                            shutil.copy(c,f'{j}/{i}')
                    if j=="valid":
                        for c in tqdm(random.sample(glob.glob(f'{i}/*.{extension}'),valid)):
                            shutil.copy(c,f'{j}/{i}')
            print(">>>>>>>>>>>>>>>>>>>>")
            print(f"Dataset created with train test and valid")
            print(">>>>>>>>>>>>>>>>>>>>")
            for j in test_valid_train:
                for i in classes:
                    path=f"{j}/{i}"
                    print(f"Number of files in {j}/{i}:{len(os.listdir(path))}")
                    print("***********************")

    except Exception as e:
        print(e)
def calculate(classes,extension):
    try:
        test_valid_train = ['train','test','valid']
        for i in classes:
            path=f"{i}"
            val = len(os.listdir(path))
            print(f"Number of images in {i}:{len(os.listdir(path))} and recommended image for train:{int(val*.75)} valid:{int(val*.20)} test:{int(val*.05)}")
        print('Type Y to proceed or N to exit ')
        x = input()
        if x=="y" or x=="Y" or x=="yes" or x=="Yes":
            print("Enter the number of image to keep in train")
            train = int(input())
            print("Enter the number of image to keep in test")
            test = int(input())
            print("Enter the number of image to keep in valid")
            valid = int(input())
            form_dir(classes,train,test,valid,extension)
        else:
            print("Program closed!")
            sys.exit()
    except Exception as e:
        print(e)

try:
    if len(sys.argv)!=3:
        print(cli_data)
    else:
        cli_input = sys.argv
        extension = cli_input[1]
        file = cli_input[2]
        f = open(file,'r')
        classes = f.readlines()
        classes = [line.replace('\n','') for line in classes]
        data = []
        f.close()
        for i in classes:
            if i!='' and i!=' ' and  i!="\n":
                data.append(i)
        calculate(data,extension)
        # form_dir(data,train,test,valid,extension)

         
except Exception as e:
    print(e)


        
    


