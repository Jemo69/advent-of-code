def main():
    list = []
    with open("./test.txt") as f:
        new_file = f.readlines()
        for element in new_file:
            list.append(element.strip("\n"))
    starting_point = 50
    minimum = 0
    maximum = 99
    zero_list = []
    list2 = []
    for some in list:
        if some[0] == "L":
            starting_point -= int(some[1:])
            something = starting_point
            print(something)
            if starting_point < minimum:
                quotient, starting_point = divmod(starting_point, 100)
                print(f" left max {quotient},{starting_point}")
                if quotient == 0:
                    zero_list.append(quotient)
            if starting_point == 0:
                zero_list.append(starting_point)

            if starting_point > maximum:
                quotient, starting_point = divmod(starting_point, 100)
                print(f" left mini {quotient} , {starting_point}")
            if starting_point == 0:
                zero_list.append(starting_point)

            list2.append(starting_point)

        elif some[0] == "R":
            starting_point += int(some[1:])
            if starting_point < minimum:
                quotient, starting_point = divmod(starting_point, 100)
                print(f" the  right mini {quotient} , {starting_point}")
                if quotient == 0:
                    zero_list.append(quotient)
            if starting_point == 0:
                zero_list.append(starting_point)

            if starting_point > maximum:
                quotient, starting_point = divmod(starting_point, 100)
                print(f" right max {quotient} , {starting_point}")
            if starting_point == 0:
                zero_list.append(starting_point)
            list2.append(starting_point)

    max_var_count = 0
    dict = {}
    for other in list2:
        list3 = []
        var_counter = 0
        for j in list2:
            if other == j:
                var_counter += 1
                if var_counter >= max_var_count:
                    max_var_count = var_counter
        dict[other] = var_counter
        print(dict.get(0))

        if var_counter == 3:
            list3.append(other)
        print(f"zero : {len(zero_list)}")
        print(zero_list)
        print(list2)


if __name__ == "__main__":
    main()
