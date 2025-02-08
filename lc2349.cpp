#include <unordered_map>
#include <set>   

using namespace std;

class NumberContainers {
private:
    unordered_map<int,set<int>> numbers;
    unordered_map<int,int> container;

public:

    // LC2349 - Number Containers
    NumberContainers() {    
    }
    
    void change(int index, int number) {
        if (container[index] != 0) {
            int old_number = container[index];
            numbers[old_number].erase(index);
        }

        container[index] = number;
        numbers[number].insert(index);
    }
    
    int find(int number) {
        
        if (numbers[number].empty())
            return -1;
        else {
            return *numbers[number].begin();
        }
    }
};

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers* obj = new NumberContainers();
 * obj->change(index,number);
 * int param_2 = obj->find(number);
 */