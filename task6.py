items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    total_calories = 0
    selected_items = []
    total_cost = 0
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)

    for name, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            selected_items.append(name)
            total_calories += data["calories"]
            total_cost += data["cost"]

    return selected_items, total_calories, total_cost


def dynamic_programming(items, budget):
    names = list(items.keys())
    costs = [items[name]["cost"] for name in names]
    calories = [items[name]["calories"] for name in names]
    n = len(names)


    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(budget + 1):
            if costs[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]


    selected_items = []
    total_calories = dp[n][budget]
    j = budget

    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:  # Якщо значення змінилось, страва була взята
            selected_items.append(names[i - 1])
            j -= costs[i - 1]

    selected_items.reverse()  # Відновлення правильного порядку

    return selected_items, total_calories, budget - j


# Тестові дані

budget = 70

# Тестування обох алгоритмів
greedy_result = greedy_algorithm(items, budget)
dp_result = dynamic_programming(items, budget)

# Виведення результатів
print("Жадібний алгоритм:")
print(f"Вибрані страви: {greedy_result[0]}")
print(f"Загальна калорійність: {greedy_result[1]}")
print(f"Витрачений бюджет: {greedy_result[2]}/{budget}")

print("\nДинамічне програмування:")
print(f"Вибрані страви: {dp_result[0]}")
print(f"Загальна калорійність: {dp_result[1]}")
print(f"Витрачений бюджет: {dp_result[2]}/{budget}")
