class EngineServices(object):
    def __init__(self, cache=None, logger=None, models=None, templates=None, skeletons=None):
        self._cache = cache
        self._logger = logger
        self._models = models
        self._templates = templates
        self._skeletons = skeletons

    @property
    def cache(self):
        return self._cache

    @property
    def logger(self):
        return self._logger

    @property
    def models(self):
        return self._models

    @property
    def templates(self):
        return self._templates

    @property
    def skeletons(self):
        return self._skeletons
