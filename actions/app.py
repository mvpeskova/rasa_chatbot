from flask import Flask, request, jsonify

app = Flask(__name__)

partner_universities = [
    {"id": 1, "country": "Argentina", "universities": ["Universidad de San Martin"]},
    {"id": 2, "country": "Armenia", "universities": ["Russian-Armenian University"]},
    {"id": 3, "country": "Aruba", "universities": ["University of Aruba"]},
    {"id": 4, "country": "Australia", "universities": ["University of the Sunshine Coast"]},
    {"id": 5, "country": "Austria", "universities": ["CAMPUS 02 Fachhochschule der Wirtschaft GmbH",
                                                     "IMC FH Krems - University of Applied Management Sciences",
                                                     "Fachhochschule Kärnten",
                                                     "FH Campus Wien - University of Applied Sciences",
                                                     "FH Wien der WKW University of Applied Sciences for Management and Communication"]},
    {"id": 6, "country": "Belarus",
     "universities": ["Belarusian National Technical University", "Belarus State Economic University"]},
    {"id": 7, "country": "Belgium",
     "universities": ["Artevelde University College", "Thomas More Kempen", "University Colleges Leuven-Limburg",
                      "Thomas More Mechelen-Antwerpen"]},
    {"id": 8, "country": "Brazil", "universities": ["Universidade de Fortaleza", "Universidade de Ouro Preto",
                                                    "Universidade Federal do Espírito Santo, Vitória",
                                                    "Universidade Sagrado Coracao, Bauro/Sao Paulo"]},
    {"id": 9, "country": "Bulgaria",
     "universities": ["American University in Bulgaria", "Technical University of Sofia at Plovdiv",
                      "Angel Kanchev University of Ruse", "University of Economics",
                      "Varna Free University \"Chernorizets Hrabar\"", "Prof. Dr. Asen Zlatarov University"]},
    {"id": 10, "country": "Canada", "universities": ["Lakehead University", "Douglas College"]},
    {"id": 11, "country": "Chile",
     "universities": ["Universidad Austral de Chile", "Fundación Instituto Profesional Duoc Uc", "Universidad Mayor",
                      "Universidad de Concepción"]},
    {"id": 12, "country": "China", "universities": ["Shenzhen Technology University"]},
    {"id": 13, "country": "Colombia", "universities": ["Universidad Nacional de Colombia"]},
    {"id": 14, "country": "Croatia",
     "universities": ["University of Zagreb", "University of Osijek", "Algebra University College",
                      "University of Rijeka"]},
    {"id": 15, "country": "Cyprus", "universities": ["University of Nicosia", "Frederick University Cyprus"]},
    {"id": 16, "country": "Czech Republic",
     "universities": ["Mendel University Brno", "Tomas Bata University in Zlín", "University of West Bohemia Plzen",
                      "Institute of Technology and Busines", "University of South Bohemia", "University College Pragu",
                      "Metropolitan University Prague",
                      "University of Economics", "Czech Technical University"]},
    {"id": 17, "country": "Denmark",
     "universities": ["University of Southern Denmark", "University College of Northern Denmark (UCN)"]},
    {"id": 18, "country": "Ecuador", "universities": ["Universidad Internacional del Ecuador"]},
    {"id": 19, "country": "Estonia", "universities": ["TTK University of Applied Sciences"]},
    {"id": 20, "country": "Finland",
     "universities": ["Häme University of Applied Sciences", "Lapland University of Applied Sciences",
                      "Satakunta University of Applied Sciences",
                      "Seinäjoki University of Applied Sciences", "Savonia University of Applied Sciences",
                      "Diaconia University of Applied Sciences"]},
    {"id": 21, "country": "France",
     "universities": ["Université de Savoie Mont Blanc", "IDRAC International School of Management", "ISEN",
                      "ICAM Strasbourg - Europe",
                      "Université de Bourgogne", "Université de Nantes", "Institut Superieur de Gestion (ISG)"]},
    {"id": 22, "country": "Georgia",
     "universities": ["Guram Tavartkiladze Tbilisi Teaching University", "Caucasus International University"]},
    {"id": 23, "country": "UK",
     "universities": ["Staffordshire University", "Edinburgh Napier University", "Northumbria University Newcastle",
                      "University of the West of Scotland", "Birkbeck University of London"]},
    {"id": 24, "country": "Greece", "universities": ["University of West Attica", "International Hellenic University",
                                                     "Technological Educational Institute of Western Greece"]},
    {"id": 25, "country": "Hungary",
     "universities": ["Budapest University of Technology and Economics", "Andrássy Universität",
                      "MATE Hungarian University of Agriculture and Life Sciences, Gödöllö und Budapest",
                      "Eötvös József College", "Széchenyi István University"]},
    {"id": 26, "country": "India", "universities": ["Indian Institute of Technology Madras"]},
    {"id": 27, "country": "Ireland", "universities": ["Munster Technological University", "Griffith College"]},
    {"id": 28, "country": "Italy",
     "universities": ["Università Degli Studi di Cagliari", "Università Ca’ Foscari Venezia", "Università Di Pisa",
                      "Università Degli Studi di Trento", "Università degli Studi dell' Insubria"]},
    {"id": 29, "country": "Japan", "universities": ["Kansai Gaidai University"]},
    {"id": 30, "country": "Jordan", "universities": ["German-Jordanian University"]},
    {"id": 31, "country": "South Korea",
     "universities": ["Inha University", "Konkuk University", "Incheon National University",
                      "University of Ulsan", "Kongju National University", "Gyeongsang National University",
                      "Kookmin University", "Duksung Women’s University", "Hallym University"]},
    {"id": 32, "country": "Latvia",
     "universities": ["University of Latvia at Riga", "Riga Technical University", "Daugavpils University",
                      "Rezeknes Augstskola", "Ventspils University of Applied Sciences"]},
    {"id": 33, "country": "Lebanon", "universities": ["Rafik Hariri University Mechref"]},
    {"id": 34, "country": "Lithuania",
     "universities": ["Kazimieras Simonavicuis University", "Vilnius College of Technologies and Design"]},
    {"id": 35, "country": "Luxembourg", "universities": ["Université du Luxembourg"]},
    {"id": 36, "country": "Malaysia", "universities": ["Universiti Malaysia Pahang"]},
    {"id": 37, "country": "Malta", "universities": ["University of Malta"]},
    {"id": 38, "country": "Mexico", "universities": ["Universidad de Colima", "Universidad del Valle de Atemajac",
                                                     "Universidad Marista de Mérida",
                                                     "Universidad TEC Milenio Cancun and Merida"]},
    {"id": 39, "country": "Mongolia",
     "universities": ["Mongolian National University of Medical Sciences", "Seruuleg University"]},
    {"id": 40, "country": "Namibia", "universities": ["Namibia University of Science and Technology"]},
    {"id": 41, "country": "Netherlands",
     "universities": ["Rotterdam University of Applied Science", "Fontys University of Applied Sciences",
                      "Avans Hogeschool Breda / Tilburg", "HZ UAS Vlissingen"]},
    {"id": 42, "country": "New Zealand", "universities": ["Eastern Institute of Technology"]},
    {"id": 43, "country": "Norway", "universities": ["Molde University College", "University of Agder"]},
    {"id": 44, "country": "Peru", "universities": ["Universidad Peruana de Ciencias Aplicadas (UPC)"]},
    {"id": 45, "country": "Poland",
     "universities": ["Politechnika Slaska", "Academy of Silesia", "University of Economics Katowice",
                      "Technical University Kielce",
                      "Cracow University of Economics", "Technical University of Lodz",
                      "University College of Enterprise and Administration", "University of Bielsko-Biala"]},
    {"id": 46, "country": "Portugal",
     "universities": ["Instituto Politécnico do Porto (ISEP)", "University of the Azores",
                      "Instituto Politécnico do Cávado e do Ave", "Polytechnic Institute Beja"]},
    {"id": 47, "country": "Romania", "universities": ["West University of Timisoara", "University Aurel Vlaicu",
                                                      "Lucian Blaga University of Sibiu",
                                                      "National University of Science and Technology POLITEHNICA"]},
    {"id": 48, "country": "Russia",
     "universities": ["Kuban State University", "Saint Petersburg Electrotechnical University",
                      "Moscow Power Engineering Institute",
                      "People's Friendship University of Russia", "Tomsk State University",
                      "Saint Petersburg National Research University"]},
    {"id": 49, "country": "Slovakia", "universities": ["Alexander Dubcek University of Trencin", "Matej Bel University",
                                                       "Slovak University of Agriculture in Nitra",
                                                       "University of Zilina"]},
    {"id": 50, "country": "Slovenia",
     "universities": ["Josef Stefan International Postgraduate Schoo", "University of Maribor"]},
    {"id": 51, "country": "Spain",
     "universities": ["Universidad de Alcalá", "Universidad Rey Juan Carlos", "Universidad Antonio de Nebrija",
                      "Universitat Autònoma de Barcelona", "Universitat Politècnica de Catalunya",
                      "University of Vic - Central University of Catalonia", "University of Salamanca",
                      "University of the Basque Country", "Universidad de Burgos",
                      "Universidad Politecnica de Valencia",
                      "Universidad de Jaen", "Universidad de León", "Escuela de Turismo de Baleares",
                      "Universidad de Cantabria",
                      "Universidad Europea de Valencia", "Universidad de Valladolid", "Universidad La Laguna",
                      "Universidad Las Palmas de Gran Canaria", "Universidad San Jorge"]},
    {"id": 52, "country": "Sweden", "universities": ["Karlstad University", "Luleå University of Technology"]},
    {"id": 53, "country": "Switzerland", "universities": ["Bern University of Applied Science"]},
    {"id": 54, "country": "Taiwan", "universities": ["Chung Yuan Christian University",
                                                     "National Chung Cheng University, College of Management(Chai-Yi)",
                                                     "Da-Yeh University", "Tatung University"]},
    {"id": 55, "country": "Turkey",
     "universities": ["Istanbul Kültür University", "Istanbul Medipol University", "Dokuz Eylul Üniversitesi",
                      "University of Kocaeli", "Abdullah Gül University", "Onsekiz Mart University Canakkale"]},
    {"id": 56, "country": "Ukraine", "universities": ["West Ukrainian National University", "Kherson State University",
                                                      "National Health Care University of Ukraine",
                                                      "Ivan Franko National University of Lviv"]},
    {"id": 57, "country": "Uruguay", "universities": ["Universidad Católica del Uruguay"]},
    {"id": 58, "country": "USA", "universities": ["Muskingum University, New Concord /Ohio", "Presbyterian College",
                                                  "Haiwaii Pacific University", "University of North Carolina"]}
]

events = [
    {"id": 1, "name": "CV Check Day", "language": "English",
     "information": "Date and time: 31st of January, 9:00-12:00\nLocation: EC 1.11 - 1.12"},
    {"id": 2, "name": "How to study abroad? Your way to an exchange semester", "language": "German",
     "information": "Date and time: 25th of March, 13:00-14:00\nLocation: I107 und online"},
    {"id": 3, "name": "International Week", "language": "English",
     "information": "Date and time: 21-25th of January, 13:00-15:00\nLocation: online"},
    {"id": 4, "name": "Erzählcafé in Deggendorf", "language": "English",
     "information": "Date and time: 15th of March, 18:00-20:00\nLocation: Café im Handwerksmuseum, Maria-Ward-Platz 1, 94469 Deggendorf"},
    {"id": 5, "name": "Wie bewerbe ich mich für ein Auslandsstudium?", "language": "German",
     "information": "Date and time: 13th of March, 11:00-13:00\nLocation: K109"},
    {"id": 6, "name": "Get-together Erasmus+", "language": "German",
     "information": "Date and time: 3rd of April, 13:00-16:00\nLocation: hybrid, B004"}

]

scholarships_information = [
    {"id": 1, "name": "dit",
     "documents": "Application form\nCV in tabular form\nFinancial plan\nCurrent transcript (grade sheet)\nPassport photo\nInternship cotract, if applicable"},
    {"id": 2, "name": "erasmus",
     "documents": "CV\nTranscript of Records\nPhoto\nLetter of motivation\nEnrolment certificate"},
    {"id": 3, "name": "BAfOG",
     "documents": "Completed BAföG application forms\nEnrollment certificate\nIdentity card or if " +
                  "you are not a German citizen - nationality residence permit\nTax assessment from the last calendar year\nRental agreement or registration certificate\nCertificate of insurance"}
]

semester_abroad_options = [
    {"id": 1, "name": "partner",
     "documents": "CV with photo, motivational letter with your reasons for application, enrolment certificate and your DIT-transcript"},
    {"id": 2, "name": "independently",
     "documents": "Notice for an independent application for studies abroad \n- Letter of acceptance from the host university \n- Learning Agreement"}
]

document_information = [
    {"id": 1, "name": "contract",
     "information": "You have the option to generate a contract via Primuss, or alternatively, "
                    "if the company provides one, you may use their contract. "
                    "Regardless of the source, it is mandatory to input the contract details into the Primuss portal. "
                    "Approval from the Director of Student Internships is required to ensure that the internship aligns "
                    "with current study regulations, including international considerations and a minimum duration of 20 weeks"
                    " excluding holidays. The contract undergoes verification and approval directly through Primuss, "
                    "involving the upload of the contract. Please make sure that the international aspect to your internship is identifiable in "
                    "your contract. If necessary, please add an internship description."},
    {"id": 2, "name": "reference",
     "information": "The letter of reference must confirm the duration of the internship in weeks. "
                    "Additionally, your supervisor should specify"
                    " the type of activities you engaged in and provide an assessment of the quality of your performance."},
    {"id": 3, "name": "report",
     "information": "Your report should follow this format:\ncover page that includes your name, the semester in which you completed "
                    "your internship, name and address of the organization, the start and finish dates of the internship\n"
                    "description of the organization(one page)\ndetailed report over your activities during your internship\n"
                    "evaluation of the internship and the enterprise"}
]

transfer_credits_options = [
    {"id": 1, "name": "documents", "description": "Internal Learning Agreement/ Proposal for course recognition from abroad"
                                              "\nException: for students of the Faculty of Computer Science, special "
                                              "rules and regulations apply \nERASMUS Learning Agreement (ERASMUS + "
                                              "Studierende)"},
    {"id": 2, "name": "contact",
     "description": "- Chairman of the examination board: Prof. Dr. Stefan Götze, \n- Grading conversion: Iris Reul"}
]

summer_schools = [
    {"id": 1, "name": "The Next / The Young Global Leaders Camp",
     "description": "Lyon, France, from May 21, 2024 (first intake for 4 or 8 weeks) or June 18 (second intake for 4 weeks)."
                    "\nThe following courses are being offered: \nFrench Language Courses combined with Business & International Studies in English, "
                    "\ne.g.: ‘Sustainable Entrepreneurship’, ‘Managing Innovations’, ‘Intercultural Communication’, ‘Geopolitics’, "
                    "\n‘Sustainable Initiatives in France’, ‘Dynamic Public Speaking. (Lyon) "},

    {"id": 2, "name": "Swarm Master: Drone Fleet Commander Bootcamp",
     "description": "“Flight Dynamics, Navigation & Communication for Drone Fleets”, “Autonomous Flight and Navigation for Swarm Coordination”,"
                    "\n“Radar Technologies: LIDARS: Different Types and Applications”, “Remote Piloting and Telecommunication Networks”, "
                    "\n“5G/6G Wireless Technologies: Challenges & Trends”; "
                    "\nfurther information: via iLearn; "
                    "\nDeadline: 01.07.2024 (Riga)"},

    {"id": 3, "name": 'Fulbright Summer Scholarship Program "Diversity Initative 2024"',
     "description": "Trinity University in San Antonio, Texas, USA, August 22 – September 21, 2024 "
                    "\nAgenda: Course “Intercultural Competence” and various courses on topics such as "
                    "\nhistory, politics,culture and society, several excursions to the State Capitol, museums, etc. "
                    "\nFurther information is available on iLearn / Outgoings – First Steps; "
                    "\nDeadline: 28.02.2024 (San Antonio)"},

    {"id": 4, "name": "Time Capsule of Latvian Footprints",
     "description": "History of Latvia, its Culture, Traditions, etc.”, "
                    "\n“Personal Characteristics – Psychological Portrait of an Average Lativan”, “Introduction to Latvian Famous Global Achievements”, "
                    "\n“Latvian Lifestyle and Traditions”, “Latvian Language”; further information: via iLearn; "
                    "\nDeadline: 01.07.2024 (Riga)"},

    {"id": 5, "name": "Intensive English and Cross-Cultural Communication",
     "description": "20 hours of English lessons per week combined with sportive, cultural and entertainment activities; "
                    "\nfurther information: via iLearn; "
                    "\nDeadline: 01.07.2024 (Riga)"},

    {"id": 6, "name": 'Fulbright Summer Scholarship Program "Leaders in Entrepreneurship"',
     "description": "Virginia Polytechnic Institute and State University, USA, August 23 – September 14, 2024 "
                    "\nAgenda: Course “Foundations of Entrepreneurship”, Excursion to Washington DC, "
                    "\nvisits of local StartUps and Research Labs, Projects in cooperation with the Apex Center for Entrepreneurs,"
                    "\nParticipation in an Entrepreneurship Festival, Further information: iLearn / Outgoings- First Steps; "
                    "\nDeadline 28.02.2024 (Virginia)"},

    {"id": 7, "name": "Nanophotonics: Close up for the future",
     "description": "Courses: “Optical Nanolithography”, “Quantum pits, wires, points and rims in inorganic semiconductors”, “Optical surface plasmons”, "
                    "\n“Near-field optical microscopy”, “Carbon nanotube light emitters and receivers (Nanoantennas)”; "
                    "\nfurther information: 01.07.2024 (Riga)"},

    {"id": 8, "name": "Easter Spring School - Delightful Cappadocia",
     "description": "Easter Spring School - Delightful Cappadocia - Digital Marketing: Cappadocia Museum visits, optional tours and excursions; "
                    "\nmore Informations via iLearn / Outgoings - First Steps; "
                    "\nDates: 30.03.24 to 06.04.2024"
                    "\nDeadline: 15.01.2024 (Early Bird) or 29.02.2024 (Cappadocia)"},

    {"id": 9, "name": "CERN Summer Student Programme",
     "description": "CERN Summer Student Programme - Studierende (Bachelor / Master) aus den Bereichen Physik, Ingenieurswissenschaften, Informatik oder Mathematik, "
                    "\nmin. 3 Jahre des Studiums abgeschlossen, Interesse an 3 bis 8 Wochen am CERN; "
                    "\nweitere Informationen: CERN Summer Student Programme; "
                    "\nDirektbewerbung: https://jobs.smartrecruiters.com/CERN/743999941597814-cern-summer-student-programme-2024-member-and-non-member-state-?trid=e9e2014d-d16d-4269-9850-b7b5e1b4b7dc; "
                    "\nJuni bis September"
                    "\nBewerbungsschluss: 31.01.2024 (Genf)"},

    {"id": 10, "name": "Summer School IDRAC Summer Session",
     "description": "Lyon, France, from May 21, 2024 (first intake for 4 or 8 weeks) or June 18 (second intake for 4 weeks). "
                    "\nThe following courses are being offered: "
                    "\nFrench Language Courses combined with Business & International Studies in English, "
                    "\ne.g.: ‘Sustainable Entrepreneurship’, ‘Managing Innovations’, ‘Intercultural Communication’, "
                    "\n‘Geopolitics’, ‘Sustainable Initiatives in France’, ‘Dynamic Public Speaking. (Lyon)"}
]


def _find_next_id(elements):
    return max(element["id"] for element in elements) + 1


@app.get("/events")
def get_events():
    return jsonify(events)


@app.post("/events")
def add_event():
    print(request)
    if request.is_json:
        event = request.get_json()
        event["id"] = _find_next_id(events)
        events.append(event)
        return event, 201
    return {"error": "Request must be JSON"}, 415


@app.get("/scholarships")
def get_scholarships():
    return jsonify(scholarships_information)


@app.post("/scholarships")
def add_scholarship():
    print(request)
    if request.is_json:
        scholarship = request.get_json()
        scholarship["id"] = _find_next_id(scholarships_information)
        scholarship.append(scholarship)
        return scholarship, 201
    return {"error": "Request must be JSON"}, 415


@app.get("/semester_abroad")
def get_semester_option():
    return jsonify(semester_abroad_options)


@app.post("/semester_abroad")
def add_semester_option():
    print(request)
    if request.is_json:
        abroad_option = request.get_json()
        abroad_option["id"] = _find_next_id(semester_abroad_options)
        semester_abroad_options.append(abroad_option)
        return abroad_option, 201
    return {"error": "Request must be JSON"}, 415


@app.get("/internship")
def get_internship():
    return jsonify(document_information)


@app.post("/internship")
def add_internship():
    print(request)
    if request.is_json:
        document_option = request.get_json()
        document_option["id"] = _find_next_id(document_information)
        document_information.append(document_option)
        return document_option, 201
    return {"error": "Request must be JSON"}, 415


@app.get("/partner_universities")
def get_partner_universities():
    return jsonify(partner_universities)


@app.post("/partner_universities")
def add_partner_universities():
    print(request)
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id(partner_universities)
        partner_universities.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415


@app.get("/transfer_credits_options")
def get_events_transfer_credits_options():
    return jsonify(transfer_credits_options)


@app.post("/transfer_credits_options")
def add_transfer_credits_options():
    print(request)
    if request.is_json:
        transfer_credits_option = request.get_json()
        transfer_credits_option["id"] = _find_next_id(transfer_credits_options)
        transfer_credits_options.append(transfer_credits_option)
        return transfer_credits_option, 201
    return {"error": "Request must be JSON"}, 415


@app.get("/summer_schools")
def get_summer_schools():
    return jsonify(summer_schools)


@app.post("/summer_schools")
def add_summer_schools():
    print(request)
    if request.is_json:
        summer_school = request.get_json()
        summer_school["id"] = _find_next_id(summer_schools)
        summer_schools.append(summer_school)
        return summer_school, 201
    return {"error": "Request must be JSON"}, 415
