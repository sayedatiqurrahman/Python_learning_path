import requests


def  fetch_random_users_from_github():
        # url = 'https://api.github.com/users'
        # or
        # url = "https://api.freeapi.app/api/v1/public/randomusers"
        url = 'https://api.freeapi.app/api/v1/public/randomusers/user/random'
        response =  requests.get(url)
        data =  response.json()
        if ["success"] and "data" in data:
            user_data = data["data"]
            username= user_data["login"]["username"]
            email= user_data["email"]
            country = user_data["location"]["country"]
             
            return username,email,country
        else: raise Exception("Failed to fetch user data")



def main():
      try:
        username,email,country =fetch_random_users_from_github()
        
        print("username: ", username)    
        print("Email: ", email)    
        print("Country: ", country)          
      except Exception as e:
           print(str("Error From Main Function Except 28 no. line ", e))
  

if __name__ == "__main__":
      main()