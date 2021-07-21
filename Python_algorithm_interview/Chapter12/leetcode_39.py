def combinationSum(candidates, target):

    result = []

    def dfs(num_sum,idx,path):

        if num_sum > target:
            return

        if num_sum == target:
            result.append(path)

        for i in range(idx, len(candidates)):
            dfs(num_sum+candidates[i], i, path+[candidates[i]])

    dfs(0,0,[])

    return result