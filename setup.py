from setuptools import setup, find_packages

# Read the requirements from requirements.txt
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

version = "0.1.0"
# FIXME: No module named ModuleNotFoundError: No module named 'src.base'
# FIXME: Unistall the package
# FIXME: rename the src file to the same name of the library
setup(
    name="DocumentAI-std",
    version=version,
    packages=find_packages("src", exclude=["src.test"]),
    package_dir={"": "src"},  # Specify the root package directory
    install_requires=requirements,
    # Add other metadata like author, description, etc.
    author="Hamza Gbada",
    description="The main standards for Latis Document AI project",
)
