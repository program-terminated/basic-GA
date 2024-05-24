# n-point crossover implementation
DEBUG = 0
n_point = 1
uniform = 0

def n_point_crossover(p1, p2, n):
    n_indices = []
    while len(n_indices) < n:
        crossover_index = random.randint(1, len(p1)-1) # Bounds set to 1 and len(p1)-1 to ensure that the index actually has an effect on the offspring
        if crossover_index not in n_indices:
            n_indices.append(crossover_index)

    n_indices = np.sort(n_indices)
    if DEBUG:
        print(p1, p2)
        print(n_indices)

    # Create offspring
    offspring1 = p1[0:n_indices[0]] + p2[n_indices[0]:n_indices[1]] + p1[n_indices[1]:n_indices[2]] + p2[n_indices[2]:n_indices[3]] + p1[n_indices[3]:]
    offspring2 = p2[0:n_indices[0]] + p1[n_indices[0]:n_indices[1]] + p2[n_indices[1]:n_indices[2]] + p1[n_indices[2]:n_indices[3]] + p2[n_indices[3]:]

    return offspring1, offspring2


# Uniform crossover implementation
def uniform_crossover(p1, p2):
    offspring1 = []
    offspring2 = []

    for offspring in [offspring1, offspring2]:
        for i in range(len(p1)):
            coinflip = random.randint(1,2)
            if DEBUG:
                print(coinflip)

            # Give offspring gene from p1
            if coinflip == 1:
                offspring.append(p1[i])

            # Give offspring gene from p2
            else:
                offspring.append(p2[i])

    return offspring1, offspring2


if DEBUG:
    # n-point crossover
    if n_point:
        o1, o2 = n_point_crossover([0,0,0,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1,1,1], 4)

    # Uniform crossover
    elif uniform:
        o1, o2 = uniform_crossover([0,0,0,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1,1,1])
        
    # No crossover specified
    else:
        raise ValueError("No crossover method specified.")

    print(o1, o2)