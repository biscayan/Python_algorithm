def DFS(v,mode):

    if v>7:
        return

    #전위순회
    if mode == 'preorder':

        print(v,end=' ') 

        ###왼쪽자식
        DFS(v*2,mode='preorder')

        ###오른쪽자식
        DFS(v*2+1,mode='preorder')
    
    #중위순회
    elif mode == 'inorder':

        ###왼쪽자식
        DFS(v*2,mode='inorder')

        print(v,end=' ')

        ###오른쪽자식
        DFS(v*2+1,mode='inorder')

    #후위순회
    elif mode == 'postorder':

        ###왼쪽자식
        DFS(v*2,mode='postorder')

        ###오른쪽자식
        DFS(v*2+1,mode='postorder')

        print(v,end=' ')

if __name__=='__main__':
    DFS(1,mode='preorder')
    print()
    DFS(1,mode='inorder')
    print()
    DFS(1,mode='postorder')