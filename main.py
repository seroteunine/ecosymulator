import argparse

def main():
    parser = argparse.ArgumentParser(prog='EcoSymulator',
                    description='Simulate an ecosystem of animals',
                    epilog='At minimum, specify amount of animals in the ecosystem')
    parser.add_argument('amount', type=int, help='The starting amount of animals that live in the simulation')
    args = parser.parse_args()
    print(args.amount)
    

if __name__ == '__main__':
    main()