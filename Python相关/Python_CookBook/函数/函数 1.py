def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))
import html
def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
                  name=name,
                  attrs=attr_str,
                  value=html.escape(value))
    return element
def anyargs(*args, **kwargs):
    print(args)
    print(kwargs)
    def recv(maxsize, *, block):
        'Receives a message'
    pass

# recv(1024, True) # TypeError
    recv(1024, block=True)  # Ok
    def minimum(*values, clip=None):
        m = min(values)
        if clip is not None:
            m = clip if clip > m else m
        return m


    minimum(1, 5, 2, -5, 10)  # Returns -5
    minimum(1, 5, 2, -5, 10, clip=0)  # Returns 0