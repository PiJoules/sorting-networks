# Validating Sorting Networks
Implementation of the /r/dailyprogrammer challenge of the day: https://www.reddit.com/r/dailyprogrammer/comments/36m83a/20150520_challenge_215_intermediate_validating/

The main script for checking whether or not a network is valid is in `valid_sorting_network.py`.

The script can be run either through the testbench or on a Flask server. The testbench reads from stdin. Samples from the `samples` dir can be piped to `testbench.py` to test a network.

An interface for testing networks can be found at http://isvalidsn.appspot.com/

## Running the testbench
```sh
$ cat samples/sample.txt | python testbench.py
wire count:  4
comparators (as json string):  [["0", "2"], ["1", "3"], ["0", "1"], ["2", "3"], ["1", "2"]]
Valid Network
$ cat samples/sample2.txt | python testbench.py
wire count:  8
comparators (as json string):  [["0", "2"], ["1", "3"], ["0", "1"], ["2", "3"], ["1", "2"], ["4", "6"], ["5", "7"], ["4", "5"], ["6", "7"], ["5", "6"], ["0", "4"], ["1", "5"], ["2", "6"], ["3", "7"], ["2", "4"], ["3", "5"], ["1", "2"], ["3", "4"], ["6", "7"]]
Invalid Network
$ cat samples/sample3.txt | python testbench.py
wire count:  16
comparators (as json string):  [["0", "1"], ["2", "3"], ["4", "5"], ["6", "7"], ["8", "9"], ["10", "11"], ["12", "13"], ["14", "15"], ["0", "2"], ["1", "3"], ["4", "6"], ["5", "7"], ["8", "10"], ["9", "11"], ["12", "14"], ["13", "15"], ["0", "4"], ["1", "5"], ["2", "6"], ["3", "7"], ["8", "12"], ["9", "13"], ["10", "14"], ["11", "15"], ["0", "8"], ["1", "9"], ["2", "10"], ["3", "11"], ["4", "12"], ["5", "13"], ["6", "14"], ["7", "15"], ["5", "10"], ["6", "9"], ["3", "12"], ["7", "11"], ["13", "14"], ["1", "2"], ["4", "8"], ["1", "4"], ["7", "13"], ["2", "8"], ["11", "14"], ["2", "4"], ["5", "6"], ["9", "10"], ["11", "13"], ["3", "8"], ["7", "12"], ["6", "8"], ["3", "5"], ["7", "9"], ["10", "12"], ["3", "4"], ["5", "6"], ["7", "8"], ["9", "10"], ["11", "12"], ["6", "7"], ["12", "13"]]
Invalid Network
$ cat samples/sample4.txt | python testbench.py
wire count:  16
comparators (as json string):  [["0", "1"], ["2", "3"], ["4", "5"], ["6", "7"], ["8", "9"], ["10", "11"], ["12", "13"], ["14", "15"], ["0", "2"], ["1", "3"], ["4", "6"], ["5", "7"], ["8", "10"], ["9", "11"], ["12", "14"], ["13", "15"], ["0", "4"], ["1", "5"], ["2", "6"], ["3", "7"], ["8", "12"], ["9", "13"], ["10", "14"], ["11", "15"], ["0", "8"], ["1", "9"], ["2", "10"], ["3", "11"], ["4", "12"], ["5", "13"], ["6", "14"], ["7", "15"], ["5", "10"], ["6", "9"], ["3", "12"], ["7", "11"], ["13", "14"], ["1", "2"], ["4", "8"], ["1", "4"], ["7", "13"], ["2", "8"], ["11", "14"], ["2", "4"], ["5", "6"], ["9", "10"], ["11", "13"], ["3", "8"], ["7", "12"], ["6", "8"], ["3", "5"], ["7", "9"], ["10", "12"], ["3", "4"], ["5", "6"], ["7", "8"], ["9", "10"], ["11", "12"], ["6", "7"], ["8", "9"]]
Valid Network
```

## Running the Flask server
Running the Flask server requires `pip` and the [Google App Engine SDK for Python](https://cloud.google.com/appengine/downloads).

1) Run `setup.sh` to install the python dependencies via pip
```sh
$ source setup.sh
```

2) Start the dev server
```sh
$ dev_appserver.py .
```

3) Go to `localhost:8080` in a browser to view the interface

## Contributing
1. Fork it!
2. Create your feature branch: git checkout -b my-new-feature
3. Commit your changes: git commit -am 'Add some feature'
4. Push to the branch: git push origin my-new-feature
5. Submit a pull request :D

## Licensing
See [LICENSE](/LICENSE)

## Author
[Le]o