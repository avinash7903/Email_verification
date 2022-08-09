email=input("Enter your Email:")
space = 0
uppercase = 0
special_char = 0
if len(email)>=8:
    if email[0].isalpha():
        if("." in email ):
            if("@"in email)and(email.count("@")==1):
                if(email[-4]==".") ^ (email[-3]=="."):
                    for i in email:
                        if i== i.isspace():
                            space=1
                        elif i.isalpha():
                            if i== i.upper():
                                uppercase=1
                        elif i.isdigit():
                            continue
                        elif i=="_"or i=="."or i=="@":
                            continue
                        else:
                            special_char =1

                    if space==1 or uppercase==1 or special_char==1:
                        print("your enter email cannot contain uppcase letter, space, special char. pls cheak and try again")
                    else:
                        print("you email suceessful registered")
                else:
                    print("cheak your . position in your email")
            else:
                print("you cannot enter @ morethan one times and may be you entered letter containing contain uppcase letter, space, special char. pls cheak and try again")
        else:
            print("you email not containing .com , .in, .co.in pls cheak these and try again")
    else:
        print("you enter worng email because email cannot be contain first letter as uppercase . pls cheak and try again")
else:
    print("you enter worng email because email scannot be less than 7 letter. pls cheak and try again ")



