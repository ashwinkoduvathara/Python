import platform ,os,datetime
print('_________________________________________________________________________________________________________\n')
print('\t\t\t\tSystem Details\n')
print('_________________________________________________________________________________________________________\n')
print('1.Processor:\t\t\t|\t\t',platform.processor(),'\n')
print('3.Platform:\t\t\t|\t\t',platform.platform(),'\n')
print('4.Architecture:\t\t\t|\t\t',platform.architecture(),'\n')
print('5.Version:\t\t\t|\t\t',platform.version(),'\n')
print('6.Operating System:\t\t|\t\t',platform.system(),'\n')
print('7.Username:\t\t\t|\t\t',os.getlogin(),'\n')
print('8.Machine Number:\t\t|\t\t',platform.machine(),'\n')
print('__________________________________________________________________________[',datetime.datetime.now(),']')