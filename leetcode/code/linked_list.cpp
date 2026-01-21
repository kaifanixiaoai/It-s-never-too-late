//链表结构
struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x):val(x),next(nullptr) {}
};

//访问节点
ListNode *access(ListNode *head,int index)
{
    for(int i=0;i<=index;i++)
    {
        if(head->next==nullptr)
        {
            return nullptr;
        }
        head = head->next;
    }
    return head;
}


//查找节点
int find(ListNode *head, int target) {
    int index = 0;
    while (head != nullptr) {
        if (head->val == target)
            return index;
        head = head->next;
        index++;
    }
    return -1;
}
