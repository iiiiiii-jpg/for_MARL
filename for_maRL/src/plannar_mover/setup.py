from setuptools import find_packages
from setuptools import setup

package_name = 'plannar_mover'

setup(
    name=package_name,
    version='0.9.3',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Janardan Verma',
    author_email='janardanverma18@gmail.com',
    maintainer='Janardan Verma',
    maintainer_email='janardanverma18@gmail.com',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description=(
        'Python nodes which were previously in the ros2/examples repository '
        'but are now just used for demo purposes.'
    ),
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pub_sub_modelstate = plannar_mover.pub_sub_modelstate:main',
            'set_entity = plannar_mover.set_entity:call_set_entity_state_service',
        ],
    },
)
