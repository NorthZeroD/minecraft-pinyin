#!/bin/bash

if [ -d "download" ]; then
    rm -r download
fi
if [ -d "output" ]; then
    rm -r output
fi

echo Cleaned up download and output directories.
