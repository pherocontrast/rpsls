#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
���ڣ�2019.11.24
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
	"""
	����Ϸ�����Ӧ����ͬ������
	"""
	if name=="ʯͷ":
		pnum=0
	elif name=="ʷ����":
		pnum=1
	elif name=="��":
		pnum=2
	elif name=="����":
		pnum=3
	elif name=="����":
		pnum=4
	else:
		pnum="Error: No Correct Name"
	return pnum
    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��


    #��дִ�д���,������ɺ�passɾ��


def number_to_name(number):
	"""
	������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
	"""
	
	if number==0:
		cnam="ʯͷ"
	elif number==1:
		cnam="ʷ����"
	elif number==2:
		cnam="��"
	elif number==3:
		cnam="����"
	elif number==4:
		cnam="����"
	return cnam
    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��

     #��дִ�д���,������ɺ�passɾ��


def rpsls(player_choice):
	"""
	�û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
	"""
	a=random.randint(0,4)
	b=name_to_number(player_choice)
	print("--------")
	print("����ѡ��Ϊ��%s"%player_choice)
	print("�������ѡ��Ϊ��%s"%number_to_name(a))
	if a==0:
		if b==1 or b==2:
			print("��Ӯ��")
		elif b==3 or b==4:
			print("�����Ӯ��")
		else:
			print("���ͼ��������һ����")
	elif a==1:
		if b==3 or b==2:
			print("��Ӯ��")
		elif b==0 or b==4:
			print("�����Ӯ��")
		else:
			print("���ͼ��������һ����")
	elif a==2:
		if b==3 or b==4:
			print("��Ӯ��")
		elif b==0 or b==1:
			print("�����Ӯ��")
		else:
			print("���ͼ��������һ����")
	elif a==3:
		if b==0 or b==4:
			print("��Ӯ��")
		elif b==1 or b==2:
			print("�����Ӯ��")
		else:
			print("���ͼ��������һ����")
	elif a==4:
		if b==0 or b==1:
			print("��Ӯ��")
		elif b==2 or b==3:
			print("�����Ӯ��")
		else:
			print("���ͼ��������һ����")
    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

     #����������ʾ��дִ�д��룬������ɺ�ɾ����pass


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)


