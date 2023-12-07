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


def get_data(day, month, year):

    weather_texts = weather(day, month, year)
    rain_text = weather_texts[0]
    warmth_text = weather_texts[1]

    timestamp = pd.Timestamp(year=year, month=month, day=day)
    weekday_text = weekday(timestamp)

    song_text = song(timestamp)

    population_text = population(year)

    result_text = weekday_text + warmth_text + rain_text + song_text \
                  + population_text

    return result_text
