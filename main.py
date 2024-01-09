import argparse
import time

from world import World

def main():
    args = get_arguments()
    world = World(args.amount)
    while True:
        world.update_simulation()
        print(world.amount)
        time.sleep(args.time)
    
def get_arguments():
    parser = argparse.ArgumentParser(prog='EcoSymulator',
                    description='Simulate an ecosystem of animals')
    parser.add_argument('amount', type=int, help='The starting amount of animals that live in the simulation')
    parser.add_argument('-t','--time', type=float, help='Time in seconds per timestep (default = 1 second)', default=1)
    return parser.parse_args()

if __name__ == '__main__':
    main()