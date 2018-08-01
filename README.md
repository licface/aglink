aglink
-------------
AutoGenerateLink CLI

usage
-----------

      usage: agl.py [-h] [-c] [-N NUMBER] [-n NAME] [-d] [-s] [-f] [-v]
                    [-X [PROXY [PROXY ...]]] [-p PATH] [-i] [--pcloud]
                    [--pcloud-username PCLOUD_USERNAME]
                    [--pcloud-password PCLOUD_PASSWORD]
                    [--pcloud-folderid PCLOUD_FOLDERID]
                    [--pcloud-renameit PCLOUD_RENAMEIT]
                    [--pcloud-foldername PCLOUD_FOLDERNAME]
                    LINK

      positional arguments:
        LINK                  Link to be convert

      optional arguments:
        -h, --help            show this help message and exit
        -c, --clip            Copy converted links to Clipboard
        -N NUMBER, --number NUMBER
                              Number of Quality video download to
        -n NAME, --name NAME  Name of video download to
        -d, --download        Direct download
        -s, --support         Show support text
        -f, --fast            Fast, no check
        -v, --verbose         -v = version | -vv = Verbosity
        -X [PROXY [PROXY ...]], --proxy [PROXY [PROXY ...]]
                              Set Proxy, format example http://127.0.0.1:8118
                              https://127.0.0.1:3128
        -p PATH, --path PATH  Download Path default this
        -i, --wget            Direct use wget (build in) for download manager
        --pcloud              Remote Upload to Pcloud Storage
        --pcloud-username PCLOUD_USERNAME
                              Username of Remote Upload to Pcloud Storage
        --pcloud-password PCLOUD_PASSWORD
                              Password of Remote Upload to Pcloud Storage
        --pcloud-folderid PCLOUD_FOLDERID
                              Folder ID Remote Upload to Pcloud Storage, default=0
        --pcloud-renameit PCLOUD_RENAMEIT
                              Rename After of Remote Upload to Pcloud Storage
        --pcloud-foldername PCLOUD_FOLDERNAME
                              Folder of Remote Upload to Pcloud Storage to
                              
debug
-----------
set system environment DEBUG=1 to show debug process

author
--------
[licface](mailto:licface@yahoo.com)

