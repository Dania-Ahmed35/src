import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/danya-ahmed/ros1_ws/src/my_python_pkg/install/my_python_pkg'