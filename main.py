
import time
import yaml
import sentry_sdk

SENTRY_SDK_URL = ''


def init_sentry():
    sentry_sdk.init(
        SENTRY_SDK_URL,
        traces_sample_rate=1.0
    )


if __name__ == '__main__':

    try:
        with open('config.yml') as file:
            config = yaml.load(file, Loader=yaml.FullLoader)
            print(f"Config loaded: {yaml.dump(config, default_flow_style=False)}")

        if config.get('use_sentry'):
            init_sentry()

    except Exception as ex:
        time.sleep(5)
        raise ex

