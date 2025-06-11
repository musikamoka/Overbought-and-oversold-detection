from .en import text  # 默认使用english

def get_lang(language):
    if language == "en":
        from .en import text as t
        return t
    else:
        from .zh import text as t
        return t
