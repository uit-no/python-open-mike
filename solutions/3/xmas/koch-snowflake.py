import math
import collections


def write_svg(file_name, polygon, height, width):
    with open(file_name, 'w') as f:
        f.write('<?xml version="1.0" encoding="UTF-8" ?>\n')
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" version="1.1" height="{height}" width="{width}">\n')
        points = ' '.join([f'{polygon.xs[i]},{polygon.ys[i]}' for i in range(len(polygon.xs))])
        f.write(f'  <polygon points="{points}" style="fill:{polygon.color}; stroke-width:0" />\n')
        f.write('</svg>\n')


def rotate_v(v, angle):

    r = angle/360.0*2.0*math.pi
    cs = math.cos(r)
    sn = math.sin(r)

    vx_old, vy_old = v

    vx = cs * vx_old - sn * vy_old
    vy = sn * vx_old + cs * vy_old

    return vx, vy


def rotate_vs(vs, angle):
    return [rotate_v(v, angle) for v in vs]


def build_polygon(size, level, color):
    origin = (0.0, 0.0)
    vs = grow(0, level, (size, 0.0))
    vs2 = rotate_vs(vs, 120.0)
    vs3 = rotate_vs(vs2, 120.0)
    vs = vs + vs2 + vs3

    Polygon = collections.namedtuple('Polygon', 'xs, ys, color')
    ox, oy = origin
    xs = [ox]
    ys = [oy]
    for vx, vy in vs[:-1]:
        xs.append(xs[-1] + vx)
        ys.append(ys[-1] + vy)
    shift_x = 300 + 0.5*(200.0 - size)
    shift_y = 300 + 0.25*(200.0 - size)
    xs = [(x + shift_x) for x in xs]
    ys = [(y + shift_y) for y in ys]
    return Polygon(xs=xs, ys=ys, color=color)


def grow(level, max_level, v):
    if level == max_level:
        return [v]
    else:
        level += 1
        s = (v[0]/3.0, v[1]/3.0)
        vs1 = grow(level, max_level, s)
        vs2 = grow(level, max_level, rotate_v(s, -60.0))
        vs3 = grow(level, max_level, rotate_v(s, +60.0))
        return vs1 + vs2 + vs3 + vs1


if __name__ == '__main__':

    polygon = build_polygon(size=200.0, level=4, color='rgb(30.0%, 30.0%, 100.0%)')
    height = 1000.0
    width = 1000.0

    write_svg(file_name='example.svg',
              polygon=polygon,
              height=height,
              width=width)
