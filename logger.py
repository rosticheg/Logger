
import logging

logging.basicConfig(level='DEBUG', filename='mylog.log')
logger = logging.getLogger()
print(logger)


print(logger.level)


def main(name):
    logger.debug(f'Just test for main() function: name = {name}')


if __name__ == '__main__':
    main('test')
