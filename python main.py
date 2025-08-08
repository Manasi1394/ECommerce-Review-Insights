#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import matplotlib.pyplot as plt
import getpass

review_list=[]
Dresses = []
Bottoms = []
Tops = []
Intimate = []
Jackets = []
Trend = []

def administrator():
    admin_user_pwd = {}
    with open("admin_credentials .txt", mode='r') as admin:
        for a in admin:
            user,pwd = a.strip().split(",")
            admin_user_pwd[user] = pwd

        section1 = True
        section2 = True
        stopper = 0
        items = admin_user_pwd.items()

        while stopper == 0:
            username= input("👤Please enter your admin username:  ")
            password= input("🔒Now, let's verify your identify with the password: ")

            if section1:
                for v in items:
                    if v[0] == username and v[1]== password:
                        print()
                        print("You have got Admin Access: Go ahead and add new user and password")
                        stopper = 1
                        section2 = False
                        add_user_password()
                        
            if section2:
                print()
                print("Sorry! wrong password you are not allowed access")
                print("Please try again with correct credentials")
                
def add_user_password():
    user_pwd = {}

    with open("emp_credentials.txt", mode='r') as emp:
        for e in emp:
            user, pwd = e.strip().split(",")
            user_pwd[user] = pwd

    new_username = input("Enter a new user name: ")

    while new_username in user_pwd:
        print("Sorry, this username is not available.")
        new_username = input("Enter a new user name: ")

    new_pwd = input("Enter the new password: ")

    user_pwd[new_username] = new_pwd

    with open("emp_credentials.txt", mode='a') as emp:
        emp.write(f"\n{new_username},{new_pwd}")
        print()
        print("Username and Password added")
        
    print(
    """
    Continue working:
    
    1 - Admin login
    2 - Employee login
    """)
    
    print()
    option = int(input("Enter your option: "))
    
    if option == 1:
        administrator()
        
    elif option == 2:
        user_password()

def user_password():
    user_pwd = {}
    with open("emp_credentials.txt", mode='r') as emp:
        for e in emp:
            user,pwd = e.strip().split(",")
            user_pwd[user] = pwd

        section1 = True
        section2 = True
        stopper = 0
        items = user_pwd.items()

        while stopper == 0:
            username= input("👤Please enter your employee username:  ")
            password= getpass.getpass("🔒Now, let's verify your identify with the password: ")

            if section1:
                for v in items:
                    if v[0] == username and v[1]== password:
                        print("Access Granted! you can now analyse the data")
                        stopper = 1
                        section2 = False
                        call_required_operations()
            if section2:
                print("Sorry! wrong password you are not allowed access")
                print("Please try again with correct credentials")
                


        
def data_extraction():
    with open("ECommerce_Dataset_converted.csv", mode = "r", newline = '') as dataset:
        bytes_to_skip = 106
        dataset.seek(bytes_to_skip)
        reader = csv.reader(dataset)


        for record in reader:
            customer_list = []
            Sno,Id,age,review,rating,recommendation,feedback,name = record
            customer_list.append(Sno.strip())
            customer_list.append(Id.strip())
            customer_list.append(age.strip())
            customer_list.append(review.strip())
            customer_list.append(rating.strip())
            customer_list.append(recommendation.strip())
            customer_list.append(feedback.strip())
            customer_list.append(name.strip())

            customer_tuple = tuple(customer_list)
            review_list.append(customer_tuple)

def departmentwise_lists():
    for i,v in enumerate(review_list):
        if review_list[i][7] == "Dresses":
            Dresses.append(v)
        elif review_list[i][7] == "Bottoms":
            Bottoms.append(v)
        elif review_list[i][7] == "Tops":
            Tops.append(v)
        elif review_list[i][7] == "Intimate":
            Intimate.append(v)
        elif review_list[i][7] == "Jackets":
            Jackets.append(v)
        elif review_list[i][7] == "Trend":
            Trend.append(v)

def rating_analysis():
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    
    run = True
    choice = int(input("Choose a Department to Analyse:\n1) Dresses\n2) Bottoms\n3) Tops\n4) Intimate\n5) Jackets\n6) Trend\n"))
    print()
    while run:
        if choice == 1:
            choice_list = Dresses
            choice_str = "Dresses"
            run = False
        elif choice == 2:
            choice_list = Bottoms
            choice_str = "Bottoms"
            run = False
        elif choice == 3:
            choice_list = Tops
            choice_str = "Tops"
            run = False
        elif choice == 4:
            choice_list = Intimate
            choice_str = "Intimate"
            run = False
        elif choice == 5:
            choice_list = Jackets
            choice_str = "Jackets"
            run = False
        elif choice == 6:
            choice_list = Trend
            choice_str = "Trend"
            run = False
        else:
            print("Please choose a Department that exists in the Database!")
            choice = int(input("Choose a Department to Analyse:\n1) Dresses\n2) Bottoms\n3) Tops\n4) Intimate\n5) Jackets\n6) Trend\n"))
            print()
    
    for i, v in enumerate(choice_list):
        if int(choice_list[i][4]) == 1:
            count_1 += 1
        if int(choice_list[i][4]) == 2:
            count_2 += 1
        if int(choice_list[i][4]) == 3:
            count_3 += 1
        if int(choice_list[i][4]) == 4:
            count_4 += 1
        if int(choice_list[i][4]) == 5:
            count_5 += 1
    
    count_list = [count_1,count_2,count_3,count_4,count_5]
    max_count_list = max(count_list)
    index_count_list = count_list.index(max_count_list) + 1
    print(f'The majority of customers rated "{index_count_list}" for the products under "{choice_str}" department.')
    print()
    print("*"*79)
    print()
    print(f'Number of customers who Rated 1 for {choice_str}: {count_list[0]}')
    print(f'Number of customers who Rated 2 for {choice_str}: {count_list[1]}')
    print(f'Number of customers who Rated 3 for {choice_str}: {count_list[2]}')
    print(f'Number of customers who Rated 4 for {choice_str}: {count_list[3]}')
    print(f'Number of customers who Rated 5 for {choice_str}: {count_list[4]}')
    print()
    print("*"*79)
    print()
    
    #plotting bar graph
    values = count_list

    # Creating a bar graph
    plt.bar(range(1, len(values) + 1), values, color='blue')

    # Adding values near the bars
    for i, value in enumerate(values):
        plt.text(i + 1, value + 50, str(value), ha='center', va='bottom')

    # Adding labels and title
    plt.xlabel('Rating (1 to 5)')
    plt.ylabel('No. of Customers who rated')
    plt.title('Bar Graph for No. of Customers V/S Rating')

    # Displaying the graph
    plt.show()
    
def age_department_preference():
    dresses_count1=0
    bottoms_count1=0
    tops_count1=0
    intimate_count1=0
    jackets_count1=0
    trend_count1=0

    dresses_count2=0
    bottoms_count2=0
    tops_count2=0
    intimate_count2=0
    jackets_count2=0
    trend_count2=0

    dresses_count3=0
    bottoms_count3=0
    tops_count3=0
    intimate_count3=0
    jackets_count3=0
    trend_count3=0

    for i,v in enumerate(review_list):
        a = int(review_list[i][2])
        if a >= 15 and a <= 30:
            if review_list[i][7]=="Dresses":
                dresses_count1+=1
            elif review_list[i][7]=="Bottoms":
                bottoms_count1+=1
            elif review_list[i][7]=="Tops":
                tops_count1+=1
            elif review_list[i][7]=="Intimate":
                intimate_count1+=1
            elif review_list[i][7]=="Jackets":
                jackets_count1+=1
            elif review_list[i][7]=="Trend":
                trend_count1+=1


        elif a >= 31 and a <= 60:
            if review_list[i][7]=="Dresses":
                dresses_count2+=1
            elif review_list[i][7]=="Bottoms":
                bottoms_count2+=1
            elif review_list[i][7]=="Tops":
                tops_count2+=1
            elif review_list[i][7]=="Intimate":
                intimate_count2+=1
            elif review_list[i][7]=="Jackets":
                jackets_count2+=1
            elif review_list[i][7]=="Trend":
                trend_count2+=1



        elif a >= 61:
            if review_list[i][7]=="Dresses":
                dresses_count3+=1
            elif review_list[i][7]=="Bottoms":
                bottoms_count3+=1
            elif review_list[i][7]=="Tops":
                tops_count3+=1
            elif review_list[i][7]=="Intimate":
                intimate_count3+=1
            elif review_list[i][7]=="Jackets":
                jackets_count3+=1
            elif review_list[i][7]=="Trend":
                trend_count3+=1


    dict_15_30={"Dresses":dresses_count1,"Bottoms":bottoms_count1,"Tops":tops_count1,"Intimate":intimate_count1,"Jackets":jackets_count1,"Trend":trend_count1}
    dict_31_60={"Dresses":dresses_count2,"Bottoms":bottoms_count2,"Tops":tops_count2,"Intimate":intimate_count2,"Jackets":jackets_count2,"Trend":trend_count2}
    dict_61={"Dresses":dresses_count3,"Bottoms":bottoms_count3,"Tops":tops_count3,"Intimate":intimate_count3,"Jackets":jackets_count3,"Trend":trend_count3}

    max_dict_15_30_key=max(dict_15_30,key=dict_15_30.get)
    max_dict_15_30_value=dict_15_30[max_dict_15_30_key]

    min_dict_15_30_key=min(dict_15_30,key=dict_15_30.get)
    min_dict_15_30_value=dict_15_30[min_dict_15_30_key]


    max_dict_31_60_key=max(dict_31_60,key=dict_31_60.get)
    max_dict_31_60_value=dict_31_60[max_dict_31_60_key]

    min_dict_31_60_key=min(dict_31_60,key=dict_31_60.get)
    min_dict_31_60_value=dict_31_60[min_dict_31_60_key]

    max_dict_61_key=max(dict_61,key=dict_15_30.get)
    max_dict_61_value=dict_61[max_dict_61_key]

    min_dict_61_key=min(dict_61,key=dict_15_30.get)
    min_dict_61_value=dict_61[min_dict_61_key]

    print(f'{"Age Group":<20} {"Most Preferred Choice":>20} {"Count":>18} {"Least Preferred Choice":>30} {"Count":^22}')
    print("*"*106)
    print(f'{"15-30":<20} {max_dict_15_30_key:^19} {max_dict_15_30_value:>19} {min_dict_15_30_key:^40} {min_dict_15_30_value:<26}')
    print(f'{"31-60":<20} {max_dict_31_60_key:^19} {max_dict_31_60_value:>19} {min_dict_31_60_key:^40} {min_dict_31_60_value:<26}')
    print(f'{"61 and above":<20} {max_dict_61_key:^19} {max_dict_61_value:>19} {min_dict_61_key:^40} {min_dict_61_value:<26}')

    user_choice = '\nPlease select an age group: \n1 - 15-30\n'
    user_choice += '2 - 31-60'
    user_choice += '\n3 - 60 and above\n'
    
    choice= int(input(user_choice))
    
    if choice==1:
    
        labels1=dict_15_30.keys()
        sizes1=dict_15_30.values()

        plt.figure(figsize=(8, 8))
        plt.pie(sizes1, labels=labels1, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
        sorted_dict_15_30 = dict(sorted(dict_15_30.items(), key=lambda item: item[1], reverse=True))
        plt.title(sorted_dict_15_30)
        plt.show()
    
    elif choice==2:
        
        labels2=dict_31_60.keys()
        sizes2=dict_31_60.values()
    
        plt.figure(figsize=(8, 8))
        plt.pie(sizes2, labels=labels2, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
        sorted_dict_31_60 = dict(sorted(dict_31_60.items(), key=lambda item: item[1], reverse=True))
        plt.title(sorted_dict_31_60)
        plt.show()
    
    elif choice==3:
        labels3=dict_61.keys()
        sizes3=dict_61.values()

        plt.figure(figsize=(8, 8))
        plt.pie(sizes3, labels=labels3, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
        sorted_dict_61 = dict(sorted(dict_61.items(), key=lambda item: item[1], reverse=True))
        plt.title(sorted_dict_61)
        plt.show()
        
def recommendation_pos_nos_analysis():
    print("""
    Select the department of which recommendation analysis is requested.
    1 - Dresses
    2 - Bottoms
    3 - Tops
    4 - Intimate
    5 - Jackets
    6 - Trend
    
    """)
    option = int(input("Enter your option: "))
    print()
    
    if option == 1:

        ##DRESSES
        positive_dresses = []
        negative_dresses = []

        for i,v in enumerate(Dresses):
            if (Dresses[i][4] == '1' or Dresses[i][4] == '2' or Dresses[i][4] == '3') and Dresses[i][5] == '0':
                negative_dresses.append(v)
            elif (Dresses[i][4] == '5' or Dresses[i][4] == '4' or Dresses[i][4] == '3') and Dresses[i][5] == '1':
                positive_dresses.append(v)

        choice = int(input("Enter your feedback choice (1 - Positive ; 2 - Negative; 3 - Compared result): "))

        if choice == 1:
            print(f'{"Department":^20}|{"Rating":^20}|{"Review":^20}')
            print("-"*80)            
            print(f'{"Positive Feedback":^70}')
            print("-"*80)
            for i,v in enumerate(positive_dresses):
                print(f'{positive_dresses[i][7]:^20}|{positive_dresses[i][4]:^20}|  {positive_dresses[i][3]:^20}')
        elif choice == 2:
            print(f'{"Department":^20}|{"Rating":^20}|{"Review":^20}')
            print("-"*80)            
            print(f'{"Negative Feedback":^70}')
            print("-"*80)
            for i,v in enumerate(negative_dresses):
                print(f'{negative_dresses[i][7]:^20}|{negative_dresses[i][4]:^20}|  {negative_dresses[i][3]:^20}')
        elif choice == 3:
            positive_count_dresses = len(positive_dresses)
            negative_count_dresses = len(negative_dresses)


            labels = ['Positive Dresses', 'Negative Dresses']
            counts = [positive_count_dresses, negative_count_dresses]

            plt.bar(labels, counts, color=['green', 'red'])
            plt.xlabel('Feedback Type')
            plt.ylabel('Count')
            plt.title('Positive vs Negative Feedback for Dresses')
            plt.show()



    elif option == 2:

        ##Bottoms
        positive_bottoms = []
        negative_bottoms = []


        for i,v in enumerate(Bottoms):
            if (Bottoms[i][4] == '1' or Bottoms[i][4] == '2' or Bottoms[i][4] == '3') and Bottoms[i][5] == '0':
                negative_bottoms.append(v)
            elif (Bottoms[i][4] == '5' or Bottoms[i][4] == '4' or Bottoms[i][4] == '3') and Bottoms[i][5] == '1':
                positive_bottoms.append(v)


        choice = int(input("Enter your feedback choice (1 - Positive ; 2 - Negative; 3 - Compared result): "))
        print()

        if choice == 1:
            print(f'{"Department":^20}|{"Rating":^20}|{"Review":^20}')
            print("-"*80)            
            print(f'{"Positive Feedback":^70}')
            print("-"*80)
            for i,v in enumerate(positive_bottoms):
                print(f'{positive_bottoms[i][7]:^20}|{positive_bottoms[i][4]:^20}|  {positive_bottoms[i][3]:^20}')
        elif choice == 2:
            print(f'{"Department":^20}|{"Rating":^20}|{"Review":^20}')
            print("-"*80)            
            print(f'{"Negative Feedback":^70}')
            print("-"*80)
            for i,v in enumerate(negative_bottoms):
                print(f'{negative_bottoms[i][7]:^20}|{negative_bottoms[i][4]:^20}|  {negative_bottoms[i][3]:^20}')

        elif choice == 3:
            positive_count_bottoms = len(positive_bottoms)
            negative_count_bottoms = len(negative_bottoms)


            labels = ['Positive Bottoms', 'Negative Bottoms']
            counts = [positive_count_bottoms, negative_count_bottoms]

            plt.bar(labels, counts, color=['green', 'red'])
            plt.xlabel('Feedback Type')
            plt.ylabel('Count')
            plt.title('Positive vs Negative Feedback for Bottoms')
            plt.show()
                
                
    elif option == 3:

        ##Tops
        positive_tops = []
        negative_tops = []


        for i,v in enumerate(Tops):
            if (Tops[i][4] == '1' or Tops[i][4] == '2' or Tops[i][4] == '3') and Tops[i][5] == '0':
                negative_tops.append(v)
            elif (Tops[i][4] == '5' or Tops[i][4] == '4' or Tops[i][4] == '3') and Tops[i][5] == '1':
                positive_tops.append(v)


        choice = int(input("Enter your feedback choice (1 - Positive ; 2 - Negative; 3 - Compared result): "))
        print()


        if choice == 1:
            print(f'{"Department":^20}|{"Rating":^20}|{"Review":^20}')
            print("-"*80)            
            print(f'{"Positive Feedback":^70}')
            print("-"*80)
            for i,v in enumerate(positive_tops):
                print(f'{positive_tops[i][7]:^20}|{positive_tops[i][4]:^20}|  {positive_tops[i][3]:^20}')
        elif choice == 2:
            print(f'{"Department":^20}|{"Rating":^20}|{"Review":^20}')
            print("-"*80)            
            print(f'{"Negative Feedback":^70}')
            print("-"*80)
            for i,v in enumerate(negative_tops):
                print(f'{negative_tops[i][7]:^20}|{negative_tops[i][4]:^20}|  {negative_tops[i][3]:^20}')

        elif choice == 3:
            positive_count_tops = len(positive_tops)
            negative_count_tops = len(negative_tops)


            labels = ['Positive Tops', 'Negative Tops']
            counts = [positive_count_tops, negative_count_tops]

            plt.bar(labels, counts, color=['green', 'red'])
            plt.xlabel('Feedback Type')
            plt.ylabel('Count')
            plt.title('Positive vs Negative Feedback for Tops')
            plt.show()
                
                

    elif option == 4:

        ##Intimate

        positive_intimate = []
        negative_intimate = []


        for i,v in enumerate(Intimate):
            if (Intimate[i][4] == '1' or Intimate[i][4] == '2' or Intimate[i][4] == '3') and Intimate[i][5] == '0':
                negative_intimate.append(v)
            elif (Intimate[i][4] == '5' or Intimate[i][4] == '4' or Intimate[i][4] == '3') and Intimate[i][5] == '1':
                positive_intimate.append(v)


        choice = int(input("Enter your feedback choice (1 - Positive ; 2 - Negative; 3 - Compared result): "))
        print()



        if choice == 1:
            print(f'{"Department":^20}|{"Rating":^20}|{"Review":^20}')
            print("-"*80)            
            print(f'{"Positive Feedback":^70}')
            print("-"*80)
            for i,v in enumerate(positive_intimate):
                print(f'{positive_intimate[i][7]:^20}|{positive_intimate[i][4]:^20}|  {positive_intimate[i][3]:^20}')
        elif choice == 2:
            print(f'{"Department":^20}|{"Rating":^20}|{"Review":^20}')
            print("-"*80)            
            print(f'{"Negative Feedback":^70}')
            print("-"*80)
            for i,v in enumerate(negative_intimate):
                print(f'{negative_intimate[i][7]:^20}|{negative_intimate[i][4]:^20}|  {negative_intimate[i][3]:^20}')

        elif choice == 3:
            positive_count_intimate = len(positive_intimate)
            negative_count_intimate = len(negative_intimate)


            labels = ['Positive Intimate', 'Negative Intimate']
            counts = [positive_count_intimate, negative_count_intimate]

            plt.bar(labels, counts, color=['green', 'red'])
            plt.xlabel('Feedback Type')
            plt.ylabel('Count')
            plt.title('Positive vs Negative Feedback for Intimate')
            plt.show()
                

                
    elif option == 5:

        ##Jackets

        positive_jackets = []
        negative_jackets = []


        for i,v in enumerate(Jackets):
            if (Jackets[i][4] == '1' or Jackets[i][4] == '2' or Jackets[i][4] == '3') and Jackets[i][5] == '0':
                negative_jackets.append(v)
            elif (Jackets[i][4] == '5' or Jackets[i][4] == '4' or Jackets[i][4] == '3') and Jackets[i][5] == '1':
                positive_jackets.append(v)


        choice = int(input("Enter your feedback choice (1 - Positive ; 2 - Negative; 3 - Compared result): "))
        print()



        if choice == 1:
            print(f'{"Department":^20}|{"Rating":^20}|{"Review":^20}')
            print("-"*80)            
            print(f'{"Positive Feedback":^70}')
            print("-"*80)
            for i,v in enumerate(positive_jackets):
                print(f'{positive_jackets[i][7]:^20}|{positive_jackets[i][4]:^20}|  {positive_jackets[i][3]:^20}')
        elif choice == 2:
            print(f'{"Department":^20}|{"Rating":^20}|{"Review":^20}')
            print("-"*80)            
            print(f'{"Negative Feedback":^70}')
            print("-"*80)
            for i,v in enumerate(negative_jackets):
                print(f'{negative_jackets[i][7]:^20}|{negative_jackets[i][4]:^20}|  {negative_jackets[i][3]:^20}')

        elif choice == 3:
            positive_count_jackets = len(positive_jackets)
            negative_count_jackets = len(negative_jackets)


            labels = ['Positive Jackets', 'Negative Jackets']
            counts = [positive_count_jackets, negative_count_jackets]

            plt.bar(labels, counts, color=['green', 'red'])
            plt.xlabel('Feedback Type')
            plt.ylabel('Count')
            plt.title('Positive vs Negative Feedback for Jackets')
            plt.show()
                
                
    elif option == 6:

        ##Trend

        positive_trend = []
        negative_trend = []


        for i,v in enumerate(Trend):
            if (Trend[i][4] == '1' or Trend[i][4] == '2' or Trend[i][4] == '3') and Trend[i][5] == '0':
                negative_trend.append(v)
            elif (Trend[i][4] == '5' or Trend[i][4] == '4' or Trend[i][4] == '3') and Trend[i][5] == '1':
                positive_trend.append(v)


        choice = int(input("Enter your feedback choice (1 - Positive ; 2 - Negative; 3 - Compared result): "))
        print()



        if choice == 1:
            print(f'{"Department":^20}|{"Rating":^20}|{"Review":^20}')
            print("-"*80)
            print(f'{"Positive Feedback":^70}')
            print("-"*80)
            for i,v in enumerate(positive_trend):
                print(f'{positive_trend[i][7]:^20}|{positive_trend[i][4]:^20}|  {positive_trend[i][3]:^20}')
        elif choice == 2:
            print(f'{"Department":^20}|{"Rating":^20}|{"Review":^20}')
            print("-"*80)
            print(f'{"Negative Feedback":^70}')
            print("-"*80)
            for i,v in enumerate(negative_trend):
                print(f'{negative_trend[i][7]:^20}|{negative_trend[i][4]:^20}|  {negative_trend[i][3]:^20}')

        elif choice == 3:
            positive_count_trend = len(positive_trend)
            negative_count_trend = len(negative_trend)


            labels = ['Positive Trend', 'Negative Trend']
            counts = [positive_count_trend, negative_count_trend]

            plt.bar(labels, counts, color=['green', 'red'])
            plt.xlabel('Feedback Type')
            plt.ylabel('Count')
            plt.title('Positive vs Negative Feedback for Trend')
            plt.show()
            
def most_reviewed():
    
    dresses_count = 0
    bottoms_count = 0
    tops_count = 0
    intimate_count = 0
    jackets_count = 0
    trend_count = 0



    for i,v in enumerate(review_list):
        if review_list[i][7] == "Dresses":
            dresses_count+=1
        elif review_list[i][7] == "Bottoms":
            bottoms_count+=1
        elif review_list[i][7] == "Tops":
            tops_count+=1
        elif review_list[i][7] == "Intimate":
            intimate_count+=1
        elif review_list[i][7] == "Jackets":
            jackets_count+=1
        elif review_list[i][7] == "Trend":
            trend_count+=1

    categories = ['Dresses', 'Bottoms', 'Tops', 'Intimate', 'Jackets', 'Trend']
    counts = [dresses_count, bottoms_count, tops_count, intimate_count, jackets_count, trend_count]

    # Sort in descending order
    sorted_indices = sorted(range(len(counts)), key=lambda k: counts[k], reverse=True)
    categories = [categories[i] for i in sorted_indices]
    counts = [counts[i] for i in sorted_indices]

    # Bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(categories, counts, color='green')
    plt.title('Number of Reviews by Department (Descending Order)')
    plt.xlabel('Department')
    plt.ylabel('Number of Reviews')
    plt.show()

def call_required_operations():
    data_extraction()
    departmentwise_lists()
    print()
    print("Choose the Analysis you would like to perform:")
    emp_choice = int(input("1) Product department-wise Rating Analysis\n2) Age wise Product Preference & Analysis\n3) Recommendation & Feedback Analysis\n4) Most Reviewed Products Department-wise\n5) Exit\n"))
    print()
    
    while emp_choice != 5:
        if emp_choice == 1:
            rating_analysis()
        elif emp_choice == 2:
            age_department_preference()
        elif emp_choice == 3:
            recommendation_pos_nos_analysis()
        elif emp_choice == 4:
            most_reviewed()
            
        print()
        emp_choice = int(input("1) Product department-wise Rating Analysis\n2) Age wise Product Preference & Analysis\n3) Recommendation & Feedback Analysis\n4) Most Reviewed Products Department-wise\n5) Exit\n"))
        
def main():
    print("Welcome to Women's E-Commerce Clothing Data-Analysis Tool")
    print("*"*70)
    print(
    """
    1 - Admin login
    2 - Employee login
    """)
    
    print()
    option = int(input("Enter your option: "))
    
    if option == 1:
        administrator()
        
    elif option == 2:
        user_password()
    
main()


# In[2]:





# In[ ]:




