from socket import setdefaulttimeout


def functiontest(dictionary,key_list):
    if len(dictionary) == 0:
        print('Dictionary is empty')
    if len(key_list) == 0:
    	print("Invalid Key Supplied")
    key_to_search = key_list[0]
    if key_to_search in dictionary.keys():
    	value_found = dictionary[key_to_search]
    	if type(value_found) is dict:
    		functiontest(value_found, key_list[1:])
    	elif len(key_list) == 1:
      	    print(value_found)
    	else:
    	    print (f"Invalid key {key_list}")
    else:
    	print(f"Key {key_to_search} not found in dictionary {dictionary}")

                
                
            

if __name__=='__main__':
    sample_dict={}
    # create nested dictionary
    sample_dict.setdefault("DiGi",{}).setdefault("age",'26')
    sample_dict.setdefault("Lola",{}).setdefault("age",'22')
    #key value (in string format) to check in dictionary
    key_value=["Lola",'age', 'hobbie']
    functiontest(sample_dict,key_value)
