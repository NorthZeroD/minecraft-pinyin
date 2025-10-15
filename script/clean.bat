@echo off

if exist "download" (
    rd /s /q "download"
)
if exist "output" (
    rd /s /q "output"
)

echo Cleaned up download and output directories.
