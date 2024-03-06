import gettext
import os

def get_gettext_translations(locale):
    locales_dir = os.path.join(os.path.dirname(__file__), 'locales')
    try:
        # 찾기 함수를 사용하여 로케일에 대한 .mo 파일 경로를 찾습니다.
        lang_path = gettext.find('base', localedir=locales_dir, languages=[locale])
        # 번역 객체 생성
        translations = gettext.translation('base', localedir=locales_dir, languages=[locale], fallback=True)
    except Exception as e:
        print(f"Error loading translations for {locale}: {e}")
        translations = gettext.NullTranslations()
    return translations