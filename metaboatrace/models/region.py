from enum import Enum


class Prefecture(Enum):
    HOKKAIDO = 1
    AOMORI = 2
    IWATE = 3
    MIYAGI = 4
    AKITA = 5
    YAMAGATA = 6
    FUKUSHIMA = 7
    IBARAKI = 8
    TOCHIGI = 9
    GUNMA = 10
    SAITAMA = 11
    CHIBA = 12
    TOKYO = 13
    KANAGAWA = 14
    NIIGATA = 15
    TOYAMA = 16
    ISHIKAWA = 17
    FUKUI = 18
    YAMANASHI = 19
    NAGANO = 20
    GIFU = 21
    SHIZUOKA = 22
    AICHI = 23
    MIE = 24
    SHIGA = 25
    KYOTO = 26
    OSAKA = 27
    HYOGO = 28
    NARA = 29
    WAKAYAMA = 30
    TOTTORI = 31
    SHIMANE = 32
    OKAYAMA = 33
    HIROSHIMA = 34
    YAMAGUCHI = 35
    TOKUSHIMA = 36
    KAGAWA = 37
    EHIME = 38
    KOCHI = 39
    FUKUOKA = 40
    SAGA = 41
    NAGASAKI = 42
    KUMAMOTO = 43
    OITA = 44
    MIYAZAKI = 45
    KAGOSHIMA = 46
    OKINAWA = 47


class Branch(Enum):
    GUNMA = 10
    SAITAMA = 11
    TOKYO = 13
    FUKUI = 18
    SHIZUOKA = 22
    AICHI = 23
    MIE = 24
    SHIGA = 25
    OSAKA = 27
    HYOGO = 28
    OKAYAMA = 33
    HIROSHIMA = 34
    YAMAGUCHI = 35
    TOKUSHIMA = 36
    KAGAWA = 37
    FUKUOKA = 40
    SAGA = 41
    NAGASAKI = 42


class PrefectureFactory:
    @staticmethod
    def create(name: str) -> Prefecture:
        if "北海道" in name:
            return Prefecture.HOKKAIDO
        if "青森" in name:
            return Prefecture.AOMORI
        if "岩手" in name:
            return Prefecture.IWATE
        if "宮城" in name:
            return Prefecture.MIYAGI
        if "秋田" in name:
            return Prefecture.AKITA
        if "山形" in name:
            return Prefecture.YAMAGATA
        if "福島" in name:
            return Prefecture.FUKUSHIMA
        if "茨城" in name:
            return Prefecture.IBARAKI
        if "栃木" in name:
            return Prefecture.TOCHIGI
        if "群馬" in name:
            return Prefecture.GUNMA
        if "埼玉" in name:
            return Prefecture.SAITAMA
        if "千葉" in name:
            return Prefecture.CHIBA
        if "東京" in name:
            return Prefecture.TOKYO
        if "神奈川" in name:
            return Prefecture.KANAGAWA
        if "新潟" in name:
            return Prefecture.NIIGATA
        if "富山" in name:
            return Prefecture.TOYAMA
        if "石川" in name:
            return Prefecture.ISHIKAWA
        if "福井" in name:
            return Prefecture.FUKUI
        if "山梨" in name:
            return Prefecture.YAMANASHI
        if "長野" in name:
            return Prefecture.NAGANO
        if "岐阜" in name:
            return Prefecture.GIFU
        if "静岡" in name:
            return Prefecture.SHIZUOKA
        if "愛知" in name:
            return Prefecture.AICHI
        if "三重" in name:
            return Prefecture.MIE
        if "滋賀" in name:
            return Prefecture.SHIGA
        if "京都" in name:
            return Prefecture.KYOTO
        if "大阪" in name:
            return Prefecture.OSAKA
        if "兵庫" in name:
            return Prefecture.HYOGO
        if "奈良" in name:
            return Prefecture.NARA
        if "和歌山" in name:
            return Prefecture.WAKAYAMA
        if "鳥取" in name:
            return Prefecture.TOTTORI
        if "島根" in name:
            return Prefecture.SHIMANE
        if "岡山" in name:
            return Prefecture.OKAYAMA
        if "広島" in name:
            return Prefecture.HIROSHIMA
        if "山口" in name:
            return Prefecture.YAMAGUCHI
        if "徳島" in name:
            return Prefecture.TOKUSHIMA
        if "香川" in name:
            return Prefecture.KAGAWA
        if "愛媛" in name:
            return Prefecture.EHIME
        if "高知" in name:
            return Prefecture.KOCHI
        if "福岡" in name:
            return Prefecture.FUKUOKA
        if "佐賀" in name:
            return Prefecture.SAGA
        if "長崎" in name:
            return Prefecture.NAGASAKI
        if "熊本" in name:
            return Prefecture.KUMAMOTO
        if "大分" in name:
            return Prefecture.OITA
        if "宮崎" in name:
            return Prefecture.MIYAZAKI
        if "鹿児島" in name:
            return Prefecture.KAGOSHIMA
        if "沖縄" in name:
            return Prefecture.OKINAWA
        raise ValueError


class BranchFactory:
    @staticmethod
    def create(name: str) -> Branch:
        if "群馬" in name:
            return Branch.GUNMA
        if "埼玉" in name:
            return Branch.SAITAMA
        if "東京" in name:
            return Branch.TOKYO
        if "福井" in name:
            return Branch.FUKUI
        if "静岡" in name:
            return Branch.SHIZUOKA
        if "愛知" in name:
            return Branch.AICHI
        if "三重" in name:
            return Branch.MIE
        if "滋賀" in name:
            return Branch.SHIGA
        if "大阪" in name:
            return Branch.OSAKA
        if "兵庫" in name:
            return Branch.HYOGO
        if "岡山" in name:
            return Branch.OKAYAMA
        if "広島" in name:
            return Branch.HIROSHIMA
        if "山口" in name:
            return Branch.YAMAGUCHI
        if "徳島" in name:
            return Branch.TOKUSHIMA
        if "香川" in name:
            return Branch.KAGAWA
        if "福岡" in name:
            return Branch.FUKUOKA
        if "佐賀" in name:
            return Branch.SAGA
        if "長崎" in name:
            return Branch.NAGASAKI
        raise ValueError
