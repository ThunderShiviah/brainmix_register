
import importlib as ip
import unittest
from brainmix_register import * # TODO: Refactor into a set-up decorator.

class ImportTests(unittest.TestCase):


    # -------------- Helper functions ----------------
    def existing_module_import(self, module):

        if module == 'brainmix_register':
            assert(ip.import_module(module))
        else:
            assert(ip.import_module('brainmix_register.{module}'.format(\
            module=module)))

    def import__all__index_modules(self, module_name):
        """ Checks that all submodules listed in the module's __all__
        variable are able to be imported.
        """

        module = ip.import_module('brainmix_register.{module}'.format(\
            module=module_name))

        for item in module.__all__:
            self.existing_module_import(item)

        
    # --------------------- Tests ---------------------------

    def non_existent_module_import_test(self):

        module = 'fake'
        self.assertRaises(ImportError, __import__, module)


    def brainmix_register_import_test(self):

        self.existing_module_import('brainmix_register')

    def brainmix_register_index_test(self):

        module = 'brainmix_register'
        self.import__all__index_modules(module)

    def data_import_test(self):

        self.existing_module_import('data')

    def data_index_test(self):

        module = 'data'
        self.import__all__index_modules(module)

if __name__ == '__main__':
    unittest.main()
