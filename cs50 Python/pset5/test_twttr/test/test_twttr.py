from twttr import shorten

def test_upper_lower():
    assert shorten('TESTING testing tst ') == 'TSTNG tstng tst '
    assert shorten('   ') == '   '
    assert shorten('AbRA cADAbRA') == 'bR cDbR'

def test_nums():
    assert shorten('1234') == '1234'
    assert shorten('TEST 123 TEST') == 'TST 123 TST'

def test_punctuation():
    assert shorten('!?... <>') == '!?... <>'

if __name__ == '__main__':
    main()