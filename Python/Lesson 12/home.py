import re


class DateTypeException(Exception):
    """
    """
    pass

class CountryCodeException(Exception):
    """
    """
    pass

patterns = {
    'pattern1': [r"(\d{4})-(\d{1,2})-(\d{1,2})","YMD", "PL", "SW", "LT", "CA", "KNR"],
    'pattern2': [r"(\d{4})\.\s(\d{1,2})\.\s(\d{1,2})","YMD", "UG"],
    'pattern3': [r"(\d{4})/(\d{2})/(\d{2})","YMD", "IRN", "JAP"],
    'pattern4': [r"(\d{4})-(\d{1,2})-(\d{1,2})","YMD", "KNR"],
    'pattern5': [r"(\d{4})/(\d{1,2})/(\d{1,2})","YMD", "GON", "TAIV"],
    'pattern6': [r"(\d{1,2}).(\d{1,2}).(\d{4})","DMY", "FIN", "CHZ"],
    'pattern7': [r"(\d{1,2})-(\d{1,2})-(\d{4})","DMY", "NETH"],
    'pattern8': [r"(\d{1,2})/(\d{1,2})/(\d{4})","DMY", "BRA", "GR", "TAIL"],
    'pattern9': [r"(\d{2}).(\d{2}).(\d{4})","DMY", "BLG", "GR", "NORW", "ROM", "RUS", "TUR", "UA"],
    'pattern10': [r"(\d{2})-(\d{2})-(\d{4})","DMY", "DEN", "POR"],
    'pattern11': [r"(\d{2})/(\d{2})/(\d{4})","DMY", "GB", "VET", "ISR", "IND", "SP", "IT", "FR"],
    'pattern12': [r"(\d{1,2})/(\d{1,2})/(\d{4})","MDY", "US"]
}


def get_date(date_string, country):
    try: 
        date_match = ''
        country_flag = False
        date_flag = False
        if date_string != "": 
            date_flag = True
            for pattern in patterns:
                if country in patterns[pattern]:
                    re_pattern = re.compile(patterns[pattern][0])
                    country_flag = True
                    date_match = re_pattern.findall(date_string)
                    if date_match == []:
                        raise DateTypeException("Incorrect date type for this country")
                    else:
                        if patterns[pattern][1] == "YMD": return f"{date_match[0][0]}-{date_match[0][1] if len(date_match[0][1]) == 2 else '0'+date_match[0][1]}-{date_match[0][2]}"
                        elif patterns[pattern][1] == "DMY": return f"{date_match[0][2]}-{date_match[0][1] if len(date_match[0][1]) == 2 else '0'+date_match[0][1]}-{date_match[0][0]}"
                        elif patterns[pattern][1] == "MDY": return f"{date_match[0][2]}-{date_match[0][0]}-{date_match[0][1] if len(date_match[0][1]) == 2 else '0'+date_match[0][1]}"
                    break
                else:
                    continue
        else:
            raise DateTypeException("Incorrect date type")

        if not date_flag:
            raise DateTypeException("Incorrect date type")
        elif not country_flag:
            raise CountryCodeException("Incorrect country code")
    except Exception as e:
        return e


print(get_date("2006-05-04", "PL"))
print(get_date("2006/05/04", "IRN"))
print(get_date("4/5/2006", "BRA"))
print(get_date("2006-5-4", "KNR"))
print(get_date("2006/05/04", "PL"))
print(get_date("", "PL"))
print(get_date("2006-05-04", "PT"))