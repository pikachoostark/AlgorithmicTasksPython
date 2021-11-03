def fence(lst, numrails):
    fence_lst = [[None] * len(lst) for _ in range(numrails)]
    rails = list(range(numrails - 1)) + list(range(numrails - 1, 0, -1))
    for n, x in enumerate(lst):
        fence_lst[rails[n % len(rails)]][n] = x
    return [c for rail in fence_lst for c in rail if c is not None]


def encode(text, n):
    return ''.join(fence(text, n))


def decode(text, n):
    rng = range(len(text))
    pos = fence(rng, n)
    return ''.join(text[pos.index(n)] for n in rng)


z = encode('ATTACK.AT.DAWN', 3)
print(z)  # ACTWTAKA.ANT.D
y = decode(z, 3)
print(y)  # ATTACK.AT.DAWN

text = "AaY--rpyfneJBeaaX0n-,ZZcs-uXeeSVJ-sh2tioaZ}slrg,-ciE-anfGt.-eCIyss-TzprttFliora{GcouhQIadctm0ltt-FYluuezTyorZ-"
for i in range(3, 255):
    print(decode(text, i))
