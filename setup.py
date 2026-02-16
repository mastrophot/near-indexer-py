from setuptools import setup, find_packages

setup(
    name="near-indexer-py",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "requests",
        "pydantic>=2.0.0",
        "near-api-py"
    ],
    python_requires=">=3.8",
)
