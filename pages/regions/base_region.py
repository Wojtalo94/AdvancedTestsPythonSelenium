from pypom import Region


class BaseRegion(Region):
    def __init__(self, page, root=None):
        super().__init__(page, root)
        