import os
import glob
import shutil as sh


class file_processing():
    def __init__(self, **kwargs):
        self.path = kwargs['path']
        self.name = kwargs['name']

    # 대상 파일 리스트 뽑기
    def find_file_path(self, **kwargs):
        # \BOJ\bfs\01697-숨바꼭질\01697-숨바꼭질-yeonhee.py
        files = [f for f in glob.glob(path + '/**/**/**/*') if self.name in f]
        self.files = files

    # 복사 대상 파일
    def file_copy(self, copy_path, cover=False):

        print('파일 복사를 시작합니다.')
        is_copied = False

        for file in self.files:
            sub_path = file.split('\\')[4:]
            platform = sub_path[0]
            file_name = sub_path[-1]
            copied_path = copy_path + '\\' + platform + '\\' + file_name

            # 기존에 파일이 있을 경우 덮어씌웁니다.
            if cover:
                sh.copy2(file, copy_path + '\\' + platform)
                is_copied = True

                print(copied_path)

            # 없는 파일만 복사합니다.
            else:
                if not os.path.exists(copied_path):
                    # 메타데이터까지 복사
                    sh.copy2(file, copy_path + '\\' + platform)
                    is_copied = True

                    print(copied_path)


        print('=' * 80)
        print('완료되었습니다.' if is_copied else '복사할 파일이 없습니다.')


if __name__ == '__main__':
    # 경로 입력
    path = 'C:\\Users\\User\\algorighm-study'
    copy_path = 'C:\\Users\\User\\devpla-algorithm'

    # 파일 복사 조건
    name = 'yeonhee'

    f = file_processing(path=path, name=name)
    f.find_file_path()
    f.file_copy(copy_path)

"""
주의 : 복사 대상 폴더에 BOJ, SWEA 등 플랫폼 디렉토리를 미리 생성
생성하지 않을 경우 이상하게 복사됩니다.

copy_path
├──BOJ
└──SWEA

"""
