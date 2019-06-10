
del /F /Q /S  *.pyc *.zip *-*.json

rmdir /Q /S logs

for /R %%s in (__pycache__) do ( 
 rd /s/q %%s
)