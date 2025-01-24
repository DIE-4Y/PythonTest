# coding=gbk
import cv2
import Character
from tqdm import tqdm
import Dict

# ���ݻҶȱȽ�����ͼƬ��hash����


def dHash(img1, img2, no):
    # noֵΪ���ͣ�0�������ͱȽϣ�Ҳ���������½ṹ�������ֺ�ȫ��Χ�ṹ����1�������ҽṹ��2�������½ṹ��3���������ҽṹ
    img1 = cv2.resize(img1, (12, 12), interpolation=cv2.INTER_CUBIC)
    img2 = cv2.resize(img2, (12, 12), interpolation=cv2.INTER_CUBIC)
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    similarity = 0
    similarity_1 = 0
    similarity_2 = 0
    if no == 0:  # ��Զ����֡������¡��������Լ����߽ṹ��ͬ�����
        for i in range(12):
            for j in range(12):
                if gray1[i, j] == gray2[i, j]:
                    similarity += 1
        return similarity/144

    elif no == 1:
        # ���ҽṹ�����Ҳ���׼����(�Ҳ�����ռ�����0.75����0.5����ʱ����0.75����)
        for i in range(0, 12):
            for j in range(3, 12):
                if gray1[i, j] == gray2[i, j]:
                    similarity += 1
                else:
                    pass
        return similarity / 108

    elif no == 2:
        # ���½ṹ�����ϲ����²���׼����
        for i in range(0, 9):
            for j in range(0, 12):
                if gray1[i, j] == gray2[i, j]:
                    similarity_1 += 1
        for i in range(3, 12):
            for j in range(12):
                if gray1[i, j] == gray2[i, j]:
                    similarity_2 += 1
        return max(similarity_1, similarity_2) / 108


def main():

    # ����ִ���ļ���ղ���
    word_pic_path = 'D:/py/chinese/'
    file1 = open('D:/py/Shape_CV2.txt', 'w')
    file1.truncate()
    file1.close()

    # �ļ��ж�д��
    for index1, word1 in tqdm(enumerate(Character.Symbol_lst())):
        # ÿ��ִ��һ���ļ��򿪹رղ���
        file1 = open('D:/py/Shape_CV2.txt', 'a')
        word_pic1 = cv2.imread(word_pic_path + str(index1) + '.png')
        # д��ͷ����
        file1.write(word1 + ' ')
        for index2, word2 in enumerate(Character.Symbol_lst()):
            word_pic2 = cv2.imread(word_pic_path + str(index2) + '.png')
            if index1 == index2:
                continue
            else:
                # cv2.imshow('image1',word_pic1)
                # cv2.waitKey(0)
                # cv2.imshow('image2',word_pic2)
                # cv2.waitKey(0)

                # �������ڽṹ�ֵ��д�����ֵ��ͬ������ֲ��жϷ�֧
                if word1 in Dict.structure_dict and word2 in Dict.structure_dict and Dict.structure_dict[word1] == \
                        Dict.structure_dict[word2]:
                    # �ֵ�ֵ����0Ϊ�����֣�1Ϊ���ҽṹ��2Ϊ���½ṹ��3Ϊ�����ҽṹ��4Ϊ�����½ṹ��5Ϊ���ϰ�Χ�ṹ��6Ϊ���ϰ�Χ��7Ϊ���°�Χ
                    if Dict.structure_dict[word1] in ['1', '2']:
                        similar_index = dHash(word_pic1, word_pic2, int(Dict.structure_dict[word1]))
                    else:
                        similar_index = dHash(word_pic1, word_pic2, 0)
                # ����һ�ֲ����ֵ��У����뷺���ͱȽ�
                else:
                    similar_index = dHash(word_pic1, word_pic2, 0)

                if similar_index >= 0.8:
                    file1.write(word2)

        file1.write('\n')
        file1.close()


if __name__ == '__main__':
    main()
