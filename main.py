from mouse import getColor
from logic import colorDecision

try:
    while(True):
        c, (x, y) = getColor()
        d = colorDecision(c)
        output = 'x: ' + str(x).rjust(4) + '- y: ' + str(y).rjust(4)
        output += ' RGB: (' + str(c[0]).rjust(3) + ', ' +  str(c[1]).rjust(3) + ', ' +  str(c[2]).rjust(3) + ') - Decision: ' + str(d).rjust(7) 

        print(output, end='')
        print('\b' * len(output), end='', flush=True)
        

except KeyboardInterrupt:
    print("Done ...")
