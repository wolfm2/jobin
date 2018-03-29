#!/bin/bash

C=0

mkdir -p info haardata

for p in pos/*; do
  d=info/$C
  opencv_createsamples -img $p -bg bg.txt -info $d/info.lst -pngoutput $d -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 20 \;
  sed -i -e "s/^/info\/$C\//" $d/info.lst
  C=$((C + 1))
done

cat info/*/info.lst > infoPsudoPos.txt

echo Verified Files: `find info/* -name *.jpg | wc -l`
echo Verified Lines: `wc -l infoPsudoPos.txt`

# rm haardata/*.xml
# opencv_createsamples-info info.txt -w 20 -h 20 -vec pos.vec -num 101 # might up this to 25x25 but increases work exponentially
# opencv_traincascade -data haarData -vec pos.vec -bg bg.txt -numPos 101, -numNeg 6657 -numStages 10 -w 20 -h 20

