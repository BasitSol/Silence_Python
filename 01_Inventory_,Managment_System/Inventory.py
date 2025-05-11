# This is the inventory manager tool for a tool Shop

class Tool:
    def __init__(self, tool_id, name, price):
        self.tool_id = tool_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"ID: {self.tool_id} | Name: {self.name} | Price: {self.price}"

class Inventory(Tool):
    def __init__(self):
        self.listOfTools = []

    def add_tool(self, tool):
        self.listOfTools.append(tool)
        print(f"Tool: '{tool.name}' added Successfully !")
    
    def remove_tool(self, tool_id):
        for tool in self.listOfTools:
            if tool.tool_id == tool_id:
                self.listOfTools.remove(tool)
                print(f"Tool '{tool.name}' Removed Successfully !")
                return 
        raise ValueError('Tool Not Found !')
    
    def display_inventory(self):
        if not self.listOfTools:
            print("Inventory is empty")
        else:
            print("\n -----Tool Inventory-----")
            for tool in self.listOfTools:
                print(tool)
    
    def save_to_file(self, filename = "inventory.txt"):
        try:
            with open(filename, 'w') as file:
               for tool in self.listOfTools:
                  file.write(f"ID:{tool.tool_id}, Tool_Name:{tool.name}, Price:{tool.price} \n")
            print("Inventory saved to the file")
        except Exception as e:
            print(f"Error While Saving to file {e}")

    def load_from_file(self, filename="inventory.txt"):
        try:
            with open(filename, 'r') as file:
                self.tools = []  
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) != 3:
                        raise ValueError("Malformed line")
                    tool_id, name, price = parts
                    self.tools.append(Tool(tool_id, name, float(price)))
            print("Inventory loaded from file.")
        except FileNotFoundError:
            print("File not found.")
        except ValueError:
            print("Error loading file: Incorrect format.")
        except Exception as e:
            print(f"Unknown error: {e}")




def main():
        inventory = Inventory()
        
        while True:
            print("\nTool Inventory Manager")
            print("1. Add Tool")
            print("2. Remove Tool")
            print("3. Display Inventory")
            print("4. Save to File")
            print("5. Load from File")
            print("6. Exit")

            choice = input("Enter Your Choice (1-6)")
            
            try:
                if choice == '1':
                    tool_id = input("Enter tool ID: ")
                    name = input("Enter the name of the Tool: ")
                    price = float(input("Enter the Price of the Tool: "))
                    inventory.add_tool(Tool(tool_id, name, price))
                elif choice == '2':
                    tool_id = input("Enter the Tool ID to remove the Tool: ")
                    inventory.remove_tool(tool_id)
                elif choice == '3':
                    inventory.display_inventory()
                elif choice == '4':
                    inventory.save_to_file()
                elif choice == '5':
                    inventory.load_from_file()
                elif choice == '6':
                    print("Exiting from the Store !")
                    break
                else:
                    print("Invalid Choice Please Enter the Number from (1 - 6)")
            except ValueError as ve:
                print(f"ValueError As {ve}")
            except Exception as e:
                print(f"Error: {e}")
            
            
            
if __name__ == "__main__":
    main()