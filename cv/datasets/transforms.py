from base.utils import Registry, build_from_cfg



class SingleTransform:
    def __init__(self):
        pass

    def __call__(self, x):
        raise NotImplementedError

    def __repr__(self):
        return self.__class__.__name__


class VisionTransforms:
    _repr_indent = 4

    def __init__(self, cfg):
        self.transformers = dict()
        if isinstance(cfg, list):
            for single_cfg in cfg:
                self.transformers[single_cfg['type']] = build_from_cfg(single_cfg)
        else:
            self.transformers[cfg['type']] = build_from_cfg(cfg)

    def __call__(self, x):
        raise NotImplementedError

    def __repr__(self):
        head = f'VisionTransforms {self.__class__.__name__}'
        body = [type_name for type_name in self.transformers.keys()]
        lines = [head] + [' ' * self._repr_indent + line for line in body]
        return '\n'.join(lines)

