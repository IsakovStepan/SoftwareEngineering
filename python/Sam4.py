from typing import Tuple, Any

def slice_first_to_second(tpl: Tuple[Any, ...], x: Any) -> Tuple[Any, ...]:
    try:
        first = tpl.index(x)
    except ValueError:
        return ()
    try:
        second = tpl.index(x, first+1)
    except ValueError:
        return tpl[first:]
    return tpl[first:second+1]

if __name__ == '__main__':
    print(slice_first_to_second((1,2,3), 8))          
    print(slice_first_to_second((1,8,3,4,8,9,2), 8))      
    print(slice_first_to_second((1,2,8,5,1,2,9), 8))  