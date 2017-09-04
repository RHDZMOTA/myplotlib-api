import datetime
from os import environ, pardir
from os.path import join, dirname, abspath


DEBUG = True

PROJECT_DIR = abspath(join(dirname(__file__), pardir))
TEMPLATE_DIRS = join(PROJECT_DIR, 'templates')
STATIC_DIRS = join(PROJECT_DIR, 'static')
ASSETS_DIRS = join(PROJECT_DIR, 'assets')

GENERIC_SCATTER = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '_scatterplot.png'

TZ = 'UTC'


class FilesConf:

    class Paths:
        static = STATIC_DIRS
        assets = ASSETS_DIRS

    class FileNames:
        generic_scatterplot = join(PROJECT_DIR, GENERIC_SCATTER)


SERVICES = {
    'default': 8000,
    'static': 8001
}


def init_app(app):
    gae_instance = environ.get('GAE_INSTANCE', environ.get('GAE_MODULE_INSTANCE'))
    environment = 'production' if gae_instance is not None else 'development'
    app.config['SERVICE_MAP'] = map_services(environment)


def map_services(environment):
    url_map = {}
    for service, local_port in SERVICES.items():
        if environment == 'production':
            url_map[service] = production_url(service)
        if environment == 'development':
            url_map[service] = local_url(local_port)
    return url_map


def production_url(service_name):
    project_id = environ.get('GAE_LONG_APP_ID')
    project_url = project_id + '.appspot.com'
    if service_name == 'default':
        return 'https://' + project_url
    else:
        return 'https://' + service_name + '-dot-{}' + project_url


def local_url(port):
    return 'http://localhost:' + str(port)

