import camelot

tables = camelot.read_pdf("Test.pdf", pages='59')
print(tables)

tables.export('foot.csv', f='csv', compress=True)
tables[0].to_csv('foo.csv')