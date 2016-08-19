from fabric.contrib.files import append, exists, sed
from fabric.api import env, run, local
import random

REPO_URL = 'https://github.com/djangoStudyTeam/DjangoBlog.git'


def _create_directory_structure_if_necessary(site_folder):
    run('mkdir -p %s/%s' % (site_folder, 'env'))
    run('mkdir -p %s/%s' % (site_folder, 'source'))
    for sub_folder in ('source/weblog/database', 'source/weblog/static'):
        run('mkdir -p %s/%s' % (site_folder, sub_folder))


def _get_latest_source(source_folder):
    if exists(source_folder + '/.git'):
        run('cd %s && git fetch' % (source_folder,))
    else:
        run('git clone %s %s' % (REPO_URL, source_folder))
    current_commit = local('git log -n 1 --format=%H', capture=True)
    run('cd %s && git reset --hard %s && git checkout blog-tutorial' % (source_folder, current_commit))


def _update_virtualenv(source_folder):
    virtualenv_folder = source_folder + '/../env'
    if not exists(virtualenv_folder + '/bin/pip'):
        run('virtualenv --python=python3 %s' % (virtualenv_folder,))
    run('%s/bin/pip install -r %s/requirements.txt' %
        (virtualenv_folder, source_folder))


def _update_static_files(source_folder):
    run('cd %s && ../virtualenv/bin/python3 manage.py collectstatic --noinput' %
        (source_folder,))


def _update_database(source_folder):
    run('cd %s && ../virtualenv/bin/python3 manage.py makemigrations' %
        (source_folder,))
    run('cd %s && ../virtualenv/bin/python3 manage.py migrate --noinput' %
        (source_folder,))


def _update_settings(source_folder, site_name):
    setting_path = ''
    sed(setting_path, "DEBUG = True", "DEBUG = False")
    sed(
        setting_path,
        "ALLOWED_HOSTS = .+$",
        "ALLOWED_HOSTS = ['%s']" % site_name,
    )
    secret_key_file = source_folder + ''
    if not exists(secret_key_file):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))
        append(secret_key_file, "SECRET_KEY = '%s'" % key)
    append(setting_path, '\nfrom .secret_key import SECRET_KEY')
