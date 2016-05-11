echo "Downloading repository"

git clone https://github.com/jmavila/tdd-kata.git

cd tdd

echo "Set up virtualenv"

virtualenv tdd_venv

source tdd_venv/bin/activate

pip install -r requirements.txt

#sudo npm install gulp -g
#sudo npm install gulp-shell

#$1 should be the team number
git branch team_%1
git push --set-upstream origin team_$1