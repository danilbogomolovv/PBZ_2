import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

class Window:
	def __init__(self, width, height, title, resizable1, resizable2):
		self.root = Tk()
		self.root.title(title)
		self.width = width
		self.height = height
		self.root.geometry(f'{width}x{height}')
		self.root.resizable(resizable1, resizable2)

	def run(self):
		self.draw_widgets()
		self.root.mainloop()

	def draw_widgets(self):
		#f_top = Frame(self.root) 
		#f_bot = Frame(self.root)
		#myframe=Frame(self.root,width=self.width,height=self.height)
		#myframe.place(x = 0, y = 0)
		#canvas = Canvas(myframe,width=self.width,height=self.height)
		#frame = Frame(canvas, width=self.width,height=self.height)
		#f_top.pack()
		#f_bot.pack()
		#frame.place(relwidth = 1, relheight = 1)
		#scrollbar = Scrollbar(self.root, orient = 'vertical')
		#scrollbar.configure(command=canvas.yview)
		#canvas.configure(yscrollcommand=scrollbar.set)
		#scrollbar.pack(side="right",fill="y")
		#canvas.pack(side="left")


		self.btn1 = Button(text = 'Карточка мед. статистики', width = 38, bg = 'white', command = btn1_click)
		self.btn1.place(x = 0, y =0)
		self.btn2 = Button(text = 'Таблица переводов', width = 38, bg = 'white', command = btn2_click)
		self.btn2.place(x = 0, y = 25)
		self.btn3 = Button(text = 'Список телефонов палат', width = 38, bg = 'white', command = btn3_click)
		self.btn3.place(x = 0, y = 50)
		self.entry_btn = Button(text = 'Добавить пациента',  width = 38, bg = 'white', command = entry_btn_click)
		self.entry_btn.place(x = 280, y = 0)
		self.delete_btn = Button(text = 'Удалить пациента', width = 38, bg = 'white', command = delete_btn_click)
		self.delete_btn.place(x = 280, y = 25)
		self.update_btn = Button(text = 'Редактировать информацию о пациенте', width = 78, bg = 'white', command = update_btn_click)
		self.update_btn.place(x = 0, y = 80)
		self.check_btn1 = Button(text = 'Просмотр списка больных, достигших заданного возраста женского пола на текущую дату', width = 78, bg = 'white', command = check_btn1_click)
		self.check_btn1.place(x = 0, y = 105)
		self.check_btn2 = Button(text = 'Просмотр списка всех больных на заданное число', width = 78, bg = 'white', command = check_btn2_click)
		self.check_btn2.place(x = 0, y = 130)
		self.check_btn3 = Button(text = 'Просмотр телефона и номера палаты заданного больного', width = 78, bg = 'white', command = check_btn3_click)
		self.check_btn3.place(x = 0, y = 155)
		self.transfer_btn = Button(text = 'Перевести пациента в другую палату', width = 38, bg = 'white', command = transfer_btn_click)
		self.transfer_btn.place(x = 280, y = 50)

	def get_root(self):
		return self.root

def btn1_click():
		mscwindow=Toplevel()
		mscwindow.geometry('1000x250')
		mscwindow.title("Medical statistics card")
		mscwindow.resizable(False, False)
		msc_table = ttk.Treeview(mscwindow, columns = (1,2,3,4,5,6,7,8,9,10,11,12,13,14), show = 'headings')
		msc_table.pack()
		horscrlbar = ttk.Scrollbar( mscwindow,
                           orient ="horizontal",  
                           command = msc_table.xview) 
		horscrlbar.pack(fill = BOTH) 
		msc_table.configure(xscrollcommand = horscrlbar.set) 
		msc_table.heading(1, text = 'Number')
		msc_table.heading(2, text = 'Full name')
		msc_table.heading(3, text = 'Sex')
		msc_table.heading(4, text = 'Age')
		msc_table.heading(5, text = 'Provisional diagnosis')
		msc_table.heading(6, text = 'Admission')
		msc_table.heading(7, text = 'Date of admission')
		msc_table.heading(8, text = 'Height')
		msc_table.heading(9, text = 'Weight')
		msc_table.heading(10, text = 'Hair color')
		msc_table.heading(11, text = 'Special signs')
		msc_table.heading(12, text = 'Room number')
		msc_table.heading(13, text = 'Reason for discharge ')
		msc_table.heading(14, text = 'Discharge date')

		con = mysql.connector.connect (user ='root',password = '171000', host = '127.0.0.1', database = 'lab_2') 
		cursor = con.cursor()

		cursor.execute('SELECT * FROM medical_statistics_card ')
		rows = cursor.fetchall()
	
		for i in rows:
			msc_table.insert('', 'end', values = i)




def btn2_click():
		trwindow=Toplevel()
		#trwindow.geometry('1000x250')
		trwindow.title("Transfer")
		tr_table = ttk.Treeview(trwindow, columns = (1,2,3,4,5,6), show = 'headings', height = 10)
		tr_table.pack()
		tr_table.heading(1, text = 'Number')
		tr_table.heading(2, text = 'Full name')
		tr_table.heading(3, text = 'Previous room number')
		tr_table.heading(4, text = 'Next room number')
		tr_table.heading(5, text = 'Next room phone')
		tr_table.heading(6, text = 'Transfer date')

		con = mysql.connector.connect (user ='root',password = '171000', host = '127.0.0.1', database = 'lab_2') 
		cursor = con.cursor()

		cursor.execute('SELECT * FROM transfer')
		rows = cursor.fetchall()
	
		for i in rows:
			tr_table.insert('', 'end', values = i)
	
def btn3_click():
		dhwindow=Toplevel()
		#dhwindow.geometry('1000x250')
		dhwindow.title("Ward phone")
		dh_table = ttk.Treeview(dhwindow, columns = (1,2,3), show = 'headings', height = 10)
		dh_table.pack()
		dh_table.heading(1, text = 'Number')
		dh_table.heading(2, text = 'Room number')
		dh_table.heading(3, text = 'Room phone')

		con = mysql.connector.connect (user ='root',password = '171000', host = '127.0.0.1', database = 'lab_2') 
		cursor = con.cursor()

		cursor.execute('SELECT * FROM ward_phone')
		rows = cursor.fetchall()
	
		for i in rows:
			dh_table.insert('', 'end', values = i)

def entry_btn_click():

	def entry():
		con = mysql.connector.connect (user ='root',password = '171000', host = '127.0.0.1', database = 'lab_2') 
		cursor = con.cursor()
		if Discharge_date.get() == '-':
			cursor.execute(f"insert into medical_statistics_card (fullname, sex, age, provisional_diagnosis, admission, date_of_admission, height, weight, hair_color, special_signs, room_number,  reason_for_discharge,  discharge_date) VALUES ('{Full_name.get()}', '{Sex.get()}', '{Age.get()}', '{Provisional_diagnosis.get()}', '{Admission.get()}', '{Date_of_admission.get()}', '{Height.get()}', '{Weight.get()}', '{Hair_color.get()}', '{Special_signs.get()}', '{Room_number.get()}', '{Reason_for_discharge.get()}', NULL);")
		else:
			cursor.execute(f"insert into medical_statistics_card (fullname, sex, age, provisional_diagnosis, admission, date_of_admission, height, weight, hair_color, special_signs, room_number,  reason_for_discharge,  discharge_date) VALUES ('{Full_name.get()}', '{Sex.get()}', '{Age.get()}', '{Provisional_diagnosis.get()}', '{Admission.get()}', '{Date_of_admission.get()}', '{Height.get()}', '{Weight.get()}', '{Hair_color.get()}', '{Special_signs.get()}', '{Room_number.get()}', '{Reason_for_discharge.get()}', '{Discharge_date.get()}');")
		entrywindow.destroy()
		con.commit()

	entrywindow=Toplevel()
	entrywindow.title("Entry")
	entrywindow.resizable(False, False)  
	Label(entrywindow, text="Full name").grid(row=0, column=0)
	Label(entrywindow, text="Sex").grid(row=1, column=0)
	Label(entrywindow, text="Age").grid(row=2, column=0)
	Label(entrywindow, text="Provisional diagnosis").grid(row=3, column=0)
	Label(entrywindow, text="Admission").grid(row=4, column=0)
	Label(entrywindow, text="Date of admission").grid(row=5, column=0)
	Label(entrywindow, text="Height").grid(row=6, column=0)
	Label(entrywindow, text="Weight").grid(row=7, column=0)
	Label(entrywindow, text="Hair color").grid(row=8, column=0)
	Label(entrywindow, text="Special signs").grid(row=9, column=0)
	Label(entrywindow, text="Room number").grid(row=10, column=0)
	Label(entrywindow, text="Reason for discharge").grid(row=11, column=0)
	Label(entrywindow, text="Discharge date").grid(row=12, column=0)
	Full_name=Entry(entrywindow, width=15)
	Full_name.grid(row=0, column=3, sticky=W)
	Sex=Entry(entrywindow, width=15)
	Sex.grid(row=1, column=3,  sticky=W)
	Age=Entry(entrywindow, width=15)
	Age.grid(row=2, column=3,  sticky=W)
	Provisional_diagnosis=Entry(entrywindow, width=15)
	Provisional_diagnosis.grid(row=3, column=3,  sticky=W) 
	Admission=Entry(entrywindow, width=15)
	Admission.grid(row=4, column=3,  sticky=W) 
	Date_of_admission=Entry(entrywindow, width=15)
	Date_of_admission.grid(row=5, column=3,  sticky=W) 
	Height=Entry(entrywindow, width=15)
	Height.grid(row=6, column=3,  sticky=W) 
	Weight=Entry(entrywindow, width=15)
	Weight.grid(row=7, column=3,  sticky=W) 
	Hair_color=Entry(entrywindow, width=15)
	Hair_color.grid(row=8, column=3,  sticky=W) 
	Special_signs=Entry(entrywindow, width=15)
	Special_signs.grid(row=9, column=3,  sticky=W) 
	Room_number=Entry(entrywindow, width=15)
	Room_number.grid(row=10, column=3,  sticky=W) 
	Reason_for_discharge=Entry(entrywindow, width=15)
	Reason_for_discharge.grid(row=11, column=3,  sticky=W) 
	Discharge_date=Entry(entrywindow, width=15)
	Discharge_date.grid(row=12, column=3,  sticky=W) 
	Button(entrywindow, text="Добавить", command=entry).grid(row=13, columnspan=4)

def delete_btn_click():

	def delete():
		con = mysql.connector.connect (user ='root',password = '171000', host = '127.0.0.1', database = 'lab_2') 
		cursor = con.cursor()
		cursor.execute(f"DELETE FROM medical_statistics_card WHERE fullname = '{Full_name.get()}' and age = '{Age.get()}';")
		deletewindow.destroy()
		con.commit()

	deletewindow=Toplevel()
	deletewindow.title("Delete")
	deletewindow.resizable(False, False)  
	Label(deletewindow, text="Введите полное имя и возраст пациента, которого вы хотите удалить").grid(row=0, column=3)
	Label(deletewindow, text="Full name").grid(row=1, column=0)
	Label(deletewindow, text="Age").grid(row=2, column=0)
	Full_name=Entry(deletewindow, width=15)
	Full_name.grid(row=1, column=3, sticky=W)
	Age=Entry(deletewindow, width=15)
	Age.grid(row=2, column=3,  sticky=W)
	Button(deletewindow, text="Удалить", command=delete).grid(row=13, columnspan=4)


def update_btn_click():

	def start_to_update():

		def update():
			con = mysql.connector.connect (user ='root',password = '171000', host = '127.0.0.1', database = 'lab_2') 
			cursor = con.cursor()
			if len(patient_data) > 16:
				cursor.execute(f"UPDATE medical_statistics_card SET fullname = '{Full_name.get()}', sex = '{Sex.get()}', age = '{Age.get()}', provisional_diagnosis = '{Provisional_diagnosis.get()}', admission = '{Admission.get()}', date_of_admission = '{Date_of_admission.get()}', height = '{Height.get()}', weight = '{Weight.get()}', hair_color = '{Hair_color.get()}', special_signs = '{Special_signs.get()}', room_number = '{Room_number.get()}', reason_for_discharge = '{Reason_for_discharge.get()}', discharge_date = '{Discharge_date.get()}' WHERE id ='{patient_data[0]}';")
			else:
				cursor.execute(f"UPDATE medical_statistics_card SET fullname = '{Full_name.get()}', sex = '{Sex.get()}', age = '{Age.get()}', provisional_diagnosis = '{Provisional_diagnosis.get()}', admission = '{Admission.get()}', date_of_admission = '{Date_of_admission.get()}', height = '{Height.get()}', weight = '{Weight.get()}', hair_color = '{Hair_color.get()}', special_signs = '{Special_signs.get()}', room_number = '{Room_number.get()}', reason_for_discharge = '{Reason_for_discharge.get()}' WHERE id ='{patient_data[0]}';")
			update2window.destroy()
			con.commit()


		con = mysql.connector.connect (user ='root',password = '171000', host = '127.0.0.1', database = 'lab_2') 
		cursor = con.cursor()
		cursor.execute(f"SELECT * FROM medical_statistics_card WHERE fullname = '{global_full_name.get()}' and age = '{global_age.get()}';")
		rows = cursor.fetchall()
		patient_data = []
		for i in rows:
			patient_data = str(i).split(', ')
			for j in range(0, len(patient_data)):
				patient_data[j] = patient_data[j].replace('\'','').replace('(','').replace(')','').replace('datetime.date','')

		#cursor.execute(f"DELETE FROM medical_statistics_card WHERE fullname = '{global_full_name.get()}' and age = '{global_age.get()}';")
		con.commit()

		update2window=Toplevel()
		update2window.title("Update")
		update2window.resizable(False, False)
		Label(update2window, text="Full name").grid(row=0, column=0)
		Label(update2window, text="Sex").grid(row=1, column=0)
		Label(update2window, text="Age").grid(row=2, column=0)
		Label(update2window, text="Provisional diagnosis").grid(row=3, column=0)
		Label(update2window, text="Admission").grid(row=4, column=0)
		Label(update2window, text="Date of admission").grid(row=5, column=0)
		Label(update2window, text="Height").grid(row=6, column=0)
		Label(update2window, text="Weight").grid(row=7, column=0)
		Label(update2window, text="Hair color").grid(row=8, column=0)
		Label(update2window, text="Special signs").grid(row=9, column=0)
		Label(update2window, text="Room number").grid(row=10, column=0)
		Label(update2window, text="Reason for discharge").grid(row=11, column=0)
		Label(update2window, text="Discharge date").grid(row=12, column=0)
		Full_name=Entry(update2window, width=15)
		Full_name.insert(0,patient_data[1])
		Full_name.grid(row=0, column=3, sticky=W)
		Sex=Entry(update2window, width=15)
		Sex.insert(0,patient_data[2])
		Sex.grid(row=1, column=3,  sticky=W)
		Age=Entry(update2window, width=15)
		Age.insert(0,patient_data[3])
		Age.grid(row=2, column=3,  sticky=W)
		Provisional_diagnosis=Entry(update2window, width=15)
		Provisional_diagnosis.insert(0,patient_data[4])
		Provisional_diagnosis.grid(row=3, column=3,  sticky=W) 
		Admission=Entry(update2window, width=15)
		Admission.insert(0,patient_data[5])
		Admission.grid(row=4, column=3,  sticky=W) 
		Date_of_admission=Entry(update2window, width=15)
		if len(patient_data[7]) > 1 and len(patient_data[8]) > 1:
			Date_of_admission.insert(0,f'{patient_data[6]}-{patient_data[7]}-{patient_data[8]}')
		elif len(patient_data[7]) == 1 and len(patient_data[8]) > 1:
			Date_of_admission.insert(0,f'{patient_data[6]}-0{patient_data[7]}-{patient_data[8]}')
		elif len(patient_data[7]) > 1 and len(patient_data[8]) == 1:
			Date_of_admission.insert(0,f'{patient_data[6]}-{patient_data[7]}-0{patient_data[8]}')
		elif len(patient_data[7]) == 1 and len(patient_data[8]) == 1:	
			Date_of_admission.insert(0,f'{patient_data[6]}-0{patient_data[7]}-0{patient_data[8]}')
		Date_of_admission.grid(row=5, column=3,  sticky=W) 
		Height=Entry(update2window, width=15)
		Height.insert(0,patient_data[9])
		Height.grid(row=6, column=3,  sticky=W) 
		Weight=Entry(update2window, width=15)
		Weight.insert(0,patient_data[10])
		Weight.grid(row=7, column=3,  sticky=W) 
		Hair_color=Entry(update2window, width=15)
		Hair_color.insert(0,patient_data[11])
		Hair_color.grid(row=8, column=3,  sticky=W) 
		Special_signs=Entry(update2window, width=15)
		Special_signs.insert(0,patient_data[12])
		Special_signs.grid(row=9, column=3,  sticky=W) 
		Room_number=Entry(update2window, width=15)
		Room_number.insert(0,patient_data[13])
		Room_number.grid(row=10, column=3,  sticky=W) 
		Reason_for_discharge=Entry(update2window, width=15)
		Reason_for_discharge.insert(0,patient_data[14])
		Reason_for_discharge.grid(row=11, column=3,  sticky=W) 
		Discharge_date=Entry(update2window, width=15)
		if len(patient_data) > 16:
			if len(patient_data[16]) > 1 and len(patient_data[17]) > 1:
				Discharge_date.insert(0,f'{patient_data[15]}-{patient_data[16]}-{patient_data[17]}')
			elif len(patient_data[16]) == 1 and len(patient_data[17]) > 1:
				Discharge_date.insert(0,f'{patient_data[15]}-0{patient_data[16]}-{patient_data[17]}')
			elif len(patient_data[16]) > 1 and len(patient_data[17]) == 1:
				Discharge_date.insert(0,f'{patient_data[15]}-{patient_data[16]}-0{patient_data[17]}')
			elif len(patient_data[16]) == 1 and len(patient_data[17]) == 1:	
				Discharge_date.insert(0,f'{patient_data[15]}-0{patient_data[16]}-0{patient_data[17]}')
			Discharge_date.grid(row=12, column=3,  sticky=W) 
		Button(update2window, text="Завершить", command=update).grid(row=13, columnspan=4)
		updatewindow.destroy()


	updatewindow=Toplevel()
	updatewindow.title("Update")
	updatewindow.resizable(False, False)  
	Label(updatewindow, text="Введите полное имя и возраст пациента, информацию о котором вы хотите редактировать").grid(row=0, column=3)
	Label(updatewindow, text="Full name").grid(row=1, column=0)
	Label(updatewindow, text="Age").grid(row=2, column=0)
	global_full_name=Entry(updatewindow, width=15)
	global_full_name.grid(row=1, column=3, sticky=W)
	global_age=Entry(updatewindow, width=15)
	global_age.grid(row=2, column=3,  sticky=W)

	Button(updatewindow, text="Редактировать", command=start_to_update).grid(row=13, columnspan=4)


def check_btn1_click():

	def check1_search():
		fincheck1window=Toplevel()
		fincheck1window.title("Result")
		fincheck1window.resizable(False, False)  
		ch1_table = ttk.Treeview(fincheck1window, columns = (1,2,3,4), show = 'headings', height = 10)
		ch1_table.pack()
		ch1_table.heading(1, text = 'Number')
		ch1_table.heading(2, text = 'Full name')
		ch1_table.heading(3, text = 'Age')
		ch1_table.heading(4, text = 'Date of admission')

		con = mysql.connector.connect (user ='root',password = '171000', host = '127.0.0.1', database = 'lab_2') 
		cursor = con.cursor()

		cursor.execute(f"SELECT id, fullname, age, date_of_admission FROM medical_statistics_card WHERE sex = 'Ж' and age >= {Age.get()} and discharge_date IS NULL")
		rows = cursor.fetchall()
	
		for i in rows:
			ch1_table.insert('', 'end', values = i)
		check1window.destroy()


	check1window=Toplevel()
	check1window.title("Search")
	check1window.resizable(False, False)
	Label(check1window, text="Введите возраст которого должен достичь данный пациент").grid(row=0, column=3)
	Label(check1window, text="Age").grid(row=1, column=0)
	Age=Entry(check1window, width=15)
	Age.grid(row=1, column=3,  sticky=W)
	Button(check1window, text="Искать", command=check1_search).grid(row=13, columnspan=4)


def check_btn2_click():

	def check2_search():
		fincheck2window=Toplevel()
		fincheck2window.title("Result")
		fincheck2window.resizable(False, False) 
		ch2_table = ttk.Treeview(fincheck2window, columns = (1,2,3,4,5), show = 'headings', height = 10)
		ch2_table.pack()
		ch2_table.heading(1, text = 'Number')
		ch2_table.heading(2, text = 'Full name')
		ch2_table.heading(3, text = 'Age')
		ch2_table.heading(4, text = 'Date of admission')
		ch2_table.heading(5, text = 'Room number')

		con = mysql.connector.connect (user ='root',password = '171000', host = '127.0.0.1', database = 'lab_2') 
		cursor = con.cursor()

		cursor.execute(f"SELECT id, fullname, age, date_of_admission, room_number FROM medical_statistics_card WHERE date_of_admission <= '{Date.get()}' and (discharge_date > '{Date.get()}' or discharge_date is NULL)")
		rows = cursor.fetchall()
	
		for i in rows:
			ch2_table.insert('', 'end', values = i)
		check2window.destroy()

	check2window=Toplevel()
	check2window.title("Search")
	check2window.resizable(False, False)
	Label(check2window, text="Введите нужную вам дату").grid(row=0, column=3)
	Label(check2window, text="Date").grid(row=1, column=0)
	Date=Entry(check2window, width=15)
	Date.grid(row=1, column=3,  sticky=W)
	Button(check2window, text="Искать", command=check2_search).grid(row=13, columnspan=4)


def check_btn3_click():

	def check3_search():
		fincheck3window=Toplevel()
		fincheck3window.title("Result")
		fincheck3window.resizable(False, False) 
		ch3_table = ttk.Treeview(fincheck3window, columns = (1,2,3,4,5), show = 'headings', height = 10)
		ch3_table.pack()
		ch3_table.heading(1, text = 'Number')
		ch3_table.heading(2, text = 'Full name')
		ch3_table.heading(3, text = 'Age')
		ch3_table.heading(4, text = 'Room number')
		ch3_table.heading(5, text = 'Room phone')

		con = mysql.connector.connect (user ='root',password = '171000', host = '127.0.0.1', database = 'lab_2') 
		cursor = con.cursor()

		cursor.execute(f"SELECT medical_statistics_card.id, medical_statistics_card.fullname, medical_statistics_card.age, medical_statistics_card.room_number, ward_phone.room_phone  FROM medical_statistics_card JOIN ward_phone ON medical_statistics_card.room_number = ward_phone.room_number WHERE medical_statistics_card.fullname = '{Full_name.get()}';")
		rows = cursor.fetchall()
	
		for i in rows:
			ch3_table.insert('', 'end', values = i)
		check3window.destroy()

	check3window=Toplevel()
	check3window.title("Search")
	check3window.resizable(False, False)
	Label(check3window, text="Введите имя нужного вам пациента").grid(row=0, column=3)
	Label(check3window, text="Full name").grid(row=1, column=0)
	Full_name=Entry(check3window, width=15)
	Full_name.grid(row=1, column=3,  sticky=W)
	Button(check3window, text="Искать", command=check3_search).grid(row=13, columnspan=4)

def transfer_btn_click():
	def transfer():
		con = mysql.connector.connect (user ='root',password = '171000', host = '127.0.0.1', database = 'lab_2') 
		cursor = con.cursor()
		result_phone = []
		cursor.execute(f"SELECT room_phone FROM ward_phone WHERE room_number = '{Next_room_number.get()};'")
		rows = cursor.fetchall()
		for i in rows:
			result_phone = str(i)
		result_phone = result_phone.replace('(','').replace(')','').replace(',','')
		print(result_phone)
		cursor.execute(f"INSERT INTO transfer(fullname, previous_room_number, next_room_number, next_room_phone, transfer_date) VALUES ('{Full_name.get()}', '{Previous_room_number.get()}', '{Next_room_number.get()}', {result_phone}, '{Transfer_date.get()}');")
		cursor.execute(f"UPDATE medical_statistics_card SET room_number = '{Next_room_number.get()}' WHERE fullname = '{Full_name.get()}' AND room_number = '{Previous_room_number.get()}';")
		con.commit()
		transferwindow.destroy()


	transferwindow=Toplevel()
	transferwindow.title("Transfer")
	transferwindow.resizable(False, False)
	Label(transferwindow, text="Введите данные").grid(row=0, column=3)
	Label(transferwindow, text="Full name").grid(row=1, column=0)
	Label(transferwindow, text="Previous room number").grid(row=2, column=0)
	Label(transferwindow, text="Next room number").grid(row=3, column=0)
	#Label(transferwindow, text="Next room phone").grid(row=4, column=0)
	Label(transferwindow, text="Transfer date").grid(row=4, column=0)
	Full_name=Entry(transferwindow, width=15)
	Full_name.grid(row=1, column=3,  sticky=W)
	Previous_room_number=Entry(transferwindow, width=15)
	Previous_room_number.grid(row=2, column=3,  sticky=W)
	Next_room_number=Entry(transferwindow, width=15)
	Next_room_number.grid(row=3, column=3,  sticky=W)
	#Next_room_phone=Entry(transferwindow, width=15)
	#Next_room_phone.grid(row=4, column=3,  sticky=W)
	Transfer_date=Entry(transferwindow, width=15)
	Transfer_date.grid(row=4, column=3,  sticky=W)
	Button(transferwindow, text="Перевести", command=transfer).grid(row=5, columnspan=4)

