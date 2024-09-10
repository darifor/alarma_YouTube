import tkinter as tk
from tkinter import messagebox
import time
import datetime
import webbrowser
import random
import threading

def abrir_archivo(ruta):
    # Abre el archivo en modo lectura
    with open(ruta, "r") as archivo:
        lineas = archivo.readlines()

        # Selecciona una línea al azar
        linea_aleatoria = random.choice(lineas)
        webbrowser.open(linea_aleatoria)


def actualizar_reloj():
    hora_actual = time.strftime("%H:%M:%S")
    etiqueta_reloj.config(text=hora_actual)
    window.after(1000, actualizar_reloj)  # Actualizar cada segundo


def alarm():
    hora = datetime.time(int(horas.get()), int(minutos.get()))
    hora_c = hora.strftime("%H:%M")
    messagebox.showinfo(title="Despertador activado", message=f"Ha establecido la alarma en {hora_c}")
    while True:
        ahora = datetime.datetime.now()
        hora_actual = ahora.time()
        ha_c = hora_actual.strftime("%H:%M")
        if hora_c == ha_c:
            ruta_archivo = "enlaces_youtube.txt"
            abrir_archivo(ruta_archivo)
            break
        time.sleep(1)

def set_alarma():
    # Crear un hilo para la alarma
    hilo_alarma = threading.Thread(target=alarm)
    hilo_alarma.daemon = True
    hilo_alarma.start()

# Reloj
window = tk.Tk()
window.title("Reloj Despertador YouTube")
window.geometry("600x500")
reloj_frame = tk.LabelFrame(window, text="Reloj")
reloj_frame.place(relx=0.03, rely=0.04, relheight=0.35, relwidth=0.94)
etiqueta_reloj = tk.Label(reloj_frame, font=("Arial", 48), bg="DeepSkyBlue2", fg="white")
etiqueta_reloj.place(relx=0.2, rely=0.02, relheight=0.4, relwidth=0.6)

actualizar_reloj()

# Despertador
despertador_frame = tk.LabelFrame(window, text="Despertador")
despertador_frame.place(relx=0.03, rely=0.45, relheight=0.5, relwidth=0.94)
horas = tk.Spinbox(despertador_frame, font=("Arial", 45), bg="DeepSkyBlue2", fg="gray20", from_=00, to=23, wrap=True)
horas.place(relx=0.25, rely=0.1, relheight=0.4, relwidth=0.19)
minutos = tk.Spinbox(despertador_frame, font=("Arial", 45), bg="DeepSkyBlue2", fg="gray20", from_=00, to=59, wrap=True)
minutos.place(relx=0.6, rely=0.1, relheight=0.4, relwidth=0.19)
horas_label = tk.Label(despertador_frame, text="Horas", font=("Arial", 20))
horas_label.place(relx=0.27, rely=0.5)
minutos_label = tk.Label(despertador_frame, text="Minutos", font=("Arial", 20))
minutos_label.place(relx=0.6, rely=0.5)
boton = tk.Button(despertador_frame, text="Set", font=("Arial", 25), bg="MediumBlue", fg="white", 
                  command=set_alarma)
boton.place(relx=0.37, rely=0.69, relheight=0.25, relwidth=0.3)

window.mainloop()