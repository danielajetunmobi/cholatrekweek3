#1
import os
import shutil
current=os.getcwd()
for i in os.listdir(current):
    filename,file_ext=os.path.splitext(i)
    try:
        if not file_ext:
            pass
        elif file_ext in('.py'):
            shutil.move(
                os.path.join(current,f'{filename}{file_ext}'),
                os.path.join(current,'python files', f'{filename}{file_ext}')
            )

        elif file_ext in ('.jpg'):
            shutil.move(
                    os.path.join(current, f'{filename}{file_ext}'),
                    os.path.join(current, 'image files', f'{filename}{file_ext}')
             )
        elif file_ext in('.xlsx,cvs'):
            shutil.move(
                os.path.join(current,f'{filename}{file_ext}'),
                os.path.join(current,'excel files', f'{filename}{file_ext}')
            )
        else:
            shutil.move(
                os.path.join(current, f'{filename}{file_ext}'),
                os.path.join(current, 'other files', f'{filename}{file_ext}')
            )
    except(FileNotFoundError,PermissionError):
        pass
