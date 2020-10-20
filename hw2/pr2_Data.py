def main():
    day = 0
    month_num= 0
    month_name=''
    data_string=''
    month_list = ['January', 'February','March',
                  'April', 'May','June', 'July',
                  'August', 'September', 'October',
                  'November', 'December']
    # Get the date in mm/dd/yyyy format as input from the user.
    data_string= input("enter a date in the format mm/dd/yyyy: ")
    # Split date_string.
    data_list = data_string.split('/')
    month_num=int(data_list[0])
    day = data_list[1]
    year = data_list[2]

    month_name = month_list[month_num-1]

    long_date = month_name + ' ' + day+', '+ year
    print(long_date)
main()