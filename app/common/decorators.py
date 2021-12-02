

# --- Class decorators ---
def auto_iter(*, exclude_vars):
    if exclude_vars is None:
        exclude_vars = []
    def wrapper(cls):
        def __iter__(self): return (attr for attr in dir(self) if not attr.startswith("_") and attr not in exclude_vars)
        cls.__iter__ = __iter__
        return cls
    return wrapper


def _obj_vars_to_str(obj, exclude_vars=None):
    if exclude_vars is None:
        exclude_vars = []
    return ', '.join(f'{name}={value}' for (name, value) in sorted(vars(obj).items())
                     if not name.startswith("_") and name not in exclude_vars)


def auto_str(*, exclude_vars):
    def wrapper(cls):
        def __str__(self): return f'{type(self).__name__}({_obj_vars_to_str(self, exclude_vars)})'
        cls.__str__ = __str__
        return cls
    return wrapper


def auto_repr(*, exclude_vars):
    def wrapper(cls):
        def __repr__(self): return f'{type(self).__name__}({_obj_vars_to_str(self, exclude_vars)})'
        cls.__repr__ = __repr__
        return cls
    return wrapper
