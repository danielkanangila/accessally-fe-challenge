import pprint

# create blood group list
blood_group = ['O-', 'O+', 'A-', 'A+', 'B-', 'B+', 'AB-', 'AB+']
# initialize the number of blood group
n=len(blood_group)

# create a compatibility rules 
## create a function to check if a given patient group is compatible with a given blood group
def is_compatible(patient_group, blood_group):
    # Return True if only if the patient blood group is compatible the blood unit group
    # otherwise return False
    if patient_group == 'O-' and blood_group == 'O-':
        return True
    if patient_group == 'O+' and (blood_group in ['0+', 'O-']):
        return True
    if patient_group == 'A-' and (blood_group in ['A-', 'O-']):
        return True
    if patient_group == 'A+' and (blood_group in ['A-', 'O-', 'A+', 'O+']):
        return True
    if patient_group == 'B-' and (blood_group in ['B-', 'O-']):
        return True
    if patient_group == 'B+' and (blood_group in ['B-', 'O-', 'B+', 'O+']):
        return True
    if patient_group == 'AB-' and (blood_group in ['O-', 'A-', 'B-', 'AB-']):
        return True
    if patient_group == 'AB+' and (blood_group in ['O-', 'A-', 'B-', 'AB-', 'O+', 'A+', 'B+', 'AB+']):
        return True
    # return if no match found
    return False

# Get the number of blood units
blood_units = input(f"Enter blood units separate by space - {' '.join(blood_group)}:")
# Get the numbert of patients
patients = input(f"Enter the number of patients separate by space - {' '.join(blood_group)}:")

# split blood units input into a list of integer 
blood_units_list = [int(qty) for qty in blood_units.split(' ')]

# split the patients input into a list of integer 
patients_nbr_list = [int(num) for num in patients.split(' ')]

# # create the patient infusion record to track the number of patient infused
infusion_record = dict()
# populate the infusion record with the number of patients who need infusion
# initialize the number of infused patients to 0
# and create a list blood group compatibility
for index_i in range(n):
    for index_j in range(n):
        # check if the blood group does not exist in the infusion record
        # if yes, create the new record. Otherwise update the list blood group compatible with
        if is_compatible(blood_group[index_i], blood_group[index_j]):
            if (blood_group[index_i] not in infusion_record):
                infusion_record[blood_group[index_i]] = {
                        'nbr_patients': patients_nbr_list[index_i],
                        'nbr_infused': 0,
                        'blood_group': [blood_group[index_j]],
                }
            else:
                infusion_record[blood_group[index_i]]['blood_group'] = [*infusion_record[blood_group[index_i]]['blood_group'], blood_group[index_j]]

def get_blood_qty_subgroup(groups):
    # Get the available quantity of the subgroup blood
    # return the first index and quantity available
    for group in groups:
        index = blood_group.index(group)
        blood_qty = blood_units_list[index]
        if blood_qty > 0:
            return index, blood_qty
    return 0

# Loop through the infusion record items to populate the number of infused patient
for group, group_info in infusion_record.items():
    # get the index of blood group compatible with the patients group
    index = blood_group.index(group)
    # get the quantity of blood unit available
    blood_qty = blood_units_list[index]
    # if the blood qty is greater than or equal to the number of patients,
    # update the of infused patients by the number of patients in the infusion record.
    # Otherwise, update the number  infused patients by the result of the substraction between number of patient and available blood quantity
    # Update the blood units input relative to the patient group by substract the quantity of blood used
    if blood_qty >= group_info.get('nbr_patients'):
        infusion_record[group]['nbr_infused'] = group_info.get('nbr_patients')
        blood_units_list[index] = blood_units_list[index] - group_info.get('nbr_patients')
    else:
        if blood_qty > 0 and group_info.get('nbr_infused') == 0:
            infusion_record[group]['nbr_infused'] = group_info.get('nbr_patients') - blood_qty
            blood_units_list[index] = group_info.get('nbr_patients') - blood_units_list[index]
    # if there are remaining number of patients who did not get infused,
    # get the availabile of the subgroup blood compatible with
    # increase the number of infused patient by the number of remaining patients
    # and substract to the blood list relative to subgroup index the qty used  
    if (group_info.get('nbr_infused') < group_info.get('nbr_patients')) and group_info.get('nbr_infused') > 0:
        # compute the remaining patients
        remaingin_patient = group_info.get('nbr_patients') - group_info.get('nbr_infused') 
        # get the subgroup blood qty and index
        idx, sub_blood_qty = get_blood_qty_subgroup(group_info.get('blood_group'))
        
        if (sub_blood_qty > 0 and sub_blood_qty >= remaingin_patient) :
            infusion_record[group]['nbr_infused'] += remaingin_patient
            blood_units_list[idx] = remaingin_patient - blood_units_list[idx]
            # print(group)
# get the list of number of infused patient
infused_nbr = [values['nbr_infused'] for ket, values in infusion_record.items()]
# print the sum of infused_nbr
print(sum(infused_nbr))