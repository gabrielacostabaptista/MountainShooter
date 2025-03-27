#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH, ENTITY_SPEED
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.react.centerx -= ENTITY_SPEED[self.name] #velocidade do bg
        if self.react.right <= 0:
            self.react.left =WIN_WIDTH
        pass
