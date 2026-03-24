## Test layout

https://docs.pytest.org/en/latest/explanation/goodpractices.html#which-import-mode

## Dev build n test

Map sources and build while testing
```bash
pip install --editable .
pytest
```
Another way is to directly test the sources
```
PYTHONPATH=./src pytest
```