from termcolor import colored

lines = open('./tree.txt').read().splitlines()
top = '\n'.join(lines[:6]) + '\n'
tree = '\n'.join(lines[6:21]) + '\n'
bottom10 = '\n'.join(lines[21:22]) + '\n'
bottom20 = '\n'.join(lines[22:24]) + '\n'
bottom30 = '\n'.join(lines[24:])

R,G,B,C,M,Y,W = 'red green blue cyan magenta yellow white'.split()
r,g,b,c,m,y,w = 'on_red on_green on_blue on_cyan on_magenta on_yellow on_white'.split()
dark = ['dark']

_ = None

garland = []
rabbit = [W, _, dark]
jgs_signature = [W, _, dark]

top_colors = {
    '<' : [Y],
    '>' : [Y],
    '/' : [Y],
    '\\': [Y],
    '_' : [Y],
    '^' : [Y],
    ',' : [Y],
    '.' : [Y],
    '-' : [Y],
}

bottom10_colors = {
    '"' : [G],
    '=' : [G],
    ',' : [G],
    '.' : [G],
    '`' : [G],
    'g' : jgs_signature,
    'j' : jgs_signature,
    's' : jgs_signature,
}

bottom20_colors = {
    '#' : [R, _, dark],
    '"' : [R, _, dark],
    '(' : rabbit,
    ')' : rabbit,
    '_' : rabbit,
    '-' : rabbit,
    "'" : rabbit,
    '`' : rabbit,
    '\\': rabbit,
    '\\': rabbit,
}

tree_colors = {
    '"' : garland,
    '#' : [G],
    '%' : [G],
    '&' : [G, _, dark],
    "'" : garland,
    '+' : [G, _, dark],
    ',' : garland,
    '-' : garland,
    '.' : garland,
    '/' : [G],
    '0' : [G],
    ':' : garland,
    ';' : [G],
    '@' : [R],
    'I' : [G],
    'O' : [B, _, dark],
    '\\': [G],
    '^' : [G],
    '_' : garland,
    '`' : garland,
    'o' : [Y],
    '~' : [G],
}

image = ''

for ch in top:
    args = top_colors.get(ch)
    if args:
        image += colored(ch, *args)
    else:
        image += ch

for ch in tree:
    args = tree_colors.get(ch)
    if args:
        image += colored(ch, *args)
    else:
        image += ch

pattern = '()'
image = image.replace(pattern, colored(pattern, R, _, dark))

for ch in bottom10:
    args = bottom10_colors.get(ch)
    if args:
        image += colored(ch, *args)
    else:
        image += ch

for ch in bottom20:
    args = bottom20_colors.get(ch)
    if args:
        image += colored(ch, *args)
    else:
        image += ch

for ch in bottom30:
    image += colored(ch, *rabbit)


print(image)
