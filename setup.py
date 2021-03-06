import os
import pathlib

from setuptools import find_packages, setup

setup_path = pathlib.Path(os.path.dirname(os.path.relpath(__file__)))
readme_path = setup_path.joinpath("README.md").as_posix()
with open(readme_path, encoding="utf-8", mode="r") as f:
    long_description = f.read()

setup(
    name="AudioConverter",
    use_scm_version={"root": ".", "relative_to": __file__},
    setup_requires=["setuptools_scm"],
    description="Audio Converter CLI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="lamdav",
    author_email="david.lam@lamdav.com",
    license="MIT",
    python_requires=">=3.5",
    packages=find_packages(),
    entry_points={"console_scripts": ["audioconvert=AudioConverter.converter:cli"]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Multimedia :: Sound/Audio :: Conversion",
        "Topic :: Utilities",
    ],
    install_requires=["click==7.1.2", "colorama==0.4.3", "pydub==0.24.0"],
    extra_requires={
        "dev": {"black==19.10b0", "isort==4.3.21", "pip-tools==5.3.0", "pur==5.3.0"}
    },
    keywords=["audioconverter audio converter CLI"],
    include_package_data=True,
    project_urls={
        "Bug Reports": "https://github.com/lamdaV/AudioConverter/issues",
        "Source": "https://github.com/lamdaV/AudioConverter",
    },
)
