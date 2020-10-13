age={'bob':28,'sarah':29,'sally':23,'hank':22}

def isBobPresent(d):
    is_present = False
    for k in d.keys():
        if k =='bob':
            is_present = True
        if is_present:
            return 'The key "bob" is present! The value is ' + str(d[])


