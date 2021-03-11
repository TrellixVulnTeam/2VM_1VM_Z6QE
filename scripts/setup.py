import os
import sys
import json
import random

personas_path = '../data/personas'
NUM           = 50
phase         = '20_50'
personas      = ["News","Sports"]
Ad_Sites      = ['https://en.softonic.com']
IS            = {}

with open("../data/intent.json","r") as file:
	IS = json.load(file)

data = {}
for item in personas:
	f = open(os.path.join(personas_path,item+".json"),'r').read()
	d = json.loads(f)
	data[item] = d[list(d.keys())[0]]

## data now has all categories and top 50 sites in each cat
## data now has all categories and top 50 sites in each cat
## data now has all categories and top 50 sites in each cat


d_browser_param = json.loads(open('../automation/default_browser_params.json','r').read())
d_manager_param = json.loads(open('../automation/default_manager_params.json','r').read())


## load deafault browser and manager params
## load deafault browser and manager params
## load deafault browser and manager params

## Make N Personas for each category
## Make N Personas for each category
## Make N Personas for each category


for persona_name,value in data.items():

	#print(persona_name)
	temp = os.path.join('../config/{}'.format(phase),persona_name)
	if(not os.path.exists(temp)):
		os.makedirs(temp)


	sites = data[persona_name]

	i = 1
	while i <= NUM:
		for j in ['NoIntent','Intent']:

			Intent = j
			IntentSites = IS[persona_name]

			if j == 'NoIntent':
				 IntentSites = []

			
			with open(os.path.join(temp,'{}_{}_browser_params_{}.json'.format(Intent,persona_name,str(i))),'w') as json_file:
				t_browser_param 				      = d_browser_param
				t_browser_param["Persona_Path"]		  = "data/personas"
				t_browser_param["profile_archive_dir"]= "data/{}/{}_{}_{}".format(phase,persona_name.lower().lower(),Intent,str(i))
				t_browser_param["profile_tar"]		  = "data/{}/{}_{}_{}".format(phase,persona_name.lower().lower(),Intent,str(i))
				t_browser_param["Persona_Name"]		  = persona_name+".json"
				t_browser_param["Persona_Numb"]       = i
				t_browser_param["Browser_Config"]	  = "config/{}/{}/{}_{}_browser_params_{}.json".format(phase,persona_name,Intent,persona_name,str(i))
				t_browser_param["Manager_Config"]	  = "config/{}/{}/{}_{}_manager_params_{}.json".format(phase,persona_name,Intent,persona_name,str(i))
				t_browser_param["Browser_Config_Def"] = "default_browser_params.json"
				t_browser_param["Manager_Config_Def"] = "default_manager_params.json"
				t_browser_param["Number_of_Browsers"] = 1
				t_browser_param["Sites"]			  = sites
				t_browser_param["Storage_File"]		  = "storage.js"
				t_browser_param["ublock-origin"]	  = False
				t_browser_param["Ad_Sites"]	 	 	  = Ad_Sites
				t_browser_param["Intent"]	  		  = Intent
				t_browser_param["Intent_Sites"]		  = IntentSites
				t_browser_param["save_all_content"]	  = False
				t_browser_param["bot_mitigation"]	  = True
				json.dump(t_browser_param, json_file , indent=2)

			with open(os.path.join(temp,'{}_{}_manager_params_{}.json'.format(Intent,persona_name,str(i))),'w') as json_file:
				json.dump(d_manager_param, json_file , indent=2)


		i += 1

## Set up profile dir
## Set up profile dir
## Set up profile dir

profile_dirs = {}
for dirs in os.listdir('../config/{}'.format(phase)):
	for config_file in os.listdir('../config/{}/{}'.format(phase,dirs)):
		config_file = config_file.replace('_browser_params','')
		config_file = config_file.replace('_manager_params','')
		fpart = config_file.split("_")[0]
		mpart = '_'.join(config_file.split("_")[1:-1])
		lpart = config_file.split("_")[-1].replace('.json','')

		config_file = '_'.join([mpart.lower(),fpart,lpart])
		path = '../data/{}/{}'.format(phase,config_file)
		if(not os.path.exists(path)):
			os.makedirs(path)
