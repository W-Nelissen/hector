import re
import pygame as pg

class GameStyle:
	def __init__(self, name, font, size, fontcolor, bgimg, bgimg_hover, bgimg_pressed, bgimg_inactive, bgcolor, bgcolor_hover, bgcolor_pressed, bgcolor_inactive):
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
           	r' bgimg="(.*?)"'
           	r' bgimg_hover="(.*?)"'
           	r' bgimg_pressed="(.*?)"'
           	r' bgimg_inactive="(.*?)"'
           	r' bgcolor="(.*?)"'
           	r' bgcolor_hover="(.*?)"'
           	r' bgcolor_pressed="(.*?)"'
           	r' bgcolor_inactive="(.*?)"')
		matches = re.findall(pattern, data)
		for match in matches:
			print(match)
			name, font, size, fontcolor, bgimg, bgimg_hover, bgimg_pressed, bgimg_inactive, bgcolor, bgcolor_hover, bgcolor_pressed, bgcolor_inactive = match
			fontcolor = tuple(map(int, fontcolor.strip("()").split(',')))
			game_style = GameStyle(name, font, int(size), fontcolor, bgimg, bgimg_hover, bgimg_pressed, bgimg_inactive, bgcolor, bgcolor_hover, bgcolor_pressed, bgcolor_inactive)
			self.game_styles.append(game_style)

gs = GameStyles()

