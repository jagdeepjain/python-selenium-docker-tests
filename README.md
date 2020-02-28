# Python + Selenium + Docker
This sample project demonstrates how we can utilize docker container for running python selenium ui tests.

Script does the Docker Container start before the test gets executed and once execution is completed it will get stopped/removed.

Test script file `ui-test.py` has `setUpClass()` which instantiate the selenium container and `tearDownClass()` stop/remove the selenium container.

## Requirements
### Mac OS

Docker is installed and running.

### Lunux/Windows OS

* Docker is installed and running.
* docker-compose is installed and running. 

## pip 

```
pip install subprocess.run
pip install selenium 
```

## Test Run

```
python ui-test.py
```

## Output

```
Creating network "ui_test_default" with the default driver
Creating ui_test_chrome_standalone_1 ... done
test_case_1 (__main__.TestTemplate)
Find and click top-right button ... ok
test_case_2 (__main__.TestTemplate)
Find and click Learn more button ... ok
Removing ui_test_chrome_standalone_1...
removed...

----------------------------------------------------------------------
Ran 2 tests in 15.363s

OK
```
