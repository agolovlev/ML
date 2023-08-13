import numpy as np
import plotly.graph_objects as go

# Гравитационная постоянная (м^3 / кг / с^2)
G = 6.67430e-11

# Массы планет в кг
masses = {
    'Sun': 1.989e30,
    'Mercury': 3.285e23,
    'Venus': 4.867e24,
    'Earth': 5.972e24,
    'Mars': 6.39e23,
    'Jupiter': 1.898e27,
    'Saturn': 5.683e26,
    'Uranus': 8.681e25,
    'Neptune': 1.024e26
}

# Начальные положения и скорости планет в метрах и метрах в секунду
positions = {
    'Sun': np.array([0.0, 0.0], dtype=np.float64),
    'Mercury': np.array([46e9, 0.0], dtype=np.float64),
    'Venus': np.array([107.5e9, 0.0], dtype=np.float64),
    'Earth': np.array([147e9, 0.0], dtype=np.float64),
    'Mars': np.array([206e9, 0.0], dtype=np.float64),
    'Jupiter': np.array([740e9, 0.0], dtype=np.float64),
    'Saturn': np.array([1353e9, 0.0], dtype=np.float64),
    'Uranus': np.array([2748e9, 0.0], dtype=np.float64),
    'Neptune': np.array([4450e9, 0.0], dtype=np.float64)
}

# Начальные скорости планет в метрах в секунду
velocities = {
    'Sun': np.array([0.0, 0.0], dtype=np.float64),
    'Mercury': np.array([0.0, 47400.0], dtype=np.float64),
    'Venus': np.array([0.0, 35000.0], dtype=np.float64),
    'Earth': np.array([0.0, 30000.0], dtype=np.float64),
    'Mars': np.array([0.0, 24000.0], dtype=np.float64),
    'Jupiter': np.array([0.0, 13000.0], dtype=np.float64),
    'Saturn': np.array([0.0, 9000.0], dtype=np.float64),
    'Uranus': np.array([0.0, 6835.0], dtype=np.float64),
    'Neptune': np.array([0.0, 5477.0], dtype=np.float64)
}

# Временной интервал и количество шагов моделирования
dt = 3600.0  # 1 час в секундах
num_steps = 365 * 24  # Количество шагов для моделирования 1 года

# Массивы для хранения траекторий планет
trajectories = {planet: [] for planet in masses}

# Моделирование движения планет
for i in range(num_steps):
    for planet in masses:
        acc = np.zeros(2, dtype=np.float64)
        for other_planet in masses:
            if other_planet != planet:
                r = positions[other_planet] - positions[planet]
                acc += G * masses[other_planet] * r / np.linalg.norm(r)**3

        velocities[planet] += acc * dt
        positions[planet] += velocities[planet] * dt

        trajectories[planet].append(positions[planet].copy())

# Визуализация результатов с помощью plotly
fig = go.Figure()

for planet in masses:
    x = [pos[0] for pos in trajectories[planet]]
    y = [pos[1] for pos in trajectories[planet]]
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=planet))
    fig.add_trace(go.Scatter(x=[x[-1]], y=[y[-1]], mode='markers', name=planet, marker=dict(size=8)))

fig.update_layout(
    xaxis_title='x (м)',
    yaxis_title='y (м)',
    title='Движение планет Солнечной системы вокруг Солнца',
    showlegend=True,
    legend=dict(x=0, y=1)
)

fig.show()