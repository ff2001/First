#coding:gbk
"""
程序目标：通过自定义函数，实现RPSLS游戏
程序作者：植产4班方芳
"""
import random#调用random模块
def name_to_number(name):#定义函数，将游戏对象对应到不同的整数
	if name=="石头":
		return 0
	if name=="史波克":#使用if语句将不同对象对应到不同整数
		return 1
	if name=="纸":
		return 2#返回结果
	if name=="蜥蜴":
		return 3
	if name=="剪刀":
		return 4
	else: print("Error: No Correct Name")#若输入对象不符合以上选项，则报错
def number_to_name(num):#定义函数， 将整数 (0, 1, 2, 3, 4)对应到游戏的不同对象
	if num==0:
		return "石头"
	if num==1:#使用if语句将不同的整数对应到游戏的不同对象
		return "史波克"#返回结果
	if num==2:
		return "纸"
	if num==3:
		return "蜥蜴"
	if num==4:
		return "剪刀"
def rpsls(player_choice):#定义函数，用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
	print("----------------")
	player_choice_number=name_to_number(player_choice)# 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number
	comp_number=random.randrange(0,5)# 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number
	c_choice=number_to_name(comp_number)# 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象
	print("您的选择为%s"%choice_name)
	print("计算机的选择为%s"%c_choice)	#通过占位符输出结果
	if player_choice_number==0 and comp_number==4:
		print("您赢了！")
	if player_choice_number==4 and comp_number==2:
		print("您赢了！")
	if player_choice_number==0 and comp_number==3:
		print("您赢了！")
	if player_choice_number==3 and comp_number==1:
		print("您赢了！")
	if player_choice_number==2 and comp_number==0:
		print("您赢了！")
	if player_choice_number==4 and comp_number==0:
		print("计算机赢了!")
	if player_choice_number==2 and comp_number==4:
		print("计算机赢了!")
	if player_choice_number==3 and comp_number==0:
		print("计算机赢了!")
	if player_choice_number==1 and comp_number==3:
		print("计算机赢了!")
	if player_choice_number==0 and comp_number==2:
		print("计算机赢了!")
	elif player_choice_number==comp_number:#如果用户和计算机选择一样，则显示“您和计算机出的一样呢”
		print("您和计算机出的一样呢")
# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)
