import numpy as np
import os

def calc_distance(v1,v2):
	return np.linalg.norm(v1-v2)

def build_bond_list(coords,max_bond=1.55,min_bond=0):
    num_atoms = len(coords)
    bonds = {}
    for atom1 in range(num_atoms):
        for atom2 in range(atom1,num_atoms):
            d = dist(coords[atom1],coords[atom2])
            if (d < max_bond and d > min_bond):
                bonds[(atom1,atom2)] = d
    return bonds