from setuptools import setup, find_packages

setup(
    name="obsidian-md-watcher",
    version="0.1.0",
    packages=find_packages(include=["watcher", "watcher.*"]),
    install_requires=["psutil"],
    author="Marcus",
    description="Automatically archives ChatGPT markdown exports to your Obsidian vault with Git and tagging.",
    url="https://github.com/YOUR_USERNAME/obsidian-md-watcher",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
