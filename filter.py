from cookiecutter.utils import simple_filter


@simple_filter
def fix_boolean(string) -> bool:
    """Filter to fix boolean variables.

    Cookiecutter's json file allows defining boolean variables, but a bug in v2.1.1 makes those
    variables strings. This filter converts them back to booleans.
    """
    return string.lower() in ["true", "t", "y", "yes", "1"]


