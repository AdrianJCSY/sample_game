import customtkinter

class ButtonBoard:
    def __init__(self, display):
        self.display = display
        self.init_nodes()
        self.selecting = False
        self.selecting_node = None

        self.button_width = 50
        self.button_height = 50
        self.button_padding = 20

        self.node_connections = {}

    def init_nodes(self):
        self.nodes = []
        rows = 9
        for i in range(rows):
            col = []
            self.nodes.append(col)

    def on_button_click(self, id):
        print(f"Button {id} clicked!")
        if not self.selecting:
            self.selecting = True
            self.selecting_node = id
        elif self.selecting_node != id:
            # Check if connection already exist
            print(f"{self.selecting_node}-{id}")
            if id in self.nodes[self.selecting_node]:
                bool1 = f"{self.selecting_node}-{id}" in self.node_connections
                boolalt = f"{id}-{self.selecting_node}" in self.node_connections
                print(f"{bool1} {boolalt} {self.node_connections}")
                if bool1:
                    connection_data = self.node_connections.pop(f"{self.selecting_node}-{id}", None)
                    if connection_data:
                        print(f"Deleted line {self.selecting_node}-{id}")
                elif boolalt:
                    connection_data = self.node_connections.pop(f"{id}-{self.selecting_node}", None)
                    if connection_data:
                        print(f"Deleted line {id}-{self.selecting_node}")

                self.nodes[self.selecting_node].remove(id)
                self.nodes[id].remove(self.selecting_node)
                self.selecting = False
            else:
                #Check if placements are valid (manually; some fuckery afoot)
                #This one swaps the values around from least to great (for an easier comparison).
                if self.selecting_node > id:
                    self.selecting_node , id = id , self.selecting_node

               #ThereHasToBeABetterWay.mp4
                if self.selecting_node == 0 and id not in {1, 3, 4}:
                    print(f"Invalid placement!")
                    self.selecting = False
                
                elif self.selecting_node == 1 and id not in {0, 2, 3, 4, 5}:
                    print(f"Invalid placement!")
                    self.selecting = False
                
                elif self.selecting_node == 2 and id not in {1, 4, 5}:
                    print(f"Invalid placement!")
                    self.selecting = False
                
                elif self.selecting_node == 3 and id not in {0, 1, 4, 6, 7}:
                    print(f"Invalid placement!")
                    self.selecting = False
                
                #No 4; 4 can do anything it desires in life
                
                elif self.selecting_node == 5 and id not in {1, 2, 4, 7, 8}:
                    print(f"Invalid placement!")
                    self.selecting = False
                
                elif self.selecting_node == 6 and id not in {3, 4, 7}:
                    print(f"Invalid placement!")
                    self.selecting = False

                elif self.selecting_node == 7 and id not in {3, 4, 5, 6, 8}:
                    print(f"Invalid placement!")
                    self.selecting = False

                elif self.selecting_node == 8 and id not in {4, 5, 7}:
                    print(f"Invalid placement!")
                    self.selecting = False

                else:
                    # Add a line
                    self.node_connections[f"{self.selecting_node}-{id}"] = {
                        "x1" : (self.selecting_node % 3) * (self.button_width + self.button_padding) + self.button_width/2,
                        "y1" : 0 + self.button_height/2 if self.selecting_node < 3 
                            else (self.button_height + self.button_padding) + self.button_width/2 if self.selecting_node < 6 
                            else 2 * (self.button_height + self.button_padding) + self.button_width/2, 
                        "x2" : (id % 3) * (self.button_width + self.button_padding) + self.button_width/2,
                        "y2" : 0 + self.button_height/2 if id < 3 
                            else (self.button_height + self.button_padding) + self.button_width/2 if id < 6 
                            else 2 * (self.button_height + self.button_padding) + self.button_width/2,
                    }
                    # Add as a connection to node to node
                    self.nodes[self.selecting_node].append(id)
                    self.nodes[id].append(self.selecting_node)
                    self.selecting = False
        else:
            self.selecting = False
            
        print(f"Selecting: {self.selecting}")
        self.refresh_board()

    def refresh_board(self):
        # Clear the canvas by deleting all items on it
        for item in self.display.canvas.find_all():
            self.display.canvas.delete(item)

        # Recreate the board with buttons and lines
        self.create_board()


    def draw_line(self, start_x, start_y, end_x, end_y, width=2, color="black"):
        self.display.canvas.create_line(start_x, start_y, end_x, end_y, width=width, fill=color)

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button_id = j + (i * 3)
                button_x = j * (self.button_width + self.button_padding)
                button_y = i * (self.button_height + self.button_padding)

                button = customtkinter.CTkButton(
                    master=self.display.canvas,
                    text=f"{button_id}",
                    command=lambda id=button_id: self.on_button_click(id),
                    width=self.button_width,  # Specify width here
                    height=self.button_height  # Specify height here
                )
                button.place(x=button_x, y=button_y)  # Use place method without width and height

                color_state = "yellow" if self.selecting_node == button_id and self.selecting else \
               "green" if any(button_id in col for col in self.nodes) else \
               "blue"

                button.configure(fg_color=color_state, hover_color=color_state)

                # bg_color -> background color of the whole element
                # fg_color/hover_color -> color of the object
                # border_color -> border color
                # text_color/text_color_disabled -> text color

        for key, node_connection in self.node_connections.items():
            self.draw_line(node_connection.get("x1"), node_connection.get("y1"), 
                           node_connection.get("x2"), node_connection.get("y2"))
