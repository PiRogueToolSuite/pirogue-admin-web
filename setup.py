from setuptools import find_packages, setup

requirements = [i.strip() for i in open("requirements.txt").readlines()]

setup(
    name="[package_name]",
    version="1.0.0",
    author="U+039b",
    author_email="hello@pts-project.org",
    description="[package_description]",
    url="https://github.com/PiRogueToolSuite/[package_name]",
    install_requires=requirements,
    packages=find_packages(),
    zip_safe=True,
    entry_points={
        "console_scripts": [
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3.0 License",
        "Operating System :: OS Independent",
    ],
)