from setuptools import setup, find_packages

setup(
    name="SuluLocator",
    version="0.1",
    packages=find_packages(),
    author="Your Name",
    author_email="your.email@example.com",
    description="Indoor localization library based on Sulu from Star Trek.",
    license="MIT",
    keywords="localization indoor pozyx",
    url="URL of your project",  # e.g., GitHub repo link
    install_requires=[
        "pyserial>=3.4",
        "pypozyx",
    ]
)
