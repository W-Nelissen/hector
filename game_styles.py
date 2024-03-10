import re
import pygame as pg

class GameStyle:
	def __init__(self, name, font, size, fontcolor, bgimg, bgimg_hover, bgimg_pressed, bgimg_inactive, bgcolor, bgcolor_hover, bgcolor_pressed, bgcolor_inactive, txtcolor, txtcolor_hover, txtcolor_pressed, txtcolor_inactive):
		self.name = name
		self.font = font
		self.size = size
		self.fontcolor = fontcolor

		self.bg_image = None
		if bgimg:
			self.bg_image = pg.image.load(bgimg)
		else:
			self.img_bg = None

		self.bg_image_pressed = None
		if bgimg_pressed:
			self.bg_image_pressed = pg.image.load(bgimg_pressed)
		else:
			self.bg_image_pressed = self.bg_image
			
		self.bgimg_hover = bgimg_hover
		self.bgimg_inactive = bgimg_inactive
		self.bgcolor = bgcolor
		self.bgcolor_hover = bgcolor_hover
		self.bgcolor_pressed = bgcolor_pressed
		self.bgcolor_inactive = bgcolor_inactive
		self.txtcolor = txtcolor
		self.txtcolor_hover = txtcolor_hover
		self.txtcolor_pressed = txtcolor_pressed
		self.txtcolor_inactive = txtcolor_inactive

class GameStyles():
	def __init__(self) -> None:
		self.game_styles = []
		file_path = 'assets/styles/chess_styles.txt'
		self.load_game_styles(file_path)

	def get_style(self, name):
		for gamestyle in self.game_styles:
			if gamestyle.name == name:
				return gamestyle
		return self.game_styles[0]

	def load_game_styles(self, file_name):
		with open(file_name, 'r') as file:
			data = file.read()
		pattern = (r'<STYLE name="(.*?)"'
           r' font="(.*?)"'
           r' size="(.*?)"'
           r' fontcolor="(\(\d+,\d+,\d+\))"'
		   r' bgimg="([^"]*)"'
           r' bgimg_hover="([^"]*)"'
           r' bgimg_pressed="([^"]*)"'
           r' bgimg_inactive="([^"]*)"'
           r' bgcolor="([^"]*)"'
           r' bgcolor_hover="(\(\d+,\d+,\d+\))"'
           r' bgcolor_pressed="(\(\d+,\d+,\d+\))"'
           r' bgcolor_inactive="(\(\d+,\d+,\d+\))"'
           r' txtcolor="(\(\d+,\d+,\d+\))"'
           r' txtcolor_hover="(\(\d+,\d+,\d+\))"'
           r' txtcolor_pressed="(\(\d+,\d+,\d+\))"'
           r' txtcolor_inactive="(\(\d+,\d+,\d+\))">')
           		
		
		matches = re.findall(pattern, data)
		for match in matches:
			name, font, size, fontcolor, bgimg, bgimg_hover, bgimg_pressed, bgimg_inactive, bgcolor, bgcolor_hover, bgcolor_pressed, bgcolor_inactive, txtcolor, txtcolor_hover, txtcolor_pressed, txtcolor_inactive = match
			fontcolor = tuple(map(int, fontcolor.strip("()").split(',')))
			bgcolor = tuple(map(int, bgcolor.strip("()").split(',')))
			bgcolor_hover = tuple(map(int, bgcolor_hover.strip("()").split(',')))
			bgcolor_pressed = tuple(map(int, bgcolor_pressed.strip("()").split(',')))
			bgcolor_inactive = tuple(map(int, bgcolor_inactive.strip("()").split(',')))
			txtcolor = tuple(map(int, txtcolor.strip("()").split(',')))
			txtcolor_hover = tuple(map(int, txtcolor_hover.strip("()").split(',')))
			txtcolor_pressed = tuple(map(int, txtcolor_pressed.strip("()").split(',')))
			txtcolor_inactive = tuple(map(int, txtcolor_inactive.strip("()").split(',')))
			game_style = GameStyle(name, font, int(size), fontcolor, bgimg, bgimg_hover, bgimg_pressed, bgimg_inactive, bgcolor, bgcolor_hover, bgcolor_pressed, bgcolor_inactive, txtcolor, txtcolor_hover, txtcolor_pressed, txtcolor_inactive)
			self.game_styles.append(game_style)

gs = GameStyles()

