from subprocess import call
for i in [18, 24]:
    call(f'python ../tools/micropython-font-to-py/font_to_py.py JetBrainsMono-Regular.ttf --xmap {i} sans{i}.py ; mv sans{i}.py ../wasp/fonts/sans{i}.py', shell=True)
    

for i in [28, 36]:
    call(f'python ../tools/micropython-font-to-py/font_to_py.py JetBrainsMono-Regular.ttf --xmap {i}  -e 58 -c 0123456789:+- sans{i}.py ; mv sans{i}.py ../wasp/fonts/sans{i}.py', shell=True)
