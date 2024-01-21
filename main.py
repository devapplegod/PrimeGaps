import time
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


# Kontroluje, zda je "num" prvočíslem, používá optimalizace jako například kontrolování zda je "num" dělitelné čísly pouze do odmocniny z "num" (vyššímy čísly ani dělitelné být nemůže)
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# Vygeneruje prvních "n" prvočísel
def generate_primes(n):
    prime_list = []
    num = 2
    while len(prime_list) < n:
        if is_prime(num):
            prime_list.append(num)
        num += 1
    return prime_list


# Vypočítá rozdíl každých dvou sousedních hodnot v listu a z těchto rozdílů vytvoří nový list
def generate_gaps(number_list):
    gap_list = []
    for i in range(len(number_list) - 1):
        gap = number_list[i + 1] - number_list[i]
        gap_list.append(gap)
    return gap_list


# Opakovaně vypočítává rozdíly sousedních hodnot v listu (nejprve rozdíly, pak rozdíly rozdílů, pak rozdíly rozdílů rozdílu atd.)
def generate_n_depth_gaps(number_list, depth):
    gap_list = number_list
    for i in range(depth):
        gap_list = generate_gaps(gap_list)
    return gap_list


# Vypočítá rozdíly prvočísel (popřípadě i jejich rozdílů - do hloubky "depth") a ukáže graf.
def calculate(num_of_primes, depth):
    start_time = time.time()

    primes = generate_primes(num_of_primes)
    gaps = generate_n_depth_gaps(primes, depth)

    elapsed_time = time.time() - start_time

    # print(gaps)
    print(f"Elapsed time: {elapsed_time} seconds")

    indices = range(len(gaps))
    plt.scatter(indices, gaps, s=3)

    plt.xlabel('Xth gap')
    plt.ylabel('Gap size')
    plt.title('Plot of Prime gaps')

    current_limits = plt.gca().get_ylim()
    new_limits = (current_limits[0] * depth / 100, current_limits[1] * depth / 100)
    plt.ylim(new_limits)
    plt.show()


calculate(5000, 1000)  # Nejlepší hodnoty mezi 5 000 a 10 000, druhý argument pak mezi 500 a 1 000. Doporučuji fullscreen.
