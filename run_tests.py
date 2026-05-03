import sys
import unittest
from unittest.mock import MagicMock

# Mock problematic modules for testing environment
sys.modules['distutils'] = MagicMock()
sys.modules['distutils.dir_util'] = MagicMock()
sys.modules['prctl'] = MagicMock()
sys.modules['RPi'] = MagicMock()
sys.modules['RPi.GPIO'] = MagicMock()
sys.modules['smbus'] = MagicMock()
sys.modules['tomlkit'] = MagicMock()
sys.modules['scapy'] = MagicMock()
sys.modules['scapy.all'] = MagicMock()

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.discover('.')
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
