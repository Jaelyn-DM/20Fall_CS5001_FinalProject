'''
Duo Ma (Jaelyn)
CS5001 2020 Fall
HW7 Statistics
this program is run statistical significance testing which would help to
determine how strongly you should believe in your experienments results.
'''


def read_data(file_name):
    '''
    name: read_data()
    parameter: string (file_name): the name of a text file
    return: list of numbers (one number per line from the file read in)
    '''
    try:
        data_list = []
        input_file = open(file_name, 'r')
        file_data = input_file.readlines()
        input_file.close()

        for each_line in file_data:
            each_line = each_line.strip('\n')
            each_line = float(each_line)
            data_list.append(each_line)

        return data_list

    except FileNotFoundError:
        raise ValueError('Could not read ', file_name, ', file was not found')
    except PermissionError:
        raise ValueError('Could not read', file_name, ', permission error')
    except OSError:
        raise ValueError('OSError occurred while reading', file_name)


def average(num_list):
    '''
    name: average()
    parameter: num_list (a list of numbers)
    return: integer (average of the numbers in the list)
    '''
    if not isinstance(num_list, list):
        raise TypeError('parameter for average should be a list')
    num_sum = 0
    num_count = 0
    for numbers in num_list:
        if not isinstance(numbers, int) and not isinstance(numbers, float):
            raise ValueError('items in the input list should be integer or float')
        num_sum += numbers
        num_count += 1
    num_average = num_sum / num_count

    return num_average


def std_dev(num_list):
    '''
    name: std_dec()
    parameter: num_list (a list of number)
    return: the standard deviation of numbers in the list, which shows how
    those number are distributed around the average.
    '''
    if not isinstance(num_list, list):
        raise TypeError('parameter for std_dev should be a list')
    average_num = average(num_list)
    sum_square = 0
    for numbers in num_list:
        if not isinstance(numbers, int) and not isinstance(numbers, float):
            raise ValueError('items in the input list should be an integer or float')
        sum_square += (numbers - average_num) ** 2
    s = (sum_square/(len(num_list) - 1)) ** 0.5

    return s


def t_test(num_list_a, num_list_b):
    '''
    name: t_test(), to measure when can assume the numbers in a data sets
    are normally distributed
    parameter: two lists numbers
    return: t_test value (float)
    '''

    if not isinstance(num_list_a, list) or not isinstance(num_list_b, list):
        raise TypeError('both parameters for t_test should be lists')
    average_a = average(num_list_a)
    average_b = average(num_list_b)
    s_a = std_dev(num_list_a)
    s_b = std_dev(num_list_b)
    n_a = len(num_list_a)
    n_b = len(num_list_b)
    t = (average_a - average_b) / ((s_a ** 2 / n_a) + (s_b ** 2 / n_b)) ** 0.5

    return(t)


def degrees_of_freedom(num_list_a, num_list_b):
    '''
    name: degrees_of_freedom(), which compute the degrees of freedom of the
    data sets
    parameters: two lists of numbers (num_list a & b)
    return: a float which is the degrees of freedom
    '''
    if not isinstance(num_list_a, list) or not isinstance(num_list_b, list):
        raise TypeError('both parameters for degrees_of_freedom should be lists')

    average_a = average(num_list_a)
    average_b = average(num_list_b)
    s_a = std_dev(num_list_a)
    s_b = std_dev(num_list_b)
    n_a = len(num_list_a)
    n_b = len(num_list_b)
    f_up = ((s_a ** 2 / n_a) + (s_b ** 2 / n_b)) ** 2
    f_down_a = (s_a ** 2 / n_a) ** 2 / ((n_a) - 1)
    f_down_b = (s_b ** 2 / n_b) ** 2 / ((n_b) - 1)
    f = f_up / (f_down_a + f_down_b)

    return f


def main():
    # ask user to enter two file names
    file_name_a = str(input('Enter file name for first data set: '))
    file_name_b = str(input('Enter file name for second data set: '))
    # read the two files and output a list of numbers in the file
    output_a = read_data(file_name_a)
    output_b = read_data(file_name_b)

    t = t_test(output_a, output_b)
    print('t =', t)
    f = degrees_of_freedom(output_a, output_b)
    print('f =', f)

    return t, f


if __name__ == '__main__':
    main()
