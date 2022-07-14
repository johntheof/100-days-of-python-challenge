#sample of list
#fruits = [item1, item2]

states_of_us = ['Alabama', 'Alaska', 'American Samoa', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut',
'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Guam', 'Hawaii',
'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 
'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Minor Outlying Islands', 
'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',
'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Northern Mariana Islands', 'Ohio', 
'Oklahoma', 'Oregon', 'Pennsylvania', 'Puerto Rico', 'Rhode Island', 'South Carolina', 'South Dakota', 
'Tennessee', 'Texas', 'U.S. Virgin Islands', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

print(states_of_us[0]) # prints first item of the list by order
print(states_of_us[-1]) # prints the last item from a list by order, goes -2,-3 etc etc

#changes in the list
states_of_us[0] = 'AlabamaTest' # changes first item of list to something else
print(states_of_us[0])

#add a new item at the end of the list
states_of_us.append('JohnLand')
print(states_of_us)

states_of_us.extend(['JohnyBoyLand','MoreState']) #extending the list by adding multiple items
print(states_of_us)
