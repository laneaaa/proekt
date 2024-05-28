def player_stat(nickname: str, kills: int = 0, deaths: int = 0, supports: int = 0, rounds: int = 0) -> dict:
    diff: int = kills - deaths
    kpr: float = round(kills / rounds, 2)
    apr: float = round(supports / rounds, 2)
    impact: float = round(2.13 * kpr + 0.42 * apr - 0.63, 2)
    dpr: float = round(deaths / rounds, 2)

    try:
        kd: float = round(kills/deaths, 2)
    except ZeroDivisionError:
        kd: float = round(kills / 1, 2)

    rating: float = round(0.39 * kpr - 0.54 * dpr + 0.23 * impact + 0.00034 * 93 * kills, 2)

    return {
            'nickname': nickname,
            'kills': kills,
            'deaths': deaths,
            'kd': kd,
            'diff': diff,
            'dpr': dpr,
            'kpr': kpr,
            'impact': impact,
            'rating': rating
            }
