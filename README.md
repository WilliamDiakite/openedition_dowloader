# OpenEdition Issue Dowloader


This python script helps you retrieve issues from magazines hosted on https://www.openedition.org/


1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Example](#example)


## Requirements

Operating Systems: OSX, Linux

Tested with Python 3.6


## Installation

In a terminal enter:
>git clone https://github.com/WilliamDiakite/openedition_dowloader.git

## Usage

Enter the directory,
>cd openedition_dowloader/

Execute the script,
>python download.py -l *issue_url* -d *your_directory*

## Example

To dowload issue #17 from [Coprus magazine](https://journals.openedition.org/corpus/) and store in the *test/* folder, use the following command:

>python download.py -l https://journals.openedition.org/corpus/2726 -d ./test/
