import pandas as pd


def weather(day, month, year):
    df_weather = pd.read_csv("saa_seinajoki.csv")
    year_selected = df_weather["Vuosi"] == int(year)
    month_selected = df_weather["Kuukausi"] == int(month)
    day_selected = df_weather["Päivä"] == int(day)

    df_selected = df_weather[year_selected & month_selected & day_selected]

    rain = df_selected["Sademäärä [mm]"].values[0]
    warmth = df_selected["Ilman keskilämpötila [°C]"].values[0]

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

    warmth_text = "Päivän keskilämpötila oli " + str(warmth) + " astetta."

    return [rain_text, warmth_text]


def weekday(day, month, year):
    weekdays = {0: "maanantai",
                1: "tiistai",
                2: "keskiviikko",
                3: "torstai",
                4: "perjantai",
                5: "lauantai",
                6: "sunnuntai"}

    timestamp = pd.Timestamp(year=int(year), month=int(month), day=int(day))
    weekday_number = timestamp.weekday()
    weekday_result = weekdays[weekday_number]
    weekday_text = "Päivä oli " + weekday_result + "."

    return weekday_text


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

    weekday_text = weekday(day, month, year)

    print(weekday_text)
    print(rain_text, warmth_text)


if __name__ == "__main__":
    main()





