import pandas as pd


def weather(day, month, year):
    df_weather = pd.read_csv("saa_seinajoki.csv")
    year_filtered = df_weather["Vuosi"] == int(year)
    month_filtered = df_weather["Kuukausi"] == int(month)
    day_filtered = df_weather["Päivä"] == int(day)

    df_filtered = df_weather[year_filtered & month_filtered & day_filtered]

    rain = df_filtered["Sademäärä [mm]"].values[0]
    warmth = df_filtered["Ilman keskilämpötila [°C]"].values[0]

    # Sademäärä -1 tarkoittaa, että ei satanut ollenkaan
    # Sademäärä 0 tarkoittaa, että satoi alle 0,1 mm

    # Näissä lähteenä Ilmatieteen laitoksen sivuilta löytyvät määritelmät
    rain_text = ""
    if rain < 0.3:
        rain_text = "Päivä oli poutainen."
    elif rain <= 0.9:
        rain_text = "Kyseisenä päivänä satoi vähän."
    elif rain <= 4.4:
        rain_text = "Kyseisenä päivänä satoi."
    else:
        rain_text = "Kyseisenä päivänä satoi runsaasti."

    warmth_text = "Päivän keskilämpötila oli Seinäjoella " + str(warmth) + \
                  " astetta."

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
    weekday_result = weekdays[weekday_number]
    weekday_text = "Päivä oli " + weekday_result + "."

    return weekday_text


def population(year):

    population_text = ""

    if int(year) >= 1987:
        df_population = pd.read_csv("vakiluku_sjoki.csv")

        value = df_population.loc[0, year]

        population_text = "Vuonna " + year + " Seinäjoen väkiluku oli " \
                          + str(value) + "."

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
                    "artistin " + artist + " kappale " + single + "."

    return song_text


def get_day_month_year(date):
    day = ""
    month = ""
    year = ""
    current = ""
    count = 0

    for i in range(len(date)):
        if date[i] != ".":
            current += date[i]
        else:
            if count == 0:
                day = current

            elif count == 1:
                month = current
            current = ""
            count += 1
    year = current

    return [day, month, year]


def main():
    date = input("Choose a date (dd.mm.yyyy): ")
    # virhetarkistukset

    date_list = get_day_month_year(date)
    day = date_list[0]
    month = date_list[1]
    year = date_list[2]

    weather_texts = weather(day, month, year)
    rain_text = weather_texts[0]
    warmth_text = weather_texts[1]

    timestamp = pd.Timestamp(year=int(year), month=int(month), day=int(day))
    weekday_text = weekday(timestamp)

    song_text = song(timestamp)

    population_text = population(year)

    print(weekday_text)
    print(warmth_text, rain_text)
    if song_text != "":
        print(song_text)
    if population_text != "":
        print(population_text)


if __name__ == "__main__":
    main()
