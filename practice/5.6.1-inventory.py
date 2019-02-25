# 好玩游戏的物品清单
stuff = {'rope': 1,'torch': 6,'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))
# displayInventory(inv)

# 对一个字典进行遍历的同时，如果进行了元素的增删，会报错。解决方法为改为对字典键值进行遍历。
def addToInventory(inventory, addedItems):   
    for i in addedItems:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory[i] = 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)