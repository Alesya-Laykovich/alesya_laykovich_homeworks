class MyMixin(object):

    mixin_prop = ''

    def get_prop(self):
        return self.mixin_prop.upper()

    def get_upper(self, string: str):
        return string.upper()