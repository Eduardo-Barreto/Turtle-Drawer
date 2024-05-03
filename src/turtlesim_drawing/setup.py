from setuptools import setup

package_name = 'turtlesim_drawing'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    data_files=[
        # 'share/ament_index/resource_index/packages',
        # 'share/ament_index/resource_index/python_packages',
    ],
    entry_points={
        'console_scripts': [
            'turtlesim_drawing = turtlesim_drawing.turtlesim_drawing:main',
        ],
    },
    zip_safe=True,
)
