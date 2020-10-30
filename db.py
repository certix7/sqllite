







#!/usr/bin/python3


import sqlite3

def insert(db, row):
    db.execute('insert into test (alpha, bravo) values (?, ?)', (row['alpha'], row['bravo']))
    db.commit()

def retrieve(db, alpha):
    cursor = db.execute('select * from test where alpha = ?', (alpha,))
    return cursor.fetchone()

def update(db, row):
    db.execute('update test set bravo = ? where alpha = ?', (row['bravo'], row['alpha']))
    db.commit()

def delete(db, alpha):
    db.execute('delete from test where alpha = ?', (alpha,))
    db.commit()

def disp_rows(db):
    cursor = db.execute('select * from test order by alpha')
    for row in cursor:
        print('  {}: {}'.format(row['alpha'], row['bravo']))

def main():
    db = sqlite3.connect('test.db')
    db.row_factory = sqlite3.Row
    print('Create table test')
    db.execute('drop table if exists test')
    db.execute('create table test ( alpha text, bravo int )')

    print('Create rows')
    insert(db, dict(alpha = 'one', bravo = 1))
    insert(db, dict(alpha = 'two', bravo = 2))
    insert(db, dict(alpha = 'three', bravo = 3))
    insert(db, dict(alpha = 'four', bravo = 4))
    disp_rows(db)

    print('Retrieve rows')
    print(dict(retrieve(db, 'one')), dict(retrieve(db, 'two')))

    print('Update rows')
    update(db, dict(alpha = 'one', bravo = 101))
    update(db, dict(alpha = 'three', bravo = 103))
    disp_rows(db)

    print('Delete rows')
    delete(db, 'one')
    delete(db, 'three')
    disp_rows(db)

if __name__ == "__main__": main()
