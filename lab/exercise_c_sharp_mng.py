from ctypes import cdll


class CSharpNinja:
    def __init__(self, path_to_file, function_name):
        self.path_to_file = path_to_file
        self.function_name = function_name
        self.lib_object = self.load_the_file(self.path_to_file)

        # executions
        self.result = self.call_the_function(self.function_name)
        self.result2 = print(f'The function returned: {self.result}')

    def load_the_file(self, path_to_file):
        lib_object = cdll.LoadLibrary(path_to_file)
        return lib_object

    def call_the_function(self, function_name):
        my_call = 'self.lib_object.' + function_name + '()'
        return eval(my_call)

    def __str__(self):
        return f'{self.lib_object}'


# give the 2 parameters manually
# ----------------------------------------------------------------------------------------
# path = 'C:\\Users\\BG0DZRV\\PycharmProjects\\pythonProject1\\files\\hello-world.dll'
path = 'D:\\Study\\Projects\\VSC\c_s_pj\\bin\Debug\\net5.0\\MyDLLProject'
# function_name = 'MessageBoxThread'
function_name = 'HelloWorld'

connection = CSharpNinja(path, function_name)
