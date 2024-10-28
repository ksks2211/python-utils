import logging as logger

from python_utils.algo_utils.bit_set import BitSet


def test_bit_set():

    # possible members : 0 ~ 12
    s = BitSet(12)

    # {4}
    s.add(4)

    assert s.has(4)
    assert not s.has(10)

    # {4,10}
    s.add(10)
    assert s.has(10)

    # {10}
    s.remove(4)
    assert not s.has(4)

    # {5,10,12}
    s.add(12)
    s.add(5)

    elements = list(s)
    logger.info(elements)
    assert len(elements) == 3
