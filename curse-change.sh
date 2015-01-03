#!/bin/bash

S1="$(stat -c %Y /home/$USER/.wine/drive_c/Program\ Files\ \(x86\)/World\ of\ Warcraft/addons.csv)"
S2="$(cat /home/$USER/temp/filechanged.txt)"

if [ "$S1" -eq "$S2" ] ;
then
    echo "Nothing to update"
else
    echo "Updating..."
    /bin/bash -c "cd /home/$USER/.wine/drive_c/Program\ Files\ \(x86\)/World\ of\ Warcraft && python /home/$USER/bin/curse.py"
fi
S3="$(stat -c %Y /home/$USER/.wine/drive_c/Program\ Files\ \(x86\)/World\ of\ Warcraft/addons.csv)"
echo $S3>/home/$USER/temp/filechanged.txt

