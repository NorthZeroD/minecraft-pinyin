#!/bin/bash

# Recursively find and delete all __pycache__ directories in the src directory
find src -type d -name "__pycache__" -exec rm -rf {} +
