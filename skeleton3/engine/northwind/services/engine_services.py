from roars.common.services import EngineServices as CommonEngineServices
from templates import Templates
from model_services import ModelServices
from .. import handlers


class EngineServices(CommonEngineServices):
    def __init__(self):
        super(EngineServices, self).__init__()
        self._models = ModelServices(self)
        self._templates = Templates(self)
        self._handlers = handlers.handlers
