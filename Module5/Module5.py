def hw():     
    my_code = 'a = 3 + 4\nprint(a)'     
    my_func = exec_code(my_code)     
    my_func()     
    func= test(4)     
    print(func(4))  
    
def test(a):     
    def add(b):         
        nonlocal a        
        a += 1         
        return a+b     
    return add  
    
def exec_code(code):     
        def lazy_exec_code():
            exec(code)
        return lazy_exec_code

hw()


def word_split(poppins, word):
    print(poppins)
    slinky=len(poppins)
    print(slinky)
    slinky/2
    fuzzy = int(slinky/2)
    print(fuzzy)
    return poppins[:fuzzy] + word + poppins[fuzzy:]

print(word_split('supercalifragelisticexpialidocious', "NO"))

