import PySimpleGUI as sg

menu_def = [["File", ["Close"]], ["Help", ["About"]]]

datins = [
    [sg.Menu(menu_def)],
    [sg.Text("Ievadi vārdu un uzvārdu!"), sg.InputText(key="--vardsuzvards--")],
    [sg.Text("Kas bija pirmais Latvijas prezidents?"), sg.InputText(key="--vards--")],
    [sg.Text("Kas ir tagadējais Latvijas prezidents?"), sg.InputText(key="--uzvards--")],
    [sg.Text("Kurā gadā Latvija kļuva neatkarīga?:"), sg.Text("Kurā mēnesī svin ziemassvētkus? :"), sg.Text("Cik gadā ir nedēļas?:")],
    [sg.Combo(["1990", "1918", "1981", "2004"], key="__combo__"), sg.Text("   "),
     sg.Combo(["Janvārī", "Februārī", "Martā", 'Aprīlī', "Maijā", "Jūnijā", "Jūlijā", "Augustā", "Septembrī",
               "Oktobrī", "Novembrī", "Decembrī"], key="__combo2__"), sg.Text(""),
     sg.Combo([i for i in range(1, 53)], key="__combo3__")],
    [sg.Text("Cik pasulē ir iedzīvotāju?")],
    [sg.Checkbox("2000000", default=False, key="-IN-")],
    [sg.Checkbox("8000000000", default=False, key="-IN2-")],
    [sg.Checkbox("12", default=False, key="-IN3-")],
    [sg.Checkbox("140000", default=False, key="-IN4-")],
    [sg.Checkbox("9999999999", default=False, key="-IN5-")],
    [sg.Text("", key="--vieta--")],
    [sg.Button("Ok")],
]

logs = sg.Window("Viktorīna", datins, size=(1000, 500))
while True:
    event, values = logs.read()
    if event == sg.WIN_CLOSED or event == "Close":
        break
    elif event == "About":
        sg.popup("Autors: Toms Brūns")
    elif event == "Ok":
        izvele = values["__combo__"]
        izvele2 = values["__combo2__"].lower()
        izvele3 = values["__combo3__"]

        metematika = values["-IN-"]
        lat = values["-IN2-"]
        fizika = values["-IN3-"]
        kimija = values["-IN4-"]
        sports = values["-IN5-"]

        vards = values["--vards--"]
        uzvards = values["--uzvards--"]
        vardsuzvards = values["--vardsuzvards--"]

        iecienitie_prieksmeti = []  
        if metematika:
            iecienitie_prieksmeti.append("2000000")
        if lat:
            iecienitie_prieksmeti.append("8000000000")
        if fizika:
            iecienitie_prieksmeti.append("12")
        if kimija:
            iecienitie_prieksmeti.append("140000")
        if sports:
            iecienitie_prieksmeti.append("9999999999")
        logs["--vieta--"].update(f'Darbu pildīja: {vardsuzvards}\n'f' Pirmais Latvijas prezidents bija {vards} \n'f' Tagadējis Latvijas prezidents ir {uzvards}. \n'f' Atbildes: Latvija {izvele}. gadā kļuva neatkarīga. \n'f' Ziemassvētkus svin {izvele2}. \n'f' Gadā ir {izvele3} nedēļas. \n'f' Uz pasaules dzīvo aptuveni : {", ".join(iecienitie_prieksmeti)} iedzīvotāju')

logs()
