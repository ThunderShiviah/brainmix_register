
def import_demo_test():
    try:
        from brainmix_register import demo
    except:
        assert False

from brainmix_register import demo


def import_test_module_test():
    try:
        from brainmix_register.demo import test
    except:
        assert False

def import_main_function_test():
    try:
        from brainmix_register.demo.test import main
    except:
        assert False

def run_demo_test():
    from brainmix_register.demo.test import main
    main()

     


