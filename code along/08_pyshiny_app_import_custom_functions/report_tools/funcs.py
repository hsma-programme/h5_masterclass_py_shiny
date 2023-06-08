'''
Way to re-cycle userful tools and improve the readability of code.
'''

import numpy as np
import matplotlib.pyplot as plt

def chart(input_n):
    np.random.seed(19680801)
    x = 100 + 15 * np.random.randn(437)
    plt.title("Really Informative Histogram")
    plt.xlabel('Numbers')
    plt.ylabel("Count")
    plt.hist(x, input_n, density=True)
    
def print_hello(input_n):
    '''
    This function returns a string.
    '''

    return f"Hello, Secret Agent {input_n}"