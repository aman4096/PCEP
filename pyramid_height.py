blocks = int(input("Enter the number of blocks: "))
#
# Write your code here.
#
layer_length=0
blocks_used=0
while(blocks>layer_length):
    layer_length+=1
    blocks_used+=layer_length
    blocks-=layer_length
print("The height of the pyramid:", layer_length)