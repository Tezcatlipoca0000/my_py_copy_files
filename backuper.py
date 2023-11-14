import shutil
import os
import tqdm

db_route = r'C:\Program Files (x86)\AbarrotesPDV\db\PDVDATA.FDB'
xl_route = r'C:\Users\casa\Desktop\Provedores Todos.xlsm'
disc_route = 'D:\\'

print('Buscando el disco USB...')
try:
    free = shutil.disk_usage(disc_route).free
except Exception as e:
    print('Error con usb ---> ', e)
    quit()
if free < 1000000000:
    print('Menos de 1GB de memoria en el disco USB. Respaldo cancelado')
    quit()
else:
    print('Comenzando a respaldar los datos, espere por favor...')
    db_size = os.path.getsize(db_route)
    xl_size = os.path.getsize(xl_route)
    total_size = db_size + xl_size
    with tqdm.tqdm(total=total_size) as pbar:
        with open(db_route, "rb") as fsrc:
            with open(disc_route + "/PDVDATA.FDB", "wb") as fdst:
                for chunk in iter(lambda: fsrc.read(1024), b""):
                    fdst.write(chunk)
                    copied_bytes = len(chunk)
                    pbar.update(copied_bytes)
        with open(xl_route, "rb") as fsrc:
            with open(disc_route + "/Provedores Todos.xlsm", "wb") as fdst:
                for chunk in iter(lambda: fsrc.read(1024), b""):
                    fdst.write(chunk)
                    copied_bytes = len(chunk)
                    pbar.update(copied_bytes)
    print('Respaldo Completado')
