from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes

from loader import dp, bot
from states import ReadyToCon
from keyboards.default import kb_menu

import pygame as pg
import cv2


class AsciiConverter():
    def __init__(self, path='photos/1.jpg', font_size=12):
        pg.init()
        self.path = path
        self.image = self.get_image()
        self.RES = self.WIDTH, self.HEIGHT = self.image.shape[0], self.image.shape[1]
        self.surface = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()

        self.ASCII_CHARS = '.",:;!~+-xmo*#W&8@'
        self.ASCII_COEFF = 255 // (len(self.ASCII_CHARS) - 1)

        self.font = pg.font.SysFont('Courier', font_size, bold=True)
        self.CHAR_STEP = int(font_size * 0.6)
        self.RENDERED_ASCII_CHARS = [self.font.render(char, False, 'white') for char in self.ASCII_CHARS]

    def draw_converted_image(self):
        char_indecsies = self.image // self.ASCII_COEFF
        for x in range(0, self.WIDTH, self.CHAR_STEP):
            for y in range(0, self.HEIGHT, self.CHAR_STEP):
                char_index = char_indecsies[x, y]
                if char_index:
                    self.surface.blit(self.RENDERED_ASCII_CHARS[char_index], (x, y))

    def get_image(self):
        self.cv2_image = cv2.imread(self.path)
        transposed_image = cv2.transpose(self.cv2_image)
        gray_image = cv2.cvtColor(transposed_image, cv2.COLOR_BGR2GRAY)
        return gray_image

    def draw_cv2_image(self):
        resized_cv2_image = cv2.resize(self.cv2_image, (640, 360), interpolation=cv2.INTER_AREA)
        cv2.imshow('1.jpg', resized_cv2_image)

    def draw(self):
        self.surface.fill('black')
        self.draw_converted_image()
        #self.draw_cv2_image()

    def save_image(self):
        pygame_image = pg.surfarray.array3d(self.surface)
        cv2_img = cv2.transpose(pygame_image)
        cv2.imwrite('photos/1conv.jpg', cv2_img)
        print('Image saved')

    def run(self):
        self.draw()
        pg.display.set_caption(str(self.clock.get_fps()))
        pg.display.flip()
        self.save_image()
        self.clock.tick()
        pg.display.quit()




@dp.message_handler(content_types=ContentTypes.PHOTO, state=ReadyToCon.awaiting_ascii_photo)
async def convert_to_ascii(message: types.Message, state: FSMContext):
    await message.photo[-1].download(destination_file=f"photos/1.jpg")
    conv = AsciiConverter()
    conv.run()
    photo = open('photos/1conv.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo, caption="Вот что получилось!", reply_markup=kb_menu)
    await state.finish()



