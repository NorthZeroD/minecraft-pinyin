#!/bin/bash

find src -type d -name "__pycache__" -exec rm -rf {} +

echo Cleaned up __pycache__ directories.
