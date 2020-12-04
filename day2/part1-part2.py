# https://adventofcode.com/2015/day/2

input = open('input').read().splitlines()

# input = ['1x1x10']

paper = 0
ribbon = 0

for dimensions in input:
    [l, w, h] = [int(s) for s in dimensions.split('x')]

    paper += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
    ribbon += min(l*2+w*2, w*2+h*2, h*2+l*2) + l*w*h

print('Order {} feet of wrapping paper'.format(paper))
print('Order {} feet of ribbon'.format(ribbon))
