# website-v4

> Website powered by [Hugo](https://gohugo.io/), theme forked from [codex](https://github.com/jakewies/hugo-theme-codex)

## Dependencies
- [Python3](https://docs.python-guide.org/starting/install3/linux/)
- [Hugo](https://gohugo.io/getting-started/installing/)

### Setting up Python
you can create a virtual environment using
```
$ python3 -m venv hugo
$ source hugo/bin/activate
```

And install the packages using
```
$ pip install -r requirements.txt
```

### Fetch latest book list
> If you're running this locally, you will need to setup `GOODREADS_KEY` (api key) and `GOODREADS_SECRET` (api secret) environment variables
```
$ export GOODREADS_KEY=XXXXXXXXXXXXXXXXXXXXX
$ export GOODREADS_SECRET=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
$ python scripts/main.py
```

### Running dev server
```
$ hugo server -D
```
