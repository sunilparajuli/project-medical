import environ

env = environ.Env()

# Load .env file
environ.Env.read_env()

def get_config(type):
    if type == 'demo':
        config = {
            'base_uri': env.str('DEMO_BASE_URI'),
            'remote-user': env.str('DEMO_REMOTE_USER'),
            'auth': env.str('DEMO_AUTH'),
            'patient': env.str('DEMO_PATIENT'),
            'enterer': env.str('DEMO_ENTERER'),
            'facility': env.str('DEMO_FACILITY'),
            'provider': env.str('DEMO_PROVIDER')
        }
    else:
        config = {
            'base_uri': env.str('OPEN_BASE_URI'),
            'remote-user': env.str('OPEN_REMOTE_USER'),
            'auth': env.str('OPEN_AUTH'),
            'patient': env.str('OPEN_PATIENT'),
            'enterer': env.str('OPEN_ENTERER'),
            'facility': env.str('OPEN_FACILITY'),
            'provider': env.str('OPEN_PROVIDER')
        }
    print("config", config)
    return config
