import datetime

from opv2 import mycursor, mydb
from opv2 import ldap_handler as ldap


class Sql_get:
    def get_user_by_id(self, user_id):
        mycursor.execute(f"""select Id_uzivatel,        # 0
                                    jmeno,              # 1
                                    prijmeni,           # 2
                                    email,              # 3
                                    telefon,            # 4
                                    dat_nar,            # 5
                                    opravneni.nazev,    # 6
                                    obor,               # 7
                                    ulice,              # 8
                                    mesto,              # 9
                                    psc,                # 10
                                    aktualni_trida      # 11
                             from uzivatel
                             join opravneni on opravneni=Id_opravneni
                             where Id_uzivatel=%s""", (user_id,))
        return [element if element else "" for element in mycursor.fetchone()]

    def get_user_by_email(self, user_email):
        mycursor.execute(f"""select Id_uzivatel,        # 0
                                    jmeno,              # 1
                                    prijmeni,           # 2
                                    email,              # 3
                                    telefon,            # 4
                                    dat_nar,            # 5
                                    opravneni.nazev,    # 6
                                    obor,               # 7
                                    ulice,              # 8
                                    mesto,              # 9
                                    psc,                # 10
                                    aktualni_trida      # 11
                                 from uzivatel
                                 join opravneni on opravneni=Id_opravneni
                                 where email=%s""", (user_email,))
        return [element if element else "" for element in mycursor.fetchone()]

    def get_instruktori_by_firma(self, firma_id):
        mycursor.execute(f"""select Id_instruktor,
                                    jmeno
                                    prijmeni
                             from instruktor where firma=%s""", (firma_id,))
        return mycursor.fetchall()

    def get_students_list(self):
        mycursor.execute(f"""select Id_uzivatel,        # 0
                                    jmeno,              # 1
                                    prijmeni,           # 2
                                    email,              # 3
                                    telefon,            # 4
                                    dat_nar,            # 5
                                    opravneni.nazev,    # 6
                                    obor,               # 7
                                    ulice,              # 8
                                    mesto,              # 9
                                    psc,                # 10 
                                    aktualni_trida      # 11
                             from uzivatel 
                             join opravneni on opravneni=Id_opravneni 
                             where nazev='Zak'""")
        return mycursor.fetchall()

    def get_teacher_list(self):
        mycursor.execute(
            f"""select Id_uzivatel,      # 0
                       jmeno,            # 1
                       prijmeni,         # 2
                       email,            # 3
                       telefon,          # 4
                       dat_nar,          # 5  
                       opravneni.nazev   # 6   
                 from uzivatel
                 join opravneni on opravneni=Id_opravneni
                 where nazev='Admin' or nazev='Ucitel'""")
        return mycursor.fetchall()

    def get_company_list_by_category(self, category):
        mycursor.execute(f"""select Id_firma,       # 0
                                    nazev,          # 1
                                    ulice_vykon,    # 2
                                    mesto_vykon,    # 3
                                    psc_vykon,      # 4
                                    ulice_sidlo,    # 5
                                    mesto_sidlo,    # 6
                                    psc_sidlo,      # 7
                                    ICO,            # 8
                                    web,            # 9
                                    IT,             # 10
                                    ELE,            # 11
                                    PROJEKT,        # 12
                                    VOS,            # 13            
                                    cinnost,        # 14
                                    pomucky,        # 15
                                    poznamka        # 16
                                    from firma 
                                    where stav=%s""",
                         (category,))
        return mycursor.fetchall()

    def get_company_list(self):
        mycursor.execute(f"""select Id_firma,       # 0
                                    nazev,          # 1
                                    ulice_vykon,    # 2
                                    mesto_vykon,    # 3
                                    psc_vykon,      # 4
                                    ulice_sidlo,    # 5
                                    mesto_sidlo,    # 6
                                    psc_sidlo,      # 7
                                    ICO,            # 8
                                    web,            # 9
                                    IT,             # 10
                                    ELE,            # 11
                                    PROJEKT,        # 12
                                    VOS,            # 13            
                                    cinnost,        # 14
                                    pomucky,        # 15
                                    poznamka        # 16
                                    from firma""")
        return mycursor.fetchall()

    def get_company_by_id(self, company_id):
        mycursor.execute(f"""select Id_firma,      # 0 
                                    stav,          # 1 
                                    nazev,         # 2 
                                    ICO,           # 3
                                    ulice_vykon,   # 4 
                                    mesto_vykon,   # 5 
                                    psc_vykon,     # 6 
                                    ulice_sidlo,   # 7 
                                    mesto_sidlo,   # 8 
                                    psc_sidlo,     # 9 
                                    web,           # 10 
                                    IT,            # 11 
                                    ELE,           # 12 
                                    PROJEKT,       # 13 
                                    VOS,           # 14  
                                    zastupce,      # 15           
                                    cinnost,       # 16  
                                    pomucky,       # 17 
                                    poznamka       # 18
                             from firma where Id_firma=%s""", (company_id,))
        company = mycursor.fetchone()
        if company:
            company_out = [element if element else "" for element in company]
            return company_out
        else:
            return False

    def get_praxe_by_zak(self, zak):
        mycursor.execute(r"""select Id_praxe,    # 0
                                    firma,       # 1
                                    zak,         # 2
                                    instruktor,  # 3
                                    ucitel,      # 4
                                    trida.nazev, # 5
                                    od,          # 6
                                    do           # 7
                             from praxe 
                             left join trida on Id_trida=trida 
                             where zak=%s""", (zak,))
        return mycursor.fetchone()

    def get_praxe_list(self):
        mycursor.execute("""select distinct trida.nazev,    # 0
                                            od,             # 1
                                            do,             # 2
                                            rok_nastupu     # 3
                                            from praxe join trida on Id_trida=trida""")
        return mycursor.fetchall()

    def get_zaci_in_praxe(self, trida, rok):
        rok = int(rok) - int(trida[1:]) + 1
        mycursor.execute(f"""select uzivatel.Id_uzivatel,   # 0
                                    uzivatel.jmeno,         # 1 
                                    uzivatel.prijmeni,      # 2
                                    firma.nazev,            # 3
                                    instruktor.jmeno,       # 4
                                    instruktor.prijmeni,    # 5
                                    ucitel                  # 6
                                    from praxe
                                    join uzivatel on zak=Id_uzivatel
                                    join trida on trida=Id_trida
                                    left join firma on firma=Id_firma
                                    left join instruktor on instruktor=Id_instruktor
                                    where trida.nazev=%s and trida.rok_nastupu=%s order by uzivatel.prijmeni""",
                         (trida, rok))
        return mycursor.fetchall()

    def get_dny_praxe(self, trida, rok):
        rok = int(rok) - int(trida[1:]) + 1
        mycursor.execute(f"""select Id_praxe 
                             from praxe 
                             join trida on trida=Id_trida
                             where trida.nazev=%s and trida.rok_nastupu=%s""", (trida, rok))
        praxe = mycursor.fetchall()[0]
        mycursor.execute(f"""select distinct datum,
                                             stav,
                                             praxe
                             from den_praxe
                             where den_praxe.praxe=%s""", (praxe[0],))
        return mycursor.fetchall()

    def get_ucitele_in_praxe(self, trida, rok):
        rok = int(rok) - int(trida[1:]) + 1
        mycursor.execute(f"""select distinct Id_uzivatel,
                                             jmeno,
                                             prijmeni
                                             from praxe
                                             join trida on trida=Id_trida 
                                             left join uzivatel on ucitel=Id_uzivatel
                                             where trida.nazev=%s and trida.rok_nastupu=%s order by Id_uzivatel""",
                         (trida, rok))
        return mycursor.fetchall()

    def get_trida(self, trida_id):
        mycursor.execute(f"""select Id_trida,   # 0
                                    nazev,      # 1
                                    rok_nastupu # 2
                             from trida where Id_trida=%s""", (trida_id,))
        return mycursor.fetchone()


class Sql_insert:

    def insert_company(self, company):
        mycursor.execute(f"select * from firma where ICO='{company[1]}'")
        if mycursor.fetchone() is None:
            mycursor.execute(f"""insert into firma (nazev,          # 0
                                                    ICO,            # 1
                                                    mesto_vykon,    # 2
                                                    ulice_vykon,    # 3
                                                    psc_vykon,      # 4
                                                    mesto_sidlo,    # 5
                                                    ulice_sidlo,    # 6
                                                    psc_sidlo,      # 7
                                                    IT,             # 8
                                                    ELE,            # 9
                                                    PROJEKT,        # 10
                                                    VOS,            # 11
                                                    zastupce,       # 12
                                                    web,            # 13
                                                    cinnost,        # 14
                                                    pomucky,        # 15
                                                    poznamka)       # 16
                                 values ({16 * '%s, '} %s)""",
                             (company[0],
                              company[1],
                              company[2],
                              company[3],
                              company[4],
                              company[5],
                              company[6],
                              company[7],
                              company[8],
                              company[9],
                              company[10],
                              company[11],
                              company[12],
                              company[13],
                              company[14],
                              company[15],
                              company[16]))
            mydb.commit()
            return True
        else:
            return False

    def insert_students(self, ldap):
        for trida in ldap:
            mycursor.execute(
                f"select nazev, rok_nastupu from trida where nazev='{trida['trida']}' and rok_nastupu='{trida['rocnik']}'")
            if mycursor.fetchone() is None:
                mycursor.execute(f"insert into trida values (Null, '{trida['trida']}', '{trida['rocnik']}')")
                mydb.commit()
            for students in trida["students"]:
                mycursor.execute(f"select email from uzivatel where email='{students['email']}'")
                if mycursor.fetchone() is None:
                    mycursor.execute(
                        f"insert into uzivatel(stav, jmeno, prijmeni, email, opravneni, aktualni_trida) values (DEFAULT, '{students['name']}', '{students['surname']}', '{students['email']}', 2, (select Id_trida from trida where nazev='{trida['trida']}' and rok_nastupu='{trida['rocnik']}'))")
                    mydb.commit()
                else:
                    mycursor.execute(
                        f"update uzivatel set jmeno='{students['name']}', prijmeni='{students['surname']}', aktualni_trida=(select Id_trida from trida where nazev='{trida['trida']}' and rok_nastupu='{trida['rocnik']}') where email='{students['email']}'")
                    mydb.commit()
        print("Done")

    # import_students(ldap.insert_students(ldap.get_trida_path()))

    def insert_ucitele(self, ldap):
        for ucitel in ldap:
            mycursor.execute(f"select Id_uzivatel, stav from uzivatel where email='{ucitel['email']}'")
            if mycursor.fetchone() is None:
                mycursor.execute(
                    f"""insert into uzivatel (stav, 
                                              jmeno, 
                                              prijmeni, 
                                              email, 
                                              opravneni) 
                        values (DEFAULT, 
                                '{ucitel['name']}', 
                                '{ucitel['surname']}', 
                                '{ucitel['email']}', 
                                3)""")
                mydb.commit()
            else:
                mycursor.execute(
                    f"""update uzivatel set jmeno='{ucitel['name']}', 
                                            prijmeni='{ucitel['surname']}' 
                        where email='{ucitel['email']}'""")
                mydb.commit()

    # import_ucitele(ldap.insert_ucitele())

    def insert_praxe(self, trida, skolni_rok, zacatek, konec):
        rocnik = skolni_rok - int(trida[1:]) + 1
        mycursor.execute(f"select Id_trida from trida where nazev='{trida}' and rok_nastupu='{rocnik}'")
        trida = mycursor.fetchone()[0]
        mycursor.execute(f"select Id_uzivatel from uzivatel where aktualni_trida='{trida}'")

        for student in mycursor.fetchall():
            mycursor.execute(f"select * from praxe where zak='{student[0]}' and trida='{trida}'")
            if mycursor.fetchone() is None:
                mycursor.execute(
                    f"insert into praxe (zak, trida, od, do) values ('{student[0]}', '{trida}', '{zacatek}', '{konec}')")
                mydb.commit()
            else:
                mycursor.execute(f"update praxe set od='{zacatek}', do='{konec}' where zak='{student[0]}' and trida='{trida}'")
                mydb.commit()

            praxe = sql_get.get_praxe_by_zak(student[0])
            zacatek_praxe = praxe[6]
            konec_praxe = praxe[7]
            pocet_dnu = konec_praxe - zacatek_praxe + datetime.timedelta(days=1)
            for i in range(pocet_dnu.days):
                if zacatek_praxe.isoweekday() >= 6:
                    sql_insert.insert_day("vikend", zacatek_praxe, praxe[0])
                else:
                    sql_insert.insert_day("pracovni", zacatek_praxe, praxe[0])
                zacatek_praxe = zacatek_praxe + datetime.timedelta(days=1)

    # create_praxe("B3", 2021, "2022-02-10", "2022-02-20")

    def insert_day(self, stav, den, praxe):
        mycursor.execute(f"select Id_den from den_praxe where praxe='{praxe}' and datum='{den}'")
        id_den = mycursor.fetchone()
        if id_den is None:
            mycursor.execute(f"insert into den_praxe (stav, praxe, datum) values ('{stav}', '{praxe}', '{den}')")
        else:
            mycursor.execute(
                f"update den_praxe set praxe='{praxe}', datum='{den}', stav='{stav}' where Id_den='{id_den}'")
        mydb.commit()

    def insert_ucitel_to_praxe(self, zaci, ucitel):
        for zak in zaci:
            mycursor.execute(
                f"update praxe set ucitel=(select Id_uzivatel from uzivatel where jmeno='{ucitel.split(' ')[0]}' and prijmeni='{ucitel.split(' ')[1]}') where zak={zak}")
        mydb.commit()


class Sql_update:

    def update_company(self, company):
        mycursor.execute(r"""update firma set stav=%s,          # 0
                                              nazev=%s,         # 1
                                              ICO=%s,           # 2
                                              mesto_vykon=%s,   # 3
                                              ulice_vykon=%s,   # 4
                                              psc_vykon=%s,     # 5
                                              mesto_sidlo=%s,   # 6
                                              ulice_sidlo=%s,   # 7
                                              psc_sidlo=%s,     # 8
                                              IT=%s,            # 9
                                              ELE=%s,           # 10
                                              PROJEKT=%s,       # 11
                                              VOS=%s,           # 12
                                              zastupce=%s,      # 13
                                              web=%s,           # 14
                                              cinnost=%s,       # 15
                                              pomucky=%s,       # 16
                                              poznamka=%s       # 17
                                              where Id_firma=%s""",
                         (company[0],
                          company[1],
                          company[2],
                          company[3],
                          company[4],
                          company[5],
                          company[6],
                          company[7],
                          company[8],
                          company[9],
                          company[10],
                          company[11],
                          company[12],
                          company[13],
                          company[14],
                          company[15],
                          company[16],
                          company[17],
                          company[18]))
        mydb.commit()


sql_get = Sql_get()
sql_insert = Sql_insert()
sql_update = Sql_update()
