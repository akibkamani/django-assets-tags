from setuptools import find_packages, setup

setup(
    name="django-assets-tags",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    description="Reusable Django template tags for public and private asset URLs.",
    author="Akib Kamani",
    url="https://github.com/akibkamani/django-assets-tags",
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "Django>=5.0",
    ],
)
