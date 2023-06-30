
with open('input.txt', 'r') as file:
    inputs = [x.strip() for x in file]


# addx takes 2 cycle, increase regX by value
# noop takes 1 cycle
class Clock:
    def __init__(self):
        self.listeners = []
        self.regX = 1
        self.cycle = 0
    
    def parse_cmd(self, str):
        parts = str.split(' ')
        if len(parts) > 1:
            return self.op(AddX(), int(parts[1]))
        else:
            return self.op(noOp())

    def op(self, cmd, *args):
        cmd.do(self, *args)

    def notify(self):
        for listener in self.listeners:
            listener.update()

    def inc(self):
        self.cycle += 1
        self.notify()

class Command:
    instance = None
    def __new__(self):
        if self.instance is None:
            self.instance = super(Command, self).__new__(self)
        return self.instance
            
    def do(self, clock):
        pass

class AddX(Command):
    def do(self, clock, V):
        clock.inc()
        clock.inc()
        clock.regX += V

class noOp(Command):
    def do(self, clock):
        clock.inc()

class do_on_cycle:
    def __init__(self, clock, cycles):
        self.clock = clock
        self.cycles = cycles
        self.cycles_ss = {}
    def update(self):
        if self.clock.cycle in self.cycles:
            print(f'{self.clock.cycle}, {self.clock.regX}')
            self.cycles_ss[self.clock.cycle] = self.clock.cycle * self.clock.regX
    
class CRT:
    def __init__(self, clock, width = 40, height = 6) -> None:
        self.w = width
        self.h = height
        self.field = [None] * (self.h * self.w)
        self.lit = '#'
        self.dark = '.'
        self.clock = clock

    def update(self):
        ix = self.clock.cycle
        pos = self.clock.regX
        ix -= 1
        if self.in_sprite(pos, ix):
            self.field[ix] = self.lit
        else:
            self.field[ix] = self.dark

    def draw(self):
        for j in range(self.h):
            app = ''
            for i in range(self.w):
                app += self.field[self.w*j+i]
            print(app)

    def in_sprite(self, pos, ix):
        # ix range from (h-1)*(0 <-> w-1)
        # pos range from (0 <-> w-1)
        norm_ix = ix % self.w
        if norm_ix in { pos-1, pos, pos+1 }:
            return True
        return False
    

if __name__ == '__main__':

    clk = Clock()
    keep_track = do_on_cycle(clk, [20, 60, 100, 140, 180, 220])
    crt = CRT(clk)
    clk.listeners.append(keep_track)
    clk.listeners.append(crt)
    
    for inp in inputs:
        print(inp, clk.regX)
        clk.parse_cmd(inp)

    print(keep_track.cycles_ss)
    print(sum(keep_track.cycles_ss.values()))
    
    crt.draw()

    breakpoint()