import pandas as pd


def weather(day, month, year):
    df_weather = pd.read_csv("saa_seinajoki.csv")
    year_filtered = df_weather["Vuosi"] == year
    month_filtered = df_weather["Kuukausi"] == month
    day_filtered = df_weather["Päivä"] == day

    df_filtered = df_weather[year_filtered & month_filtered & day_filtered]

    rain = df_filtered["Sademäärä [mm]"].values[0]
    warmth = df_filtered["Ilman keskilämpötila [°C]"].values[0]

    # Sademäärä -1 tarkoittaa, että ei satanut ollenkaan
    # Sademäärä 0 tarkoittaa, että satoi alle 0,1 mm

    # Näissä lähteenä Ilmatieteen laitoksen sivuilta löytyvät määritelmät
    rain_text = ""
    if rain < 0.3:
        rain_text = "ja sää oli poutainen. "
    elif rain <= 0.9:
        rain_text = "ja päivä aikana satoi vähän. "
    elif rain <= 4.4:
        rain_text = "ja päivä oli sateinen. "
    else:
        rain_text = "ja päivän aikana satoi runsaasti. "

    warmth_text = "Päivän keskilämpötila oli Seinäjoella " + str(warmth) + \
                  " astetta "

    return [rain_text, warmth_text]


def weekday(timestamp):
    weekdays = {0: "maanantai",
                1: "tiistai",
                2: "keskiviikko",
                3: "torstai",
                4: "perjantai",
                5: "lauantai",
                6: "sunnuntai"}

    weekday_number = timestamp.weekday()
    weekday_text = "Päivä, jona synnyit, oli " + weekdays[weekday_number] \
                   + ". "

    return weekday_text


def population(year):

    population_text = ""

    if year >= 1987:
        df_population = pd.read_csv("vakiluku_sjoki.csv")

        value = df_population.loc[0, str(year)]

        population_text = "Vuonna " + str(year) + " Seinäjoen väkiluku oli " \
                          + str(value) + ". "

    return population_text


def song(timestamp):
    week = timestamp.isocalendar().week
    year = timestamp.isocalendar().year

    song_text = ""

    if 1994 <= year <= 2019:
        df_songs = pd.read_csv("suomi_singlelista_yksi_1994-2019.csv")
        year_filtered = df_songs["Vuosi"] == year
        week_filtered = df_songs["Viikko"] == week
        df_filtered = df_songs[year_filtered & week_filtered]

        single = df_filtered["Single"].values[0]
        artist = df_filtered["Artisti"].values[0]

        song_text = "Suomen singlelistan kärjessä oli kyseisellä viikolla " \
                    "artistin " + artist + " kappale " + single + ". "

    return song_text


def history(year):
    history_text1 = ""

    if year == 1960:
        history_text1 = "Seinäjoki sai kaupunkioikeudet synnyinvuonnasi 1960. "
    elif year == 1961:
        history_text1 = "Seinäjoki sai kaupunkioikeudet vuonna 1960 eli " \
                        "vuosi ennen syntymääsi. "
    else:
        difference = year - 1960
        history_text1 = "Seinäjoki sai kaupunkioikeudet vuonna 1960 " \
                        "eli " + str(difference) + " vuotta ennen syntymääsi. "

    history_text2 = ""

    if year < 2005:
        history_text2 = "Synnyinvuonnasi Peräseinäjoki, Nurmo ja Ylistaro " \
                        "olivat vielä omia kuntiaan. Peräseinäjoki " \
                        "liitettiin Seinäjokeen vuonna 2005 ja Nurmo ja " \
                        "Ylistaro vuonna 2009."
    elif year == 2005:
        history_text2 = "Peräseinäjoki liitettiin Seinäjokeen " \
                        "synnyinvuonnasi 2005. Nurmo ja Ylistaro olivat " \
                        "tuolloin vielä omia kuntiaan. Nurmo ja Ylistaro " \
                        "liitettiin Seinäjokeen vuonna 2009."
    elif year < 2009:
        history_text2 = "Synnyinvuonnasi Peräseinäjoki oli jo osa " \
                        "Seinäjokea. Nurmo ja Ylistaro olivat tuolloin " \
                        "vielä omia kuntiaan. Nurmo ja Ylistaro liitettiin " \
                        "Seinäjokeen vuonna 2009."
    elif year == 2009:
        history_text2 = "Nurmo ja Ylistaro liitettiin Seinäjokeen " \
                        "synnyinvuonnasi 2009. Peräseinäjoki oli tuolloin " \
                        "jo osa Seinäjokea."
    else:
        history_text2 = "Synnyinvuonnasi Peräseinäjoki, Nurmo ja Ylistaro " \
                        "olivat jo osa Seinäjokea."

    return [history_text1, history_text2]


def check_validity(day, month, year):
    is_valid_date = True
    is_leap_year = False
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        is_leap_year = True

    if month == 2:
        if is_leap_year:
            if day > 29:
                is_valid_date = False
        else:
            if day > 28:
                is_valid_date = False

    elif month == 4 or 6 or 9 or 11:
        if day > 30:
            is_valid_date = False

    return is_valid_date


def get_data(day, month, year):

    date = str(day) + "." + str(month) + "." + str(year)

    if not check_validity(day, month, year):
        result_text1 = "Virheellinen päivämäärä."
        result_text2 = ""

    else:
        weather_texts = weather(day, month, year)
        rain_text = weather_texts[0]
        warmth_text = weather_texts[1]

        timestamp = pd.Timestamp(year=year, month=month, day=day)
        weekday_text = weekday(timestamp)

        song_text = song(timestamp)

        population_text = population(year)

        history_list = history(year)
        history_text1 = history_list[0]
        history_text2 = history_list[1]

        result_text1 = weekday_text + warmth_text + rain_text + song_text \
                      + population_text

        result_text2 = history_text1 + history_text2

    return [date, result_text1, result_text2]
