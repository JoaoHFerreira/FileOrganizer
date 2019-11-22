# FileOrganizer
Script to organize files in folders.

## Problem
Probably you already have an file organization problem, having lots of files in a same place without any clear categories to classify your contents. This simple tool your probleming, dealing with this matters for you.

## Setup
To make things easier, we a have an yaml file were describes the acces points to set your python. Explaning yaml.

### path:
The is the place were the most part of your files will be dropped, in my case was /`home/joaoh/Downloads`. Basically the script looks for this path and put the files in the right place.

### destiny_root:
Is the prefix of all your folders name. In my case for example I used my user space as root `/home/joaoh/`. 

### default_folders
`default_folders`  are the sufix folders and they specify the final path name where files will be placed in, the will be like the following way:

 - `/home/joaoh/Imagens`
 - `/home/joaoh/Documentos`
 - `/home/joaoh/Vídeos`

 Inside every item cited above, we could or not, have a list describing the file types that will be sended in. In my case, as example.
 ```
default_folders:
    Imagens: png,jpg,jpeg
    Documentos: pdf,ipynb,json,tf,jar,zip,gz,me,xml,script,sh,py
    Vídeos:
 ```
Taking the folder `Documentos`, every pdf file in path will be put in this destiny.

 If the file type as not tracked  then a folder in the path will be created.

 The rull of folders name creation is simple, if exists, not create, if not, create.

## Cron
To make sure that your script will run scheduled, we need to add in your system cron. To do that follow the next steps.
- 1. Enter in your system as admin using: `sudo su`;
- 2. Digit `crontab -e` to enter in your and specify a scheduler that satisfies your requirements.
```
Example:

*/5 * * * *  python3 YOUR_PATH_TO_YOUR_SCRIPT/file_organizer.py
```
In this example we put a scheduler every 5 minutes. To understand more abou cron I suggest the following links:
- https://crontab.guru
- https://www.ostechnix.com/a-beginners-guide-to-cron-jobs/

## How do I contribute for FileOrganizer
Check this [link](https://github.com/JoaoHFerreira/FileOrganizer/blob/master/CONTRIBUTING.md) for detailed instructions
