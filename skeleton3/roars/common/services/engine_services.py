from pl import services
from templates import Templates
from model_services import ModelServices
from ..handlers import handlers
from skeletons import Skeletons


__all__ = ['EngineServices']


class EngineServices(services.EngineServices):
    def __init__(self):
        self._cache = services.caches.DictCache()
        self._logger = None
        self._templates = Templates(self)
        self._models = ModelServices(self)
        self._skeletons = Skeletons(self)

    @property
    def templates(self):
        return self._templates

    @property
    def models(self):
        return self._models

    @property
    def cache(self):
        return self._cache

    @property
    def logger(self):
        return self._logger

    @property
    def handlers(self):
        return handlers

    @property
    def skeletons(self):
        return self._skeletons
