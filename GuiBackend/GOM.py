import asyncio
from GuiBackend.Components import Base

class GlobalObjectManager(object):

    # Parameters
    # Initialized
    Objects: list = []
    SelectedObject : object = None

    def __init__(self) -> None:
        return

    def AddObject(self, object: object) -> None:
        return self.Objects.append(object)
    
    async def GetDrawables(self) -> list[asyncio.coroutine]:
        """ Checks Object Attributes for *.Draw

        Returns:
            list[coroutines]: list of drawables
        """
        return [
            _object
            for _object in self.Objects
            if(getattr(_object, 'Draw') and getattr(_object, 'visible'))
        ]

    async def GetComponents(self) -> list[Base]:
        """ Checks MRO of Component for Base Parent

        Returns:
            list[Base]: list of components
        """
        return [
            _object
            for _object in self.Objects
            if(Base in _object.__class__.__mro__)
        ]

    async def GetType(self, type: any) -> list[object]:
        """ Checks MRO of Object for type Parent

        Args:
            type (any): parent type

        Returns:
            list[object]: list of objects
        """
        return [
            _object
            for _object in self.Objects
            if(type in _object.__class__.__mro__)
        ]