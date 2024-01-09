import argparse
import time

from world import World
from GUI import GUI

def main():
    args = get_arguments()
    world = World(args.amount, args.dimension)
    frontend = GUI(world)
    while True:
        world.update_simulation()
        frontend.refresh()
        time.sleep(args.time)
    
def get_arguments():
    parser = argparse.ArgumentParser(prog='EcoSymulator',
                    description='Simulate an ecosystem of animals')
    parser.add_argument('amount', type=int, help='The starting amount of animals that live in the simulation')
    parser.add_argument('-t','--time', type=float, help='Time in seconds per timestep (default = 1 second)', default=1)
    parser.add_argument('-d','--dimension', type=int, nargs=2, help='Dimension (x and y) of the world (default = 50 50 )', default=(50,50))
    return parser.parse_args()

if __name__ == '__main__':
    main()