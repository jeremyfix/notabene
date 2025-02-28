
from . import basics
from pathlib import Path

class defs:
    def __init__(self, path):
        if isinstance(path, Path):
            self.path = path
        else:
            self.path = Path(path)
        self.prefix = None
        self.content = []

    
    def __setitem__(self, at, value):
        if self.prefix:
            key = '{}{}'.format(self.prefix, at)
        else:
            key = at
        v = basics.to(value)
        expr = str(v)
        command = '\\newcommand{\\' + key + '}[' + str(v.max_argnum) + ']{' + expr + '}\n'
        self.f.write(command)
        self.content.append((key, v.max_argnum))
    

    def __enter__(self):
        self.f = open(self.path, 'w')
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.f.close()
        if exc_type:
            print(f'exc_type: {exc_type}')
            print(f'exc_value: {exc_value}')
            print(f'exc_traceback: {exc_traceback}')

    def __arg_calls(self, num):
        return ''.join(['{\\mathbf{' + str(i+1) + '}}' for i in range(num)])
    
    def __arg_print(self, num):
        return ''.join(['\\{' + str(i+1) + '\\}' for i in range(num)])

    def cheatsheet(self):
        name = Path(self.path.stem + '-cheatsheet.tex')
        with open(name, 'w') as f:
            f.write('\\documentclass[a4paper, 10pt]{article}\n')
            f.write('\\usepackage[margin=20mm]{geometry}\n')
            f.write('\\usepackage{bbold}\n')
            f.write('\\usepackage{esvect}\n')
            f.write('\\usepackage{amsmath}\n')
            f.write('\\usepackage{amssymb}\n')
            f.write('\\usepackage{amsthm}\n')
            f.write('\\usepackage{mathdots}\n')
            f.write('\n')
            f.write('% Your commands come from that file\n')
            f.write('\\input{' + str(self.path) + '}\n')
            f.write('\n')
            f.write('\\begin{document}\n')
            f.write('\\hrule\n')
            f.write('\\vspace{3mm}\n')
            f.write('\\centerline{\\large Cheatsheet for {\\tt ' + self.path.stem + '.tex}}\n')
            f.write('\\vspace{3mm}\n')
            f.write('\\hrule\n')
            f.write('\\vspace{5mm}\n')
            f.write('\\begin{eqnarray*}\n')
            for k, num in self.content[:-1]:
                f.write('\\mbox{\\tt \\textbackslash ' + k + '}' + self.__arg_print(num) + ' & : & \\')
                f.write(k)
                f.write(self.__arg_calls(num))
                f.write(' \\\\\n')
            if len(self.content) > 0:
                k, num = self.content[-1]
                f.write('\\mbox{\\tt \\textbackslash ' + k + '}' + self.__arg_print(num) + ' & : & \\')
                f.write(k)
                f.write(self.__arg_calls(num))
                f.write(' \n')
            f.write('\\end{eqnarray*}\n')
            f.write('\\end{document}\n')
        print()
        print('Cheatsheet {} generated.'.format(name))
        print()
    
