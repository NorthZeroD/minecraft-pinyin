@echo off

for /r "src" %%d in (__pycache__) do (
    if exist "%%d" (
        rmdir /s /q "%%d"
    )
)

echo Cleaned up __pycache__ directories.
