# windows not supported
# need to install gunicorn first: conda/pip
# https://www.linode.com/docs/development/python/flask-and-gunicorn-on-ubuntu/
# https://devcenter.heroku.com/articles/python-gunicorn
# https://martin-thoma.com/flask-gunicorn/
# https://medium.com/ymedialabs-innovation/deploy-flask-app-with-nginx-using-gunicorn-and-supervisor-d7a93aa07c18
# # https://medium.com/faun/deploy-flask-app-with-nginx-using-gunicorn-7fda4f50066a
export CURR_DIR=$(dirname "$0")
export PYTHONPATH=$CURR_DIR/src

gunicorn --bind 0.0.0.0:8080 flask_test_app.gunicorn_main:app
