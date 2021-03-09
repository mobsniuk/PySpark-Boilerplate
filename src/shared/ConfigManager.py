from configparser import ConfigParser, ExtendedInterpolation


def getConfig(**job_args):
    """
    Create a config object using the path defined job_args with the 'conf' keyword.
    :param job_args: job arguments
    :return: config object
    """
    print(job_args)
    conf_file = job_args['conf']

    config = ConfigParser(interpolation=ExtendedInterpolation())
    config.read(conf_file)
    return config
