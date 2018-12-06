git rm test*.pdf
git commit -m "remove spectra"
git push

#####Master pull 

git fetch --all
git reset --hard origin/master

