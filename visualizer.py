import matplotlib.pyplot as plt
import matplotlib.animation as animation
from safewalk import Solution

def visualize(grid, current, visited):
    fig, ax = plt.subplots()
    ax.clear()
    ax.imshow(grid, cmap='Greys', interpolation='none')
    
    for (r, c) in visited:
        ax.text(c, r, 'X', ha='center', va='center', color='red')
    
    ax.text(current[1], current[0], 'O', ha='center', va='center', color='blue')
    plt.pause(0.1)

def main():
    grid = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    health = 10
    solution = Solution()
    result = solution.findSafeWalk(grid, health, visualize)
    print("Path found:", result)
    plt.show()

if __name__ == "__main__":
    main()