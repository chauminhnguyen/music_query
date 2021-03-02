# Music Query

This music query has 3 parts:

* Music Query
* Lyric Query
* Keyword Query

## Report

Our report is below:

[Report](Report.pdf)


## Pre Proccessing

Prepare musics + images(albums) + lyrics path.

**NOTES:**
* Images: Put in ./static/ images/ path.
* All of musics, images, lyrics of 1 song must have same name.

## 1. Activate environment

    ./env/Scripts/activate

## 2. Create necessary file

* Create musics model:

      python build_model.py --data-dir"./data"

      --data-dir: directory of music with .mp3/wav extension.

* Create lyrics model:

      python ./utils/lyrics_inverted_file.py

* Create song keyword model:

      python ./utils/create_songs_db.py

    
## 3. Run music query's website

    python app.py
    
