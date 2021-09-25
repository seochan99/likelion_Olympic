from pathlib import Path
import os

STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'blog','static')]
#현재 static 파일들이 어디에 있는지

STATIC_ROOT = os.path.join(BASE_DIR, 'static')