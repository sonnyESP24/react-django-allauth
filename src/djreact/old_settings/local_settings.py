import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# This is for prod:
# WEBPACK_LOADER = {
#     'DEFAULT': {
#         'BUNDLE_DIR_NAME': 'bundles/prod/',  # end with slash
#         'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats-prod.json'),
#     }
# }

# This is for stage:
# WEBPACK_LOADER = {
#     'DEFAULT': {
#         'BUNDLE_DIR_NAME': 'bundles/stage/',  # end with slash
#         'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats-stage.json'),
#     }
# }

# This is for local development
WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/local/',  # end with slash
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats-local.json'),
    }
}
