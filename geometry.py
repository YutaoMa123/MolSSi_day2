import numpy as np
import os

def calc_distance(v1,v2):
	"Compute dist between 2 vectors"
	return np.linalg.norm(v1-v2)

def build_bond_list(coords, max_bond = 2.93, min_bond = 0):
	"""Build list of bonds from atomic coordinates based on distances.

	Parameters
	----------
	coordinates : Numpy array
		An array of atomic coordinates
	max_bond : float, optional
		The maximum distance between atoms to be considered a bond. Default is 2.93 Bohr.
	min_bond : float , optional
		The minimum distance atoms to be considered a bond.

	Returns
	-------
	bonds : dict
		A dictionary where the keys are atom pairs in bonds and values are the corresponding bond length
	"""
	num_atoms = len(coords)
	bonds = {}
	for atom1 in range(num_atoms):
		for atom2 in range(atom1,num_atoms):
			d = dist(coords[atom1],coords[atom2])
			if (d < max_bond and d > min_bond):
				bonds[(atom1,atom2)] = d
	return bonds