#include <cstdlib>
#include <iostream>
#include <ctime>
#include <vector>

// int random_access(int *num, int size)
// {
// int random_index = rand() % size;//随机数对数组长度取余，得到数组长度的随机数
// int random_number = num[random_index];
// return random_number;
// }

// int main()
// {
//     std::srand(std::time(0)); // 用当前时间作为随机数种子（rand函数在使用前需要指定随机数种子，通常用当前时间）
//     int test[] = {1, 2, 3, 4, 5};
//     std::cout << random_access(test, 5) << std::endl;
// }

// int main()
// {
//     std::vector<int> test = {1, 2, 3, 4, 5};
//     test.insert(test.begin()+4, 6);
//     for(int i=0;i<6;i++)
//     {
//         std::cout<<test[i]<<" ";
//     }
// }


// /* 删除索引 index 处的元素 */
// void remove(int *nums, int size, int index) {
//     // 把索引 index 之后的所有元素向前移动一位
//     for(int i = index;i < size-1;i++)
//     {
//         nums[i] = nums[i+1];
//     }

// }

// int main()
// {
//     std::vector<int> test = {1,2,3,4,5,6,7};
//     int size = test.size();
//     remove(test.data(),size,4);
//     size--; 
//     for(int i = 0;i<=size-1;i++)
//     {
//         std::cout<<test[i]<<" ";
//     }
// }


void find(const std::vector<int>& nums,int target,int size)
{
    for(int i = 0;i <= size-1;i++ )
    {
        if(nums[i] == target)
        {
            std::cout<<i;
        }
    }
}

int main()
{
    std::vector<int> test = {1,2,3,4,5,6,7,8,9};
    find(test,9,9);
}