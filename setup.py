# Copyright 2021 Brave Mobile Co., Ltd.
import setuptools

install_requires = [
    "marshmallow",
    "google-api-python-client",
    "google-ads",
]

tests_requires = [
    "black>=20.8b1",
    "flake8>=3.8.2",
    "pytest",
    "pytest-cov",
    "tox",
    "Sphinx>=3.2.1",
    "docutils==0.15.2",
    "isort",
    "requests_mock",
    "pytest-mock",
] + install_requires


def get_long_description() -> str:
    return (
        open("README.md", encoding="utf8").read().strip()
        + "\n\n"
        + open("CHANGELOG.md", encoding="utf8").read().strip()
    )


setuptools.setup(
    name="Soomgo-gather",
    version=open("VERSION").read().strip(),
    url="https://github.com/Soomgo-Platform/soomgo-gather",
    description="",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    keywords="Naver,NaverSearchAD,GA,collect,data,gather,soomgo-gather,soomgo",
    author="Brave Mobile Co., Ltd.",
    author_email="platform@soomgo.com",
    project_urls={
        "Changelog": "https://github.com/Soomgo-Platform/soomgo-gather/blob/main/CHANGELOG.md",
        "Tracker": "https://github.com/Soomgo-Platform/soomgo-gather/issues",
    },
    license="MIT",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires=install_requires,
    extras_require={"test": tests_requires},
    zip_safe=False,
    # test_suite=''
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
