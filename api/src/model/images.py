from marshmallow import post_load

# TODO: ACTUAL IMPLEMENTATION
class Image():
    def __init__(self, name, image_type):
        super(Image, self).__init__(name, image_type)

    def __repr__(self):
        return '<Image(name={self.description!r})>'.format(self=self)


class ImageSchema():
    @post_load
    def make_image(self, data, **kwargs):
        return Image(**data)