print("Chương trình kiểm tra Binary Min-Heap dùng vòng lặp !")

array = [1, 5, 3, 7, 9, 8]
length = len(array)
min_heap = True
for i in range(length):
    left = i * 2 + 1
    right = left + 1
    left_ok = False
    right_ok = False
    if left > length - 1 or array[i] < array[left]:
        left_ok = True
    else:
        min_heap = False
        break
    if right > length - 1 or array[i] < array[right]:
        right_ok = True
    else:
        min_heap = False
        break
    # if left_ok and right_ok:
    #     print('%d is OK' % array[i])
    # else:
    #     print('%d is NOT OK' % array[i])

if min_heap:
    print('array is a binary min-heap')
else:
    print('array is NOT a binary min-heap')
