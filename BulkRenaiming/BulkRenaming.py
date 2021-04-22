import os


def main():
    i = 0
    path = input("Enter directory path : ").replace('\\', '/') # replacing '\' -> '/' (python req.)
    path = path+'/' # adding slah to end of path (phyton req.)
    for filename in os.listdir(path):
        my_dest = "img" + str(i)+".jpg" # youwant to conver into
        my_src = path + filename # source of file
        my_dest = path + my_dest #alloting the file with new name
        os.rename(my_src, my_dest) # renaiming it
        i += 1


if __name__ == '__main__':
    main()
