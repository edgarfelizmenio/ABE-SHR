#! /bin/bash -x

apt-get -y -q update
apt-get -y -q upgrade
apt-get -y -q install htop
apt-get -y -q install build-essential
apt-get -y -q install git
apt-get -y -q install vim

apt-get -y -q install python python-dev
apt-get -y -q install python-pip

apt-get -y -q install libssl-dev libffi-dev python3-dev
apt-get -y -q install python3-pip
apt-get -y -q install python3.4-venv

apt-get -y -q install nginx

debconf-set-selections <<< 'mysql-server-5.6 mysql-server/root_password password password'
debconf-set-selections <<< 'mysql-server-5.6 mysql-server/root_password_again password password'
apt-get -y -q install mysql-server-5.6 mysql-client-5.6

cd /home/ABE-SHR

mysql --user=root --password=password --execute="CREATE DATABASE raw_shr"
mysql --user=root --password=password raw_shr --execute="source empty_shr.sql"

pyvenv-3.4 env
source env/bin/activate
pip3 install --upgrade pip

pip3 install -r requirements.txt

# install gunicorn
# pip3 install gunicorn

# install and enable nginx
# cp nginx/source-shr /etc/nginx/sites-available/source-shr
# ln -s /etc/nginx/sites-available/source-shr /etc/nginx/sites-enabled/source-shr
# sudo service nginx restart

# start the mediator
# cp upstart/source-shr.conf /etc/init/source-shr.conf
# sudo service source-shr start