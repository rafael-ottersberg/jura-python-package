import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="rv_curve_rafael",
    long_description=long_description,
    license="GPLv3",
    version="0.0.1",
    author="Rafael",
    author_email="rafael.ottersberg@unibe.ch",
    description="Plot RV curve",
    packages=setuptools.find_packages(),
    install_requires=['numpy', 'matplotlib'],
    classifiers=["Programming Language :: Python :: 3",],
)