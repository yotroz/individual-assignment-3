#%%

#from ./gitignore import apikey 
import requests
import secret



secret.apikey
#apikey = "0cdbfaf52c0506f369cd4b76e71f3828c7f68a5e"
#
#print(apikey)
#
#url = "https://api.github.com?access_token="
#
##response = requests.get("https://api.github.com/users/yotroz/repos?access_token=" + apikey)
##response = requests.get(url + apikey + "/users/yotroz/repos")


def get_all_repositories(user): 
    
    response = requests.get("https://api.github.com/users/" + user + "/repos")
            
    repos = response.json()
    
    
    all_repos = []
            
    for repo in repos: 
        
        element = {
                    "description": repo["description"],       
                    "name": repo["name"],
                    "stars": repo["stargazers_count"],     
                    "language": repo["language"], 
                    "url": repo["url"] 
                }
        
        all_repos.append(element)
        
        
        
    return all_repos
        
    
#%%
    
    