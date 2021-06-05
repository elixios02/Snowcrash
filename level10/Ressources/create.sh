#!/bin/sh

while true
do
        touch /tmp/tokken
        ln -sf ~/token /tmp/tokken
        rm -rf /tmp/tokken 
done 
