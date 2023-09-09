class SVG:
    def __init__(self):
        self.lines = []
        self.circles = []

    def line(self, x1, y1, x2, y2, color='black'):
        self.lines.append((x1, y1, x2, y2, color))

    def circle(self, cx, cy, r, color='black'):
        self.circles.append((cx, cy, r, color))

    def save(self, filename, width, height):
        with open(filename, 'w') as f:
            f.write(
                '<svg version="1.1" width="{:.6f}" height="{:.6f}" xmlns="http://www.w3.org/2000/svg">\n'.format(width,
                                                                                                                 height))
            for x1, y1, x2, y2, color in self.lines:
                f.write('<line x1="{:.6f}" y1="{:.6f}" x2="{:.6f}" y2="{:.6f}" stroke="{}" />\n'.format(x1, y1, x2, y2,
                                                                                                        color))
            for cx, cy, r, color in self.circles:
                f.write('<circle cx="{:.6f}" cy="{:.6f}" r="{:.6f}" fill="{}" />\n'.format(cx, cy, r, color))
            f.write('</svg>')
svg = SVG()

svg.line(10, 10, 60, 10, color='black')
svg.line(60, 10, 60, 60, color='black')
svg.line(60, 60, 10, 60, color='black')
svg.line(10, 60, 10, 10, color='black')

svg.circle(10, 10, r=5, color='red')
svg.circle(60, 10, r=5, color='red')
svg.circle(60, 60, r=5, color='red')
svg.circle(10, 60, r=5, color='red')

svg.save('pic.svg', 100, 100)
