from setuptools import find_packages, setup

setup(
    name="youtube00e1f862e5eff",
    version="0.0.2",
    packages=find_packages(),
    install_requires=[
        "lxml",
        "exorde_data",
        "aiohttp",
        "HTMLParser",
        "youtube_comment_downloader==0.1.68"
    ],
    extras_require={"dev": ["pytest", "pytest-cov", "pytest-asyncio"]},
)
