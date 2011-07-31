## Linky: Keep your links alive!
[http://linky.ep.io/](http://linky.ep.io/)

#### Install

##### Epio
1. `git clone git://github.com/alexanderad/Super-Cow-Task-Force.git`
2. `epio create` (make sure that you use epio.ini file that comes with Linky)
3. `epio upload`
4. `epio run_command shell`
5. `./manage.py syncdb && ./manage.py migrate`

##### Standalone
1. `git clone git://github.com/alexanderad/Super-Cow-Task-Force.git`
2. `pip install -r requirements.txt` 
3. uncomment/edit DATABASES option in `settings.py` (you can omit this step in case of ep.io)
4. run `./manage.py syncdb and ./manage.py migrate` if necessary
5. `./manage.py runserver`
6. locate http://localhost:8000/ in you browser

#### TODO
* `crontab` script that will check user's pages/sites at given intervals and notify in case of problems
