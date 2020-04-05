import shelve

shhelf_file = shelve.open('../resource/my_binary_data')
cats = ['Zophie', 'Pooka', 'Simon']
shhelf_file['cats'] = cats
shhelf_file.close()
