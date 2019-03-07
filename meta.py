
file = "meta1.py"

code = "def foo(x,y):/n/tprint('foobbar:' + str(x*y))/na = lambda: foo(x,y)"
code_lines = code.replace("/t","    ").split("/n")

with open(file, 'w') as in_file:
  #in_file.writelines("print('it worked!') \n" * 29)
  for line in code_lines:
    in_file.writelines(line + "\n")

file = file.split(".")[0]


x = 1
y = 1
g = lambda: eval(file)

exec 'import {}'.format(file)
print g()
g().x = 4
g().y = 9
g().a()