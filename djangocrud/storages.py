from whitenoise.storage import CompressedManifestStaticFilesStorage


class SilentCollectstaticStorage(CompressedManifestStaticFilesStorage):
    """
    Igual que CompressedManifestStaticFilesStorage, pero no truena
    el collectstatic cuando encuentra referencias a archivos que
    no puede resolver (ej. los locales de i18n de select2 en el
    admin de Django). Los archivos reales se siguen sirviendo bien.
    """
    manifest_strict = False