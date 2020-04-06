import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of progrma')


def factorial(n):
    logging.debug('Start of factorial(%s)' % n)
    total = 1

    for i in range(n + 1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))

    logging.debug('End of factorial(%s)' % n)
    return total


print(factorial(5))
logging.debug('End of program')
"""
0
2020-04-06 18:40:17,141 - DEBUG - Start of progrma
2020-04-06 18:40:17,142 - DEBUG - Start of factorial(5)
2020-04-06 18:40:17,142 - DEBUG - i is 0, total is 0
2020-04-06 18:40:17,142 - DEBUG - i is 1, total is 0
2020-04-06 18:40:17,142 - DEBUG - i is 2, total is 0
2020-04-06 18:40:17,142 - DEBUG - i is 3, total is 0
2020-04-06 18:40:17,142 - DEBUG - i is 4, total is 0
2020-04-06 18:40:17,142 - DEBUG - i is 5, total is 0
2020-04-06 18:40:17,142 - DEBUG - End of factorial(5)
2020-04-06 18:40:17,142 - DEBUG - End of program
"""
