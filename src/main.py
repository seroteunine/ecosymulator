import argparse
import time

import pygame

from world import World
from GUI import GUI

def main():
    args = get_arguments()
    world = World(args.amount, args.dimension)
    frontend = GUI(world)
    while True:
        if not frontend.process_events():
            break
        world.update_simulation()
        frontend.refresh()
        time.sleep(args.time)
    pygame.quit() 
    
def get_arguments():
    parser = argparse.ArgumentParser(prog='EcoSymulator',
                    description='Simulate an ecosystem of animals')
    parser.add_argument('amount', type=int, nargs='?', help='The starting amount of animals that live in the simulation (default = 50)', default=150)
    parser.add_argument('-t','--time', type=float, help='Time in seconds per timestep (default = 0.05 second)', default=0.05)
    parser.add_argument('-d','--dimension', type=int, nargs=2, help='Dimension (x and y) of the world (default = 50 50 )', default=(80, 80))
    return parser.parse_args()

if __name__ == '__main__':
    main()