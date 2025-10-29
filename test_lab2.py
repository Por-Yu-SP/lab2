import Lab2 

def test_min_max():
    result=0
    input_arr = [10,21,44,12,313,3232,4343,567,344,252,242,234,234,45,36,5345,234,1]
    result = Lab2.find_min_max(input_arr)
    assert(result==[1,5345])

def test_calc_average():
    result=0
    input_arr = [1,5,10,15]
    result=Lab2.calc_average(input_arr)
    assert(result==7.75)

def test_median_temp():
    result=0
    input_arr = [4,20,18,3,0]
    result=Lab2.calc_median_temperature(input_arr)
    assert(result==4)