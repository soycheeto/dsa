import re
import urllib.request
def extract_links(html_content):
    pattern = r'href="(http[s]?://.*?)"'
    links = re.findall(pattern, html_content)
    return links
def bfs_web_crawl(start_url):
    visited = set()
    queue = [start_url]

    while queue:
        current_url = queue.pop(0)
        
        if current_url not in visited:
            print("Crawling:", current_url)
            visited.add(current_url)

            try:
                response = urllib.request.urlopen(current_url)
                page_content = response.read().decode('utf-8')
                links = extract_links(page_content)
                for link in links:
                    if link not in visited:
                        queue.append(link)
            except Exception as e:
                print(f"Failed to crawl {current_url}: {e}")
bfs_web_crawl("http://example.com")

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True
def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num 

                        if solve_sudoku(board): 
                            return True
                        
                        board[row][col] = 0 

                return False
    return True
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
if solve_sudoku(sudoku_board):
    for row in sudoku_board:
        print(row)
else:
    print("No solution exists")
