is_male = True
is_tall = False

#if is_male or is_tall:
    #print("This dude Mato is male or tall or both")
#else:
    #print("Mato is neither a male nor tall")

if is_male and is_tall:
    print("This dude Mato is male")
elif is_male and not(is_tall):
    print("You are not a short male")
elif not (is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("Mato is neither a male nor tall")

