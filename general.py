import os

#Each website you crawl is a separate project(folder)
def create_project_dir(directory):
	if not os.path.exists(directory):
		print('creating project' +directory)
		os.makedirs(directory)
		
#Create queue and crawled files(if not created)
def create_data_files(project_name,base_url):
	#queue = project_name +'/queue.txt'
	#crawled = project_name+'/crawled.txt'
	queue = os.path.join(project_name , 'queue.txt')
	crawled = os.path.join(project_name,"crawled.txt")
	if not os.path.isfile(queue):
		write_file(queue,base_url)
	if not os.path.isfile(crawled):
		write_file(crawled,'')

#Create a new files 
def write_file(path, data):
	#f = open(path,'w')
	#f.write(data)
	with open(path,'w') as f:
		f.write(data)

#Delete the contents of a file
def delete_file_contents(path):
	open(path,'w').close()
		
#Read a file and convert each line to set items
def file_to_set(file_name):
	results = set()
	with open(file_name,'rt') as f:
		for line in f:
			results.add(line.replace('\n',''))
	return results
	
#Iterate through a set, each item will be a new line in the file
def set_to_file(links,file_name):
	with open(file_name,"w") as f:
		for l in sorted(links):
			l=l.encode('utf-8')
			f.write(l+"\n")
		
