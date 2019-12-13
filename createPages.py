def createPage(page_name):
	#create hbs
	try:
		f = open("./src/templates/"+page_name+".hbs","x")
		f = open("./src/templates/"+page_name+".hbs","w+")
		f.write('{{> header }}')
		f.close();
	except:
		print("HBS file already exists! Updating other files")

	#create js

	try:
		f = open("./src/pages/"+page_name+".js","x")
		f = open("./src/pages/"+page_name+".js","w+")
		f.write('import App from \'../lib/App\';\n\nconst ' + page_name + 'Template = require(\'../templates/'+page_name+'.hbs\');\n\nexport default () => {\n\tconst title = \''+page_name+' automatic\';\n\n\tApp.render('+page_name+'Template({ title }));\n\tApp.router.navigate(\'/'+page_name+'\');\n};\n')
		f.close();
	except:
		print("JS file already exists! Updating other files")

	#add route

	f = open("./src/routes.js", 'r')
	lines = f.readlines()
	insert_indexes = []
	for index in range(0, len(lines)):
		if lines[index] == '\n' and index != 0:
			insert_indexes.append(index)
			
		if lines[index] == '];\n':
			insert_indexes.append(index-1)
	import_string = 'import '+page_name.capitalize()+' from \'./pages/'+page_name+'\';\n';
	object_string = '\t{ path: \'/'+page_name+'\', view: '+page_name.capitalize()+' },\n';

	if import_string in lines:
		if object_string in lines:
			print("Routes already up to date.")
	else:
		if object_string in lines:
			print("Added import_string to routes")
		else:
			print("Added object_string to routes")		
	lines.insert(insert_indexes[0], import_string)
	lines.insert(insert_indexes[1], object_string)

	f = open("./src/routes.js", 'w')
	for line in lines:
		f.write(line)

	f.close();

input_string = input("type all pages you want to add seperated by spaces. MUST USE CAMELCASE")
pages = input_string.split(' ')
print(pages)
for page in pages:
	createPage(page)