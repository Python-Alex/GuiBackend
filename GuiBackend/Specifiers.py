import pygame
import asyncio


class ClickAction(object):

    """Specifies a Component to Execute a Callback Function.

    These should used for actions that have no return value.
    """

    # Parameters
    # Non-Initialized
    async_callback: asyncio.coroutine

    def __init__(self, async_callback: asyncio.coroutine) -> None:
        """Constructor for ClickAction

        Args:
            callback (callable): Method to Execute
        """
        self.async_callback = async_callback

    async def CheckEvent(self, pos: tuple) -> None:
        """Check if game mouse has clicked this button

        Args:
            pos (tuple): x,y of event dispatched
        """
        if(self.collidepoint(pos)):
            await self.async_callback()

class CenterTextAlign(object):
    """Specifies a Component to Declare a Text Value Center Aligned
    """

    # Parameters
    # Non-Initialized
    text_string: str
    text_size: int
    text_font: pygame.font.Font

    def __init__(self, text_string: str, text_size: int, text_font: str) -> None:
        self.text_string = text_string
        self.text_size = text_size

        self.text_font = pygame.font.Font(text_font, text_size)

class LeftTextAlign(object):
    """Specifies a Component to Declare a Text Value Left Aligned
    """

    # Parameters
    # Non-Initialized
    text_string: str
    text_size: int
    text_font: pygame.font.Font
    left_buffer: int

    def __init__(self, text_string: str, text_size: int, text_font: str, left_buffer: int) -> None:
        self.text_string = text_string
        self.text_size = text_size

        self.text_font = pygame.font.Font(text_font, text_size)

        self.left_buffer = left_buffer

class RightTextAlign(object):
    """Specifies a Component to Declare a Text Value Left Aligned
    """

    # Parameters
    # Non-Initialized
    text_string: str
    text_size: int
    text_font: pygame.font.Font
    right_buffer: int

    def __init__(self, text_string: str, text_size: int, text_font: str, right_buffer: int) -> None:
        self.text_string = text_string
        self.text_size = text_size

        self.text_font = pygame.font.Font(text_font, text_size)

        self.right_buffer = right_buffer

class Input(object):

    """Specifies a Component to Declare a Text Input
    """

    # Parameters
    # Non-Initialized
    text_buffer: str

    def __init__(self):
        self.text_buffer = ""
