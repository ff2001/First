#coding:gbk
"""
����Ŀ�꣺ͨ���Զ��庯����ʵ��RPSLS��Ϸ
�������ߣ�ֲ��4�෽��
"""
import random#����randomģ��
def name_to_number(name):#���庯��������Ϸ�����Ӧ����ͬ������
	if name=="ʯͷ":
		return 0
	if name=="ʷ����":#ʹ��if��佫��ͬ�����Ӧ����ͬ����
		return 1
	if name=="ֽ":
		return 2#���ؽ��
	if name=="����":
		return 3
	if name=="����":
		return 4
	else: print("Error: No Correct Name")#��������󲻷�������ѡ��򱨴�
def number_to_name(num):#���庯���� ������ (0, 1, 2, 3, 4)��Ӧ����Ϸ�Ĳ�ͬ����
	if num==0:
		return "ʯͷ"
	if num==1:#ʹ��if��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
		return "ʷ����"#���ؽ��
	if num==2:
		return "ֽ"
	if num==3:
		return "����"
	if num==4:
		return "����"
def rpsls(player_choice):#���庯�����û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
	print("----------------")
	player_choice_number=name_to_number(player_choice)# ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number
	comp_number=random.randrange(0,5)# ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number
	c_choice=number_to_name(comp_number)# ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
	print("����ѡ��Ϊ%s"%choice_name)
	print("�������ѡ��Ϊ%s"%c_choice)	#ͨ��ռλ��������
	if player_choice_number==0 and comp_number==4:
		print("��Ӯ�ˣ�")
	if player_choice_number==4 and comp_number==2:
		print("��Ӯ�ˣ�")
	if player_choice_number==0 and comp_number==3:
		print("��Ӯ�ˣ�")
	if player_choice_number==3 and comp_number==1:
		print("��Ӯ�ˣ�")
	if player_choice_number==2 and comp_number==0:
		print("��Ӯ�ˣ�")
	if player_choice_number==4 and comp_number==0:
		print("�����Ӯ��!")
	if player_choice_number==2 and comp_number==4:
		print("�����Ӯ��!")
	if player_choice_number==3 and comp_number==0:
		print("�����Ӯ��!")
	if player_choice_number==1 and comp_number==3:
		print("�����Ӯ��!")
	if player_choice_number==0 and comp_number==2:
		print("�����Ӯ��!")
	elif player_choice_number==comp_number:#����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�
		print("���ͼ��������һ����")
# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)
