import sys

def main():
    if len(sys.argv) < 3:
        print 'You have not specified a file or a class name'
    else:
        my_file = sys.argv[1]
        class_name = sys.argv[2]
        out_file_name = class_name.title() + '.java'
        out_file = open(out_file_name, 'w')
        java_writer(out_file, class_name)
        get_set_generator(out_file, my_file)
        out_file.close()


def java_writer(out_file, class_name):
    header = 'public class {} {{ \n'.format(class_name.title())
    out_file.write(header)


def get_set_generator(out_file, my_file):
    f = open(my_file, 'r')
    f2 = open(my_file, 'r')

    for line in f2:
        if not line.strip('\n').endswith(';'):
            line = line.strip('\n')
            line += ';\n'
        var = '    {}'.format(line)
        out_file.write(var)
    out_file.write('\n')

    for line in f:
        ret_type = ''
        var_name = ''
        temp = line.strip(';\n').split(' ')
        if (temp[0].lower() == 'private' or temp[0].lower() == 'public' or temp[0].lower() == 'protected'):
            ret_type = temp[1]
            var_name = temp[2]
        else:
            ret_type = temp[0]
            var_name = temp[1]
        getter = '{}public {} get{}() {{ return this.{}; }}'.format('    ', ret_type, var_name.title(), var_name)
        setter = '{}public void set{}({} {}) {{ this.{} = {}; }}'.format('    ', var_name.title(), ret_type, var_name, var_name, var_name)
        out_file.write(getter + '\n')
        out_file.write(setter + '\n\n')
    out_file.write('}\n')
    f.close()
    f2.close()

main()