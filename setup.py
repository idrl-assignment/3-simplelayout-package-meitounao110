import setuptools

setuptools.setup(
    name="simplelayout-meitounao110",  # Replace with your own username
    version="0.0.1",
    author="meitounao110",
    author_email="none",
    description="A simplelayout package",
    long_description_content_type="text/markdown",
    url="https://github.com/idrl-assignment/3-simplelayout-package-meitounao110",
    packages=['src/simplelayout'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: linux",
    ],
    python_requires='>=3.6',
    install_requires=['matplotlib', 'numpy', 'scipy', 'pytest'],
    entry_points={
        'console_scripts': [  # 配置生成命令行工具及入口
            'simplelayout = src.simplelayout.__main__:main'
        ]
    },
)
