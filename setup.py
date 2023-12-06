from setuptools import setup, find_packages

setup(
    name='Laura',
    version='1.0',  # Replace with your project's version
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'colorama==0.4.6',
        'Flask==2.3.2',
        'Flask-SocketIO==5.3.4',
        'importlib-metadata==6.8.0',
        'numpy==1.24.3',
        'openai==0.27.8',
        'regex==2023.6.3',
        'requests==2.31.0',
        'tenacity==8.2.2',
        'tiktoken==0.4.0',
        'virtualenv==20.23.0',
        'Werkzeug==2.3.6',
        'Markdown==3.4.4',
        'Pillow==10.1.0'
    ],
    entry_points={
        'console_scripts': [
            'laura=laura.run:main',
        ],
    },
)
