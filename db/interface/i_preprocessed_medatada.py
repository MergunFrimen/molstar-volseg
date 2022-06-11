import abc
from typing import Dict, List
from preprocessor.src.preprocessors.implementations.sff.preprocessor._metadata_methods import MeshComponentNumbers
import numpy as np


class IPreprocessedMetadata(abc.ABC):
    @abc.abstractmethod
    def json_metadata(self) -> str:
        pass

    @abc.abstractmethod
    def segmentation_lattice_ids(self) -> List[int]:
        pass

    @abc.abstractmethod
    def segmentation_downsamplings(self, lattice_id: int) -> List[int]:
        pass

    @abc.abstractmethod
    def volume_downsamplings(self) -> List[int]:
        pass

    @abc.abstractmethod
    def origin(self) -> List[float]:
        '''
        Returns the coordinates of the initial point in Angstroms
        '''
        pass
    
    @abc.abstractmethod
    def voxel_size(self, downsampling_rate: int) -> List[float]:
        '''
        Returns the step size in Angstroms for each axis (X, Y, Z) for a given downsampling rate
        '''
        pass

    @abc.abstractmethod
    def grid_dimensions(self)  -> List[int]:
        '''
        Returns the number of points along each axis (X, Y, Z)
        '''
        pass
    
    @abc.abstractmethod
    def sampled_grid_dimensions(self, level: int) -> List[int]:
        '''
        Returns the number of points along each axis (X, Y, Z) for specific downsampling level
        '''
        pass

    @abc.abstractmethod
    def mean(self, level: int)  -> np.float64:
        '''Return mean for data at given downsampling level'''
        pass

    @abc.abstractmethod
    def std(self, level: int)  -> np.float64:
        '''Return standard deviation for data at given downsampling level'''
        pass
    
    @abc.abstractmethod
    def max(self, level: int)  -> np.float64:
        '''Return max for data at given downsampling level'''
        pass
    
    @abc.abstractmethod
    def min(self, level: int)  -> np.float64:
        '''Return min for data at given downsampling level'''
        pass

    @abc.abstractmethod
    def mesh_component_numbers(self) -> MeshComponentNumbers:
        '''Return typed dict with numbers of mesh components (triangles, vertices etc.) for
        each segment, detail level and mesh id'''
        pass

    @abc.abstractmethod
    def detail_lvl_to_fraction(self) -> dict:
        '''Returns dict with detail lvls (1,2,3 ...) as keys and corresponding
        mesh simplification ratios (fractions, e.g. 0.8) as values'''
        pass