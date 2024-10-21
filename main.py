import pygame
import random
import math

pygame.init()

screen_info = pygame.display.Info()
WIDTH, HEIGHT = screen_info.current_w, screen_info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT))
CELL_SIZE = 50
FPS = 7
WAVE_SPEED = 0.08
WAVE_AMPLITUDE = 20
MAX_SEGMENTS = 7

SNAKE_COLORS = [
    (255, 127, 80),
    (192, 192, 192),
    (255, 165, 0),
    (220, 20, 60),
    (106, 90, 205),
    (0, 255, 0),
    (0, 255, 127),
    (0, 100, 0),
    (128, 128, 0),
    (173, 255, 47),
    (123, 104, 238),
    (0, 128, 128),
    (0, 0, 255),
    (255, 0, 0),
    (240, 230, 140),
    (47, 79, 79),
    (0, 128, 0),
    (255, 105, 180),
    (205, 133, 63),
    (139, 69, 19),
    (255, 140, 0),
    (95, 158, 160),
]

selected_snake_color = SNAKE_COLORS[0]

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('Змейка')

default_background = pygame.image.load("skins/fon.jpg").convert()
default_background = pygame.transform.scale(default_background,
                                            (WIDTH, HEIGHT))

background_images = [
    pygame.image.load("alfons/fons1.png").convert(),
    pygame.image.load("alfons/fons2.png").convert(),
    pygame.image.load("alfons/fons4.png").convert(),
    pygame.image.load("alfons/fons6.png").convert(),
    pygame.image.load("alfons/fons7.png").convert(),
    pygame.image.load("alfons/fons8.png").convert(),
    pygame.image.load("alfons/fons9.png").convert(),
    pygame.image.load("alfons/fons11.png").convert(),
    pygame.image.load("alfons/fons12.png").convert(),
    pygame.image.load("alfons/fons10.png").convert(),
    pygame.image.load("alfons/fons13.png").convert(),
    pygame.image.load("alfons/fons3.png").convert(),
    pygame.image.load("alfons/fons14.png").convert(),
    pygame.image.load("alfons/fons15.png").convert(),
    pygame.image.load("alfons/fons16.png").convert(),
    pygame.image.load("alfons/fons17.png").convert(),
    pygame.image.load("alfons/fons18.png").convert(),
    pygame.image.load("alfons/fons19.png").convert(),
    pygame.image.load("alfons/fons20.png").convert(),
    pygame.image.load("alfons/fons21.png").convert(),
    pygame.image.load("alfons/fons5.png").convert(),
    pygame.image.load("alfons/fons22.png").convert()
]

for i in range(len(background_images)):
    background_images[i] = pygame.transform.scale(background_images[i],
                                                  (WIDTH, HEIGHT))

SKIN_WINDOW_HEAD_SIZE = (150, 150)
GAME_HEAD_SIZE = (CELL_SIZE, CELL_SIZE)

skins = [
    pygame.image.load("skins/skin10.png").convert_alpha(),
    pygame.image.load("skins/skin2.png").convert_alpha(),
    pygame.image.load("skins/skin17.png").convert_alpha(),
    pygame.image.load("skins/skin9.png").convert_alpha(),
    pygame.image.load("skins/skin7.png").convert_alpha(),
    pygame.image.load("skins/skin8.png").convert_alpha(),
    pygame.image.load("skins/skin1.png").convert_alpha(),
    pygame.image.load("skins/skin19.png").convert_alpha(),
    pygame.image.load("skins/skin6.png").convert_alpha(),
    pygame.image.load("skins/skin20.png").convert_alpha(),
    pygame.image.load("skins/skin13.png").convert_alpha(),
    pygame.image.load("skins/skin21.png").convert_alpha(),
    pygame.image.load("skins/skin3.png").convert_alpha(),
    pygame.image.load("skins/skin4.png").convert_alpha(),
    pygame.image.load("skins/skin12.png").convert_alpha(),
    pygame.image.load("skins/skin14.png").convert_alpha(),
    pygame.image.load("skins/skin16.png").convert_alpha(),
    pygame.image.load("skins/skin5.png").convert_alpha(),
    pygame.image.load("skins/skin15.png").convert_alpha(),
    pygame.image.load("skins/skin18.png").convert_alpha(),
    pygame.image.load("skins/skin22.png").convert_alpha(),
    pygame.image.load("skins/skin11.png").convert_alpha()
]

snake_head_image_skin = pygame.transform.scale(skins[0], SKIN_WINDOW_HEAD_SIZE)
snake_head_image_game = pygame.transform.scale(skins[0], GAME_HEAD_SIZE)

selected_skin_index = 0

music_files = [
    "songs/Raffaella Carrà - Pedro (TikTok Remix).mp3",
    "songs/Ksenon-—-Дельфины-_Symphony-пародия-БЕЗ-МАТА_-_.mp3",
    "songs/viki-show-prosto-mp3.mp3",
    "songs/tyr_tyr_tyr_-_tyr_tyr_tyr_(SkySound.cc).mp3",
    "songs/Lida, Серега Пират - Спасибо господь что я такой.mp3",
    "songs/dartagnan-was-wollen-wir-trinken-mp3.mp3",
    "songs/В'ячеслав Кукоба - Кабанчик (DJ Crab1k Remix).mp3",
    "songs/pesnya-ya-goryachij-meksikanec-mp3.mp3",
    "songs/3nst1s1mk1_z1_d2ng3_d1_l2zg3nk1_r2m3ks.mp3",
    "songs/Синий трактор - Рыбы.mp3",
    "songs/Песня - Шни Шна Шнапи.mp3",
    "songs/bandicam-2024-10-07-21-18-10-075.mp3",
    "songs/ernest-merkel-ver-ace-shajlushaj-remix-mp3.mp3",
    "songs/1617021342_1617018828dlrvtnnstshplmntktk.mp3",
    "songs/Neizvesten_-_kumi_kumi_(SkySound.cc).mp3",
    "songs/ya-glebas-vacok-pochuvstvuj-mp3.mp3",
    "songs/BaRbi_-_a_YA_bArBi_GyoRl_YA_lYUbLyu_FuTbOl_i_DiRoL_(SkySound.cc).mp3",
    "songs/Амира - Киса.mp3",
    "songs/bandicam-2024-10-06-21-36-01-684.mp3",
    "songs/mem-ichwillnicht.mp3",
    "songs/Моргенштерн - Последняя любовь пепел на простынях.mp3",
    "songs/BASSBOOSTED-.mp3",
]

BUTTON_SIZE = 50
BUTTON_COLOR = (100, 100, 100)
ARROW_COLOR = (255, 255, 255)
LOCK_COLOR = (100, 100, 100)
FONT_COLOR = (255, 255, 255)

skin_names = [
    "Саныч",
    "Бабуин",
    "Сёмга",
    "Олег",
    "БУМ",
    "Дигимончик",
    "Ди(е)мон",
    "Котлета",
    "Светлан",
    "Дэнич",
    "Котик",
    "Лук парей",
    "MakSoS",
    "Лизочек",
    "Зайчик",
    "Игнатус",
    "Булочка",
    "Аниме",
    "Хлэб",
    "Капуста",
    "Тоха",
    "БОС"
]

apple_image = pygame.image.load("skins/images.png").convert_alpha()
apple_image = pygame.transform.scale(apple_image, (CELL_SIZE, CELL_SIZE))

game_over_image = pygame.image.load("skins/images.jpg").convert()
game_over_image = pygame.transform.scale(game_over_image, (WIDTH, HEIGHT))


def draw_button(text, x, y, width, height, active=True):
    if active:
        pygame.draw.rect(screen, BUTTON_COLOR, (x, y, width, height))
    else:
        pygame.draw.rect(screen, LOCK_COLOR, (x, y, width, height))
    font = pygame.font.Font(None, 36)
    label = font.render(text, True, (255, 255, 255))
    text_rect = label.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(label, text_rect)


class Snake:
    def __init__(self, x, y, color, skin):
        self.body = [(x, y)]
        self.direction = (CELL_SIZE, 0)
        self.color = color
        self.growing = False
        self.skin = skin

    def move(self):
        head_x, head_y = self.body[0]
        new_head_x = head_x + self.direction[0]
        new_head_y = head_y + self.direction[1]

        self.body.insert(0, (new_head_x, new_head_y))
        if not self.growing:
            self.body.pop()
        else:
            self.growing = False

    def grow(self):
        if len(self.body) < MAX_SEGMENTS:
            self.growing = True

    def draw(self):
        circle_radius = CELL_SIZE // 2
        circle_spacing = 1, 5 * circle_radius

        for i in range(len(self.body)):
            snake_x, snake_y = self.body[i]
            pygame.draw.circle(
                screen,
                self.color,
                (snake_x + CELL_SIZE // 2, snake_y + CELL_SIZE // 2),
                circle_radius * (MAX_SEGMENTS - i) / MAX_SEGMENTS,
            )

        snake_x, snake_y = self.body[0]
        screen.blit(
            self.skin,
            (
                snake_x,
                snake_y,
            ),
        )


class Apple:
    def __init__(self):
        self.spawn()

    def spawn(self):
        self.position = (
            random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
            random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)

    def draw(self):
        screen.blit(apple_image, (self.position[0], self.position[1]))


def skin_snake_window():
    global selected_skin_index, snake_head_image_skin, snake_head_image_game, selected_snake_color
    window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("Выбор скина")

    time = 0
    segments = 7

    total_apples = 0
    try:
        with open("scores.txt", "r") as file:
            total_apples = sum(int(line.strip()) for line in file)
    except FileNotFoundError:
        pass

    while True:
        screen.blit(default_background, (0, 0))
        label = pygame.font.Font(None, 40).render("Скин змеи", True,
                                                  (255, 255, 255))
        window.blit(label, (WIDTH // 2 - 50, 30))

        draw_button("Выбрать скин", (WIDTH - 250) // 2, 550, 200, 50)

        snake_x = WIDTH // 3
        snake_y = HEIGHT // 2
        circle_radius = 45
        circle_spacing = 1.5 * circle_radius

        for i in range(1, segments):
            offset_y = math.sin(
                time * WAVE_SPEED + i * math.pi / segments) * WAVE_AMPLITUDE
            pygame.draw.circle(
                window,
                SNAKE_COLORS[selected_skin_index],
                (snake_x + i * circle_spacing, snake_y + offset_y),
                circle_radius,
            )

        offset_y = math.sin(time * WAVE_SPEED) * WAVE_AMPLITUDE
        pygame.draw.circle(
            window, SNAKE_COLORS[selected_skin_index],
            (snake_x, snake_y + offset_y), circle_radius
        )

        window.blit(
            snake_head_image_skin,
            (
                snake_x - SKIN_WINDOW_HEAD_SIZE[0] // 2,
                snake_y + offset_y - SKIN_WINDOW_HEAD_SIZE[1] // 2,
            ),
        )

        pygame.draw.rect(window, BUTTON_COLOR, (
            snake_x - SKIN_WINDOW_HEAD_SIZE[0] // 2 - 100, snake_y - 50,
            BUTTON_SIZE, BUTTON_SIZE))
        pygame.draw.polygon(window, ARROW_COLOR, [
            (snake_x - SKIN_WINDOW_HEAD_SIZE[0] // 2 - 80, snake_y - 30),
            (snake_x - SKIN_WINDOW_HEAD_SIZE[0] // 2 - 60, snake_y - 50),
            (snake_x - SKIN_WINDOW_HEAD_SIZE[0] // 2 - 60, snake_y - 10)])

        pygame.draw.rect(window, BUTTON_COLOR, (
            snake_x + SKIN_WINDOW_HEAD_SIZE[0] // 2 + 30 + circle_spacing * (
                    segments - 1), snake_y - 50, BUTTON_SIZE, BUTTON_SIZE))
        pygame.draw.polygon(window, ARROW_COLOR, [(snake_x +
                                                   SKIN_WINDOW_HEAD_SIZE[
                                                       0] // 2 + 50 + circle_spacing * (
                                                           segments - 1),
                                                   snake_y - 30), (snake_x +
                                                                   SKIN_WINDOW_HEAD_SIZE[
                                                                       0] // 2 + 70 + circle_spacing * (
                                                                           segments - 1),
                                                                   snake_y - 50),
                                                  (snake_x +
                                                   SKIN_WINDOW_HEAD_SIZE[
                                                       0] // 2 + 70 + circle_spacing * (
                                                           segments - 1),
                                                   snake_y - 10)])

        font_small = pygame.font.Font(None, 30)
        apple_counter_text = font_small.render(
            f"Всего у вас {total_apples} яблок", True, (255, 255, 255))
        window.blit(apple_counter_text, (10, 10))

        font = pygame.font.Font(None, 60)
        skin_name = font.render(skin_names[selected_skin_index], True,
                                (255, 255, 255))
        window.blit(skin_name, (snake_x + 180, snake_y - 150))

        if 4 <= selected_skin_index <= 21:
            font_small = pygame.font.Font(None, 30)
            unlock_text = font_small.render(
                f"Соберите {5 + 5 * (selected_skin_index - 4)} яблок, чтобы открыть этот скин",
                True, FONT_COLOR)
            window.blit(unlock_text, (snake_x, snake_y + 140))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    selected_skin_index = (selected_skin_index + 1) % len(
                        skins)
                    snake_head_image_skin = pygame.transform.scale(
                        skins[selected_skin_index], SKIN_WINDOW_HEAD_SIZE
                    )
                    snake_head_image_game = pygame.transform.scale(
                        skins[selected_skin_index], GAME_HEAD_SIZE
                    )
                    selected_snake_color = SNAKE_COLORS[selected_skin_index]
                elif event.key == pygame.K_LEFT:
                    selected_skin_index = (selected_skin_index - 1) % len(
                        skins)
                    snake_head_image_skin = pygame.transform.scale(
                        skins[selected_skin_index], SKIN_WINDOW_HEAD_SIZE
                    )
                    snake_head_image_game = pygame.transform.scale(
                        skins[selected_skin_index], GAME_HEAD_SIZE
                    )
                    selected_snake_color = SNAKE_COLORS[selected_skin_index]
                elif event.key == pygame.K_RETURN:
                    if selected_skin_index < 4 or is_skin_unlocked(
                            selected_skin_index):
                        return
                    else:
                        font_error = pygame.font.Font(None, 40)
                        error_text = font_error.render(
                            "Скин ещё не разблокирован", True, (255, 0, 0))
                        window.blit(error_text, (
                            WIDTH // 2 - error_text.get_width() // 2,
                            HEIGHT // 2 - error_text.get_height() // 2))
                        pygame.display.flip()
                        pygame.time.delay(1000)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if (
                        (WIDTH // 2 - 250 // 2) < mouse_pos[0] < (
                        WIDTH // 2 + 250 // 2)
                        and 550 < mouse_pos[1] < 600
                ):
                    if selected_skin_index < 4 or is_skin_unlocked(
                            selected_skin_index):
                        return
                    else:
                        font_error = pygame.font.Font(None, 40)
                        error_text = font_error.render(
                            "Недостаточное количество яблок", True,
                            (255, 0, 0))
                        window.blit(error_text, (
                            WIDTH // 2 - error_text.get_width() // 2,
                            HEIGHT // 2 - error_text.get_height() // 2 - 100))
                        pygame.display.flip()
                        pygame.time.delay(1000)

                if (
                        snake_x - SKIN_WINDOW_HEAD_SIZE[0] // 2 - 100 <
                        mouse_pos[0] <
                        snake_x - SKIN_WINDOW_HEAD_SIZE[0] // 2 - 50
                        and snake_y - 50 < mouse_pos[1] <
                        snake_y
                ):
                    selected_skin_index = (selected_skin_index - 1) % len(
                        skins)
                    snake_head_image_skin = pygame.transform.scale(
                        skins[selected_skin_index], SKIN_WINDOW_HEAD_SIZE
                    )
                    snake_head_image_game = pygame.transform.scale(
                        skins[selected_skin_index], GAME_HEAD_SIZE
                    )
                    selected_snake_color = SNAKE_COLORS[selected_skin_index]

                if (
                        snake_x + SKIN_WINDOW_HEAD_SIZE[
                    0] // 2 + 30 + circle_spacing * (segments - 1) < mouse_pos[
                    0] <
                        snake_x + SKIN_WINDOW_HEAD_SIZE[
                    0] // 2 + 80 + circle_spacing * (segments - 1)
                        and snake_y - 50 < mouse_pos[1] <
                        snake_y
                ):
                    selected_skin_index = (selected_skin_index + 1) % len(
                        skins)
                    snake_head_image_skin = pygame.transform.scale(
                        skins[selected_skin_index], SKIN_WINDOW_HEAD_SIZE
                    )
                    snake_head_image_game = pygame.transform.scale(
                        skins[selected_skin_index], GAME_HEAD_SIZE
                    )
                    selected_snake_color = SNAKE_COLORS[selected_skin_index]

        time += 0.1
        pygame.display.flip()


def start_screen():
    global selected_skin_index
    while True:
        screen.blit(default_background, (0, 0))
        font = pygame.font.Font(None, 70)
        text = font.render("Нажмите Пробел для начала игры", True,
                           (255, 255, 255))
        screen.blit(text, (250, 300))
        draw_button("Скин змеи", WIDTH // 2 - 100, 50, 200, 50)
        draw_button("Выход", 50, HEIGHT - 100, 100, 50)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_window(selected_snake_color,
                                music_files[selected_skin_index],
                                snake_head_image_game)
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if (
                        WIDTH // 2 - 100 < mouse_pos[0] < WIDTH // 2 + 100
                        and 50 < mouse_pos[1] < 100
                ):
                    skin_snake_window()

                if (
                        50 < mouse_pos[0] < 150
                        and HEIGHT - 100 < mouse_pos[1] < HEIGHT
                ):
                    pygame.quit()
                    exit()


def game_over(score, total_apples):
    global selected_skin_index
    with open("scores.txt", "a") as file:
        file.write(f"{score}\n")

    with open("scores.txt", "r") as file:
        scores = [int(line.strip()) for line in file]

    best_score = max(scores) if scores else 0

    while True:
        screen.blit(game_over_image, (0, 0))

        font = pygame.font.Font(None, 60)
        text = font.render("Игра окончена", True, (0, 0, 0))
        score_label = font.render(f'Ваш счёт: {score}', True, (0, 0, 0))
        best_score_label = font.render(f'Лучший результат: {best_score}', True,
                                       (0, 0, 0))

        text_width = text.get_width()

        restart_button_rect = pygame.Rect(WIDTH // 2 - text_width // 2,
                                          HEIGHT // 2 + 100,
                                          text_width,
                                          50)
        pygame.draw.rect(screen, BUTTON_COLOR, restart_button_rect)
        restart_button_text = font.render("Начать сначала", True,
                                          (0, 0, 0))
        restart_button_text_rect = restart_button_text.get_rect(
            center=restart_button_rect.center)
        screen.blit(restart_button_text, restart_button_text_rect)

        exit_button_rect = pygame.Rect(WIDTH // 2 - text_width // 2,
                                       HEIGHT // 2 + 170,
                                       text_width, 50)
        pygame.draw.rect(screen, BUTTON_COLOR, exit_button_rect)
        exit_button_text = font.render("Выход", True, (0, 0, 0))
        screen.blit(exit_button_text,
                    (exit_button_rect.x + 75, exit_button_rect.y + 10))

        screen.blit(text,
                    (WIDTH // 2 - text.get_width() // 2,
                     HEIGHT // 2 - 150))
        screen.blit(score_label,
                    (WIDTH // 2 - score_label.get_width() // 2,
                     HEIGHT // 2 - 100))
        screen.blit(best_score_label,
                    (WIDTH // 2 - best_score_label.get_width() // 2,
                     HEIGHT // 2 - 50))

        font_small = pygame.font.Font(None, 30)
        apple_hint_text = font_small.render(
            "Соберите яблоки, чтобы открыть новые скины", True, (0, 0, 0))
        screen.blit(apple_hint_text, (WIDTH // 2 -
                                      apple_hint_text.get_width() // 2,
                                      HEIGHT // 2 + 230))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if restart_button_rect.collidepoint(mouse_pos):
                    game_window(selected_snake_color,
                                music_files[selected_skin_index],
                                snake_head_image_game)
                    return
                if exit_button_rect.collidepoint(mouse_pos):
                    pygame.mixer.music.stop()
                    start_screen()


def game_window(snake_color, music, skin):
    global selected_skin_index
    snake = Snake(WIDTH // 4, HEIGHT // 2, snake_color, skin)
    apple = Apple()

    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(-1)

    score = 0
    total_apples = 0
    clock = pygame.time.Clock()

    try:
        with open("scores.txt", "r") as file:
            total_apples = sum(int(line.strip()) for line in file)
    except FileNotFoundError:
        pass

    overlay_surface = pygame.Surface((WIDTH, HEIGHT))
    overlay_surface.fill((0, 0, 0))
    overlay_surface.set_alpha(150)

    while True:
        screen.blit(background_images[selected_skin_index], (0, 0))
        screen.blit(overlay_surface, (0, 0))

        head_x, head_y = snake.body[0]
        apple_center_x = apple.position[0] + CELL_SIZE // 2
        apple_center_y = apple.position[1] + CELL_SIZE // 2
        head_center_x = head_x + CELL_SIZE // 2
        head_center_y = head_y + CELL_SIZE // 2

        if (
                math.sqrt(
                    (head_center_x - apple_center_x) ** 2 + (
                            head_center_y - apple_center_y
                    ) ** 2
                ) < CELL_SIZE // 2
        ):
            snake.grow()
            score += 1
            total_apples += 1
            apple.spawn()

        if (snake.body[0][0] < 0 or snake.body[0][0] >= WIDTH or
                snake.body[0][1] < 0 or snake.body[0][1] >= HEIGHT or
                snake.body[0] in snake.body[1:]):
            game_over(score, total_apples)

        snake.move()

        apple.draw()
        snake.draw()

        font = pygame.font.Font(None, 36)
        score_label = font.render(f'Счёт: {score}', True, (255, 255, 255))
        screen.blit(score_label, (10, 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != (
                        0, CELL_SIZE):
                    snake.direction = (0, -CELL_SIZE)
                elif event.key == pygame.K_DOWN and snake.direction != (
                        0, -CELL_SIZE):
                    snake.direction = (0, CELL_SIZE)
                elif event.key == pygame.K_LEFT and snake.direction != (
                        CELL_SIZE, 0):
                    snake.direction = (-CELL_SIZE, 0)
                elif event.key == pygame.K_RIGHT and snake.direction != (
                        -CELL_SIZE, 0):
                    snake.direction = (CELL_SIZE, 0)

        clock.tick(FPS)


def unlock_skins(total_apples):
    global selected_skin_index
    for i in range(4, 22):
        required_apples = 5 + 5 * (i - 4)
        if total_apples >= required_apples:
            if i not in [selected_skin_index]:
                skins[i] = pygame.image.load(
                    f"skins/skin{i + 1}.png").convert_alpha()
            if i == selected_skin_index:
                snake_head_image_skin = pygame.transform.scale(
                    skins[i], SKIN_WINDOW_HEAD_SIZE
                )
                snake_head_image_game = pygame.transform.scale(
                    skins[i], GAME_HEAD_SIZE
                )


def is_skin_unlocked(skin_index):
    with open("scores.txt", "r") as file:
        scores = [int(line.strip()) for line in file]
        total_apples = sum(scores)
    required_apples = 5 + 5 * (skin_index - 4)
    return total_apples >= required_apples


while True:
    start_screen()
    game_window(selected_snake_color, music_files[selected_skin_index],
                snake_head_image_game)

pygame.quit()
