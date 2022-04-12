import torch.utils.data as data


class VisionDataset(data.Dataset):
    _repr_indent = 4

    def __init__(self, root, transforms=None):
        self.root = root
        if isinstance(transforms, list):
            self.transforms = transforms
        else:
            self.transforms = [transforms]

    def __getitem__(self, index):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def __repr__(self):
        head = 'VisionDataset' + self.__class__.__name__
        body = [f'Number of data: {self.__len__()}']
        if self.root is not None:
            body.append(f'Data root location: {self.root}')
        if self.transforms:
            for transform in self.transforms:
                body.append(f'Transform: {repr(transform)}')
        lines = [head] + [' ' * self._repr_indent + line for line in body]
        return '\n'.join(lines)
