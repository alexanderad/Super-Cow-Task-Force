## Linky: Keep your links alive!
[http://linky.ep.io/](http://linky.ep.io/)

Linky is a service that monitors links on the provided page and notifies you on possible problems with them. 
With Linky your links are safe. The smart way. Your links are divided into the following categories:

* internal
* external
* images
* system files (javascript and css)
  
Each of the categories has its own criteria for detection of broken links. There doesn’t have to be a 404 error for the link to be considered broken – redirects to a custom “Page not found” webpage or to the homepage will also be considered as errors.
In case you are aware of certain errors, Linky can keep record of problems you do not want to be notified about.
By default, a problem link is rechecked several times to make sure the page or file is no longer available and the problem is not temporary. In 48 hours the link’s status will be changed from “temporary unavailable” to “dead”.
At the same time Linky will keep log of availability of the page you are monitoring and create monthly graphs for each page so that you can keep track of you site uptime as well.


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
* fully functional dashboard & settings tabs
* allow user to add `sitemap.xml` of site that needs to be checked
* user customizible timeout
