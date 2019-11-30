"""Baseclass for writer functions."""
from __future__ import absolute_import

import os
import textwrap


class BaseClass(object):
    """Base class for writing inits."""

    def __init__(self):
        """Empty placeholder."""
        pass

    def write_init(self):
        """Write the imports string and all_udefs list to the init file."""
        init_path = os.path.join(self._base_path, '__init__.py')
        with open(init_path, 'w+') as init_file:
            # Write the __init__, create if it doesn't exist
            init_file.write(self.imports)

            # The objects that will be added for __all__
            # Template for __all__ functions in all modules
            self._write_all(init_file)
            self._write_credit(init_file)

        init_file.close()
        print('{} has been appended/generated\n'.format(init_path))

    def _write_all(self, init_file=None):
        """Write the __all__ line to the init.

        Parameters
        ----------
        init_file : _io.TextIOWrapper, optional
            file connection to init_file. If optional the all list
            is printed.

        """
        slist = textwrap.wrap(
            sorted(
                self.all_udefs,
                key=lambda x: x.lower()
            ).__str__().strip('[').strip(']'),
            79
        )

        all_ = '__all__ = ['
        for _ in range(len(slist)):
            all_ += '\n    {}'
        all_ += '\n]'

        if init_file:
            init_file.write(all_)
        else:
            print(all_)

    def _write_credit(self, init_file=None):
        """Write the __all__ line to the init.

        Parameters
        ----------
        init_file : _io.TextIOWrapper, optional
            file connection to init_file. If optional the all list
            is printed.

        """
        init_file.write(
            '# this __init__ was automatically generated by afinipy'
        )
