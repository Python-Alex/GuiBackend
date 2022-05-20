import pygame
import asyncio 

from GuiBackend import Components, GameVars, Specifiers, GOM

pygame.init()

SystemLoop = asyncio.new_event_loop()
LocalClock = pygame.time.Clock()

SystemGOM = GOM.GlobalObjectManager()

pygame.display.set_mode((1600, 900))

async def TestButtonCallback():
    print("x")

TestButton = Components.Button("Test", (10, 10), (100, 30), (255,255,255), 1, TestButtonCallback)
TestLabel = Components.Label("Label", (10, 40), (100,30))

SystemGOM.AddObject(TestButton)
SystemGOM.AddObject(TestLabel)

async def GameLoop():
    while(True):

        pygame.display.get_surface().fill((0,0,0))

        # draw existing objects
        for drawable in await SystemGOM.GetDrawables():
            await drawable.Draw()

        for event in pygame.event.get(exclude=[pygame.MOUSEMOTION]):
            if(event.type == pygame.QUIT):
                pygame.quit(); exit()

            # check for button click
            if(event.type == pygame.MOUSEBUTTONDOWN):
                for button_search in await SystemGOM.GetType(Specifiers.ClickAction):
                    await button_search.CheckEvent(event.pos)

                for component in await SystemGOM.GetComponents():
                    if(component.collidepoint(event.pos)):
                        SystemGOM.SelectedObject = component 

            elif(event.type == pygame.KEYDOWN):
                continue

        pygame.display.update()
        LocalClock.tick(144)

        pygame.display.set_caption("%d - %s" % (LocalClock.get_fps(), SystemGOM.SelectedObject))

SystemLoop.create_task(GameLoop())
SystemLoop.run_forever()