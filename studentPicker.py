import random

KREWES = {
    'orpheus': ['one', 'two', 'three'],
    'rex': ['1', '2', '3'],
    'endymion': ['X', 'Y', 'Z']
}

def studentPicker( krew):
    student = random.randint(0, len(KREWES[krew])-1 )
    print( KREWES[krew][student] )


studentPicker('orpheus')
studentPicker('rex')
studentPicker('endymion')
