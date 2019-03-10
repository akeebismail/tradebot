import sys

from trade import main

if __name__ == '__main__':
    main.set_loggers()
    main.main(sys.argv[1:])