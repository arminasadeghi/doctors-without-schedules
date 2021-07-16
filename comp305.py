# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

doctors = [
    ["Jonathan" , 10],
    ["Dimitris" , 8],
    ["Marcel" , 8],
    ["Samantha" , 8]
    ]

patients = [
    ["Mustapha" , 2],
    ["Gregor" , 3],
    ["Michael" , 3],
    ["Alicia" , 3],
    ["Martin" , 1],
    ["Wachowski" , 6],
    ["Mariam" , 8],
    ["Cisse" , 6]
    ]

def canAllPatientsBeSeen(doctors, patients):
    doctors.sort(key = lambda x : x[1])
    patients.sort(key = lambda x : x[1], reverse=True)
    schedule = {doctors[i][0] : [] for i in range(len(doctors))}
    return canAllPatientsBeSeenHelper(doctors, patients, schedule)

def canAllPatientsBeSeenHelper(doctors, patients, schedule):
    if not patients:
        return schedule
    elif not doctors:
        return False;
    else:
        patientHour = patients[0][1]
        patientPlaced = False
        for i in range(len(doctors)):
            doctorHour = doctors[i][1]
            if patientHour < doctorHour:
                schedule[doctors[i][0]].append(patients[0][0])
                doctors[i][1] = doctorHour - patientHour
                patients.pop(0)
                patientPlaced = True
                break
            elif patientHour == doctorHour:
                schedule[doctors[i][0]].append(patients[0][0])
                doctors.pop(i)
                patients.pop(0)
                patientPlaced = True
                break
        if not patientPlaced:
            return False
        return canAllPatientsBeSeenHelper(doctors, patients, schedule)
        
    
result = canAllPatientsBeSeen(doctors, patients)
print("\nRESULT\n")
print(result)
