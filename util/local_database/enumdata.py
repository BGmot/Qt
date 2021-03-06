#!/usr/bin/env python
#############################################################################
##
## Copyright (C) 2011 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
## Contact: Nokia Corporation (qt-info@nokia.com)
##
## This file is part of the test suite of the Qt Toolkit.
##
## $QT_BEGIN_LICENSE:LGPL$
## GNU Lesser General Public License Usage
## This file may be used under the terms of the GNU Lesser General Public
## License version 2.1 as published by the Free Software Foundation and
## appearing in the file LICENSE.LGPL included in the packaging of this
## file. Please review the following information to ensure the GNU Lesser
## General Public License version 2.1 requirements will be met:
## http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
##
## In addition, as a special exception, Nokia gives you certain additional
## rights. These rights are described in the Nokia Qt LGPL Exception
## version 1.1, included in the file LGPL_EXCEPTION.txt in this package.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU General
## Public License version 3.0 as published by the Free Software Foundation
## and appearing in the file LICENSE.GPL included in the packaging of this
## file. Please review the following information to ensure the GNU General
## Public License version 3.0 requirements will be met:
## http://www.gnu.org/copyleft/gpl.html.
##
## Other Usage
## Alternatively, this file may be used in accordance with the terms and
## conditions contained in a signed written agreement between you and Nokia.
##
##
##
##
##
## $QT_END_LICENSE$
##
#############################################################################

# langugae_list and country_list reflect the current values of enums in qlocale.h
# If new xml language files are available in CLDR, these languages and countries
# need to be *appended* to this list.

language_list = {
    0 : [ "AnyLanguage",          "  " ],
    1 : [ "C",                    "  " ],
    2 : [ "Abkhazian",            "ab" ],
    3 : [ "Afan",                 "om" ],
    4 : [ "Afar",                 "aa" ],
    5 : [ "Afrikaans",            "af" ],
    6 : [ "Albanian",             "sq" ],
    7 : [ "Amharic",              "am" ],
    8 : [ "Arabic",               "ar" ],
    9 : [ "Armenian",             "hy" ],
    10 : [ "Assamese",            "as" ],
    11 : [ "Aymara",              "ay" ],
    12 : [ "Azerbaijani",         "az" ],
    13 : [ "Bashkir",             "ba" ],
    14 : [ "Basque",              "eu" ],
    15 : [ "Bengali",             "bn" ],
    16 : [ "Bhutani",             "dz" ],
    17 : [ "Bihari",              "bh" ],
    18 : [ "Bislama",             "bi" ],
    19 : [ "Breton",              "br" ],
    20 : [ "Bulgarian",           "bg" ],
    21 : [ "Burmese",             "my" ],
    22 : [ "Byelorussian",        "be" ],
    23 : [ "Cambodian",           "km" ],
    24 : [ "Catalan",             "ca" ],
    25 : [ "Chinese",             "zh" ],
    26 : [ "Corsican",            "co" ],
    27 : [ "Croatian",            "hr" ],
    28 : [ "Czech",               "cs" ],
    29 : [ "Danish",              "da" ],
    30 : [ "Dutch",               "nl" ],
    31 : [ "English",             "en" ],
    32 : [ "Esperanto",           "eo" ],
    33 : [ "Estonian",            "et" ],
    34 : [ "Faroese",             "fo" ],
    35 : [ "Fiji",        "fj" ],
    36 : [ "Finnish",             "fi" ],
    37 : [ "French",              "fr" ],
    38 : [ "Frisian",             "fy" ],
    39 : [ "Gaelic",              "gd" ],
    40 : [ "Galician",            "gl" ],
    41 : [ "Georgian",            "ka" ],
    42 : [ "German",              "de" ],
    43 : [ "Greek",               "el" ],
    44 : [ "Greenlandic",         "kl" ],
    45 : [ "Guarani",             "gn" ],
    46 : [ "Gujarati",            "gu" ],
    47 : [ "Hausa",               "ha" ],
    48 : [ "Hebrew",              "he" ],
    49 : [ "Hindi",               "hi" ],
    50 : [ "Hungarian",           "hu" ],
    51 : [ "Icelandic",           "is" ],
    52 : [ "Indonesian",          "id" ],
    53 : [ "Interlingua",         "ia" ],
    54 : [ "Interlingue",         "ie" ],
    55 : [ "Inuktitut",           "iu" ],
    56 : [ "Inupiak",             "ik" ],
    57 : [ "Irish",               "ga" ],
    58 : [ "Italian",             "it" ],
    59 : [ "Japanese",            "ja" ],
    60 : [ "Javanese",            "jv" ],
    61 : [ "Kannada",             "kn" ],
    62 : [ "Kashmiri",            "ks" ],
    63 : [ "Kazakh",              "kk" ],
    64 : [ "Kinyarwanda",         "rw" ],
    65 : [ "Kirghiz",             "ky" ],
    66 : [ "Korean",              "ko" ],
    67 : [ "Kurdish",             "ku" ],
    68 : [ "Kurundi",             "rn" ],
    69 : [ "Laothian",            "lo" ],
    70 : [ "Latin",               "la" ],
    71 : [ "Latvian",             "lv" ],
    72 : [ "Lingala",             "ln" ],
    73 : [ "Lithuanian",          "lt" ],
    74 : [ "Macedonian",          "mk" ],
    75 : [ "Malagasy",            "mg" ],
    76 : [ "Malay",               "ms" ],
    77 : [ "Malayalam",           "ml" ],
    78 : [ "Maltese",             "mt" ],
    79 : [ "Maori",               "mi" ],
    80 : [ "Marathi",             "mr" ],
    81 : [ "Moldavian",           "mo" ],
    82 : [ "Mongolian",           "mn" ],
    83 : [ "Nauru",       "na" ],
    84 : [ "Nepali",              "ne" ],
    85 : [ "Norwegian",           "nb" ],
    86 : [ "Occitan",             "oc" ],
    87 : [ "Oriya",               "or" ],
    88 : [ "Pashto",              "ps" ],
    89 : [ "Persian",             "fa" ],
    90 : [ "Polish",              "pl" ],
    91 : [ "Portuguese",          "pt" ],
    92 : [ "Punjabi",             "pa" ],
    93 : [ "Quechua",             "qu" ],
    94 : [ "RhaetoRomance",       "rm" ],
    95 : [ "Romanian",            "ro" ],
    96 : [ "Russian",             "ru" ],
    97 : [ "Samoan",              "sm" ],
    98 : [ "Sangho",              "sg" ],
    99 : [ "Sanskrit",            "sa" ],
    100 : [ "Serbian",            "sr" ],
    101 : [ "SerboCroatian",      "sh" ],
    102 : [ "Sesotho",            "st" ],
    103 : [ "Setswana",           "tn" ],
    104 : [ "Shona",              "sn" ],
    105 : [ "Sindhi",             "sd" ],
    106 : [ "Singhalese",         "si" ],
    107 : [ "Siswati",            "ss" ],
    108 : [ "Slovak",             "sk" ],
    109 : [ "Slovenian",          "sl" ],
    110 : [ "Somali",             "so" ],
    111 : [ "Spanish",            "es" ],
    112 : [ "Sundanese",          "su" ],
    113 : [ "Swahili",            "sw" ],
    114 : [ "Swedish",            "sv" ],
    115 : [ "Tagalog",            "tl" ],
    116 : [ "Tajik",              "tg" ],
    117 : [ "Tamil",              "ta" ],
    118 : [ "Tatar",              "tt" ],
    119 : [ "Telugu",             "te" ],
    120 : [ "Thai",               "th" ],
    121 : [ "Tibetan",            "bo" ],
    122 : [ "Tigrinya",           "ti" ],
    123 : [ "Tonga",      "to" ],
    124 : [ "Tsonga",             "ts" ],
    125 : [ "Turkish",            "tr" ],
    126 : [ "Turkmen",            "tk" ],
    127 : [ "Twi",                "tw" ],
    128 : [ "Uigur",              "ug" ],
    129 : [ "Ukrainian",          "uk" ],
    130 : [ "Urdu",               "ur" ],
    131 : [ "Uzbek",              "uz" ],
    132 : [ "Vietnamese",         "vi" ],
    133 : [ "Volapuk",            "vo" ],
    134 : [ "Welsh",              "cy" ],
    135 : [ "Wolof",              "wo" ],
    136 : [ "Xhosa",              "xh" ],
    137 : [ "Yiddish",            "yi" ],
    138 : [ "Yoruba",             "yo" ],
    139 : [ "Zhuang",             "za" ],
    140 : [ "Zulu",               "zu" ],
    141 : [ "Nynorsk",            "nn" ],
    142 : [ "Bosnian",            "bs" ],
    143 : [ "Divehi",             "dv" ],
    144 : [ "Manx",               "gv" ],
    145 : [ "Cornish",            "kw" ],
    146 : [ "Akan",               "ak"  ],
    147 : [ "Konkani",            "kok" ],
    148 : [ "Ga",                 "gaa" ],
    149 : [ "Igbo",               "ig"  ],
    150 : [ "Kamba",              "kam" ],
    151 : [ "Syriac",             "syr" ],
    152 : [ "Blin",               "byn" ],
    153 : [ "Geez",               "gez" ],
    154 : [ "Koro",               "kfo" ],
    155 : [ "Sidamo",             "sid" ],
    156 : [ "Atsam",              "cch" ],
    157 : [ "Tigre",              "tig" ],
    158 : [ "Jju",                "kaj" ],
    159 : [ "Friulian",           "fur" ],
    160 : [ "Venda",              "ve"  ],
    161 : [ "Ewe",                "ee"  ],
    162 : [ "Walamo",             "wal" ],
    163 : [ "Hawaiian",           "haw" ],
    164 : [ "Tyap",               "kcg" ],
    165 : [ "Chewa",              "ny"  ],
    166 : [ "Filipino",           "fil" ],
    167 : [ "Swiss German",       "gsw" ],
    168 : [ "Sichuan Yi",         "ii"  ],
    169 : [ "Kpelle",             "kpe" ],
    170 : [ "Low German",         "nds" ],
    171 : [ "South Ndebele",      "nr"  ],
    172 : [ "Northern Sotho",     "nso" ],
    173 : [ "Northern Sami",      "se"  ],
    174 : [ "Taroko",             "trv" ],
    175 : [ "Gusii",              "guz" ],
    176 : [ "Taita",              "dav" ],
    177 : [ "Fulah",              "ff" ],
    178 : [ "Kikuyu",             "ki" ],
    179 : [ "Samburu",            "saq" ],
    180 : [ "Sena",               "seh" ],
    181 : [ "North Ndebele",      "nd" ],
    182 : [ "Rombo",              "rof" ],
    183 : [ "Tachelhit",          "shi" ],
    184 : [ "Kabyle",             "kab" ],
    185 : [ "Nyankole",           "nyn" ],
    186 : [ "Bena",               "bez" ],
    187 : [ "Vunjo",              "vun" ],
    188 : [ "Bambara",            "bm" ],
    189 : [ "Embu",               "ebu" ],
    190 : [ "Cherokee",           "chr" ],
    191 : [ "Morisyen",           "mfe" ],
    192 : [ "Makonde",            "kde" ],
    193 : [ "Langi",              "lag" ],
    194 : [ "Ganda",              "lg" ],
    195 : [ "Bemba",              "bem" ],
    196 : [ "Kabuverdianu",       "kea" ],
    197 : [ "Meru",               "mer" ],
    198 : [ "Kalenjin",           "kln" ],
    199 : [ "Nama",               "naq" ],
    200 : [ "Machame",            "jmc" ],
    201 : [ "Colognian",          "ksh" ],
    202 : [ "Masai",              "mas" ],
    203 : [ "Soga",               "xog" ],
    204 : [ "Luyia",              "luy" ],
    205 : [ "Asu",                "asa" ],
    206 : [ "Teso",               "teo" ],
    207 : [ "Saho",               "ssy" ],
    208 : [ "Koyra Chiini",       "khq" ],
    209 : [ "Rwa",                "rwk" ],
    210 : [ "Luo",                "luo" ],
    211 : [ "Chiga",              "cgg" ],
    212 : [ "Central Morocco Tamazight", "tzm" ],
    213 : [ "Koyraboro Senni",    "ses" ],
    214 : [ "Shambala",           "ksb" ]
}

country_list = {
    0 : [ "AnyCountry",                                 "  "  ],
    1 : [ "Afghanistan",                                "AF"  ],
    2 : [ "Albania",                                    "AL"  ],
    3 : [ "Algeria",                                    "DZ"  ],
    4 : [ "AmericanSamoa",                              "AS"  ],
    5 : [ "Andorra",                                    "AD"  ],
    6 : [ "Angola",                                     "AO"  ],
    7 : [ "Anguilla",                                   "AI"  ],
    8 : [ "Antarctica",                                 "AQ"  ],
    9 : [ "AntiguaAndBarbuda",                          "AG"  ],
    10 : [ "Argentina",                                 "AR"  ],
    11 : [ "Armenia",                                   "AM"  ],
    12 : [ "Aruba",                                     "AW"  ],
    13 : [ "Australia",                                 "AU"  ],
    14 : [ "Austria",                                   "AT"  ],
    15 : [ "Azerbaijan",                                "AZ"  ],
    16 : [ "Bahamas",                                   "BS"  ],
    17 : [ "Bahrain",                                   "BH"  ],
    18 : [ "Bangladesh",                                "BD"  ],
    19 : [ "Barbados",                                  "BB"  ],
    20 : [ "Belarus",                                   "BY"  ],
    21 : [ "Belgium",                                   "BE"  ],
    22 : [ "Belize",                                    "BZ"  ],
    23 : [ "Benin",                                     "BJ"  ],
    24 : [ "Bermuda",                                   "BM"  ],
    25 : [ "Bhutan",                                    "BT"  ],
    26 : [ "Bolivia",                                   "BO"  ],
    27 : [ "BosniaAndHerzegowina",                      "BA"  ],
    28 : [ "Botswana",                                  "BW"  ],
    29 : [ "BouvetIsland",                              "BV"  ],
    30 : [ "Brazil",                                    "BR"  ],
    31 : [ "BritishIndianOceanTerritory",               "IO"  ],
    32 : [ "BruneiDarussalam",                          "BN"  ],
    33 : [ "Bulgaria",                                  "BG"  ],
    34 : [ "BurkinaFaso",                               "BF"  ],
    35 : [ "Burundi",                                   "BI"  ],
    36 : [ "Cambodia",                                  "KH"  ],
    37 : [ "Cameroon",                                  "CM"  ],
    38 : [ "Canada",                                    "CA"  ],
    39 : [ "CapeVerde",                                 "CV"  ],
    40 : [ "CaymanIslands",                             "KY"  ],
    41 : [ "CentralAfricanRepublic",                    "CF"  ],
    42 : [ "Chad",                                      "TD"  ],
    43 : [ "Chile",                                     "CL"  ],
    44 : [ "China",                                     "CN"  ],
    45 : [ "ChristmasIsland",                           "CX"  ],
    46 : [ "CocosIslands",                              "CC"  ],
    47 : [ "Colombia",                                  "CO"  ],
    48 : [ "Comoros",                                   "KM"  ],
    49 : [ "DemocraticRepublicOfCongo",                 "CD"  ],
    50 : [ "PeoplesRepublicOfCongo",                    "CG"  ],
    51 : [ "CookIslands",                               "CK"  ],
    52 : [ "CostaRica",                                 "CR"  ],
    53 : [ "IvoryCoast",                                "CI"  ],
    54 : [ "Croatia",                                   "HR"  ],
    55 : [ "Cuba",                                      "CU"  ],
    56 : [ "Cyprus",                                    "CY"  ],
    57 : [ "CzechRepublic",                             "CZ"  ],
    58 : [ "Denmark",                                   "DK"  ],
    59 : [ "Djibouti",                                  "DJ"  ],
    60 : [ "Dominica",                                  "DM"  ],
    61 : [ "DominicanRepublic",                         "DO"  ],
    62 : [ "EastTimor",                                 "TL"  ],
    63 : [ "Ecuador",                                   "EC"  ],
    64 : [ "Egypt",                                     "EG"  ],
    65 : [ "ElSalvador",                                "SV"  ],
    66 : [ "EquatorialGuinea",                          "GQ"  ],
    67 : [ "Eritrea",                                   "ER"  ],
    68 : [ "Estonia",                                   "EE"  ],
    69 : [ "Ethiopia",                                  "ET"  ],
    70 : [ "FalklandIslands",                           "FK"  ],
    71 : [ "FaroeIslands",                              "FO"  ],
    72 : [ "Fiji",                               "FJ"  ],
    73 : [ "Finland",                                   "FI"  ],
    74 : [ "France",                                    "FR"  ],
    75 : [ "MetropolitanFrance",                        "FX"  ],
    76 : [ "FrenchGuiana",                              "GF"  ],
    77 : [ "FrenchPolynesia",                           "PF"  ],
    78 : [ "FrenchSouthernTerritories",                 "TF"  ],
    79 : [ "Gabon",                                     "GA"  ],
    80 : [ "Gambia",                                    "GM"  ],
    81 : [ "Georgia",                                   "GE"  ],
    82 : [ "Germany",                                   "DE"  ],
    83 : [ "Ghana",                                     "GH"  ],
    84 : [ "Gibraltar",                                 "GI"  ],
    85 : [ "Greece",                                    "GR"  ],
    86 : [ "Greenland",                                 "GL"  ],
    87 : [ "Grenada",                                   "GD"  ],
    88 : [ "Guadeloupe",                                "GP"  ],
    89 : [ "Guam",                                      "GU"  ],
    90 : [ "Guatemala",                                 "GT"  ],
    91 : [ "Guinea",                                    "GN"  ],
    92 : [ "GuineaBissau",                              "GW"  ],
    93 : [ "Guyana",                                    "GY"  ],
    94 : [ "Haiti",                                     "HT"  ],
    95 : [ "HeardAndMcDonaldIslands",                   "HM"  ],
    96 : [ "Honduras",                                  "HN"  ],
    97 : [ "HongKong",                                  "HK"  ],
    98 : [ "Hungary",                                   "HU"  ],
    99 : [ "Iceland",                                   "IS"  ],
    100 : [ "India",                                    "IN"  ],
    101 : [ "Indonesia",                                "ID"  ],
    102 : [ "Iran",                                     "IR"  ],
    103 : [ "Iraq",                                     "IQ"  ],
    104 : [ "Ireland",                                  "IE"  ],
    105 : [ "Israel",                                   "IL"  ],
    106 : [ "Italy",                                    "IT"  ],
    107 : [ "Jamaica",                                  "JM"  ],
    108 : [ "Japan",                                    "JP"  ],
    109 : [ "Jordan",                                   "JO"  ],
    110 : [ "Kazakhstan",                               "KZ"  ],
    111 : [ "Kenya",                                    "KE"  ],
    112 : [ "Kiribati",                                 "KI"  ],
    113 : [ "DemocraticRepublicOfKorea",                "KP"  ],
    114 : [ "RepublicOfKorea",                          "KR"  ],
    115 : [ "Kuwait",                                   "KW"  ],
    116 : [ "Kyrgyzstan",                               "KG"  ],
    117 : [ "Lao",                                      "LA"  ],
    118 : [ "Latvia",                                   "LV"  ],
    119 : [ "Lebanon",                                  "LB"  ],
    120 : [ "Lesotho",                                  "LS"  ],
    121 : [ "Liberia",                                  "LR"  ],
    122 : [ "LibyanArabJamahiriya",                     "LY"  ],
    123 : [ "Liechtenstein",                            "LI"  ],
    124 : [ "Lithuania",                                "LT"  ],
    125 : [ "Luxembourg",                               "LU"  ],
    126 : [ "Macau",                                    "MO"  ],
    127 : [ "Macedonia",                                "MK"  ],
    128 : [ "Madagascar",                               "MG"  ],
    129 : [ "Malawi",                                   "MW"  ],
    130 : [ "Malaysia",                                 "MY"  ],
    131 : [ "Maldives",                                 "MV"  ],
    132 : [ "Mali",                                     "ML"  ],
    133 : [ "Malta",                                    "MT"  ],
    134 : [ "MarshallIslands",                          "MH"  ],
    135 : [ "Martinique",                               "MQ"  ],
    136 : [ "Mauritania",                               "MR"  ],
    137 : [ "Mauritius",                                "MU"  ],
    138 : [ "Mayotte",                                  "YT"  ],
    139 : [ "Mexico",                                   "MX"  ],
    140 : [ "Micronesia",                               "FM"  ],
    141 : [ "Moldova",                                  "MD"  ],
    142 : [ "Monaco",                                   "MC"  ],
    143 : [ "Mongolia",                                 "MN"  ],
    144 : [ "Montserrat",                               "MS"  ],
    145 : [ "Morocco",                                  "MA"  ],
    146 : [ "Mozambique",                               "MZ"  ],
    147 : [ "Myanmar",                                  "MM"  ],
    148 : [ "Namibia",                                  "NA"  ],
    149 : [ "Nauru",                             "NR"  ],
    150 : [ "Nepal",                                    "NP"  ],
    151 : [ "Netherlands",                              "NL"  ],
    152 : [ "NetherlandsAntilles",                      "AN"  ],
    153 : [ "NewCaledonia",                             "NC"  ],
    154 : [ "NewZealand",                               "NZ"  ],
    155 : [ "Nicaragua",                                "NI"  ],
    156 : [ "Niger",                                    "NE"  ],
    157 : [ "Nigeria",                                  "NG"  ],
    158 : [ "Niue",                                     "NU"  ],
    159 : [ "NorfolkIsland",                            "NF"  ],
    160 : [ "NorthernMarianaIslands",                   "MP"  ],
    161 : [ "Norway",                                   "NO"  ],
    162 : [ "Oman",                                     "OM"  ],
    163 : [ "Pakistan",                                 "PK"  ],
    164 : [ "Palau",                                    "PW"  ],
    165 : [ "PalestinianTerritory",                     "PS"  ],
    166 : [ "Panama",                                   "PA"  ],
    167 : [ "PapuaNewGuinea",                           "PG"  ],
    168 : [ "Paraguay",                                 "PY"  ],
    169 : [ "Peru",                                     "PE"  ],
    170 : [ "Philippines",                              "PH"  ],
    171 : [ "Pitcairn",                                 "PN"  ],
    172 : [ "Poland",                                   "PL"  ],
    173 : [ "Portugal",                                 "PT"  ],
    174 : [ "PuertoRico",                               "PR"  ],
    175 : [ "Qatar",                                    "QA"  ],
    176 : [ "Reunion",                                  "RE"  ],
    177 : [ "Romania",                                  "RO"  ],
    178 : [ "RussianFederation",                        "RU"  ],
    179 : [ "Rwanda",                                   "RW"  ],
    180 : [ "SaintKittsAndNevis",                       "KN"  ],
    181 : [ "StLucia",                                  "LC"  ],
    182 : [ "StVincentAndTheGrenadines",                "VC"  ],
    183 : [ "Samoa",                                    "WS"  ],
    184 : [ "SanMarino",                                "SM"  ],
    185 : [ "SaoTomeAndPrincipe",                       "ST"  ],
    186 : [ "SaudiArabia",                              "SA"  ],
    187 : [ "Senegal",                                  "SN"  ],
    188 : [ "Seychelles",                               "SC"  ],
    189 : [ "SierraLeone",                              "SL"  ],
    190 : [ "Singapore",                                "SG"  ],
    191 : [ "Slovakia",                                 "SK"  ],
    192 : [ "Slovenia",                                 "SI"  ],
    193 : [ "SolomonIslands",                           "SB"  ],
    194 : [ "Somalia",                                  "SO"  ],
    195 : [ "SouthAfrica",                              "ZA"  ],
    196 : [ "SouthGeorgiaAndTheSouthSandwichIslands",   "GS"  ],
    197 : [ "Spain",                                    "ES"  ],
    198 : [ "SriLanka",                                 "LK"  ],
    199 : [ "StHelena",                                 "SH"  ],
    200 : [ "StPierreAndMiquelon",                      "PM"  ],
    201 : [ "Sudan",                                    "SD"  ],
    202 : [ "Suriname",                                 "SR"  ],
    203 : [ "SvalbardAndJanMayenIslands",               "SJ"  ],
    204 : [ "Swaziland",                                "SZ"  ],
    205 : [ "Sweden",                                   "SE"  ],
    206 : [ "Switzerland",                              "CH"  ],
    207 : [ "SyrianArabRepublic",                       "SY"  ],
    208 : [ "Taiwan",                                   "TW"  ],
    209 : [ "Tajikistan",                               "TJ"  ],
    210 : [ "Tanzania",                                 "TZ"  ],
    211 : [ "Thailand",                                 "TH"  ],
    212 : [ "Togo",                                     "TG"  ],
    213 : [ "Tokelau",                                  "TK"  ],
    214 : [ "Tonga",                             "TO"  ],
    215 : [ "TrinidadAndTobago",                        "TT"  ],
    216 : [ "Tunisia",                                  "TN"  ],
    217 : [ "Turkey",                                   "TR"  ],
    218 : [ "Turkmenistan",                             "TM"  ],
    219 : [ "TurksAndCaicosIslands",                    "TC"  ],
    220 : [ "Tuvalu",                                   "TV"  ],
    221 : [ "Uganda",                                   "UG"  ],
    222 : [ "Ukraine",                                  "UA"  ],
    223 : [ "UnitedArabEmirates",                       "AE"  ],
    224 : [ "UnitedKingdom",                            "GB"  ],
    225 : [ "UnitedStates",                             "US"  ],
    226 : [ "UnitedStatesMinorOutlyingIslands",         "UM"  ],
    227 : [ "Uruguay",                                  "UY"  ],
    228 : [ "Uzbekistan",                               "UZ"  ],
    229 : [ "Vanuatu",                                  "VU"  ],
    230 : [ "VaticanCityState",                         "VA"  ],
    231 : [ "Venezuela",                                "VE"  ],
    232 : [ "VietNam",                                  "VN"  ],
    233 : [ "BritishVirginIslands",                     "VG"  ],
    234 : [ "USVirginIslands",                          "VI"  ],
    235 : [ "WallisAndFutunaIslands",                   "WF"  ],
    236 : [ "WesternSahara",                            "EH"  ],
    237 : [ "Yemen",                                    "YE"  ],
    238 : [ "Yugoslavia",                               "YU"  ],
    239 : [ "Zambia",                                   "ZM"  ],
    240 : [ "Zimbabwe",                                 "ZW"  ],
    241 : [ "SerbiaAndMontenegro",                      "CS"  ],
    242 : [ "Montenegro",                               "ME"  ],
    243 : [ "Serbia",                                   "RS"  ],
    244 : [ "Saint Barthelemy",                         "BL"  ],
    245 : [ "Saint Martin",                             "MF"  ],
    246 : [ "LatinAmericaAndTheCaribbean",              "419" ]
}

script_list = {
    0   : [ "AnyScript",         "" ],
    1   : [ "Arabic",            "Arab" ],
    2   : [ "Cyrillic",          "Cyrl" ],
    3   : [ "Deseret",           "Dsrt" ],
    4   : [ "Gurmukhi",          "Guru" ],
    5   : [ "Simplified Han",    "Hans" ],
    6   : [ "Traditional Han",   "Hant" ],
    7   : [ "Latin",             "Latn" ],
    8   : [ "Mongolian",         "Mong" ],
    9   : [ "Tifinagh",          "Tfng" ]
}

def countryCodeToId(code):
    for country_id in country_list:
        if country_list[country_id][1] == code:
            return country_id
    return -1

def languageCodeToId(code):
    for language_id in language_list:
        if language_list[language_id][1] == code:
            return language_id
    return -1

def scriptCodeToId(code):
    for script_id in script_list:
        if script_list[script_id][1] == code:
            return script_id
    return -1
