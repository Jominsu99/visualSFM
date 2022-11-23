text_file_path = './Data_path.nvm'


with open(text_file_path,'r') as f:
    
    lines = f.readlines()
    num = int(lines[2])         # 3번째 줄을 읽어드린다.
    
with open("text.txt", 'w') as f:    
    i = 0
    for line in lines:
        i = i + 1
        if i > 3 and i < num + 4:
            result = ""
            c = line.split()
    
            t = c[0].rfind('\\')    # 몇번째 이미지인지까지만 가져온다.
            x = [c[0][t:], c[6], c[7], c[8], c[2], c[3], c[4], c[5]]
            
            for j in x:
                result += j + " "
            result += "\n"
            result1 = result.replace('\\','/') # 모든 \문자를 /로 바꿔준다 (리눅스에서 쓰기 위함)
            f.write(result1) 
       
            
        
    
    
    
    
    

        
