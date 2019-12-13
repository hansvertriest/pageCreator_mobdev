def createPage(page_name):
	#create hbs
	f = open("./src/templates/"+page_name+".hbs","w+")
	f.write('{{> header }}')
	f.close();
	#create js
	f = open("./src/pages/"+page_name+".js","w+")
	f.write('import App from \'../lib/App\';\n\nconst ' + page_name + 'Template = require(\'../templates/'+page_name+'.hbs\');\n\nexport default () => {\n\tconst title = \''+page_name+' automatic\';\n\n\tApp.render('+page_name+'Template({ title }));\n\tApp.router.navigate(\'/'+page_name+'\');\n};\n')
	f.close();
	#add route
	f = open("./src/routes.js", 'r')
	lines = f.readlines()
	print lines
	insert_indexes = []
	for index in range(0, len(lines)):
		if lines[index] == '\n':
			insert_indexes.append(index)
			#lines_new.insert(index, 'import '+page_name.capitalize()+' from \'./pages/'+page_name+'\';\n')
			
		if lines[index] == '];\n':
			insert_indexes.append(index+1)
			#lines.insert(index, '{ path: \'/'+page_name+'\', view: '+page_name.capitalize()+'}\n')
		
	lines.insert(insert_indexes[0], 'import '+page_name.capitalize()+' from \'./pages/'+page_name+'\';\n')
	lines.insert(insert_indexes[1], '\t{ path: \'/'+page_name+'\', view: '+page_name.capitalize()+' },\n')

	f = open("./src/routes.js", 'w')
	for line in lines:
		f.write(line)

	f.close();

input_string = raw_input("type all pages you want to add seperated by spaces. MUST USE CAMELCASE")
pages = input_string.split(' ')