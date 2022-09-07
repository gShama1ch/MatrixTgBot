from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes
from loader import dp, bot
from states import ReadyToCon

import pygame as pg
import pygame.gfxdraw
import numpy as np
import cv2


class EightBitConverter():
    def __init__(self, path='photos/2.jpg', pixel_size=7, color_level=20):
        pg.init()
        self.path = path
        self.COLOR_LEVEL = color_level
        self.PIXEL_SIZE = pixel_size
        self.image = self.get_image()
        self.RES = self.WIDTH, self.HEIGHT = self.image.shape[0], self.image.shape[1]
        self.surface = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.PALETTE, self.COLOR_COEFF = self.create_palette()

    def draw_converted_image(self):
        color_indices = self.image // self.COLOR_COEFF
        for x in range(0, self.WIDTH, self.PIXEL_SIZE):
            for y in range(0, self.HEIGHT, self.PIXEL_SIZE):
                color_key = tuple(color_indices[x, y])
                if sum(color_key):
                    color = self.PALETTE[color_key]
                    pygame.gfxdraw.box(self.surface, (x, y, self.PIXEL_SIZE, self.PIXEL_SIZE), color)

    def create_palette(self):
        colors, color_coeff = np.linspace(0, 255, num=self.COLOR_LEVEL, dtype=int, retstep=True)
        color_palette = [np.array([r, g, b]) for r in colors for g in colors for b in colors]
        palette = {}
        color_coeff = int(color_coeff)
        for color in color_palette:
            color_key = tuple(color // color_coeff)
            palette[color_key] = color
        return palette, color_coeff

    def get_image(self):
        self.cv2_image = cv2.imread(self.path)
        transposed_image = cv2.transpose(self.cv2_image)
        image = cv2.cvtColor(transposed_image, cv2.COLOR_BGR2RGB)
        return image

    def draw_cv2_image(self):
        resized_cv2_image = cv2.resize(self.cv2_image, (640, 360), interpolation=cv2.INTER_AREA)
        cv2.imshow('2.jpg', resized_cv2_image)

    def draw(self):
        self.surface.fill('black')
        self.draw_converted_image()

    def save_image(self):
        pygame_image = pg.surfarray.array3d(self.surface)
        cv2_img = cv2.transpose(pygame_image)
        cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_RGB2BGR)
        cv2.imwrite('photos/2conv.jpg', cv2_img)
        print('Image saved')

    def run(self):
        self.draw()
        pg.display.set_caption(str(self.clock.get_fps()))
        pg.display.flip()
        self.save_image()
        self.clock.tick()
        pg.display.quit()


@dp.message_handler(content_types=ContentTypes.PHOTO, state=ReadyToCon.awaiting_8_bit_photo)
async def convert_to_ascii(message: types.Message, state: FSMContext):
    await message.photo[-1].download(destination_file=f"photos/2.jpg")
    conv = EightBitConverter()
    conv.run()
    photo = open('photos/2conv.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo, caption="Вот что получилось!")
    await state.finish()
