import pygame
import random
import sys
import math

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 120
BALL_SIZE = 20
PADDLE_SPEED = 8
BALL_SPEED_X = 6
BALL_SPEED_Y = 6
AI_SPEED = 5

NEON_CYAN = (0, 255, 255)
NEON_PINK = (255, 20, 147)
NEON_GREEN = (57, 255, 20)
NEON_ORANGE = (255, 165, 0)
NEON_PURPLE = (138, 43, 226)
DARK_BG = (10, 10, 25)
GRID_COLOR = (30, 30, 60)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("NEON TENNIS 2024 ⚡")
clock = pygame.time.Clock()

try:
    font = pygame.font.Font(None, 120)
    small_font = pygame.font.Font(None, 48)
    tiny_font = pygame.font.Font(None, 32)
except:
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)
    tiny_font = pygame.font.Font(None, 24)

class Paddle:
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.color = color
        self.glow_intensity = 0
        self.velocity = 0
        self.trail_particles = []
        
    def move_up(self):
        if self.rect.top > 40:
            self.rect.y -= PADDLE_SPEED
            self.velocity = -PADDLE_SPEED
            self.glow_intensity = min(50, self.glow_intensity + 5)
            self.add_trail_particle()
            
    def move_down(self):
        if self.rect.bottom < SCREEN_HEIGHT - 40:
            self.rect.y += PADDLE_SPEED
            self.velocity = PADDLE_SPEED
            self.glow_intensity = min(50, self.glow_intensity + 5)
            self.add_trail_particle()
    
    def add_trail_particle(self):
        if len(self.trail_particles) < 20:
            particle_x = self.rect.centerx + random.randint(-5, 5)
            particle_y = self.rect.centery + random.randint(-30, 30)
            particle = {
                'x': particle_x,
                'y': particle_y,
                'life': 30,
                'vel_x': random.uniform(-2, 2),
                'vel_y': random.uniform(-2, 2)
            }
            self.trail_particles.append(particle)
    
    def update_particles(self):
        for particle in self.trail_particles[:]:
            particle['x'] += particle['vel_x']
            particle['y'] += particle['vel_y']
            particle['life'] -= 1
            if particle['life'] <= 0:
                self.trail_particles.remove(particle)
        
        self.glow_intensity = max(0, self.glow_intensity - 1)
        self.velocity *= 0.8
            
    def draw(self, surface):
        for particle in self.trail_particles:
            alpha = particle['life'] / 30.0
            size = int(alpha * 8)
            if size > 0:
                glow_color = tuple(int(c * alpha) for c in self.color)
                pygame.draw.circle(surface, glow_color, 
                                 (int(particle['x']), int(particle['y'])), size)
        
        glow_radius = PADDLE_WIDTH + self.glow_intensity
        glow_color = tuple(min(255, int(c * 0.3)) for c in self.color)
        
        for i in range(3):
            radius = glow_radius - i * 3
            if radius > 0:
                alpha_surface = pygame.Surface((radius * 2, PADDLE_HEIGHT + 20), pygame.SRCALPHA)
                pygame.draw.rect(alpha_surface, (*glow_color, 50 - i * 15),
                               (0, 10, radius * 2, PADDLE_HEIGHT))
                surface.blit(alpha_surface, 
                           (self.rect.centerx - radius, self.rect.y - 10))
        
        pygame.draw.rect(surface, self.color, self.rect)
        
        inner_rect = pygame.Rect(self.rect.x + 3, self.rect.y + 3, 
                                PADDLE_WIDTH - 6, PADDLE_HEIGHT - 6)
        inner_color = tuple(min(255, int(c * 1.5)) for c in self.color)
        pygame.draw.rect(surface, inner_color, inner_rect)

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, 
                               SCREEN_HEIGHT // 2 - BALL_SIZE // 2,
                               BALL_SIZE, BALL_SIZE)
        self.speed_x = BALL_SPEED_X * random.choice([-1, 1])
        self.speed_y = BALL_SPEED_Y * random.choice([-1, 1])
        self.trail_particles = []
        self.hit_particles = []
        self.color = NEON_CYAN
        self.glow_intensity = 0
        self.rotation = 0
        
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.rotation += math.sqrt(self.speed_x**2 + self.speed_y**2) * 0.1
        
        if self.rect.top <= 40 or self.rect.bottom >= SCREEN_HEIGHT - 40:
            self.speed_y = -self.speed_y
            self.create_hit_particles()
            self.glow_intensity = 30
            
        self.add_trail_particle()
        self.update_particles()
            
    def add_trail_particle(self):
        if len(self.trail_particles) < 30:
            particle = {
                'x': self.rect.centerx + random.randint(-3, 3),
                'y': self.rect.centery + random.randint(-3, 3),
                'life': 20,
                'vel_x': random.uniform(-1, 1),
                'vel_y': random.uniform(-1, 1),
                'size': random.uniform(2, 6)
            }
            self.trail_particles.append(particle)
    
    def create_hit_particles(self):
        for _ in range(15):
            particle = {
                'x': self.rect.centerx,
                'y': self.rect.centery,
                'life': 40,
                'vel_x': random.uniform(-8, 8),
                'vel_y': random.uniform(-8, 8),
                'size': random.uniform(3, 8),
                'color': random.choice([NEON_ORANGE, NEON_PINK, NEON_GREEN])
            }
            self.hit_particles.append(particle)
    
    def update_particles(self):
        for particle in self.trail_particles[:]:
            particle['x'] += particle['vel_x']
            particle['y'] += particle['vel_y']
            particle['life'] -= 1
            particle['size'] *= 0.98
            if particle['life'] <= 0:
                self.trail_particles.remove(particle)
        
        for particle in self.hit_particles[:]:
            particle['x'] += particle['vel_x']
            particle['y'] += particle['vel_y']
            particle['vel_x'] *= 0.95
            particle['vel_y'] *= 0.95
            particle['life'] -= 1
            particle['size'] *= 0.97
            if particle['life'] <= 0:
                self.hit_particles.remove(particle)
                
        self.glow_intensity = max(0, self.glow_intensity - 1)
            
    def draw(self, surface):
        for particle in self.trail_particles:
            alpha = particle['life'] / 20.0
            size = int(particle['size'] * alpha)
            if size > 0:
                color = tuple(int(c * alpha * 0.7) for c in self.color)
                pygame.draw.circle(surface, color, 
                                 (int(particle['x']), int(particle['y'])), size)
        
        for particle in self.hit_particles:
            alpha = particle['life'] / 40.0
            size = int(particle['size'] * alpha)
            if size > 0:
                color = tuple(int(c * alpha) for c in particle['color'])
                pygame.draw.circle(surface, color, 
                                 (int(particle['x']), int(particle['y'])), size)
        
        glow_size = BALL_SIZE + self.glow_intensity
        for i in range(5):
            radius = glow_size - i * 2
            if radius > 0:
                alpha = 100 - i * 20
                glow_color = (*self.color, alpha)
                glow_surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
                pygame.draw.circle(glow_surface, glow_color, (radius, radius), radius)
                surface.blit(glow_surface, 
                           (self.rect.centerx - radius, self.rect.centery - radius))
        
        pygame.draw.circle(surface, self.color, self.rect.center, BALL_SIZE // 2)
        
        core_color = tuple(min(255, int(c * 1.8)) for c in self.color)
        pygame.draw.circle(surface, core_color, self.rect.center, BALL_SIZE // 3)
        
    def reset(self):
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed_x = BALL_SPEED_X * random.choice([-1, 1])
        self.speed_y = BALL_SPEED_Y * random.choice([-1, 1])
        self.trail_particles.clear()
        self.hit_particles.clear()
        self.glow_intensity = 0

class Game:
    def __init__(self):
        self.player_paddle = Paddle(50, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, NEON_CYAN)
        self.ai_paddle = Paddle(SCREEN_WIDTH - 50 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, NEON_PINK)
        self.ball = Ball()
        self.player_score = 0
        self.ai_score = 0
        self.game_over = False
        self.winner = None
        self.background_particles = []
        self.score_particles = []
        self.frame_count = 0
        self.combo_count = 0
        self.last_hit = None
        
        for _ in range(50):
            self.background_particles.append({
                'x': random.randint(0, SCREEN_WIDTH),
                'y': random.randint(0, SCREEN_HEIGHT),
                'speed': random.uniform(0.1, 0.5),
                'size': random.uniform(1, 3),
                'color': random.choice([GRID_COLOR, NEON_PURPLE])
            })
        
    def handle_collision(self):
        player_hit = self.ball.rect.colliderect(self.player_paddle.rect)
        ai_hit = self.ball.rect.colliderect(self.ai_paddle.rect)
        
        if player_hit or ai_hit:
            self.ball.speed_x = -self.ball.speed_x
            
            if player_hit:
                paddle_center = self.player_paddle.rect.centery
                self.last_hit = "player"
            else:
                paddle_center = self.ai_paddle.rect.centery
                self.last_hit = "ai"
                
            ball_center = self.ball.rect.centery
            relative_intersect = (ball_center - paddle_center) / (PADDLE_HEIGHT / 2)
            self.ball.speed_y += relative_intersect * 2
            
            speed_increase = 1.08
            self.ball.speed_x *= speed_increase
            self.ball.speed_y *= speed_increase
            
            max_speed = 15
            if abs(self.ball.speed_x) > max_speed:
                self.ball.speed_x = max_speed if self.ball.speed_x > 0 else -max_speed
            if abs(self.ball.speed_y) > max_speed:
                self.ball.speed_y = max_speed if self.ball.speed_y > 0 else -max_speed
            
            self.ball.create_hit_particles()
            self.ball.glow_intensity = 40
            
            self.combo_count += 1
            if self.combo_count > 5:
                self.ball.color = random.choice([NEON_GREEN, NEON_ORANGE, NEON_PURPLE])
            
    def ai_movement(self):
        target_y = self.ball.rect.centery
        
        prediction_frames = 30
        future_y = self.ball.rect.centery + (self.ball.speed_y * prediction_frames)
        future_y = max(40, min(SCREEN_HEIGHT - 40, future_y))
        
        paddle_center = self.ai_paddle.rect.centery
        diff = future_y - paddle_center
        
        if abs(diff) > 10:
            if diff > 0:
                self.ai_paddle.move_down()
            else:
                self.ai_paddle.move_up()
                
    def check_score(self):
        scored = False
        if self.ball.rect.left <= 0:
            self.ai_score += 1
            self.create_score_particles(SCREEN_WIDTH - 200, 100, NEON_PINK)
            scored = True
            
        if self.ball.rect.right >= SCREEN_WIDTH:
            self.player_score += 1
            self.create_score_particles(200, 100, NEON_CYAN)
            scored = True
            
        if scored:
            self.ball.reset()
            self.ball.color = NEON_CYAN
            self.combo_count = 0
            
        if self.player_score >= 7:
            self.game_over = True
            self.winner = "PLAYER"
        elif self.ai_score >= 7:
            self.game_over = True
            self.winner = "AI"
    
    def create_score_particles(self, x, y, color):
        for _ in range(30):
            particle = {
                'x': x,
                'y': y,
                'life': 60,
                'vel_x': random.uniform(-10, 10),
                'vel_y': random.uniform(-10, 10),
                'size': random.uniform(4, 12),
                'color': color
            }
            self.score_particles.append(particle)
    
    def update_background_particles(self):
        for particle in self.background_particles:
            particle['y'] += particle['speed']
            if particle['y'] > SCREEN_HEIGHT:
                particle['y'] = 0
                particle['x'] = random.randint(0, SCREEN_WIDTH)
        
        for particle in self.score_particles[:]:
            particle['x'] += particle['vel_x']
            particle['y'] += particle['vel_y']
            particle['vel_x'] *= 0.98
            particle['vel_y'] *= 0.98
            particle['life'] -= 1
            particle['size'] *= 0.99
            if particle['life'] <= 0:
                self.score_particles.remove(particle)
            
    def draw_futuristic_background(self, surface):
        surface.fill(DARK_BG)
        
        for particle in self.background_particles:
            alpha = 100
            color = (*particle['color'], alpha)
            glow_surface = pygame.Surface((particle['size'] * 4, particle['size'] * 4), pygame.SRCALPHA)
            pygame.draw.circle(glow_surface, color, 
                             (particle['size'] * 2, particle['size'] * 2), int(particle['size']))
            surface.blit(glow_surface, (particle['x'] - particle['size'] * 2, particle['y'] - particle['size'] * 2))
        
        grid_spacing = 50
        for x in range(0, SCREEN_WIDTH, grid_spacing):
            pygame.draw.line(surface, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT), 1)
        for y in range(0, SCREEN_HEIGHT, grid_spacing):
            pygame.draw.line(surface, GRID_COLOR, (0, y), (SCREEN_WIDTH, y), 1)
        
        border_glow = 3
        for i in range(border_glow):
            alpha = 80 - i * 20
            border_color = (*NEON_CYAN, alpha)
            border_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            pygame.draw.rect(border_surface, border_color, (i * 5, i * 5, SCREEN_WIDTH - i * 10, SCREEN_HEIGHT - i * 10), 2)
            surface.blit(border_surface, (0, 0))
            
    def draw_center_line(self, surface):
        line_segments = 20
        segment_height = SCREEN_HEIGHT // line_segments
        
        for i in range(line_segments):
            y = i * segment_height
            if i % 2 == 0:
                alpha = int(150 + 50 * math.sin(self.frame_count * 0.1 + i))
                color = (*NEON_GREEN, alpha)
                line_surface = pygame.Surface((6, segment_height - 5), pygame.SRCALPHA)
                pygame.draw.rect(line_surface, color, (0, 0, 6, segment_height - 5))
                surface.blit(line_surface, (SCREEN_WIDTH // 2 - 3, y))
            
    def draw_scores(self, surface):
        for particle in self.score_particles:
            alpha = particle['life'] / 60.0
            size = int(particle['size'] * alpha)
            if size > 0:
                color = tuple(int(c * alpha) for c in particle['color'])
                pygame.draw.circle(surface, color, 
                                 (int(particle['x']), int(particle['y'])), size)
        
        glow_intensity = int(30 + 20 * math.sin(self.frame_count * 0.15))
        
        player_text = font.render(str(self.player_score), True, NEON_CYAN)
        ai_text = font.render(str(self.ai_score), True, NEON_PINK)
        
        for i in range(3):
            offset = glow_intensity - i * 10
            glow_color = tuple(int(c * (0.3 - i * 0.1)) for c in NEON_CYAN)
            player_glow = font.render(str(self.player_score), True, glow_color)
            surface.blit(player_glow, (SCREEN_WIDTH // 2 - 150 - i, 60 - i))
            
            glow_color = tuple(int(c * (0.3 - i * 0.1)) for c in NEON_PINK)
            ai_glow = font.render(str(self.ai_score), True, glow_color)
            surface.blit(ai_glow, (SCREEN_WIDTH // 2 + 100 + i, 60 + i))
        
        surface.blit(player_text, (SCREEN_WIDTH // 2 - 150, 60))
        surface.blit(ai_text, (SCREEN_WIDTH // 2 + 100, 60))
        
        if self.combo_count > 3:
            combo_text = tiny_font.render(f"COMBO x{self.combo_count}!", True, NEON_ORANGE)
            surface.blit(combo_text, (SCREEN_WIDTH // 2 - 50, 150))
        
    def draw_game_over(self, surface):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        surface.blit(overlay, (0, 0))
        
        winner_color = NEON_CYAN if self.winner == "PLAYER" else NEON_PINK
        
        for i in range(5):
            glow_text = font.render(f"{self.winner} WINS!", True, 
                                  tuple(int(c * (0.8 - i * 0.15)) for c in winner_color))
            text_rect = glow_text.get_rect(center=(SCREEN_WIDTH // 2 + i, SCREEN_HEIGHT // 2 - 50 + i))
            surface.blit(glow_text, text_rect)
        
        game_over_text = font.render(f"{self.winner} WINS!", True, winner_color)
        text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        surface.blit(game_over_text, text_rect)
        
        restart_text = small_font.render("SPACE: NEW GAME  |  ESC: QUIT", True, NEON_GREEN)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
        surface.blit(restart_text, restart_rect)
        
    def update(self):
        self.frame_count += 1
        self.update_background_particles()
        self.player_paddle.update_particles()
        self.ai_paddle.update_particles()
        
    def reset_game(self):
        self.player_score = 0
        self.ai_score = 0
        self.game_over = False
        self.winner = None
        self.combo_count = 0
        self.ball.reset()
        self.player_paddle.rect.centery = SCREEN_HEIGHT // 2
        self.ai_paddle.rect.centery = SCREEN_HEIGHT // 2
        self.score_particles.clear()

def main():
    game = Game()
    running = True
    
    title_font = pygame.font.Font(None, 72)
    subtitle_font = pygame.font.Font(None, 36)
    
    show_intro = True
    intro_timer = 0
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if show_intro:
                    show_intro = False
                elif game.game_over:
                    if event.key == pygame.K_SPACE:
                        game.reset_game()
                    elif event.key == pygame.K_ESCAPE:
                        running = False
                        
        if show_intro:
            screen.fill(DARK_BG)
            
            for i in range(3):
                glow_color = tuple(int(c * (0.5 - i * 0.1)) for c in NEON_CYAN)
                title_glow = title_font.render("NEON TENNIS 2024", True, glow_color)
                title_rect = title_glow.get_rect(center=(SCREEN_WIDTH // 2 + i, SCREEN_HEIGHT // 2 - 100 + i))
                screen.blit(title_glow, title_rect)
            
            title_text = title_font.render("NEON TENNIS 2024", True, NEON_CYAN)
            title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
            screen.blit(title_text, title_rect)
            
            subtitle_text = subtitle_font.render("Press any key to start", True, NEON_GREEN)
            subtitle_rect = subtitle_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
            screen.blit(subtitle_text, subtitle_rect)
            
            controls_text = tiny_font.render("Controls: W/S or ↑/↓ keys", True, NEON_ORANGE)
            controls_rect = controls_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
            screen.blit(controls_text, controls_rect)
            
            intro_timer += 1
            if intro_timer % 60 < 30:
                pulse_text = subtitle_font.render("⚡ ENTER THE GRID ⚡", True, NEON_PINK)
                pulse_rect = pulse_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))
                screen.blit(pulse_text, pulse_rect)
            
        else:
            if not game.game_over:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP] or keys[pygame.K_w]:
                    game.player_paddle.move_up()
                if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    game.player_paddle.move_down()
                    
                game.ball.move()
                game.handle_collision()
                game.ai_movement()
                game.check_score()
            
            game.update()
            
            game.draw_futuristic_background(screen)
            game.draw_center_line(screen)
            game.draw_scores(screen)
            
            if not game.game_over:
                game.player_paddle.draw(screen)
                game.ai_paddle.draw(screen)
                game.ball.draw(screen)
            else:
                game.draw_game_over(screen)
        
        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()