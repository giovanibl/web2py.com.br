# -*- coding: utf-8 -*-

def get_last_version():
    try:
        import urllib

        #TODO armazenar em cache?
        f = urllib.urlopen("http://web2py.com/examples/default/version")
        v = f.read()
        v = dict(version = v[8:14], datetime = v[15:])
        f.close()
    except:
        v = dict(version = 'erro ao obter versão', datetime = 'erro ao obter data versão')
    return v

