import pygame
import asyncio
from GuiBackend import Specifiers

pygame.font.init()

class Base(pygame.Rect):
    """Component Base

    This Declares a Object to the GOM [GuiBackend : GlobalObjectManager]

    This should not be Instanced on its own, This is for Inheritance
    """

    # Parameters
    # Non-Initialized
    x: int
    y: int
    w: int
    h: int

    border_color: tuple
    border_width: int

    visible: bool

    def __init__(self, x: int, y: int, w: int, h: int, border_color: tuple, border_width: int) -> None:
        """ 

        Args:
            x (int): x value
            y (int): y value
            w (int): w value
            h (int): h value
            border_color (tuple): color rgb value
            border_width (tuple): border width
        """
        pygame.Rect(x, y, w, h)

        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.border_color = border_color
        self.border_width = border_width

        self.visible = True

    def Hide(self):
        self.visible = False
    def Show(self):
        self.visible = True

    async def Draw(self):
        if(not self.visible):
            return

        pygame.draw.rect(pygame.display.get_surface(), self.border_color, self, self.border_width)
        text = self.text_font.render(self.text_string, True, (255,255,255))

        if(Specifiers.CenterTextAlign in self.__class__.__mro__):
            pygame.display.get_surface().blit(text, text.get_rect(center=(self.x + (self.w // 2), self.y + (self.h // 2))))
        elif(Specifiers.LeftTextAlign in self.__class__.__mro__):
            pygame.display.get_surface().blit(text, text.get_rect(center=(self.x + self.left_buffer, self.y + (self.h // 2))))
        elif(Specifiers.RightTextAlign in self.__class__.__mro__):
            pygame.display.get_surface().blit(text, (self.x + self.right_buffer, self.y + (self.h // 2)))
            

class Button(Base, Specifiers.ClickAction, Specifiers.CenterTextAlign):
    """ Button

    When clicked, async_callback is called

    Text is Automatically Centered
    """

    # Parameters
    # Non-Initialized
    location: tuple
    rsize: tuple

    def __init__(self, button_text: str, location: tuple, rsize: tuple, border_color: tuple, border_width: int, async_callback: asyncio.coroutine = None) -> None:
        super().__init__(location[0], location[1], rsize[0], rsize[1], border_color, border_width)
        
        Specifiers.ClickAction.__init__(self, async_callback)
        Specifiers.CenterTextAlign.__init__(self, button_text, rsize[1] // 2, pygame.font.get_default_font())
        
        self.location = location
        self.rsize = rsize

class Label(Base, Specifiers.CenterTextAlign):
    """ Label

    Display Text Label
    """

    # Parameters
    # Non-Initialized
    location: tuple
    rsize: tuple

    def __init__(self, label_text: str, location: tuple, rsize: tuple):
        super().__init__(location[0], location[1], rsize[0], rsize[1], (0,0,0), 0)
        Specifiers.CenterTextAlign.__init__(self, label_text, rsize[1] // 2, pygame.font.get_default_font())

        self.location = location
        self.rsize = rsize

class TextInput(Base, Specifiers.LeftTextAlign, Specifiers.Input):
    """ Text Input
    
    Takes User Input
    """

    # Parameters
    # Non-Initialized
    location: tuple
    rsize: tuple

    def __init__(self, location: tuple, rsize: tuple, border_color: tuple, border_width: int):
        super().__init__(location[0], location[1], rsize[0], rsize[1], border_color, border_width)
        Specifiers.LeftTextAlign.__init__(self, "", rsize[1] // 2, pygame.font.get_default_font(), 5)
        Specifiers.Input.__init__(self)

        self.location = location
        self.rsize = rsize