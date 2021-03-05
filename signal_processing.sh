#! /bin/bash

c=10; while [ $c -ge 0 ]; do espeak $c; let c--; done; sleep 1 ## here lengthy code
espeak "We are done with counting"
