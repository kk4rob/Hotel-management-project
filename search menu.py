import mysql.connector as mydb
from datetime import datetime
import tabulate as tabulate

con=mydb.connect(host="localhost",user="root",passwd="",database="Hotel management")
cur=con.cursor()
def sql_query(query,params=None):
    cur.execute(query,params or ())
    result=cur.fetchall()
    if result:
        print("==•○•♦DATA FOUND♦•○•===")
        print(tabulate.tabulate(result,tablefmt="fancy_grid"))
    else:
        print("\n ==#•○DATA NOT FOUND○•#==")
def search_date():
    while True:
        menu3=[["1","Search by Date:"],
               ["2","Search by Month:"],
               ["3","Search by Year:"],
               ["4","Exit"]]
        headers3=["OPTIONS","descriptions"]
        print(tabulate.tabulate(menu3,headers=headers3,tablefmt="simple_grid"))
        
        cho=input("Enter a option:")
        if cho=='1':
            while True:
                print("\n ○--○•○•DATE MENU○•○•--○")
                dmenu=[["1","Exect date"],
                       ["2","Date Range"],
                       ["3","Exit"]]
                headers4=["Option","Descpt."]
                print(tabulate.tabulate(dmenu,headers=headers4,tablefmt="simple_grid"))
                mch1=input("Enter a option:")
                if mch1=='1':
                    
                    da=input("Enter the exect date(DD-MM-YYYY):")
                    search_date=datetime.strptime(da,"%d-%m-%Y").date()
                    date_qu=("select * from `daily data` where `Date of entry`=%s;")
                    cur.execute(date_qu,[search_date])
                    r5=cur.fetchall()
                    if r5:
                        print("==♦Date of entry founded♦===")
                        print(tabulate.tabulate(r5,tablefmt="simple_grid"))
                    else:
                            print("*== Data not found *==")
                elif mch1=='2':
                    da1=input("Enter start date(DD-MM-YYYY):")
                    da2=input("Enter end date(DD-MM-YYYY):")
                    search_date1=datetime.strptime(da1,"%d-%m-%Y").date()
                    search_date2=datetime.strptime(da2,"%d-%m-%Y").date()
                    date_que=("select * from `daily data` where (`Date of entry`) BETWEEN %s AND %s;")
                    sql_query(date_que,(search_date1,search_date2))
                elif mch1=='3':
                    break
                else:
                    print("please try again..!")
                
                
        elif cho=='2':
            while True:
                print("\n ○•○---○•MONTH MENU○•---○•○")
                mmenu=[["1","Exect Month"],
                       ["2","Months range"],
                       ["3","Exit"]
                        ]
                headers5=["Option","Descpt."]
                print(tabulate.tabulate(mmenu,headers=headers5,tablefmt="simple_grid"))
                mch=input("Enter a option:")
                if mch=='1':
                    mt=input("\n enter month (1-12):")
                    mtsl=("select * from `daily data` where MONTH(`Date of entry`)=%s;")
                    sql_query(mtsl,[mt])
                    
                elif mch=='2':
                    while True :
                        print("=---○•SEARCH BY MONTH RANGE:•○---=")
                        mmenu2=[["1","Month with day"],
                              ["2","Month with Date Range"],
                              ["3","Month Range"],
                              ["4","Month Range with Date"],
                              ["5","Month Range with Date Range"],
                                ["6","Exit"]]
                        headers6=["Option","Descpt"]
                        print(tabulate.tabulate(mmenu2,headers=headers6,tablefmt="simple_grid"))
                        mo=input(" Enter a option:")
                        if mo=='1':
                            mn=input("Enter month (MM)(1-12):")
                            d1=input("Enter day DD(1-30):")
                            d2=("select* from `daily data` where MONTH(`Date of entry`)=%s AND DAY(`Date of entry`)=%s;")
                            sql_query(mnq,(mn,mnd))
                                
                        elif mo=='2':
                            mt=input("Enter Month (MM)(1-12):")
                            dm=input("Enter start day (DD)(1-30):")
                            dme=input("Enter end day  (DD)(1-30):")
                            dmeq=("select* from `daily data` where MONTH(`Date of entry`)=%s AND DAY(`Date of entry`)BETWEEN %s AND %s;")
                            sql_query(dmeq,(mt,dm,dme))
                        elif mo=='3':
                            m1=input("Enter start month (MM) (1-12):")
                            m2=input("Enter end month (MM) (1-12):")
                            m12q=("select* from `daily data` where MONTH(`Date of entry`)BETWEEN %s AND %s;")
                            sql_query(m12q,(m1,m2))
                        elif mo=='4':
                            mr1=input("Enter start month (MM) (1-12):")
                            mr2=input("Enter end month (MM) (1-12):")
                            dr1=input("Enter day (DD) (1-30):")
                            medql=("select * from `daily data` where MONTH(`Date of entry`)BETWEEN %s AND %s  AND DAY(`Date of entry`)=%s ;")
                            sql_query(medql,(mr1,mr2,dr1))
                        elif mo=='5':
                            mrg=input("Enter start month (MM) (1-12):")
                            mrg1=input("Enter end month (MM) (1-12):")
                            drg=input("Enter start day (DD) (1-30):")
                            drg1=input("Enter end day (DD) (1-30):")
                            mdg=("select* from `daily data` where MONTH(`Date of entry`)BETWEEN %s AND %s AND DAY(`Date of entry`)BETWEEN %s AND %s")
                            sql_query(mdg,(mrg,mrg1,drg,drg1))
                        elif mo=='6':
                            break
                elif mch=='3':
                    break
        elif cho=='3':
            while True:
                print("\n-===•○YEAR MENU○•===-")
                menuy=[["1","Exect Year"],
                       ["2","Year Range"],
                       ["3","Exit"]]
                headers8=["Option","Descpt."]
                print(tabulate.tabulate(menuy,headers=headers8,tablefmt="simple_grid"))
            
                yr=input("\n Enter a option:")
                if yr=='1':
                    yrx=input("Enter the year:")
                    yrxq=("select * from `daily data` where YEAR(`Date of entry`)=%s")
                    sql_query(yrxq,[yrx])
                elif yr=='2':
                    while True:
                        print("---* SEARCH BY YEAR RANGE *---")
                        ymenu=[["A","Year with Month"],
                              ["B","Year (Range)"],
                              ["C","Year (Range) with Month"],
                              ["D","Year (Range) with Month (Range)"],
                              ["E","Year (Range) with Month (Range) and Day"],
                              ["F","Year (Range) with Month (Range) and Day (Range)"],
                               ["3","Exit"]]
                        headers7=["Option","Descpt."]
                        print(tabulate.tabulate(ymenu,headers=headers7,tablefmt="simple_grid"))
                        yxd=input("\n Enter a option:")
                        if yxd=='A' or yxd=='a':
                            ywd=input("Enter the year (YYYY):")
                            ymm=input("Enter the Month (MM) (1-12):")
                            yxdq=("select * from `daily data` where YEAR(`Date of entry`)=%s AND MONTH (`Date of entry`)=%s;")
                            sql_query(yxdq,(ywd,ymm))
                        elif yxd=='B'or yxd=='b':
                            yrg=input("Enter start year (YYYY):")
                            yrg1=input("Enter end year (YYYY):")
                            yrgq=("select * from `daily data` where YEAR(`Date of entry`)BETWEEN %s AND %s;")
                            sql_query(yrgq,(yrg,yrg1))
                        elif yxd=='C' or yxd=='c':
                            yrd=input("Enter start Year (YYYY):")
                            yrd1=input("Enter end Year (YYYY):")
                            yrd2=input("Enter the month(MM),(1-12):")
                            yrdq=("select * from `daily data` where YEAR(`Date of entry`)BETWEEN %s AND %s AND MONTH(`Date of entry`)=%s;")
                            sql_query(yrdq,(yrd,yrd1,yrd2))
                        elif yxd=='D' or yxd=='d':
                            yrdr=input("Enter start  year (YYYY)")
                            yrdr1=input("Enter end Year (YYYY):")
                            myr=input("Enter start month(MM),(1-12):")
                            myr1=input("Enter end month(MM),(1-12):")
                            yrmyq=("select * from `daily data` where YEAR(`Date of entry`)BETWEEN %s AND %s AND MONTH(`Date of entry`)BETWEEN %s AND %s;") 
                            sql_query(yrmyq,(yrdr,yrdr1,mry,mry1))
                        elif yxd=='E' or yxd=='e':
                            ydr=input("Enter start  year (YYYY)")
                            ydr1=input("Enter end Year (YYYY):")
                            mry=input("Enter start month(MM),(1-12):")
                            mry1=input("Enter end month(MM),(1-12):")
                            ydd=input("Enter the day (DD),(1-30):")
                            ydrsql=("select * from `daily data` where YEAR(`Date of entry`)BETWEEN %s AND %s AND MONTH(`Date of entry`)BETWEEN %s AND %s AND DAY (`Date of entry`)=%s;")
                            sql_query(ydrsql,(ydr,ydr1,mry,mry1,ydd))
                        elif yxd=='F' or yxd=='f':
                            yf=input("Enter start  year (YYYY)") 
                            yf1=input("Enter end Year (YYYY):")
                            mfy=input("Enter start month(MM),(1-12):")
                            mfy1=input("Enter end month(MM),(1-12):")
                            yfd=input("Enter the starting day (DD),(1-30):")
                            yfd1=input("Enter the ending day (DD),(1-30):")
                            yfql=("select * from `daily data` where YEAR(`Date of entry`)BETWEEN %s AND %s AND MONTH(`Date of entry`)BETWEEN %s AND %s AND DAY (`Date of entry`)BETWEEN %s AND %s;")
                            sql_query(yfql,(yf,yf1,mfy,mfy1,yfd,yfd1))
                        elif yxd=='3':
                            break
                elif yr=='3':
                    break
        else:
            if cho=='exit' or cho=='4':
                print("\n.##..Moving back to SEARCH Menu.##..")
                break
def DailyData():
    try:
        q="select *from `daily data`;"
        k="select count(*)  as ' Total peoples in Hotel' from `daily data`;"
        
        cur.execute(q)
        s=cur.fetchall()
        headers=[r[0] for r in cur.description]
        print(tabulate.tabulate(s,headers=headers,tablefmt="fancy_outline"))
        
        cur.execute(k)
        j=cur.fetchall()
        
        #headers=[r[0] for r in cur.description]
        #print(tabulate.tabulate(s,headers=headers,tablefmt="fancy_outline"))

        headers=[i[0] for i in cur.description]
        print(tabulate.tabulate(j,headers=headers,tablefmt="simple_grid"))
        while True:
            print("\n ---•♦○SEARCH FOR RECORD'S•♦○---")
            print("\n     •♦○♣○SEARCH MENU○♣○♦•")
            menu2=[["1","Search for Name"],
                   ["2","Search for Custemor ID"],
                   ["3","Search for Room Number"],
                   ["4","Search for phone Number"],
                   ["5","Search for Date of Entry"],
                   ["6","Exit"]
                   ]
            headers1=["OPTIONS","Descriptions"]
            print(tabulate.tabulate(menu2,headers=headers1,tablefmt="simple_grid"))

            r=(input("\n Enter a option:"))
            if r=='1' or r=='name':
                na=input("\nEnter name:")
                R="select * from`daily data`where name like %s;"
                cur.execute(R,['%'+na+'%'])
                r1=cur.fetchall()
                if r1:
                    print("\n ○•☻•Name found•☻•○")
                    print(tabulate.tabulate(r1,tablefmt="simple_grid"))
                else:
                    print("\n*--•○♣Name not found•○♣--*")
            elif r=='2' or r=='Id' or r=='id':
                cu=input("Enter customer ID:")
                R1=("select * from `daily data` where `customer ID`= %s ;")
                cur.execute(R1,[cu])
                r2=cur.fetchall()
                if r2:
                    print("#== ID found ==#")
                    print(tabulate.tabulate(r2,tablefmt="simple_grid"))
                else:
                    print("*== ID not found ==*")
            elif r=='3'or r=='room number':
                Rn=int(input("Enter room number:"))
                R2=("select * from `daily data` where `Room number` =%s;")
                cur.execute(R2,[Rn])
                r3=cur.fetchall()
                if r3:
                    print("#== Room found ==#")
                    print(tabulate.tabulate(r3,tablefmt="simple_grid"))
                else:
                    print("*== Room not found ==*")
            elif r=='4'or r=='number'or r=='phone':
                pn=int(input("Enter phone number:"))
                R3=("select *from `daily data` where Number =%s;")
                cur.execute(R3,[pn])
                r4=cur.fetchall()
                if r4: 
                    print("#== Number found ==#")
                    print(tabulate.tabulate(r4,tablefmt="simple_grid"))
                else:
                    print("*== Number mis-match ==*")
            elif r=='5'or r=='date':
                search_date()
    #
            elif r=='6' or r=='exit'or r=='next'or r=='first menu':
                print("Exiting..☻..byee...☺")
                break
    except Exception as e4:
        print(e4,"please try again...!")
        Dailydata()

def extra_person():
        try:
            e=int(input("\nEnter customer's Total Number of Extra Persons:"))
            for y in range(e):
                        ak=[["1","Family"],
                            ["2","Friend"]]
                        head=["opt.","Menu"]
                        print(tabulate.tabulate(ak,headers=head,tablefmt="fancy_grid"))
                        opt=int(input("Enter a option:"))
                        if opt== 1:
                           sk1=int(input("Enter Total Number of Family's:"))
                           relt="Family"
                           for yz in range(sk1):
                               fname=(input("Enter Family Member name:"))
                               fnum=int(input("Enter the Member's contact number:"))
                               fsty=input("Name of registered person (with whome the Family member is):")
                               fs1t=int(input("Enter room number:"))
                               fadds=input("Enter the address of the Member:")
                               yzsql=("insert into `extra persons`(Name,Contact,`Staying with`,Relation,Address,`Room No.`)values(%s,%s,%s,%s,%s,%s);")
                               yzsql2=(fname,fnum,fsty,relt,fadds,fs1t)
                               cur.execute(yzsql,yzsql2,)
                               con.commit()
                               #print("Data saved...\n")
                        else:
                                if opt== 2:
                                        sk2=int(input("Enter number of friend's:"))
                                        relt2="Friend"
                                        for yz2 in range(sk2):
                                            fname2=input("Enter Friend name:")
                                            fnum2=int(input("Enter Friend contact number:"))
                                            fsty2=input("Name of registered person (with whome extra person is):")
                                            fs2t=int(input("Enter room number:"))
                                            fadds2=input("Enter the address of friend:")
                                            faddsql=("insert into `extra persons`(Name,Contact,`Staying with`,Relation,Address,`Room No.`)values(%s,%s,%s,%s,%s,%s);")
                                            faddsql2=(fname2,fnum2,fsty2,relt2,fadds2,fs2t)
                                            cur.execute(faddsql,faddsql2,)
                                            con.commit()
                                            #print("Data saved...\n")
        except Exception as e:
                print(e,"\n<--___*Please try again*___-->")
                print()
                extra_person()

                

def Entry():
    try:
        b1=int(input("Enter total no.of Entry's you want to make:"))
        for b12 in range(b1):
            #b=datetime.now().time()
            c=input("Enter customer name:")
            d=int(input("Enter customer phone number:"))
            f=input("Enter customer Adress:")
            g=datetime.now().date()
            i=int(input("Enter customer Room number:"))
            h=datetime.now().strftime("%H:%M:%S")
            p=input("Enter the Cheak Out Time: yyyy-mm-dd HH:MM:")
            e=int(input("Enter total no. of extra persons,(If not enter 0):"))
            if e!= 0:
                extra_person()#here if type 0 then data saved but the loop of b1 get break (also if e=! the data dont get saved)
            q=("insert into`daily data`(Name,Number,`Extra person's`,Address,`Date of entry`,`Time of entry`,`Room number`,`cheak out time`)values(%s,%s,%s,%s,%s,%s,%s,%s);")
            k=(c,d,e,f,g,h,i,p)
            cur.execute(q,k)
            con.commit()
            print("Data saved...")
            break
            
    except Exception as e2:
        print(e2,"<__Please try again__>")
        print()
        Entry()
# improve the entry function the extra person taking same input 3 time ,also to add room number in extra person automatic while the person entry
#and to show the extra person in the details with the one person serching for.auto add the details of the person with.
#to delete the extra person record with the main person room number

#pk1=int(input("\nEnter total number of customer's for Cheak Out/Temp.Out:"))
def Exit():
    try:
        pk1=int(input("\nEnter total number of customer's for Cheak Out/Temp.Out:"))
        for pk11 in range(pk1):
            prk=[["1","Cheak out"],
                 ["2","Temporary OUT/IN"],
                 ["3","Cancel"]]
            prk1=["Opt.","Menu"]
            print(tabulate.tabulate(prk,headers=prk1,tablefmt="fancy_grid"))
            choice=int(input("enter a option:"))
            if choice== 1:
                cid=(input("\nEnter the Customer's-Room No. to make cheak Out:"))
                ci2d=cid.split(" ")#so to make many customers out in single entry
                for cid1d in ci2d:
                    
                    R1=("select * from `daily data` where `Room number` =%s;")
                    cur.execute(R1,[cid1d])
                    data=cur.fetchall()
                    data=[tuple(row)for row in data]
                    #adding data from daily data table to cheak out table
                    que2=("insert into `cheak out peoples` (`customer ID`,Name,Number,`Extra person`,Address,`Date of entry`,`Time of entry`,`Room number`,`cheak out time`,Status) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);")
                    cur.executemany(que2,data)
                    con.commit()
                    #r1q="select* form `extra persons` where `Room No.`=%s;"
                    #cur.execute(r1q,[cid1d])
                    #datar1=cur.fetchall()
                    #datar1=[tuple(row)for row in datar1]
                    #inserting data of given customer extra person(table) into cheak out table 
                    #qur1=("""insert into `cheak out peoples`
                    #      (`customer ID`,Name,Number,`Extra person`,Address,`Date of entry`,
                     #      `Time of entry`,`Room number`,`cheak out time`,Status)
                      #    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""")
                    #cur.executemany(qur1,datar1)
                    #con.commit()
                    #deleting data from extra person table through room no.
                    #qur3="delete from`extra persons` where `Room No.`=%s;"
                    #cur.execute(qur3,[cid1d])
                    #con.commit()
                    qur331="update `extra person set status='OUT' where`room no.` =%s"
                    cur.execute(qur331,[cid1d])
                    con.commit()
                    #deleting data from daily data table through room no.
                    que3=("delete from `daily data` where `Room number`=%s;")
                    cur.execute(que3,[cid1d])
                    con.commit()
                    #changing the status in cheak out table =out &also its set to be default 
                    que4="update `cheak out peoples` set status='OUT' where `Room number`=%s;"
                    cur.execute(que4,[cid1d])
                    con.commit()
                #ci2d=cid.split(" ")
                #for cid1d in ci2d:
                   # cique="delete from `daily data` where `Room number`=%s"
                  #  cur.execute(cique,[cid1d])
                    #con.commit()
                print("\ncheak out successfully......")

                main()
            elif choice== 2:
                while True:
                    print("\nTemporary:\n         1)Out\n         2)IN\n         3)Cancle")
                    cid11=(input("\nEnter a option:"))
                    if cid11 == '1' or cid11=='out':
                            cid1=(input("Enter the Customer-Room No.to make Temporary Out :"))
                            cid136=cid1.split(" ")#to make more then one customer out at ones
                            for cid1d2 in cid136:
                        
                                R11=("select * from `daily data` where `Room number` =%s;")
                                cur.execute(R11,[cid1d2])
                                data1=cur.fetchall()
                                data1=[tuple(row)for row in data1]
                                que21=("insert into `cheak out peoples` (`customer ID`,Name,Number,`Extra person`,Address,`Date of entry`,`Time of entry`,`Room number`,`cheak out time`,Status) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);")
                                cur.executemany(que21,data1)
                                con.commit()
                                #to put data of extra person in cheak out table
                                #r111="select * from `extra persons` where `Room No.`=%s;"
                                #cur.execute(r111,[cid1d2])
                                #data12=cur.fetchall()
                                #data12=[tuple(row)for row in data12]
                                #qeu1=("""insert into `cheak out peoples`
                                #(Name,Contact,` Staying with`,Relation,Address,
                                 #`Room number`,Status) values(%s,%s,%s,%s,%s,%s,%s);""")
                                #cur.executemany(qeu1,data12)
                                #con.commit()
                                que211="update `cheak out peoples` set status='Temp.Out' where `Room number` =%s;"
                                cur.execute(que211,[cid1d2])
                                con.commit()
                                #updating the status of extra person in his table 
                                qeu21="update `extra persons` set Status='Temp.out' where `Room no.` =%s;"
                                cur.execute(qeu21,[cid1d2])
                                con.commit()
                                que2111=("update `daily data` set status='Temp.Out' where `Room number` =%s;")
                                cur.execute(que2111,[cid1d2])
                                con.commit()
                                print(" Temp.out successfully......")
                    elif cid11== '2' or cid11=='in':
                            cid12=(input("\nEnter the Customer-Room No. to make IN :"))
                            cid139=cid12.split(" ")
                            for cid1d29 in cid139:
                                que31=("delete from `cheak out peoples` where `Room number` =%s;")
                                cur.execute(que31,[cid1d29])
                                con.commit()
                                #updating status as IN
                                que311=("update `daily data` set status='IN' where `Room number`=%s;")
                                cur.execute(que311,[cid1d29])
                                con.commit()
                                que1123=("update `extra persons` set Status='IN' where `Room No.`=%s;")
                                cur.execute(que1123,[cid1d29])
                                con.commit()
                                print("Again IN successfully...")
                    elif cid11=='3':
                        main()
                    else:
                        print("\n!Alert!:please Enter a valid option..!")
            elif choice== 3:
                main()
            else:
                print("Invalid option please try again...!\n")
                Exit()
           # if pk1=='e':
              #  break
    except Exception as e2:
        print("error!:",e2,"\n<---please try again...!--->")
        Exit()
    finally:
       Exit()
print3=[["Namasta Aapka Hamara Hotel Management System Mai Sawaggat Hai...♥☻♥"],
            ["Welcome To Our Hotel Management System ♥☺♥...\n"]]
j2=["                   ***__MOST WELCOME__***"]
print(tabulate.tabulate(print3,headers=j2,tablefmt="double_grid"))
def cheakout():
    chk1=("select * from `cheak out peoples`;")
    cur.execute(chk1)
    chk2=cur.fetchall()
    hrd=[r[0] for r in cur.description]
    print(tabulate.tabulate(chk2,headers=hrd,tablefmt="fancy_grid"))

            
def main():
    while True:
#
                print("\n       *○•♦•MENU•♦•○*")
                menu=[["1","Show Daily Data, (search menu)"],
                      ["2","Check-IN (Entry)"],
                      ["3","Check-OUT"],
                       ["4","Show check-out Data"],
                      ["5","Exit"]
                      ]
                headers=["OPTION","Descriptions"]
                print(tabulate.tabulate(menu,headers=headers,tablefmt="simple_grid"))
                
                z=input(" Enter a option :")
                if z=='1'or z=='show'or z=='show data'or z=='daily data'or z=='show daily data' or z=='data' or z=='table' or z=='show table':
                    DailyData()
                elif z=='2' or z=='entry' or z=='store'or z=='record'or z=='add'or z=='Add':
                    Entry()
                elif z=='3' or z=='cheak out'or z=='out'or z=='Exit'or z=='Cheak out'or z=='Cheak Out' or z=='cheak Out'or z=='CHEAK OUT'or z=='exit':
                    Exit()
                elif z=='4' or z=='check out data':
                    cheakout()
                elif z=='5'or z=='exit':
                    break
                    
                else:
                    print("Invelid option..!")
main()


#improve the serch by date month year menues ok.!










