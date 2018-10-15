# shakuyaku-yuri

立てば芍薬座れば牡丹歩く姿は百合の花っていう言葉っぽいのを生成するためのプログラム

ATOKフォーマットの辞書を./setup.shに食べさせてからgenerate345.pyを実行すると何か出てきます．

python3で実行するのを前提としています

## To Run

```
$ nkf --overwrite <oritinal input dictionary> # Convert Shift-JIS to UTF-8
$ ./setup.sh <input dictionary> # Prepare the aux words file
$ python ./generate345.py # run program with Python3
```

## LICENSE

This software is released under the MIT License, see LICENSE.txt.
