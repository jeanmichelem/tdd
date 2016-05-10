echo "Downloading repository"

git clone https://github.com/jeanmichelem/tdd.git

cd tdd

virtualenv tdd_venv

source tdd_venv/bin/activate

pip install -r requirements.txt


npm install grunt-cli -g
npm install grunt
npm install grunt-contrib-watch
npm install grunt-shell

sudo npm install gulp -g
sudo npm install gulp-shell

#$1 should be the team number
git branch team_%1
git push --set-upstream origin team_$1