from nose.tools import assert_equals
from nose.plugins.attrib import attr

import Dot_Product

def check(package, a,b, ideal_output):
    output = package.dot_product(a,b)
    #save_to_text (str(fn), fn)
    assert_equals(output, ideal_output, f"{output} != {ideal_output}")

@attr('test1')
def Tes_Dot_Product():
    a_tests = [[1,2,3,4,5],[6,7,8,9], [1,5,6,9], [2,8,12,83]]
    b_tests = [[5,5,1,7,11],[5,0,3,1], [3,4,7,8], [4,6,62,72]]
    for a, b in zip(a_tests, b_tests):
        yield check, Dot_Product, a,b, np.dot(a,b)
