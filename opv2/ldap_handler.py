from opv2 import ldap_server
from ldap3 import Connection, SAFE_SYNC


def get_trida_path():
    conn = Connection(ldap_server, "op@sps-pi.cz", "***", client_strategy=SAFE_SYNC, auto_bind=True)

    status, result, response, _ = conn.search('OU=Studenti,ou=uzivatele,ou=skola,dc=sps-pi,dc=cz',
                                              '(samaccountname=*)', attributes=["OU","CN", "description"])

    tridy = []

    for res in response:  # Jenom zaci
        if len(res.get("attributes").get("cn")) == 2:
            tridy.append(res.get("attributes").get("cn"))

    #print(tridy)
    return_list=[]
    for res in response:  # Jenom zaci
        trida = res.get("dn").split("=")[1].split(",")[0]
        if trida in tridy:
            path_trida = res.get("dn")[6:]
            return_list.append(path_trida)
    return return_list

def insert_students(paths):
    conn = Connection(ldap_server, "op@sps-pi.cz", "B7Jx&vG{eFu:9dH(", client_strategy=SAFE_SYNC, auto_bind=True)
    output = []
    for path in paths:
        status, result, response, _ = conn.search(path, '(samaccountname=*)', attributes=["name", "userPrincipalName"])
        rocnik = path.split("=")[1].split(",")[0].split("_")[0]
        trida = {"trida": "", "rocnik": rocnik, "students": []}
        for res in response:
            student = {"name": "", "surname": "", "email": ""}
            if res.get("attributes").get("userPrincipalName") == []:
                if not "wifi" in res.get("attributes").get("name"):
                    student_trida = res.get("attributes").get("name")
                    trida["trida"] = student_trida
                else:
                    continue
            else:
                student_name = " ".join(res.get("attributes").get("name").split()).split()[1]
                student["name"] = student_name
                student_surname = " ".join(res.get("attributes").get("name").split()).split()[0]
                student["surname"] = student_surname
                student_email = res.get("attributes").get("userPrincipalName")
                student["email"] = student_email
                trida["students"].append(student)
        output.append(trida)
    return output

def insert_ucitele():
    output = []
    conn = Connection(ldap_server, "op@sps-pi.cz", "B7Jx&vG{eFu:9dH(", client_strategy=SAFE_SYNC, auto_bind=True)

    status, result, response, _ = conn.search('OU=Ucitele,ou=uzivatele,ou=skola,dc=sps-pi,dc=cz',
                                              '(samaccountname=*)', attributes=["displayName", "userPrincipalName"])
    for res in response:
        ucitel = {"name": "", "surname": "", "email": ""}
        ucitel_name = " ".join(res.get("attributes").get("displayName").split()).split()[1]
        ucitel["name"] = ucitel_name
        ucitel_surname = " ".join(res.get("attributes").get("displayName").split()).split()[0]
        ucitel["surname"] = ucitel_surname
        ucitel_email = res.get("attributes").get("userPrincipalName")
        ucitel["email"] = ucitel_email
        output.append(ucitel)

    status, result, response, _ = conn.search('OU=Vedení,ou=uzivatele,ou=skola,dc=sps-pi,dc=cz',
                                              '(samaccountname=*)', attributes=["displayName", "userPrincipalName"])
    for res in response:
        ucitel = {"name": "", "surname": "", "email": ""}
        ucitel_name = " ".join(res.get("attributes").get("displayName").split()).split()[1]
        ucitel["name"] = ucitel_name
        ucitel_surname = " ".join(res.get("attributes").get("displayName").split()).split()[0]
        ucitel["surname"] = ucitel_surname
        ucitel_email = res.get("attributes").get("userPrincipalName")
        ucitel["email"] = ucitel_email
        output.append(ucitel)
    return output