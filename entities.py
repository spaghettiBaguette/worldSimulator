import numpy
from crowdSimulator import global_dimensions

entity_needs = {}


class Entity(object):
    def __init__(self, **kwargs):
        self.entity_id = id(self)
        self.name = kwargs.get('name') or str()
        self.type = kwargs.get('entity_type') or str()
        self.position = kwargs.get('position') or numpy.array([0 for x in range(global_dimensions)])
        self.hierarchy_of_needs = entity_needs.get(self.type) or list()
        self.components = kwargs.get('components') or list()
        self.model = kwargs.get('model') or str()
        self.mobile = kwargs.get('mobile') or bool()
        self.inventory = kwargs.get('inventory') or list()
