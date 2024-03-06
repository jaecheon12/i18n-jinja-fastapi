from pytz import timezone
from dotenv import dotenv_values

config = dotenv_values(".env") 

class settings:
    TVCF_SSO_TOKEN_KEY = config["G_TOKEN_KEY"]
    TVCF_SSO_TOKEN_IIS = config["G_TOKEN_IIS"]
    TVCF_SSO_TOKEN_EXP = config["G_TOKEN_EXP"]
    TVCF_SSO_ALGORITHM = "HS256"

    PROJECT_NAME: str = "i18n-jinja-fastapi"
    PROJECT_PORT: int = 8000
    PROJECT_CORS: str = "*"
    
    # tvcf
    # GOOGLE_CLIENT_ID: str = "410389210235-lqtrqbkj2dbunjbk7cvqomf6qabel2kb.apps.googleusercontent.com"
    
    # isinthesky
    GOOGLE_CLIENT_ID: str = config["GOOGLE_OAUTH_CLIENT_ID"]
    GOOGLE_CLIENT_SECRET: str = config["GOOGLE_OAUTH_CLIENT_SECRET"]
    # GOOGLE_REDIRECT_URI: str = "http://localhost:50002/api/v1/auth/callback"
    GOOGLE_REDIRECT_URI: str = config["GOOGLE_OAUTH_REDIRECT_URL"]
    GOOGLE_JWT_ALGORITHM = "RS256"

    ENV_FILE = ".env"
    ENV_FILE_ENCODING = "utf-8"
    
class timezone:
    SEOUL = timezone('Asia/Seoul')
    UTC = timezone('UTC')
    