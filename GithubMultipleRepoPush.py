import os 
from os import system 
import sys 


def restor(user_name,directory):
	## A function that upload multiple repositories to github 

	### user_name: Your Github UserName 
	###directory: Directory that contains  your local repositories 

	Projects=next(os.walk(directory))[1]
	Projects.sort()
	for project in Projects: 
		if(project.strip()=='' or project[0]=='.'):
			continue
		print("Uploading project : ",project)
		os.chdir((directory+project+"/"))
		system("git init")
		system("git add *")
		system("git lfs install")
		system("git lfs track '*.nc'")
		system("git lfs track '*.csv'")
		system('git commit -m "Backup commit"')
		system('git branch -M main')
		system('git remote rm origin ')
		system('git remote add origin https://github.com/{}/{}.git'.format(user_name,project))
		system("git lfs push --all origin master")
		system("git push -u origin main")
		os.chdir("../../")


if len(sys.argv) > 3:
    print('You have specified too many arguments')
    sys.exit()

if len(sys.argv) < 3:
    print('You need to specify the  directory and username')
    sys.exit()

directory = sys.argv[1]
user_name=sys.argv[2]
restor(user_name,directory)
