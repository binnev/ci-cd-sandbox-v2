# Readme

## Routines 

### mkdocs
Setup: 
```shell
mkdocs new .
```
This will create the `docs` folder

View docs website:
```shell
mkdocs serve 
```

Build: 
```shell
mkdocs build 
```

Deploy to github 
```shell
mkdocs gh-deploy
```
Running this command rebuilds the documentation from your Markdown files and source code and pushes it to the gh-pages branch on your remote GitHub repository.

Because of GitHub’s default configuration, that’ll make your documentation available at the URL that MkDocs shows you at the end of your terminal output:

```shell
INFO - Your documentation should shortly be available at:
       https://user-name.github.io/project-name/
```

## Links 
- https://realpython.com/pypi-publish-python-package/#publish-your-package-to-pypi
- https://realpython.com/python-project-documentation-with-mkdocs