

# Helper function to find the length of the cycle
def find_cycle_length(slow):
  # Find the length of the cycle
  start = slow
  current = slow.next
  cycle_length = 1
  while current != start:
    current = current.next
    cycle_length += 1
  return cycle_length

# Function to check if a linked list contains a cycle
def contains_cycle(head):
  # Handle the case of an empty linked list
  if head == None:
    return False

  # Initialize the "hare" and "tortoise" pointers
  hare = head
  tortoise = head

  # Loop until the hare catches up to the tortoise or the linked list ends
  while hare != None and hare.next != None:
    hare = hare.next.next
    tortoise = tortoise.next

    # If the hare and tortoise meet, there is a cycle
    if hare == tortoise:
      # Find the length of the cycle
      cycle_length = find_cycle_length(tortoise)

      # Return True to indicate that a cycle was found
      return True

  # If the hare reaches the end of the linked list, there is no cycle
  return False



def find_center(lst):
	if (lst == None): return None
	slowpointer = lst # still the first node
	fastpointer = lst # still the first node
	
	while(fastpointer != None):
		fastpointer = fastpointer.next
		if(fastpointer != None):
			fastpointer.next
			slowpointer.next
	return slowpointer


def detectCycle(list):
	if list == None: return False
	slowpointer = list
	fastpointer = list 

	while(fastpointer != None): 
		fastpointer = fastpointer.next.next 
		slowpointer = slowpointer.next
		if fastpointer == slowpointer: return True 
	return False
