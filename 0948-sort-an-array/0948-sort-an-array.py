class Solution:

    
    def sortArray(self, nums: List[int]) -> List[int]:

        
        def merge(arr, L, M, R): # capitals to be more clear

            # get left and right halfs of the array
            left, right = arr[L:M+1], arr[M+1:R+1]

            # i for the main array and j, k for the two sub-arrays
            i, j, k = L, 0, 0

            while j<len(left) and k< len(right): # while loop as long as they are in bounds
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1

                # incrementing the i pointer regardless of which condition executes
                i += 1

            while j<len(left):
                arr[i] = left[j]
                j+=1
                i+=1
            while k<len(right):
                arr[i] = right[k]
                k+=1
                i+=1
        



        def mergeSort(arr, l, r):
            if l==r:
                return arr

            # find middle
            m = (l+r) // 2

            # run mergeSort on left and right halfa
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)


            # helper function
            merge(arr, l, m, r)

            #at this point it will be sorted, so return it
            return arr

        return mergeSort(nums, 0, len(nums)-1)


        