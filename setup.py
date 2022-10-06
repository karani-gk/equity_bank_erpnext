from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in equity_bank/__init__.py
from equity_bank import __version__ as version

setup(
	name="equity_bank",
	version=version,
	description="Equity Bank ERPNext Integration",
	author="Upeosoft Limited",
	author_email="karani@upeosoft.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
