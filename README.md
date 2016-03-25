# Chore-Tracker
Hello and welcome to the Chore Tracker web application repository!
### Description:
The Chore Tracker web application stores and keeps track of all the chores within a household
that need to be done. Features include adding or removing housemates from a list of housemates,
addition or deletion of chores for a housemate and editing housemate information (first names, last names, email).
### Features to come:
* Login page
* Create username/password registration
* Logout capabilities
* `House` data model entity

### Steps to install and use the Django API:
Skip steps as needed if you know you've already completed them i.e. already have Python 2.7+ installed.

1. Install Python 2.7+ <a href='https://www.python.org/downloads/'>here</a> (although we've been developing with Python 			version 3.4+) 
2. Install Pip for an easier installation process <a href='https://bootstrap.pypa.io/get-pip.py'>here</a>. This is a link to the script for pip that contains data for installation. Right click and select 'Save As' and place it somewhere. Make sure your environment variables allow python scripts to be callable from the command line. Depending on your Operating System, if you aren't sure how to add python to your path, google 'Adding Python to Path'. You can check if your path has been correctly configured by executing this command on the command line: `python --version`. Change directory (cd) over to the folder directory containing the pip script. Once all of that is done, execute the command: `python get-pip.py`. This will install Pip onto your computer.
3. Install Django by executing the command: `pip install django`. This will install the Django API onto your computer.
4. Install the datetime widget for Django by executing the command: `pip install django-datetime-widget`.
5. Clone this repository somewhere on your local hard drive and change directory into `~chore-tracker/chore_tracker` and execute the command: `python manage.py runserver` which will, as the API says, run the server. Now open up a web browser and go over to the localhost url: `127.0.0.1:8000/chore_app/`.

