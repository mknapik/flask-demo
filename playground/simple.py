from injector import inject


class Config:
    def __init__(self):
        self.cfg = "default"


class DevConfig(Config):
    def __init__(self):
        super().__init__()
        self.cfg = "dev"


class Foo:
    @inject
    def __init__(self, config: Config):
        self.config = config


@inject
def foo(config: Config):
    return config.cfg


__all__ = [Config, DevConfig, Foo, foo]
