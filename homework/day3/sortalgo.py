def customsort(list_tobe_sorted):
    sorted_list = []
    list_len = len(list_tobe_sorted)

    for garbage in range(list_len):
        minimum_temp = list_tobe_sorted[0]
        for index in range(len(list_tobe_sorted)):
            if list_tobe_sorted[index] < minimum_temp:
                minimum_temp = list_tobe_sorted[index]
        sorted_list.append(minimum_temp)
        list_tobe_sorted.remove(minimum_temp)
    
    return sorted_list

if __name__ == "__main__":
    ip_list = list(map(int, input().split(" ")))
    print ("Original list=>\t", ip_list)
    ip_list = customsort(ip_list)

    print ("Sorted list=>\t", ip_list)