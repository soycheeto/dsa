class Node:
    def __init__(self, doc, next=None):
        self.doc = doc  
        self.next = next  

class PrinterQueue:
    def __init__(self):
        self.front = None  
        self.rear = None  
        
    def is_empty(self):
        return self.front is None

    def submit_print_job(self, doc):
        new_node = Node(doc)
        if self.is_empty():
            self.front = self.rear = new_node 
        else:
            self.rear.next = new_node  
            self.rear = new_node  

        print(f"Print job '{doc}' submitted to the queue.")

    def process_print_job(self):
        if self.is_empty():
            print("No print jobs to process. Queue is empty.")
            return None
        else:
            print_job = self.front.doc
            self.front = self.front.next 

            if self.front is None:
                self.rear = None

            print(f"Processing print job: '{print_job}'")
            return print_job

    def display_queue(self):
        if self.is_empty():
            print("No print jobs in the queue.")
        else:
            print("Current print queue:")
            current = self.front
            while current:
                print(f"- {current.doc}")
                current = current.next


printer_queue = PrinterQueue()


printer_queue.submit_print_job("Document_A.pdf")
printer_queue.submit_print_job("Document_B.docx")
printer_queue.submit_print_job("Document_C.pptx")


printer_queue.display_queue()

printer_queue.process_print_job() 
printer_queue.process_print_job()  
printer_queue.display_queue()
printer_queue.process_print_job() 

printer_queue.process_print_job()  
