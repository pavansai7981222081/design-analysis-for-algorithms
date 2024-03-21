def get_largest_element(arr):
    if not arr:
        return None  

    max_element = arr[0]  
    for num in arr:
        if num > max_element:
            max_element = num  

    return max_element

def main():
    
    arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))


    largest_element = get_largest_element(arr)

    if largest_element is not None:
        print("The largest element in the array is:", largest_element)
    else:
        print("The array is empty.")

if __name__ == "__main__":
    main()
