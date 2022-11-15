import pywhatkit
import tkinter as tk
from tkinter import messagebox

def gui():
    window = tk.Tk()
    window.title("Whatsapp bot - Valdivia Ricardo")
    window.geometry("800x500")
    window.configure(bg="#494949")

    

    def send_a_message():
        number = str(ent2.get() + ent3.get())
        messagebox.showinfo("Espera!", f"El mensaje se esta enviando al numero: {number}. Porfavor espera")

        message = str(ent1.get('1.0', tk.END))
        if (ent4.index("end")== 0 and ent5.index("end") == 0):
                pywhatkit.sendwhatmsg_instantly(number, message, 31, True, 3)
                messagebox.showinfo("EXITO!", f"has enviado el mensaje:'{message}' al numero: {number}")
        else:
                pywhatkit.sendwhatmsg(number, message, int(ent4.get()), int(ent5.get()), 31, True, 2)
                messagebox.showinfo("EXITO!", f"has enviado el mensaje:'{message}' al numero: {number}")
        
        
        
        # ("imgs/{}".format(i), caption="Caption for the post")
    tk.Label(window, text="Bienvenido", font=(
        "Roboto", 36), bg="#F0FF00").pack(pady=10)
    tk.Label(window, text="El mensaje a enviar sera: ",
            font=("Roboto", 20), bg="#00FAFA").pack(pady=10)
    ent1 = tk.Text(window)
    ent1.place(x=10, y=136, height=100, width=750)

    tk.Label(window, text="Cod. Area + 9 ",
            font=("Roboto", 10), bg="#00FAFA").place(x=200, y=240)
    ent2 = tk.Entry(window)
    ent2.place(x=298, y=240, width=30)

    tk.Label(window, text="Ingrese el numero: ",
            font=("Roboto", 10), bg="#00FAFA").place(x=335, y=240)
    ent3 = tk.Entry(window)
    ent3.place(x=460, y=240, width=300)
    tk.Label(window, text="El '+9' es porque es un telefono movil",
            font=("Roboto", 10), bg="#00FAFA").place(x=200, y=270)

    tk.Label(window, text="Ejemplo de poner correctamente un numero:",
            font=("Roboto", 10), bg="#00FAFA").place(x=200, y=300)
    tk.Label(window, text="+549  12345678",
            font=("Roboto", 10), bg="#00FAFA").place(x=200, y=330)
    tk.Label(window, text="Ingrese la hora (Opcional): ",
            font=("Roboto", 10), bg="#00FAFA").place(x=10, y=240)
    ent4 = tk.Entry(window)
    ent4.place(x=10, y=270, width=20)
    tk.Label(window, text=":",
            font=("Roboto", 10), bg="#00FAFA").place(x=35, y=270)
    ent5 = tk.Entry(window)
    ent5.place(x=50, y=270, width=20)            
    button1 = tk.Button(window, text="SUBMIT",
                        font=("Roboto", 20), bg="#18D848",
                        command=send_a_message)
    button1.place(x=350, y=360)  # pack issue
    window.mainloop()



if __name__ == '__main__':
    gui()
    # enter name of your image bellow
    
    # upload_post()