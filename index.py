import matplotlib.pyplot as plt
import numpy as np

def ask_user_balance():
    user_input=input("===>")
    if user_input.find("$")!=-1:
        user_input=user_input[1:]
    try:
        float(user_input)
    except:
        print("Invalid value try again")
        ask_user_balance()
    else:
        print(f"${float(user_input):,.2f}\n")
        return float(user_input)

def ask_time():
    user_input=input("===>")
    try:
        int(user_input)
    except:
        print("Invalid value try again")
        ask_time()
    else:
        print(f"{int(user_input)} years\n")
        return int(user_input)

def ask_rate():
    user_input=input("===>")

    try:
        float(user_input)
    except:
        print("Invalid value try again")
        ask_rate()
    else:
        print(f"{float(user_input):.2f}%")
        return float(user_input)

def compounding_interest():
    print("\nWelcome to the compounding interest calculator!\n")
    print("How much money you got?")
    user_balance=ask_user_balance()
    print("How many years are you not gonna touch this money for?")
    time=ask_time()
    print("""What rate will this compound at annually?
    Hint*: The stock market averages 10.26%""")
    rate=ask_rate()
    final_principal=user_balance*((1+(rate*0.01))**time)
    deflated_balance=user_balance*((1+(-0.03))**time)

    print(f"""
    
--------------------------------------
Starting Balance: ${user_balance:,.2f}
----------------------------------------
Deflated Balance (@3% inflation rate): ${deflated_balance:,.2f}

Compounded Balance: ${final_principal:,.2f}\n

Over {time} years 
================
    """)

    saved_time=time
    super_saved_time=time

    
    xpoints_time=[]
    ypoints_money=[]
    while time>=0:
        xpoints_time.append(time)
        time-=1
    
    for i in xpoints_time:
        final_money=user_balance*((1+(rate*0.01))**i)
        ypoints_money.append(final_money)
    
    xpoints_time.reverse()
    ypoints_money.reverse()

    xpoints=np.array(xpoints_time)
    ypoints=np.array(ypoints_money)

    plt.plot(xpoints,ypoints,c = 'r',lw='3',marker="|",ms=15, mec='g')
    font1={'family':'monospace','size':18}
    font2={'family':'monospace','size':15}
    plt.title(f"Compound Interest Calculation Over {super_saved_time} Years", fontdict=font1)
    plt.xlabel("Years", fontdict=font2)
    plt.ylabel("Dollars $", fontdict=font2)

    plt.grid()


    xpoints_time_deflation=[]
    ypoints_money_deflation=[]
    while saved_time>=0:
        xpoints_time_deflation.append(saved_time)
        saved_time-=1

    for x in xpoints_time_deflation:
        deflated_money=user_balance*((1+(-0.03))**x)
        ypoints_money_deflation.append(deflated_money)
    
    plt.plot(xpoints_time_deflation,ypoints_money_deflation, c='g',lw='3',marker="|",ms=15, mec='r')

    plt.show()

    
    


    
    

compounding_interest()