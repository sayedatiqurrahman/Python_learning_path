import time 

wait_time = 1
max_tries = 5
tries = 0

while tries < max_tries:
      print(f"Attempt {tries + 1} of {max_tries}. Waiting for {wait_time} seconds...")
      time.sleep(wait_time)

      wait_time *= 2
      tries += 1

print("Waiting complete.")