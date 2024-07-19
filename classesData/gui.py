from tkinter import *
from tkinter import messagebox
from .users import Users
from .graph import Graph
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class SocialNetworkApp:
    def __init__(self, root):
        self.user_manager = Users()
        self.social_network = Graph()
        
        self.root = root
        self.root.title("Social Network ")

        self.frame = Frame(root)
        self.frame.pack()

       # User Section
        Label(self.frame, text="User ID").grid(row=0, column=0)
        self.user_id_entry = Entry(self.frame)
        self.user_id_entry.grid(row=0, column=1)

        Label(self.frame, text="Name").grid(row=1, column=0)
        self.name_entry = Entry(self.frame)
        self.name_entry.grid(row=1, column=1)

        Label(self.frame, text="Email").grid(row=2, column=0)
        self.email_entry = Entry(self.frame)
        self.email_entry.grid(row=2, column=1)

        Label(self.frame, text="Age").grid(row=3, column=0)
        self.age_entry = Entry(self.frame)
        self.age_entry.grid(row=3, column=1)

        Button(self.frame, text="Add User", command=self.add_user).grid(row=4, column=0, columnspan=2)

        # Friendship Section
        Label(self.frame, text="User ID 1").grid(row=5, column=0)
        self.user_id1_entry = Entry(self.frame)
        self.user_id1_entry.grid(row=5, column=1)

        Label(self.frame, text="User ID 2").grid(row=6, column=0)
        self.user_id2_entry = Entry(self.frame)
        self.user_id2_entry.grid(row=6, column=1)

        Label(self.frame, text="Weight").grid(row=7, column=0)
        self.weight_entry = Entry(self.frame)
        self.weight_entry.grid(row=7, column=1)

        Button(self.frame, text="Add Friendship", command=self.add_friendship).grid(row=8, column=0, columnspan=2)

        # Remove Friendship Button
        Button(self.frame, text="Remove Friendship", command=self.remove_friendship).grid(row=9, column=0, columnspan=2)

        # Display Section
        Button(self.frame, text="Display Users", command=self.display_users).grid(row=9, column=0, columnspan=2)
        self.output_text = Text(self.frame, height=10, width=40)
        self.output_text.grid(row=10, column=0, columnspan=2)

        # Graph Visualization Section
        Button(self.frame, text="Show Network Graph", command=self.show_network_graph).grid(row=11, column=0, columnspan=2)

    def add_user(self):
         try:
             
             user_id = int(self.user_id_entry.get())
             name = self.name_entry.get()
             email = self.email_entry.get()
             age = int(self.age_entry.get())

             if self.user_manager.get_user(user_id):
                messagebox.showerror("Error", f"User ID {user_id} already exists.")
                return
             
             self.user_manager.add_user(user_id, name, email, age)
             self.social_network.add_user(user_id, name)
            
             messagebox.showinfo("Success", f"User {name} added successfully!")
         except ValueError:
             messagebox.showerror("Error", "Invalid input. Please enter valid data.")

        
       
        
      

    def add_friendship(self):
        try:
            user_id1 = int(self.user_id1_entry.get())
            user_id2 = int(self.user_id2_entry.get())
            weight = float(self.weight_entry.get())

            if not self.user_manager.get_user(user_id1):
                messagebox.showerror("Error", f"User ID {user_id1} does not exist.")
                return

            if not self.user_manager.get_user(user_id2):
                messagebox.showerror("Error", f"User ID {user_id2} does not exist.")
                return

            if user_id1 == user_id2:
                messagebox.showerror("Error", "A user cannot be friends with themselves.")
                return

            #self.user_manager.add_friend(user_id1, user_id2)
            self.social_network.add_friendship(user_id1, user_id2, weight)
            
            messagebox.showinfo("Success", f"Friendship added between User {user_id1} and User {user_id2} with weight {weight}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid user IDs.")

    def display_users(self):
        self.output_text.delete(1.0, END)
        users = self.social_network.get_users()
        if not users:
            self.output_text.insert(END, "No users in the network.\n")
        for user in users:
            self.output_text.insert(END, f"User: {user[1]} (ID: {user[0]})\n")
            friends = self.social_network.get_friends(user[0])
            if friends:
                self.output_text.insert(END, "  Friends: " + ", ".join([friend[1] for friend in friends]) + "\n")
            else:
                self.output_text.insert(END, "  No friends\n")
    
    def show_network_graph(self):
        self.social_network.draw_graph()