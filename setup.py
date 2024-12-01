from setuptools import setup, find_packages

setup(
    name="pocketoptionapi",
    version="1.0.0",
    description="Pocket Options API",
    long_description="A Python API for PocketOption",
    long_description_content_type="text/plain",
    url="https://github.com/honza-toegel/PocketOptionAPI",
    author="",
    author_email="",  # Add your email address if applicable
    license="MIT",
    packages=find_packages(where="./pocketoptionapi"),
    package_dir={"": "./pocketoptionapi"},
    python_requires=">=3.10",
    install_requires=[
        "numpy>=1.26.4",
        "pandas>=2.2.2",
        "requests>=2.32.3",
        "anyio>=4.6.2",
        "numexpr>=2.10.1",
        "bottleneck>=1.4.2",
        "pytz>=2024.1",
        "tzlocal>=5.2",
        "websockets>=10.4",
        "typing_extensions>=4.11.0",
        "urllib3>=2.2.3",
        "python-dateutil>=2.9.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    zip_safe=False,
)