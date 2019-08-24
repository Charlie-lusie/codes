//在n个点（坐标不同）中选取m个点是一个方案。每个方案Si有m-1相邻点距离，假设最小值记为d_i，求所有方案的最小值d_i的最大值
#include<stdio.h>
#include<algorithm>
using namespace std;
const int INF = 0x3f3f3f3f;
int n, m, a[100005];

bool judge(int x)
{
    int last = 0;//记录起点
    for(int i = 1; i < m; i++)   //判断是否能在m-1步以内到达最后一个位置  即能否找出包括起点在内的m个点
    {
        int now = last + 1;
        while(now < n && a[now] - a[last] < x)
            now++;
        if(now == n)  //若能到达则表示此时假设的间距x太大，应缩小x，即更新右端点
            return false;
        last = now;
    }
    return true;  //反之则是在m-1次以内不能更新到最后一个点，代表间距过小，更新左端点
}

int main()
{
    scanf("%d %d", &n, &m);
    for(int i = 0; i < n; i++)
        scanf("%d", &a[i]);
    sort(a,a + n);  //从小到大将位置排序
    int l = 0,r = INF;
    while(l < r)
    {
        int mid = (l + r + 1) >> 1;
        if(judge(mid))
            l = mid;
        else
            r = mid - 1;
    }
    printf("%d", l);
    return 0;
}