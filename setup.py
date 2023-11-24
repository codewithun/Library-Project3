from setuptools import setup

setup(
    name='tebakcobi',
    version='0.1.0',
    packages=['tebakcobi'],
    install_requires=[
        # Tidak ada dependensi khusus pada contoh ini
    ],
    entry_points={
        'console_scripts': [
            'tebakangka=tebakangka.game:main',
        ],
    },
    author='Untara Eka Saputra',
    author_email='untara337@gmail.com',
    description='A simple number guessing game library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/codewithun/tebakangka',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
