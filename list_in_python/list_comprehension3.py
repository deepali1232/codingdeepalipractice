names=['divya','ayushi','pinky','vaibhav','ayushi','ridhi']
names_containing_e=[name for name in names if 'e' in name]
print(names_containing_e)
names_capitalized=[name.title() for name in names]
print(names_capitalized)
names_ending_with_a=[name for name in names if name.endswith('a')]
print(names_ending_with_a)