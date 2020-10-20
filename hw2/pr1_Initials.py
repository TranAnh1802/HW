def main():
    full_name = input("enter your full name:")
    name = full_name.split()

    for string in name:
        print(string[0].upper(),sep='',end='')
        print('.',sep='',end='')

main()