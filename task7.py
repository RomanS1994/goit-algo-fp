import random
import matplotlib.pyplot as plt
from collections import Counter

# Аналітичні ймовірності для порівняння
analytical_probabilities = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36,
    7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}

def simulate_dice_rolls(num_rolls):
    sums_count = Counter(random.randint(1, 6) + random.randint(1, 6) for _ in range(num_rolls))
    
    # Обчислення ймовірностей
    probabilities = {s: sums_count[s] / num_rolls for s in range(2, 13)}
    return probabilities

def plot_probabilities(probabilities, num_rolls):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.figure(figsize=(10, 5))
    plt.bar(sums, probs, width=0.4, label="Monte Carlo", color="blue", alpha=0.7)
    plt.bar(sums, [analytical_probabilities[s] for s in sums], width=0.4, label="Analytical", color="red", alpha=0.5)

    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність')
    plt.title(f'Ймовірність суми чисел на двох кубиках ({num_rolls} кидків)')
    plt.xticks(sums)
    plt.legend()

    # Додавання підписів (відсотків)
    for i, prob in enumerate(probs):
        plt.text(sums[i], prob, f"{prob*100:.2f}%", ha='center', va='bottom', fontsize=9)

    plt.show()

if __name__ == "__main__":
    for accuracy in [100, 1000, 10000, 100000]:
        print(f"\nСимуляція {accuracy} кидків...")
        
        # Симуляція кидків
        probabilities = simulate_dice_rolls(accuracy)

        # Відображення на графіку
        plot_probabilities(probabilities, accuracy)
