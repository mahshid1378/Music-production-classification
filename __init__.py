import os
import pathlib

import cached_conv as cc
import gin
import torch

gin.add_config_file_search_path(os.path.dirname(__file__))
gin.add_config_file_search_path(
    os.path.join(
        os.path.dirname(__file__),
        'configs',
    ))

cc.get_padding = gin.external_configurable(cc.get_padding, module="cc")
cc.Conv1d = gin.external_configurable(cc.Conv1d, module="cc")
cc.ConvTranspose1d = gin.external_configurable(cc.ConvTranspose1d, module="cc")

#from .blocks import *
from blocks import *
#from .discriminator import *
from discriminator import *
#from .model import RAVE, BetaWarmupCallback
from model import RAVE, BetaWarmupCallback
#from .pqmf import *
from pqmf import *