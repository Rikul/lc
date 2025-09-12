class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        
        fixed_path = []
        for i,x in enumerate(paths):
            if x == '..':
                if len(fixed_path):
                    fixed_path.pop()
                continue
            elif x == '.' or x == '':
                continue

            fixed_path.append(x)

        return "/" + "/".join(fixed_path)   
        