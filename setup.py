from setuptools import setup, find_packages

setup(
    name="c-med_alpha_data_merge_program",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "PySide6",
        "pandas"
    ],
    entry_points={
        'console_scripts': [
            'c-med_alpha_data_merge_program=main:main',
        ],
    },
    include_package_data=True,
    package_data={
        # Include any package data files here, if needed.
    },
    author="Byeongkuk Oh",
    author_email="byeongkukoh@gmail.com",
    description="본 프로그램은 in-ear 고막온도 측정계인 c-med alpha에서 추출한 데이터를 하나의 파일로 합쳐주는 프로그램입니다.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/lunamundus/c-med_alpha_data_merge_program",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
