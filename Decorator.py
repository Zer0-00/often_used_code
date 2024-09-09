def main(func):
    import sys, inspect, argparse

    parent_frame = inspect.stack()[1].frame
    __name__ = parent_frame.f_locals.get('__name__')

    if __name__ == '__main__':

        # get full argument specification
        argspec = inspect.getfullargspec(func)
        args = argspec.args or []
        defaults = argspec.defaults or ()
        undefined = object() # sentinel object
        n_undefined = len(args) - len(defaults)
        defaults = (undefined,) * n_undefined + defaults

        # automatically generate argument parser
        parser = argparse.ArgumentParser()
        for name, default in zip(argspec.args, defaults):
            type_ = argspec.annotations.get(name, None)

            if default is undefined: # positional argument
                parser.add_argument(name, type=type_)

            elif default is False and type_ in {bool, None}: # flag
                parser.add_argument(
                    '--' + name, default=False, type=as_bool, help=f'[{default}]'
                )
            else: # optional argument
                if type_ is None and default is not None:
                    type_ = type(default)
                parser.add_argument(
                    '--' + name, default=default, type=type_, help=f'[{default}]'
                )

        # parse and display command line arguments
        kwargs = vars(parser.parse_args(sys.argv[1:]))
        print(kwargs)

        # call the main function
        func(**kwargs)

    return func
