#write functions here, don't add input('') statements here!
def test_config():
    return True

GLOBAL_INT = 100

def use_global():
    global GLOBAL_INT
    GLOBAL_INT = 1000

GLOBAL_INT = 50
def change_global_variable():
   global use_global
    
   print(use_global)
