from datetime import datetime
from datetime import timezone

def ordinal(n: int) -> str:
    """
    derive the ordinal numeral for a given number n
    """
    return f"{n:d}{'tsnrhtdd'[(n//10%10!=1)*(n%10<4)*n%10::4]}"

def translate_date(a_date):

    date1 = datetime.date(datetime.fromisoformat(a_date[:-1]).astimezone(timezone.utc))

    dayOrdinal = ordinal(date1.day)
    
    return  date1.strftime(f'%A, {dayOrdinal.strip()} %B %Y')
