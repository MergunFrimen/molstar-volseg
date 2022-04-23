import abc
from typing import Union

import numpy as np

from db.interface.i_preprocessed_db import ProcessedVolumeSliceData
from db.interface.i_preprocessed_medatada import IPreprocessedMetadata


class IVolumeToCifConverter(abc.ABC):
    @abc.abstractmethod
    def convert(self, preprocessed_volume: ProcessedVolumeSliceData, metadata: IPreprocessedMetadata, downsampling: int, grid_size: list[int]) -> Union[bytes, str]:
        pass

    @abc.abstractmethod
    def convert_metadata(self, metadata: IPreprocessedMetadata):
        pass
