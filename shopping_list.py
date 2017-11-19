
# coding: utf-8

# In[1]:


"""Our Shopping List"""
import sys
MAX_ITEMS = 10

def make_shopping_list():
    shopping_list = []
    return shopping_list


def add_item(shopping_list, item):
    shopping_list.append(item)
    return shopping_list



def read_shopping_list(shopping_list):
    return shopping_list


def remove_item(shopping_list, item):
    """Get an item from the shopping list"""
    new_item = None
    try:
        new_item = shopping_list.pop(shopping_list.index(item))
    except (IndexError, ValueError) as error:
        print 'oops!'
    else:
        print "Houston we have a problem"
    return new_item


def main(args):
	items = args
	# get rid of script name
	del items[0]
	shopping_list = make_shopping_list()
	for item in items:
		shopping_list = add_item(shopping_list, item)
	
	num_items = len(shopping_list)
	for i in range(MAX_ITEMS - num_items):
		print "add another item?"
                input = raw_input()
		if input:
		  shopping_list = add_item(shopping_list, input)
		else:
			break

        shopping_list =  read_shopping_list(shopping_list)
	print "Your shopping list is"
	for item in shopping_list:
		print item
	for item in shopping_list:
		print "what do you want to buy?" 
		inpt = raw_input()
		if inpt:
		  item = remove_item(shopping_list, inpt)
		  print "go buy a"
		  print item
		else:
			break
		

	

if __name__ == "__main__":
    main(sys.argv)


