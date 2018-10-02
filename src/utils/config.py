import os

class Config:
    @staticmethod
    def debug():
        """Ativa modo DEBUG"""
        return os.getenv("DEBUG", False)

    @staticmethod
    def timezone():
        """
        Força a aplicação a usar o timezone definido abaixo (ignore o timezone do host)

        Columna "TZ": https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
        """
        return os.getenv("TIMEZONE", "America/Recife")

    @staticmethod
    def sync_interval():
        """Intervalo (segundos) entre sincronização com o db (firebase)"""
        return os.getenv("SYNC_INTERVAL", 300)

    @staticmethod
    def telegram_group_id():
        """Telegram group id"""
        return os.getenv("TELEGRAM_GROUP_ID")

    # Pode ser conseguido conversando com BotFather (https://telegram.me/BotFather):
    # /newbot, /token
    @staticmethod
    def telegram_token():
        """
        Telegram bot token

        Pode ser conseguido conversando com BotFather (https://telegram.me/BotFather): /newbot, /token
        """
        return os.getenv("TELEGRAM_TOKEN")

    @staticmethod
    def firebase_api_key():
        """Firebase information"""
        return os.getenv("FIREBASE_API_KEY")

    @staticmethod
    def firebase_auth_domain():
        """Firebase authentication domain (i.e. "<firebase-project-name>.firebaseapp.com")"""
        return os.getenv("FIREBASE_AUTH_DOMAIN")

    @staticmethod
    def firebase_data_base_url():
        """Firebase database url (i.e. "https://<firebase-project-name>.firebaseio.com")"""
        return os.getenv("FIREBASE_DATA_BASE_URL")

    @staticmethod
    def firebase_storage_bucket():
        """Firebase storage bucket url (i.e. "<firebase-project-name>.appspot.com")"""
        return os.getenv("FIREBASE_STORAGE_BUCKET")

    @staticmethod
    def firebase_service_account():
        return os.getenv("FIREBASE_SERVICE_ACCOUNT")

    @staticmethod
    def master_admin_telegram_id():
        """O bot sempre vai permitir os comandos desse usuário"""
        return os.getenv("MASTER_ADMIN_TELEGRAM_ID")

    @staticmethod
    def racha_complete_teams_with_fake_players():
        """Quando /times for executado, o bot vai colocar jogadores fakes até completar os times"""
        return os.getenv("RACHA_COMPLETE_TEAMS_WITH_FAKE_PLAYERS", True)

    @staticmethod
    def racha_max_teams():
        """Número máximo de times (minimo sempre é 2)"""
        return os.getenv("RACHA_MAX_TEAMS", 4)

    @staticmethod
    def racha_max_number_players_team():
        """Número de jogadores por time"""
        return os.getenv("RACHA_MAX_NUMBER_PLAYERS_TEAM", 6)

    @staticmethod
    def racha_teams_colors():
        """Cores usadas nos times"""
        return os.getenv("RACHA_TEAMS_COLORS", "Azul,Vermelho,Verde,Branco")

    @staticmethod
    def racha_default_rating():
        """Se jogador não tiver rating, bot usa DEFAULT_RATING"""
        return os.getenv("RACHA_DEFAULT_RATING", 3.00)

    @staticmethod
    def racha_rating_range_variation_min():
        """Quando o bot calcula os times, para cada jogador um número entre o [RACHA_RATING_RANGE_VARIATION_MIN, RACHA_RATING_RANGE_VARIATION_MAX] é somado ao rating do jogador"""
        return os.getenv("RACHA_RATING_RANGE_VARIATION_MIN", -0.25)

    @staticmethod
    def racha_rating_range_variation_max():
        """Quando o bot calcula os times, para cada jogador um número entre o [RACHA_RATING_RANGE_VARIATION_MIN, RACHA_RATING_RANGE_VARIATION_MAX] é somado ao rating do jogador"""
        return os.getenv("RACHA_RATING_RANGE_VARIATION_MAX", 0.25)

    @staticmethod
    def racha_hide_subscriber_label():
        """Escode (M) depois do nome do jogador"""
        return os.getenv("RACHA_HIDE_SUBSCRIBER_LABEL", False)

    @staticmethod
    def racha_hide_guest_label():
        """Esconde (C) depois do nome do jogador"""
        return os.getenv("RACHA_HIDE_GUEST_LABEL", False)

    @staticmethod
    def racha_has_substitutes_list():
        """Mostra lista de jogadores substitutos quando usar o comando /times"""
        return os.getenv("RACHA_HAS_SUBSTITUTES_LIST", False)

    @staticmethod
    def racha_open_check_in_date():
        """Se OPEN_CHECK_IN_DATE for definido, o bot irá automaticamente abrir o check in do racha"""
        return os.getenv("RACHA_OPEN_CHECK_IN_DATE", "monday 20:00")

    @staticmethod
    def racha_close_check_in_date():
        """Se CLOSE_CHECK_IN_DATE for definido, o bot irá automaticamente fechar o check in do racha"""
        return os.getenv("RACHA_CLOSE_CHECK_IN_DATE", "tuesday 15:00")
