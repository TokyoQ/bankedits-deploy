import setuptools

with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="bankedits_deploy",
    version="0.1.0",

    description="A CDK Python app to deploy bankedits",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="TokyoQ",

    package_dir={"": "bankedits"},
    packages=setuptools.find_packages(where="bankedits"),

    install_requires=[
        "aws-cdk.core",
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
