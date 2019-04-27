from setuptools import setup, find_packages
from setuptools.command.install import install as InstallCommand


def parse_requirements(requirements):
    with open(requirements) as f:
        return [l.strip('\n') for l in f if l.strip('\n') and not l.startswith('#')]


class Install(InstallCommand):
    """ Customized setuptools install command which uses pip. """

    def run(self, *args, **kwargs):
        from pip._internal import main as _main
        _main(['install', '.'])
        InstallCommand.run(self, *args, **kwargs)


setup(
    name="NGF",
    author="Ties van Rozendaal",
    author_email="git@tivaro.nl",
    maintainer="Thomas Evangelidis",
    maintainer_email="tevang3@gmail.com",
    description="\n*** An implementation of Convolutional Networks on Graphs for Learning Molecular Fingerprints in Keras 2.x. ***\n",
    long_description="Read the README.md file.",
    url="https://github.com/iwatobipen/keras-neural-graph-fingerprint",
    license="MIT.",
    version="1.0",
    platforms="Unix",
    dependency_links=[],
    cmdclass={
        'install': Install,
    },
    packages=find_packages(where='.', exclude=()),
    # package_dir={'':'dev'},
    install_requires=parse_requirements('requirements.txt')
)

# NOTES:
# Install RDKit manually, preferably through conda: conda install -c conda-forge rdkit
