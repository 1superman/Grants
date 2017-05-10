from method import merge, cross_validation
from feature_extraction import *

card_train_path = '../../data/card_train.txt'
card_test_path = '../../data/card_test.txt' 
borrow_train_path = '../../data/borrow_train.txt'
borrow_test_path = '../../data/borrow_test.txt'
dorm_train_path = '../../data/dorm_train.txt'
dorm_test_path = '../../data/dorm_test.txt'
library_train_path = '../../data/library_train.txt'
library_test_path = '../../data/library_test.txt'
score_train_path = '../../data/score_train.txt'
score_test_path = '../../data/score_test.txt'
subsidy_train_path = '../../data/subsidy_train.txt'
subsidy_test_path = '../../data/studentID_test.txt'

card_train = card.card(card_train_path, '../../now/card_train.csv')
card_test = card.card(card_test_path, '../../now/card_test.csv')
borrow_train = borrow.borrow(borrow_train_path, '../../now/borrow_train.csv')
borrow_test = borrow.borrow(borrow_test_path, '../../now/borrow_test.csv')
dorm_train = dorm.dorm(dorm_train_path, '../../now/dorm_train.csv')
dorm_test = dorm.dorm(dorm_test_path, '../../now/dorm_test.csv')
library_train = library.library(library_train_path, '../../now/library_train.csv')
library_test = library.library(library_test_path, '../../now/library_test.csv')
score_train = score.score(score_train_path, '../../now/score_train.csv')
score_testn = score.score(score_test_path, '../../now/score_test.csv')
subsidy_train = subsidy.subsidy(subsidy_train_path, '../../now/student_train.csv')
subsidy_test = subsidy.subsidy(subsidy_test_path, '../../now/student_test.csv')

final_train = merge.rate('train')
final_test = merge.rate('test')
score = cross_validation.get_score(final_train)
