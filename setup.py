from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    # Basics
    name='styledlogger',
    version='0.1 PRE',
    description='A simple, styled logging library.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    
    # Author
    author='ImAlek (splayzdk)',
    author_email='alek@imalek.me',
    
    # Package
    package_dir={'': 'styledlogger'},
    packages=find_packages(where='src'),
    url='https://github.com/SpLayzDK/StyledLogger/',

    # License
    license='BSL 1.0',
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Boost Software License 1.0 (BSL-1.0)",
        "Operating System :: OS Independent"
    ],

    # Dependencies
    python_requires='>=3.7',
    install_requires=[
        'colorama>=0.4.6',
        'arrow>=1.2.3'
    ],

    extras_require={
        'dev': [
            'pytest>=7.0',
            "twine>=4.0.2"
        ]
    }

)