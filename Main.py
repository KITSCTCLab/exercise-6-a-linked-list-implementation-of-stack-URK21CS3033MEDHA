Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@URK21CS3035 
KITSCTCLab
/
exercise-6-a-linked-list-implementation-of-stack-URK21CS3035
Public
generated from brightvarghese/22_ODD_DS_Exercise-6.a
Code
Issues
Pull requests
1
Actions
Projects
Wiki
Security
Insights
exercise-6-a-linked-list-implementation-of-stack-URK21CS3035/Main.py /
@URK21CS3035
URK21CS3035 Update Main.py
Latest commit 3e8b717 2 hours ago
 History
 2 contributors
@URK21CS3035@github-classroom
57 lines (53 sloc)  1.26 KB

class Node:
  def _init_(self, data):
    self.data = data
    self.next = None


class Queue:
  def _init_(self):
    self.head = None
    self.last = None

  def enqueue(self, data) -> None:
    # Write your code here
    if self.last==None:
      self.last=Node(data)
      self.last.next=None
      self.last.data=data
      self.head=self.last
    else:
      t=Node(data)
      self.last.next=t
      t.data=data
      t.next=None
      self.last=t
  def dequeue(self) -> None:
    # Write your code here
    t=self.head
    if self.head==None:
      return None
    self.head = t.next
    if(self.head == None):
      self.last = None
  def status(self) -> None:
    # Write your code here
    t=self.head
    if self.head==None and self.last==None:
      print("None")
    while(t!=None):
      print(t.data,end="")
      print("=>",end="")
      t=t.next
      if t==None:
        print("None")

# Do not change the following code
queue = Queue()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "enqueue":
    queue.enqueue(int(data[i]))
  elif operations[i] == "dequeue":
    queue.dequeue()
queue.status()
