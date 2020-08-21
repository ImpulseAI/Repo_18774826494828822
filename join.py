
import os
import zipfile
def join(files, dest_file):
    output_file = open(dest_file, 'wb')
    for file in files:
        print('Joining',file,'...')
        input_file = open(file, 'rb')
        while True:
            byte = input_file.read(100000)
            if not byte:
                break
            output_file.write(byte)
        input_file.close()
    output_file.close()
    for file in files:
        print('Removing',file,'...')
        os.remove(file)
join(['yyumv.zip.000.NOTES', 'yyumv.zip.001.NOTES', 'yyumv.zip.002.NOTES', 'yyumv.zip.003.NOTES', 'yyumv.zip.004.NOTES', 'yyumv.zip.005.NOTES', 'yyumv.zip.006.NOTES', 'yyumv.zip.007.NOTES', 'yyumv.zip.008.NOTES', 'yyumv.zip.009.NOTES', 'yyumv.zip.010.NOTES', 'yyumv.zip.011.NOTES', 'yyumv.zip.012.NOTES', 'yyumv.zip.013.NOTES', 'yyumv.zip.014.NOTES', 'yyumv.zip.015.NOTES', 'yyumv.zip.016.NOTES', 'yyumv.zip.017.NOTES', 'yyumv.zip.018.NOTES', 'yyumv.zip.019.NOTES', 'yyumv.zip.020.NOTES', 'yyumv.zip.021.NOTES', 'yyumv.zip.022.NOTES', 'yyumv.zip.023.NOTES', 'yyumv.zip.024.NOTES', 'yyumv.zip.025.NOTES', 'yyumv.zip.026.NOTES', 'yyumv.zip.027.NOTES'],'yyumv.zip')
print('unziping')
with zipfile.ZipFile('yyumv.zip', 'r') as zip_ref:
    zip_ref.extractall('yyumv')
os.remove('yyumv.zip')
os.remove('join.py')
