import pygame, sys 
from pygame import Vector2 as vector
# ( l, Middle, r 리스트)
from pygame.mouse import get_pressed as mouse_buttons
from pygame.mouse import get_pos as mouse_position

from settings import *

class Editor:
	def __init__(self):

		# main setup 
		self.display_surface = pygame.display.get_surface()
  
		self.origin = vector()
		self.pan_active = False
		self.pan_offset = vector()
  
		#라인 설정
		self.support_line_surf = pygame.Surface((WINDOW_WIDTH,WINDOW_HEIGHT))
		#해당 surf의 컬러키에 해당하는걸 제거함
		self.support_line_surf.set_colorkey('green')
		self.support_line_surf.set_alpha(30)


	def event_loop(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			self.pan_input(event)

	def pan_input(self,event):
        
        #마우스 버튼
		if event.type == pygame.MOUSEBUTTONDOWN and mouse_buttons()[1]:
			self.pan_active = True
			self.pan_offset = vector(mouse_position()) - self.origin
		if not mouse_buttons()[1]:
			self.pan_active = False
   
		if event.type == pygame.MOUSEWHEEL:
			#마우스 휠로 원점을 옮기는 처리
			if pygame.key.get_pressed()[pygame.K_LCTRL]:
				self.origin.y -= event.y * 50
			else: self.origin.x -= event.y * 50
   
        #마우스 움직임
		if self.pan_active:
			self.origin = vector(mouse_position()) - self.pan_offset
        
	def draw_tile_lines(self):
		#격자 생성을 위한 행 열 갯수
		cols = WINDOW_WIDTH // TILE_SIZE
		rows = WINDOW_HEIGHT // TILE_SIZE

		#offset 점이 첫번째 열 안에서만 놀게 하기위한 처리
		#origin 점 - 첫번째 타일로 부터의 거리 = > 첫번째 타일 에서 offset 점(디스플레이용) 의 위치
		origin_offset = vector(
			x= self.origin.x - int(self.origin.x / TILE_SIZE) * TILE_SIZE,
			y= self.origin.y - int(self.origin.y / TILE_SIZE) * TILE_SIZE
		)
  
		self.support_line_surf.fill('green')
  
		for col in range(cols + 1):
			x = origin_offset.x + col * TILE_SIZE
			pygame.draw.line(self.support_line_surf,LINE_COLOR,(x,0),(x,WINDOW_HEIGHT))

		for row in range(rows + 1 ):
			y = origin_offset.y + row * TILE_SIZE
			pygame.draw.line(self.support_line_surf,LINE_COLOR,(0,y),(WINDOW_WIDTH,y))

		self.display_surface.blit(self.support_line_surf,(0,0))

	def run(self, dt):
		self.display_surface.fill('white')
		self.event_loop()
  
		#드로잉
		self.draw_tile_lines()
  
		pygame.draw.circle(self.display_surface,'red',self.origin,10)