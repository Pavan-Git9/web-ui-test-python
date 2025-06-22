# petfinder-api-test-python

run with `pytest -s --html=reports/report.html`

## cross-site compatible installation

pip install webdriver-manager

pip install selenium webdriver-manager

run with `pytest --browser edge --html=reports/report.html`

## parallel test

pip install pytest-xdist

run with `pytest -n auto`