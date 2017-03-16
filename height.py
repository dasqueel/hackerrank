def height(root):
	longest = 0
    #if right go to right
    #change root to current
    if root.left == None and root.right == None:
    	return height