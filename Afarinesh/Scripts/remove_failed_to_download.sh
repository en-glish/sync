#/bin/sh
cd Afarinesh
for i in $(ls -d */); do
    cd $i
    echo "----------------------- FOLDER $i -----------------------"
    ls | grep aria2 | xargs --replace={} basename {} '.aria2' >tmp.txt
    input="tmp.txt"
    while IFS= read -r line; do
        echo "$line"
        rm "$line"
    done <"$input"
    ls | grep aria2 | xargs -I{} rm {}
    cd ..
done
