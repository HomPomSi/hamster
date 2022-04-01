#! /usr/bin/python3

import app_base


class App(app_base.AppBase):
    def __init__(self):
        super().__init__("../resources/territories/max-grain-8x8.ter")
        #super().__init__("../resources/territories/portal-5x5.ter")
   
    
    def _pick_all(self):
        while self._paule.grainAvailable():
            self._paule.pickGrain()
            
            

    def _execute_hamstergame(self) -> None:
        while self._paule.frontIsClear():
            self._pick_all()
            self._paule.move()
            if self._paule.portalIsOpen():
                self._paule.teleport()
        self._pick_all()

App()
