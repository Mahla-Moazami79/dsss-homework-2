from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:math_quiz',
        ],
    },
    author="Mahla Moazamigoudarzi",
    author_email="moazamimahla807@gmail.com",
    description="A math quiz game",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Mahla-Moazami79/DSSS_HOMEWORK_2.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
