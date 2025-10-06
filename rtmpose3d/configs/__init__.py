"""
Configuration files for RTMPose3D models
"""

import os
from pathlib import Path

# Get the directory where config files are stored
CONFIG_DIR = Path(__file__).parent

# Model configurations
DETECTOR_CONFIG = str(CONFIG_DIR / 'rtmdet_m_640-8xb32_coco-person.py')
POSE_L_CONFIG = str(CONFIG_DIR / 'rtmw3d-l_8xb64_cocktail14-384x288.py')
POSE_X_CONFIG = str(CONFIG_DIR / 'rtmw3d-x_8xb32_cocktail14-384x288.py')

# Checkpoint URLs - hosted on GitHub Releases
GITHUB_RELEASE_BASE = 'https://github.com/mutedeparture/rtmpose3d/releases/download/v1.0.0'

DETECTOR_CHECKPOINT_URL = f'{GITHUB_RELEASE_BASE}/rtmdet_m_8xb32-100e_coco-obj365-person-235e8209.pth'
POSE_L_CHECKPOINT_URL = f'{GITHUB_RELEASE_BASE}/rtmw3d-l_cock14-0d4ad840_20240422.pth'
POSE_X_CHECKPOINT_URL = None  # Add if X model checkpoint is available
POSE_L_CHECKPOINT_URL = None  # Will use local demo checkpoint
POSE_X_CHECKPOINT_URL = None  # Not available yet

__all__ = [
    'CONFIG_DIR',
    'DETECTOR_CONFIG',
    'POSE_L_CONFIG', 
    'POSE_X_CONFIG',
    'DETECTOR_CHECKPOINT_URL',
    'POSE_L_CHECKPOINT_URL',
    'POSE_X_CHECKPOINT_URL'
]
