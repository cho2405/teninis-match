import streamlit as st
import random

# 정적 파일 생성 활성화
st.set_option('deprecation.showfileUploaderEncoding', False)

def create_groups_from_mixed(mixed_group, num_groups):
    females = [member for member in mixed_group if member['성별'] == '여자']
    males = [member for member in mixed_group if member['성별'] == '남자']
    random.shuffle(females)
    random.shuffle(males)

    new_groups = []
    for _ in range(num_groups):
        new_group = {'여자': [], '남자': []}

        while len(new_group['여자']) < 2 and females:
            new_group['여자'].append(females.pop()['이름'])

        while len(new_group['남자']) < 2 and males:
            new_group['남자'].append(males.pop()['이름'])

        # 여자가 부족할 경우 남자로 채워줌
        while len(new_group['여자']) < 2 and males:
            new_group['여자'].append(males.pop()['이름'])

        # 남자가 부족할 경우 여자로 채워줌
        while len(new_group['남자']) < 2 and males:
            new_group['남자'].append(males.pop()['이름'])
            
        new_groups.append(new_group)
    new_group = {'여자': [], '남자': []}
    while males:
        new_group['남자'].append(males.pop()['이름'])
    while females:
        new_group['여자'].append(females.pop()['이름'])
    new_groups.append(new_group)
    return new_groups


def main():
    st.title('그룹 만들기')

    # 그룹 수 입력 받기
    num_groups = st.number_input('그룹 수를 입력하세요:', min_value=1, step=1)

    
    # 사용자로부터 섞인 그룹을 입력 받음
    mixed_group = [
        {'이름': '반건우', '성별': '남자'},
        {'이름': '조하나', '성별': '여자'},
        {'이름': '이기민', '성별': '남자'},
        {'이름': '김애경', '성별': '여자'},
        {'이름': '강태훈', '성별': '남자'},
        {'이름': '문소현', '성별': '여자'},
        {'이름': '김원석', '성별': '남자'},
        {'이름': '김미영', '성별': '여자'},
        {'이름': '김현욱', '성별': '남자'},
        {'이름': '박한영', '성별': '여자'},
        {'이름': '박종현', '성별': '남자'},
        {'이름': '김하은', '성별': '여자'},
        {'이름': '김하늘', '성별': '남자'},
        {'이름': '조연수', '성별': '여자'},
        {'이름': '이승훈', '성별': '남자'},
        {'이름': '정윤기', '성별': '남자'},
        {'이름': '홍우선', '성별': '남자'},
        # 추가적인 그룹 멤버들...
    ]
    if st.button('그룹 만들기'):
        for i in range(1, 6):  # 5번 반복
            st.header(f"그룹 만들기 - {i}")
            try:
                result = create_groups_from_mixed(mixed_group, num_groups)

                # Streamlit 테이블 생성
                st.table(result)
            except ValueError:
                st.error("올바른 숫자를 입력하세요.")
            
            
#    if st.button('그룹 만들기'):
#        try:
#            result = create_groups_from_mixed(mixed_group, num_groups)

#            # Streamlit 테이블 생성
#            st.table(result)
#        except ValueError:
#            st.error("올바른 숫자를 입력하세요.")

if __name__ == '__main__':
    main()
