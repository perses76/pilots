def main():
    print 'hello'
    res = func(5)
    print 'next', res.next()
    print 'res', res

    process_func = get_processor(3)
    print 'process_func={}'.format(process_func(4))
    print 'end'


def func(a):
    print "start func"
    yield a + 1
    print "end func"


def get_processor(init_val):
    def process(a):
        return init_val + a
    return process

if __name__ == '__main__':
    main()
