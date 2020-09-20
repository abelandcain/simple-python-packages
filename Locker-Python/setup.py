import setuptools

requires = [
    'printplus>=1',
    'tqdm>=4.48.2',
    'passlib>=1.7.2'
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="renamelocker",
    version="1.1",
    author="noidea",
    author_email="noidea1238@gmail.com",
    description="Simple package to rename files with extension to hide videos and images",
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=requires,
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': ['renamelocker=renamelocker.app:main'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
