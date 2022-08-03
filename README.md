# Essence of Machine Learning 1st Edition

Managing some code and Dockerfile

You can use this environment by executing the commands below.
```bash
git clone http://github.com/Aconitum3/EoML.git
cd EoML
docker-compose up
docker-compose exec eoml bash

# if you want to use jupyter-lab, you need execute additional command.
jupyter lab --ip=0.0.0.0 --port=8888 --allow-root --no-browser
``` 

If you want to manage .ipynb files, edit .gitiginore. 
