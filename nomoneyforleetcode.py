import time
import traceback
import math

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time:.5f} seconds")
        return result
    return wrapper

class Solution:
    @timer
    def solve(self, *args):
        matrix = args[0]
        target = args[1]
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[mid][-1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                mid_l, mid_r = 0, len(matrix[mid]) - 1
                while mid_l <= mid_r:
                    m = (mid_l + mid_r) //2
                    if target > matrix[mid][m]:
                        mid_l  = m + 1
                    elif target < matrix[mid][m]:
                        mid_r = m - 1
                    else: 
                        return True 
                break
        return False
            





def test_cases():
    return [
        # Example: (inputs, expected_output)

        ([[[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13], False),  


    ]

@timer
def practice():
    solution = Solution()
    
    for i, (inputs, expected) in enumerate(test_cases(), 1):
        print(f"\nTest Case {i}:")
        print(f"Inputs: {inputs}")
        print(f"Expected Output: {expected}")
        
        try:
            result = solution.solve(*inputs)
            print(f"Your Output: {result}")
            
            if result == expected:
                print("Status: PASSED")
            else:
                print("Status: FAILED")
        except Exception as e:
            print("Status: ERROR")
            print("Exception:", str(e))
            print("Traceback:")
            print(traceback.format_exc())

if __name__ == "__main__":
    practice()


            # assigned_lockers = {}
        # free_lockers = []
        # last_assigned = 0
        # next_locker = 1

        # for client in clients:
        #     if client in assigned_lockers:
        #         # Free the locker if client already has one assigned
        #         freed_locker = assigned_lockers.pop(client)
        #         free_lockers.append(freed_locker)
        #     else:
        #         # Assign the next available locker
        #         if free_lockers:
        #             min_avail = min(free_lockers)
        #             # Use a previously freed locker if available
        #             locker_to_assign = free_lockers.pop(free_lockers.index(min_avail))
        #         else:
        #             # Otherwise, use the next new locker
        #             locker_to_assign = next_locker
        #             next_locker += 1
                
        #         assigned_lockers[client] = locker_to_assign
        #         last_assigned = locker_to_assign

        # return last_assigned
                