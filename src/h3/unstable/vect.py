from .._cy import unstable_vect as _vect

import numpy as np


def h3_to_parent(h, res):
    """
    Get parent of arrays of cells

    Parameters
    ----------
    h : array of H3Cells

    res: int
        Resolution for output cells.

    Returns
    -------
    array of H3Cells
    """
    out = _vect.h3_to_parent_vect(h, res)

    return out


def geo_to_h3(lats, lngs, res):
    """
    Convert arrays describing lat/lng pairs to cells.

    Parameters
    ----------
    lats, lngs : arrays of floats

    res: int
        Resolution for output cells.

    Returns
    -------
    array of H3Cells
    """
    assert len(lats) == len(lngs)

    out = np.zeros(len(lats), dtype='uint64')

    _vect.geo_to_h3_vect(lats, lngs, res, out)

    return out


def cell_haversine(a, b):
    """
    Compute haversine distance between the centers of cells given in
    arrays a and b.


    Parameters
    ----------
    a, b : arrays of H3Cell

    Returns
    -------
    float
        Haversine distance in kilometers
    """

    assert len(a) == len(b)

    out = np.zeros(len(a), dtype='double')

    _vect.haversine_vect(a, b, out)

    return out
