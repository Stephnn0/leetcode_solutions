# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]

def combinationSum2(candidates, target):
            
        candidates.sort()
        
        def backtrack(start, target, path, result):
            
            if target == 0:
                
                    result.append(path[:]) #appends new copy of path
                    return 
            
            for i in range(start, len(candidates)):
                
                #skip duplicates
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                #skip bigger nums than target
                if candidates[i] > target:
                    break
                
                #append current num
                path.append(candidates[i])
                
                
                backtrack(i+1, target-candidates[i], path, result)
            
                path.pop()
                
        
        
        result = []
        backtrack(0, target, [], result)
        
        return result


candidates = [10,1,2,7,6,1,5]
target = 8

print(combinationSum2(candidates, target))
