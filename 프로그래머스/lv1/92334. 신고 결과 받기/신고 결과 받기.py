def solution(id_list, report, k):
    mail = {key: 0 for key in id_list}
    reported = {key: 0 for key in id_list}
    report = list(set(report))
    
    for r in report:
        a, b = r.split(' ')
        reported[b] += 1
        
    for r in report:
        a, b = r.split(' ')
        if reported[b] >= k:
            mail[a] += 1
            
    return list(mail.values())