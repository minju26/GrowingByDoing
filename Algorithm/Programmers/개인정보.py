from datetime import datetime, date

def dateCal(fdate, term):
    y, m, d = map(int, fdate.split("."))
    term = int(term)
    
    if d != 1:
        d -= 1
    else: 
        d = 28
        m -= 1
    
    if (m+term)%12 == 0:
        m = 12
        y += int((m+term)/12)
    else:
        y += int((m+term)/12)
        m += int((m+term)%12)
    
    print(m+term, y, m)
    due = date(y, m, d)
    return due
    

def solution(today, terms, privacies):
    answer = []
    today = datetime.strptime(today, "%Y.%m.%d").date()
    dic_terms = {}
    
    for t in terms:
        k, v = t.split()
        dic_terms[k] = v
        
    for n in privacies:
        fdate, term = n.split()
        due = dateCal(fdate, dic_terms[term])
        
        if due < today: answer.append(privacies.index(n)+1)
        
    return answer

# solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
# solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])



'''
틀렸습니다
- m이 0이 되는 경우에 대한 처리. 이 경우 실제 달은 12월이 되어야 하며, 연도도 1년 줄어들어야 함.
- privacies.index(n)+1 사용. 같은 값이 여러 번 나타날 경우 잘못된 인덱스를 반환, 리스트를 매번 검색하므로 시간 복잡도가 높아짐. 대신 enumerate 함수를 사용하여 인덱스를 직접 관리.
'''