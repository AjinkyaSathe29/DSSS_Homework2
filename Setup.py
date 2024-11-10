from setuptools import setup, find_packages, setup

setup(
    name='math_quiz_game',  
    version="1.0",  
    description='A math quiz to practise problem with two integers and an operator'        
    packages=find_packages(),  
    include_package_data=True
    install_requires=[],
    license='Apache License'
    author='Ajinkya Sathe',      
    author_email='ajinkya.sathe@fau.de', 
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown',  
    url='https://github.com/AjinkyaSathe29/DSSS_Homework2.git',  
    classifiers=[          
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)