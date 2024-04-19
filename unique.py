def combinationSum2(candidates, target):
            
        candidates.sort()
        
        def backtrack(start, target, path, result):
            
            if target == 0:
                
                    result.append(path[:])
                    return 
            
            for i in range(start, len(candidates)):
                
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                
                path.append(candidates[i])
                
                
                backtrack(i+1, target-candidates[i], path, result)
            
                path.pop()
                
        
        
        result = []
        backtrack(0, target, [], result)
        
        return result
