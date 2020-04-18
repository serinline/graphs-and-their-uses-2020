import setuptools

setuptools.setup(
    name="graphlib",
    packages=setuptools.find_packages(),
    install_requires=[
        "networkx",
        "matplotlib",
        "numpy"
    ],
    python_requires='>=3.6',
)
