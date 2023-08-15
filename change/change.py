def find_fewest_coins(coins: list[int], target: int):
    pass


def recursion(coins: list[int], 
              target: int, 
              current_length: int, 
              shortest_length: int, 
              change: list):
    print("---------------------------------------")
    print("current_length: " + str(current_length))
    print("shortest_length: " + str(shortest_length))
    print("target: " + str(target))
    print("coins: " + str(coins))
    new_current_length = current_length
    new_coins = coins.copy()
    for coin in reversed(coins):
        print("target: " + str(target))
        print("coin: " + str(coin))
        
        if new_current_length + 1 >= shortest_length:
            break

        if coin <= target:
            new_current_length = current_length + 1
            change.append(coin)
            if coin == target:
                shortest_length = new_current_length
                
                print("shortest_length: " + str(shortest_length))
                print("change: " + str(change))
                return shortest_length
            if coin < target:# and not new_current_length + 1 >= shortest_length:
                new_target = target - coin
                print("coins passed on: " + str(new_coins))
                shortest_length = recursion(new_coins, new_target, new_current_length, shortest_length, change)

        new_coins.remove(coin)
    print("change: " + str(change))
    return shortest_length
