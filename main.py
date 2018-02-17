from crowdSimulator.entities import Entity

from crowdSimulator.render import build_gui

build_gui()


def create_world(name):
    return Entity(name=name)


create_world('World')
