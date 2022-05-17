*Sample Project*
=================

**Playing the project**
-----------
-----------

*Where to go:*
~~~~~~~~~~~~~~~~~~~~
DEV:  localhost:3000
PROD: localhost:8000
~~~~~~~~~~~~~~~~~~~~

**Environments**
--------------------

The only difference between *Dev* & *Prod* environments is how services exposed:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DEV-Django: Request -> Django App -> DB
DEV-React:  Exposed directly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROD-Django: Request -> Nginx -> Gunicorn -> Django App -> DB
PROD-React:  Nginx -> React
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Project commands**
--------------------

*Building the project*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DEV: docker-compose -f docker-compose-dev.yml build
PROD: docker-compose -f docker-compose-prod.yml build
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Running the project*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DEV: docker-compose -f docker-compose-dev.yml up
PROD: docker-compose -f docker-compose-prod.yml up
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Stop the project*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DEV: docker-compose -f docker-compose-dev.yml down
PROD: docker-compose -f docker-compose-prod.yml down
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Testing (only Development environment)**
------------------------------------------
------------------------------------------

*Functional & Unit*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
docker-compose -f docker-compose-dev.yml exec django pytest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Linting*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
docker-compose -f docker-compose-dev.yml exec django flake8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Coverage*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
docker-compose -f docker-compose-dev.yml exec django pytest --cov .
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Note: as you might noticed, I mention testing for dev only. 
The reason for that is that usually pre-prod & prod testings are automated on CI/CD.**
