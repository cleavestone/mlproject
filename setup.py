from setuptools import setup, find_packages

def get_requirements():
    requirements = []
    with open('requirements.txt') as f:
        lines = f.readlines()
        for line in lines:
            if not line.startswith('-e'):
                requirements.append(line.strip())
    return requirements

setup(
    name='mlproject',
    version='0.1',
    packages=find_packages(),
    license='MIT',
    author= 'Cleave',
    install_requires=get_requirements(),
)