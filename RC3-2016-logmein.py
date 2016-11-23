import angr

def main():
    p = angr.Project("logmein", load_options={'auto_load_libs': False})
    pr = p.surveyors.Explorer(find=(0x4007F0, ), avoid=(0x4007C0,))
    pr.run()

    return pr.found[0].state.posix.dumps(0).split('\x00')[0]


def test():
    assert main() == 'RC3-2016-XORISGUD'

if __name__ == '__main__':
    print main()

