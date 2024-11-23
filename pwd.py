import os

def pwd():
    """打印当前工作目录"""
    print("当前目录：", os.getcwd())

def ls():
    """列出当前目录的内容"""
    print("目录内容：")
    for item in os.listdir():
        print(item)

def cd(directory):
    """更改当前目录"""
    try:
        os.chdir(directory)
        print("目录切换成功。")
    except OSError as e:
        print("目录切换失败：", e)

def rename_file(old_name, new_name):
    """重命名单个文件"""
    try:
        os.rename(old_name, new_name)
        print(f"文件 {old_name} 已重命名为 {new_name}。")
    except Exception as e:
        print(f"重命名失败：{e}")

def batch_rename():
    """批量重命名文件"""
    print("当前目录：", os.getcwd())
    file_types = input("请输入需要重命名的文件后缀（默认为jpg）：") or "jpg"
    prefix = input("请输入新的文件名前缀（默认为furina）：") or "furina"

    files = [f for f in os.listdir() if f.endswith(file_types)]
    if not files:
        print("没有找到指定后缀的文件。")
        return

    print("找到以下文件：")
    for index, file in enumerate(files):
        print(f"{index + 1}. {file}")

    count = 1
    for file in files:
        new_name = f"{prefix}-{count}{os.path.splitext(file)[1]}"
        while os.path.exists(new_name):  # 如果文件已存在，增加编号直到找到未使用的文件名
            count += 1
            new_name = f"{prefix}-{count}{os.path.splitext(file)[1]}"
        rename_file(file, new_name)
        print(f"文件 {file} 已重命名为 {new_name}。")
        count += 1
    print("批量重命名完成。")

def main():
    while True:
        print("请输入命令：")
        command = input("> ")

        parts = command.split()
        if not parts:
            continue
        elif parts[0] == 'pwd':
            pwd()
        elif parts[0] == 'ls':
            ls()
        elif parts[0] == 'cd' and len(parts) > 1:
            cd(parts[1])
        elif parts[0] == 'rename' and len(parts) == 3:
            rename_file(parts[1], parts[2])
        elif parts[0] == 'batch_rename':
            batch_rename()
        elif parts[0] == 'exit':
            print("谢谢使用，再见！")
            break
        else:
            print("未知命令，请重新输入。")
        print("操作完成。")

if __name__ == '__main__':
    main()