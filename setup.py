from setuptools import setup, find_packages

setup(
    name="NetSpy",
    version="1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "netspy=netspy.main:main",
        ]
    },
    author="Hamzah",
    description="A penetration testing tool for network analysis and payload generation.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
