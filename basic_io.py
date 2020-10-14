"""



"""

FILE_NAME = 'student_info.txt'
MAX = 50
MIN = 1


def write_to_file(*args):
    print(args)
    try:
        with open(FILE_NAME, 'a') as f:
            f.write('{}, {}:\t'.format(args[1], args[0]))
            for i in args[2]:
                f.write('{}\t'.format(i))
            f.write('\n')
    except IOError:
        print('Cannot open file on file system')


def get_student_info(**kwargs):
    print('Welcome, {} {}!'.format(kwargs['first_name'], kwargs['last_name']))
    scores = []
    num = 0
    while num != -1:
        try:
            num = float(input('Enter a score between {} and {}, (-1 to exit)'.format(MIN, MAX)))
            if num == -1:
                break
            elif num < MIN or num > MAX:
                raise ValueError('Score Must be between {} and {}'.format(MIN, MAX))
            else:
                scores.append(num)
        except ValueError as err:
            print(err)
    all_scores = kwargs['first_name'], kwargs['last_name'], scores
    print(all_scores)
    write_to_file(all_scores)


def read_from_file():
    pass


if __name__ == '__main__':
    get_student_info(first_name='Alex', last_name='Kelso')
    get_student_info(first_name='Marco', last_name='Polo')
    #read_from_file()
    input('Press any key to end')
