from setuptools import setup, find_packages

setup(
    name='ActiveGraphNetworks',
    version='0.1.0',
    author='Callum Maystone',
    author_email='callum@youmatter.systems',
    description='AGNs – The architecture of emergence. Data that remembers.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/QuantumBeers/ActiveGraphNetworks',
    packages=find_packages(),
    install_requires=[
        'torch>=2.0.0',
        'networkx',
        'fastapi',
        'uvicorn',
        'pydantic',
        'matplotlib',
        'numpy'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'agn-explore = shell.explorer:main',  # Hook into your ActiveShell maybe?
        ],
    },
)
