from setuptools import setup, find_packages

setup(
    name="unhcrplotlystyle",
    version="0.1.0",  # Update for new releases
    author="Lei Chen",
    author_email="chen@unhcr.org",
    description="A Plotly template for UNHCR-style visualizations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/leichen88/unhcrplotlystyle",
    packages=find_packages(),
    install_requires=["plotly>=5.0.0"],  # Specify dependencies
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)