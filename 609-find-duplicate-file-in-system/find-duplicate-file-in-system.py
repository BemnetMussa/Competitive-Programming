class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        # ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
        #  

        path_dict = dict(list())

        for path in paths:
            path_file = path.split(" ")
            # ["root/a", "1.txt(abcd)", "2.txt(efgh)"]
       

            for i in range(1, len(path_file)):
         
                file_list = path_file[i].split('(')
              
                # [1.txt, abcd)]
                file_list[1] = file_list[1][:-1]
                file_key = file_list[1]

                file_value = path_file[0] + "/" + file_list[0]

                if file_key in path_dict:
                    path_dict[file_key].append(file_value)

                else:
                    path_dict[file_key] = [file_value]

        ans = [path for path in path_dict.values() if len(path) > 1]

        return ans
        


