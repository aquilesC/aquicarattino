from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

# Source mail address used for notifications.
COMMENTS_XTD_FROM_EMAIL = "noreply@aquicarattino.com"

# Contact mail address to show in messages.
COMMENTS_XTD_CONTACT_EMAIL = "aquiles@aquicarattino.com"

MANAGERS = (
    ('Aquiles Carattino', 'aqui.carattino@gmail.com'),
)