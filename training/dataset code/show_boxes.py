from dataset import dataset

path='C:/Users/Ari/Documents/scripts/xprize/database files'

test=dataset(f'C:/Users/Ari/Documents/scripts/bugfinder/inat2017/data/images/all',f'{path}/annotations/inat2017.json',f'{path}/image_splits')

test.test_set(5)
test.show_boxes()
