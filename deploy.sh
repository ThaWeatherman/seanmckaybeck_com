echo Making html...
make html
echo Deploying to server. Have password ready
rsync -av output/ root@107.170.239.239:/var/www/pelican/output
echo Deployed.
