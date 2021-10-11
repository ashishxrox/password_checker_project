from tkinter import*
import requests
import hashlib
root = Tk()
root.title('SecurePass')
root.geometry("420x250")
def request_api_data(query_char):
        url = 'https://api.pwnedpasswords.com/range/' + query_char
        res = requests.get(url)
        if res.status_code != 200:
            raise RuntimeError(f'Error fetching :{res.status_code}, check the api and try again')
        return res
def get_password_leaks_counts(hashes, hash_to_check):
        hashes = (line.split(':') for line in hashes.text.splitlines())
        for h, count in hashes:
            if h == hash_to_check:
                return count
        return 0
def pwned_api_check(password):

        sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        first5_char, tail = sha1password[:5], sha1password[5:]
        response = request_api_data(first5_char)
        return get_password_leaks_counts(response, tail)
def main(args):
        password = args
        count = pwned_api_check(password)
        if count:
            lbl1 = Label(root,
                         text=f'{password} was found {count} times.... You should probably change your password!!!', bg="#FFB6C1")
            lbl1.pack()
            # print(f'{password} was found {count} times.... You should probably change your password!!!')
        else:
            lbl2 = Label(root, text=f'{password} was not found. Carry on!!', bg="#FFB6C1")
            lbl2.pack()
            # print((f'{password} was not found. Carry on!!'))
        return 'done!!'
if __name__ == '__main__':
    #argu = input("please Enter The Password \n")
    bg = PhotoImage(file="./images/download1.png")
    llabel = Label(root, image=bg)
    llabel.place(x=0, y=0, relwidth=1, relheight=1)
    lock = PhotoImage(file="./images/lock2.png")
    lLabel = Label(root, image=lock, bg= "#FFB6C1")
    lLabel.pack()
    myLabel = Label(root, text='Please Enter A Password', font= 'bold',bg="#FFB6C1")
    myLabel.pack()
    e = Entry(root, width=30)
    e.pack()
    e.get()  #cannot be assigned to variable
    my_frame=Frame(root)
    my_frame.pack()
    btn1 = Button(my_frame, text = 'GO!!!', font='bold',command = lambda:main(e.get()))  #No argument in command func without lambda operator
    btn1.grid(row=0,column=0)
    btn2 = Button(my_frame,text = 'EXIT',font='bold', command = root.quit)
    btn2.grid(row=0, column=1)

    root.resizable(False, False )
    root.mainloop()


