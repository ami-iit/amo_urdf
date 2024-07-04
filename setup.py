from setuptools import setup, find_packages

setup(
    name="amo_urdf",
    version="0.0.1",
    maintainer="ami-iit",
    maintainer_email="",
    description="Friendly mantainance fork of odio-urdf.",
    license="MIT",
    packages=find_packages("amo_urdf"),
    package_dir={"amo_urdf": "amo_urdf"},
    python_requires=">=3.8, <4",
    install_requires=["six"],
)
