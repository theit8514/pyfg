from setuptools import setup, find_packages
from pip.req import parse_requirements

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements('requirements.txt')

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name = "pyfg",
    version = "0.40",
    packages = find_packages(),
    author = "XNET",
    author_email = "xnet@spotify.com.com",
    description = "Python API for fortigate",
    url = "https://ghe.spotify.net/XNET/FortiAPI",
    include_package_data = True,
    install_requires=reqs
)
