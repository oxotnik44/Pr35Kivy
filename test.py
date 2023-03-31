from ursina import *

app = Ursina()  # Создание приложения

# Создание объектов сцены
table = Entity(model='cube', color=color.black, scale=(2, 1, 3), rotation=(90, 0, 0))
ball = Entity(model='sphere', color=color.cyan, z=-1, scale=0.1, collider='box')
player1 = Entity(model='cube', color=color.cyan, scale=(0.6, 0.1, 1), position=(0, -1.4, -1), collider='box')
player2 = duplicate(player1, y=1.4)

# Начальные скорости мяча по оси X и Y
speed_x = speed_y = 0.6

def update():
    global speed_x, speed_y  # Используем глобальные переменные

    # Движение мяча по осям X и Y с учетом времени
    ball.x += speed_x * time.dt
    ball.y += speed_y * time.dt

    # Отражение мяча от стенок поля
    if abs(ball.x) > 0.95:
        speed_x = -speed_x

    # Возвращение мяча в центр поля и сброс скорости, если он попадает за ворота
    if abs(ball.y) > 1.45:
        speed_x = speed_y = 0.6
        ball.x = ball.y = 0

 # Движение игроков по оси X в зависимости от нажатых клавиш
    if player1.x < -0.7:
        player1.x = -0.7
    if player1.x > 0.7:
        player1.x = 0.7
    if player2.x < -0.7:
        player2.x = -0.7
    if player2.x > 0.7:
        player2.x = 0.7

    player1.x += held_keys['d'] * time.dt
    player1.x -= held_keys['a'] * time.dt
    player2.x += held_keys['right arrow'] * time.dt
    player2.x -= held_keys['left arrow'] * time.dt


    # Отражение мяча от ракеток игроков
    if ball.intersects().hit:
        speed_y = -speed_y
        speed_x *= 1.1
        speed_y *= 1.1

# Настройка камеры
camera.orthographic = True
camera.fov = 4

app.run()  # Запуск приложения
