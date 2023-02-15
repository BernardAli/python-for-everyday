import camelot

tables = camelot.read_pdf("Test.pdf", pages='68')
print(tables)

tables.export('foot.csv', f='csv', compress=True)
tables[1].to_csv('foo.csv')