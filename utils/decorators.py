import os
import functools


def capture_screenshot_on_fail(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        driver = args[0].driver if hasattr(args[0], "driver") else None

        try:
            return func(*args, **kwargs)

        except Exception as e:

            if driver:
                os.makedirs("output/screenshots", exist_ok=True)
                driver.save_screenshot(
                    f"output/screenshots/{func.__name__}.png"
                )

            raise e

    return wrapper