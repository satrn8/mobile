import pydantic
from appium.options.android import UiAutomator2Options
from typing import Literal, Optional
from dotenv import load_dotenv
import os
from mobile_tests.utils import file

load_dotenv()

EnvContext = Literal['browserstack', 'local']


USER = os.getenv('LOGIN')
KEY = os.getenv('KEY')
APPIUM_BROWSERSTACK = os.getenv('APPIUM_BROWSERSTACK')


class Settings(pydantic.BaseSettings):
    context: EnvContext = 'local'

    platformName: Optional[str] = None
    os_version: Optional[str] = None
    deviceName: Optional[str] = None
    app: Optional[str] = None
    appName: Optional[str] = None
    appWaitActivity: Optional[str] = None
    newCommandTimeout: Optional[int] = 6
    projectName: Optional[str] = None
    buildName: Optional[str] = None
    sessionName: Optional[str] = None
    udid: Optional[str] = None
    remote_url: str = 'http://127.0.0.1:4723/wd/hub'
    timeout: float = 6.0

    @property
    def driver_options(self):
        options = UiAutomator2Options()
        if self.deviceName:
            options.device_name = self.deviceName
        if self.platformName:
            options.platform_name = self.platformName
        options.app = (
            file.abs_path_from_project(self.app)
            if self.app.startswith('./') or self.app.startswith('../')
            else self.app
        )
        options.new_command_timeout = self.newCommandTimeout
        if self.udid:
            options.udid = self.udid
        if self.appWaitActivity:
            options.app_wait_activity = self.appWaitActivity

        return options

    @classmethod
    def in_context(cls, env: Optional[EnvContext] = None) -> 'Settings':
        """
        factory method to init Settings with values from corresponding .env file
        """
        asked_or_current = env or cls().context
        asked_or_current = 'local'
        return cls(
            _env_file=file.abs_path_from_project(f'config.{asked_or_current}.env')
        )


settings = Settings.in_context()