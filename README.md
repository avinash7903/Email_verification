# EMAIL VERIFICATION - PYTHON PROJECTS
This project ia base on email verification. To create this project I used a python string and for loop.

We divided an email verification into 6 condition. After completing these condition, our email verification is successfully executed.

condition - 1 

![image](https://user-images.githubusercontent.com/109716461/183668437-cab210dc-52cc-4d02-8e18-87600fbed5bb.png)
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

condition - 2

![image](https://user-images.githubusercontent.com/109716461/183670325-cbd63e90-c7d2-4ac2-aa6c-fdcac074a932.png)


condition - 3

![image](https://user-images.githubusercontent.com/109716461/183670422-c6927b40-b51c-4f56-ae8e-833f8ef00a30.png)


condition - 4

![image](https://user-images.githubusercontent.com/109716461/183670526-c8414df3-2cb5-49bc-8f83-be64eae3bdd8.png)


condition - 5

![image](https://user-images.githubusercontent.com/109716461/183670581-60d6e244-f388-462a-98c1-323c30a0dc11.png)


condition - 6(final)


![image](https://user-images.githubusercontent.com/109716461/183670691-1e4cab60-ab12-434e-845c-d0e048f8264c.png)



final code after applying all conditions :

![image](https://user-images.githubusercontent.com/109716461/183671312-d5e91dbd-7960-47de-84d0-222dd5840a67.png)



