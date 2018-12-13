#%%

#from ./gitignore import apikey 
import requests



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
    
    