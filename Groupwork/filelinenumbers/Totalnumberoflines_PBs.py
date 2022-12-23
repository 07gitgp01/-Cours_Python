#coding:utf-8
fich = "PaulBoss.txt"
### First way
# def PAULBoss(fich)
#     with open(fich, 'r') as fp:
#     print('Total Number of lines:', len(fp.readlines()))

# Other way
def PAULBoss(filename):
    with open(fich, "r") as Pbs:
        for count, line in enumerate(Pbs):
            pass

        print("total number of lines is: ", count + 1)

PAULBoss(fich)