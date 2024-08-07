tuple1 = (2, 7, [5,7,8], 'Tutor' , True, 'T', 3.21)
          
tuple2 = tuple1[:1] + tuple1[2:-1]

print(f"Original tuple : {tuple1}")
print(f"Final tuple : {tuple2}")