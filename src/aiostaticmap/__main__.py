from .aiostaticmap import Line, StaticMap

if __name__ == '__main__':
    map_ = StaticMap(300, 400, 10)
    line = Line([(13.4, 52.5), (2.3, 48.9)], 'blue', 3)
    map_.add_line(line)
    image = map_.render()
    image.save('berlin_paris.png')
