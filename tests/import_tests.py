
def brainmix_import_test():
    try:
        import brainmix_register
    except:
        assert False

import brainmix_register as bm

def data_import_test():
    try:
        from brainmix_register import data
    except:
        assert False
