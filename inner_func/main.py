def get_func(init_val):
    some_val = init_val + 5
    def func(val):
        return some_val + val
    return func

def main():
    func = get_func(3)
    print func(4)
    print 'end'

main()
