import setuptools

# Reads the content of your README.md into a variable to be used in the setup below
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='scrotrem',                           # should match the package folder
    packages=['scrotrem'],                     # should match the package folder
    version='0.1',                                # important for updates
    license='MIT',                                  # should match your chosen license
    description='Screenshot Tool for Raspberry Pi users who are tired of using Scrot',
    long_description=long_description,              # loads your README.md
    long_description_content_type="text/markdown",  # README.md is of type 'markdown'
    author='Sachit Ramesh',
    author_email='quantechlxxi.corp@gmail.com',
    url='https://github.com/Sachit71/scrotrem', 
    project_urls = {                                # Optional
        "Headless Chrome": "https://github.com/Sachit71/scrotrem/issues"
    },
    install_requires=['pyfiglet','pyautogui','pynput'],                  # list all packages that your package uses
    keywords=["screenshot", "pyautogui", "scrot", "raspberry pi"], #descriptive meta-data
    classifiers=[                                   # https://pypi.org/classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    
    download_url="https://github.com/Sachit71/scrotrem/archive/refs/tags/hacktober.tar.gz")
