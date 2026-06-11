import pandas as pd
import random


num_records = 100
first_names = ["Ali", "Mona", "Ahmed", "Sara", "Mahmoud", "Fatma", "Eslam", "Omnia", "Hoda", "Tarek"]
last_names = ["Shahin", "Eldaly", "Nafae", "Ragab", "Salem", "Gaber", "Kamal", "Bakr", "Soliman", "Radwan"]
blood_types = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']

data = []
used_ids = set()

for i in range(num_records):
    
    while True:
        century = "2"  
        year = str(random.randint(60, 99))
        month = str(random.randint(1, 12)).zfill(2)
        day = str(random.randint(1, 28)).zfill(2)
        gov = "01"  
        serial = str(random.randint(100, 999)) 
        gender_digit = random.choice(["1", "2"])
        check = str(random.randint(0, 9))
        
        # الدمج: 1+2+2+2+2+3+1+1 = 14 خانة
        nid = f"{century}{year}{month}{day}{gov}{serial}{gender_digit}{check}"
        
        if nid not in used_ids:
            used_ids.add(nid)
            break

    
    gender = "Male" if gender_digit == "1" else "Female"
    f_name = random.choice(first_names)
    l_name = random.choice(last_names)
    
    data.append({
        'national_id': nid,
        'first_name': f_name,
        'last_name': l_name,
        'date_of_birth': f"19{year}-{month}-{day}",
        'gender': gender,
        'blood_type': random.choice(blood_types),
        'contact_email': f"{f_name.lower()}.{l_name.lower()}{random.randint(10,99)}@example.com"
    })


df = pd.DataFrame(data)
df.to_csv("Final-Unique-Patients_Data.csv", index=False)

print(f"تم توليد {num_records} سجل فريد (14 خانة) بنجاح.")
print("عينة من البيانات:")
print(df[['national_id', 'first_name']].head())