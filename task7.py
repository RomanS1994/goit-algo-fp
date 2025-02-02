import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):
    sums_count = {i: 0 for i in range(2, 13)}  # Частоти сум від 2 до 12

    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)  
        dice2 = random.randint(1, 6)  
        total = dice1 + dice2  
        sums_count[total] += 1  # Оновлення частоти

    # Обрахування ймовірностей
    probabilities = {s: count / num_rolls for s, count in sums_count.items()}
    return probabilities


def plot_probabilities(probabilities):

    sums = list(probabilities.keys())  
    probs = list(probabilities.values())  

    plt.figure(figsize=(8, 5))
    plt.bar(sums, probs, tick_label=sums)
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірність суми чисел на двох кубиках')

    # Додавання текстових підписів (відсоткове значення)
    for i, prob in enumerate(probs):
        plt.text(sums[i], prob, f"{prob*100:.2f}%", ha='center')

    plt.show()


if __name__ == "__main__":
    for accuracy in [100, 1000, 10000, 100000]:
        print(f"\nСимуляція {accuracy} кидків...")
        
        # Симуляція кидків
        probabilities = simulate_dice_rolls(accuracy)

        # Відображення на графіку
        plot_probabilities(probabilities)
