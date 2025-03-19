import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate_damage():
    try:
        # 입력값을 가져와 float 형식으로 변환
        attack = float(entry_attack.get())
        speed = float(entry_speed.get())
        crit_damage = float(entry_crit_dmg.get()) / 100  # %를 소수로 변환
        crit_rate = 1.0  # 치명타 확률을 100%로 고정
        
        # 선택된 캐릭터와 스킬 계수 가져오기
        character = character_var.get()
        basic_coeff, e_skill_coeff, q_skill_coeff = skill_coefficients.get(character, (0, 0, 0))

        if character == "웰트":
            # 웰트의 기본 공격, E스킬, Q스킬 계산
            basic_attack_damage = attack * basic_coeff 
            e_skill_damage = attack * e_skill_coeff
            q_skill_damage = attack * q_skill_coeff

            # 웰트의 E스킬은 기본 공격 데미지와 동일하지만, 추가 피해 2회 적용
            additional_e_skill_damage = 2 * (attack * e_skill_coeff)

            # 치명타 계산 (기본 공식: 기본 데미지 * (1 + 치명타 확률 * 치명타 피해))
            basic_attack_damage = basic_attack_damage * (1 + crit_rate * crit_damage)
            e_skill_damage = e_skill_damage * (1 + crit_rate * crit_damage)
            q_skill_damage = q_skill_damage * (1 + crit_rate * crit_damage)
            additional_e_skill_damage = additional_e_skill_damage * (1 + crit_rate * crit_damage)

            total_damage = f"기본 공격 데미지: {basic_attack_damage:.2f}\n" \
                           f"E 스킬 데미지: {additional_e_skill_damage:.2f}\n" \
                           f"Q 스킬 데미지: {q_skill_damage:.2f}"
            
        elif character == "아스타":
            # 아스타의 기본 공격, E스킬, Q스킬 계산
            basic_attack_damage = attack * basic_coeff
            e_skill_damage = attack * e_skill_coeff
            q_skill_damage = attack * q_skill_coeff

            # 아스타의 E스킬은 기본 공격 데미지와 동일하지만, 추가 피해 4회 적용
            additional_e_skill_damage = 4 * (attack * e_skill_coeff)

            # 치명타 계산 (기본 공식: 기본 데미지 * (1 + 치명타 확률 * 치명타 피해))
            basic_attack_damage = basic_attack_damage * (1 + crit_rate * crit_damage)
            e_skill_damage = e_skill_damage * (1 + crit_rate * crit_damage)
            q_skill_damage = q_skill_damage * (1 + crit_rate * crit_damage)
            additional_e_skill_damage = additional_e_skill_damage * (1 + crit_rate * crit_damage)

            total_damage = f"기본 공격 데미지: {basic_attack_damage:.2f}\n" \
                           f"E 스킬 데미지: {additional_e_skill_damage:.2f}\n" \
                           f"Q 스킬 데미지: {q_skill_damage:.2f}"
            
        elif character == "클라라":
            basic_damage = attack * basic_coeff
            e_skill_damage = attack * e_skill_coeff
            q_skill_damage = attack * q_skill_coeff

            basic_damage = basic_damage * (1 + crit_rate * crit_damage)
            e_skill_damage = e_skill_damage * (1 + crit_rate * crit_damage)
            q_skill_damage = q_skill_damage * (1 + crit_rate * crit_damage)

            total_damage = f"기본 공격 데미지: {basic_damage:.2f}\n" \
                           f"E 스킬 데미지: {e_skill_damage:.2f}\n" \
                           f"Q 스킬 데미지(반격데미지 피해증가 기준): {q_skill_damage:.2f}"
            
        elif character == "토파즈":
            basic_damage = attack * basic_coeff
            e_skill_damage = attack * e_skill_coeff
            q_skill_damage = attack * (q_skill_coeff + 0.27)

            basic_damage = basic_damage * (1 + crit_rate * crit_damage)
            e_skill_damage = e_skill_damage * (1 + crit_rate * crit_damage)
            q_skill_damage = q_skill_damage * (1 + crit_rate * crit_damage)

            total_damage = f"기본 공격 데미지: {basic_damage:.2f}\n" \
                           f"E 스킬 데미지: {e_skill_damage:.2f}\n" \
                           f"Q 스킬 데미지(추공 기준): {q_skill_damage:.2f}"
            
        elif character == "어벤츄린":
            basic_attack_damage = attack * basic_coeff
            e_skill_damage = attack * e_skill_coeff
            q_skill_damage = attack * q_skill_coeff
            
            additional_e_skill_damage = 7 * (attack * e_skill_coeff)

            basic_attack_damage = basic_attack_damage * (1 + crit_rate * crit_damage)
            e_skill_damage = e_skill_damage * (1 + crit_rate * crit_damage)
            q_skill_damage = q_skill_damage * (1 + crit_rate * crit_damage)
            additional_e_skill_damage = additional_e_skill_damage * (1 + crit_rate * crit_damage)

            total_damage = f"기본 공격 데미지: {basic_attack_damage:.2f}\n" \
                           f"추공 데미지: {additional_e_skill_damage:.2f}\n" \
                           f"Q 스킬 데미지: {q_skill_damage:.2f}"

        elif character == "미샤":
            basic_damage = attack * basic_coeff
            e_skill_damage = attack * e_skill_coeff
            q_skill_damage = attack * (0.64 + 9 * 0.32)

            basic_damage = basic_damage * (1 + crit_rate * crit_damage)
            e_skill_damage = e_skill_damage * (1 + crit_rate * crit_damage)
            q_skill_damage = q_skill_damage * (1 + crit_rate * crit_damage)

            total_damage = f"기본 공격 데미지: {basic_damage:.2f}\n" \
                           f"E 스킬 데미지: {e_skill_damage:.2f}\n" \
                           f"Q 스킬 데미지(10단기준): {q_skill_damage:.2f}"

        elif character == "연경":
            basic_damage = attack * basic_coeff
            e_skill_damage = attack * e_skill_coeff
            q_skill_damage = attack * q_skill_coeff

            basic_damage = basic_damage * (1 + crit_rate * crit_damage)
            e_skill_damage = e_skill_damage * (1 + crit_rate * crit_damage)
            q_skill_damage = q_skill_damage * (1 + crit_rate * (crit_damage+0.54))

            total_damage = f"기본 공격 데미지: {basic_damage:.2f}\n" \
                           f"E 스킬 데미지: {e_skill_damage:.2f}\n" \
                           f"Q 스킬 데미지(신검합일 기준): {q_skill_damage:.2f}"
        
        elif character == "청작":
            basic_damage = attack * basic_coeff
            e_skill_damage = attack * e_skill_coeff
            q_skill_damage = attack * q_skill_coeff

            basic_damage = basic_damage * (1 + crit_rate * crit_damage)
            e_skill_damage = (e_skill_damage*0.79) * (1 + crit_rate * crit_damage)
            q_skill_damage = q_skill_damage * (1 + crit_rate * (crit_damage))

            total_damage = f"기본 공격 데미지: {basic_damage:.2f}\n" \
                           f"E 스킬 데미지(꿀조합 기준): {e_skill_damage:.2f}\n" \
                           f"Q 스킬 데미지: {q_skill_damage:.2f}"

        elif character == "신경원":
            basic_damage = attack * basic_coeff
            e_skill_damage = attack * e_skill_coeff
            q_skill_damage = attack * q_skill_coeff
            p_damage = attack * 0.72

            basic_damage = basic_damage * (1 + crit_rate * crit_damage)
            e_skill_damage = e_skill_damage *  (1 + crit_rate * crit_damage)
            q_skill_damage = q_skill_damage * (1 + crit_rate * (crit_damage))
            p_skill_damage = (10*p_damage) * (1+crit_rate*crit_damage)

            total_damage = f"기본 공격 데미지: {basic_damage:.2f}\n" \
                           f"E 스킬 데미지: {e_skill_damage:.2f}\n" \
                           f"Q 스킬 데미지: {q_skill_damage:.2f}\n"\
                           f"신군 데미지: {p_skill_damage:.2f}"

        elif character == "단항·음월":
            basic_damage = attack * basic_coeff
            e_skill_damage = attack * e_skill_coeff
            q_skill_damage = attack * q_skill_coeff

            basic_damage = 7 * (basic_damage * (1 + crit_rate * (crit_damage * 0.132)))
            e_skill_damage = e_skill_damage * (1 + crit_rate * crit_damage)
            q_skill_damage = 3 *(q_skill_damage * (1 + crit_rate * (crit_damage)))

            total_damage = f"기본 공격 데미지(3단계 기준): {basic_damage:.2f}\n" \
                           f"E 스킬 데미지: {e_skill_damage:.2f}\n" \
                           f"Q 스킬 데미지: {q_skill_damage:.2f}"

        elif character == "경류":
            
            basic_damage = attack * basic_coeff
            e_skill_damage = (attack*1.98) * e_skill_coeff
            q_skill_damage = (attack*1.98) * q_skill_coeff

            basic_damage = basic_damage * (1 + crit_rate * crit_damage)
            e_skill_damage = e_skill_damage * (1 + crit_rate * crit_damage)
            q_skill_damage = q_skill_damage * (1 + crit_rate * crit_damage)

            total_damage = f"기본 공격 데미지: {basic_damage:.2f}\n" \
                           f"E 스킬 데미지(전백상태): {e_skill_damage:.2f}\n" \
                           f"Q 스킬 데미지(전백상태): {q_skill_damage:.2f}"

        elif character=="운리":
            #캐릭터의 기본 공격, E스킬, Q스킬 계산
            basic_damage = attack * basic_coeff
            e_skill_damage = attack * e_skill_coeff
            q_skill_damage = attack * q_skill_coeff

            # 치명타 계산 (기본 공식: 기본 데미지 * (1 + 치명타 확률 * 치명타 피해))
            basic_damage = basic_damage * (1 + crit_rate * crit_damage)
            e_skill_damage = e_skill_damage * (1 + crit_rate * crit_damage)
            q_skill_damage = q_skill_damage * (1 + crit_rate * (crit_damage*1.08))

            total_damage = f"기본 공격 데미지: {basic_damage:.2f}\n" \
                           f"E 스킬 데미지: {e_skill_damage:.2f}\n" \
                           f"Q 스킬 데미지: {q_skill_damage:.2f}"
        
        elif character=="비소":
            #캐릭터의 기본 공격, E스킬, Q스킬 계산
            basic_damage = attack * basic_coeff
            e_skill_damage = attack * e_skill_coeff
            q_skill_damage = attack * q_skill_coeff
            last_damage = attack * 1.73

            # 치명타 계산 (기본 공식: 기본 데미지 * (1 + 치명타 확률 * 치명타 피해))
            basic_damage = basic_damage * (1 + crit_rate * crit_damage)
            e_skill_damage = e_skill_damage * (1 + crit_rate * crit_damage)
            q_skill_damage = 6 * (q_skill_damage * (1 + crit_rate * crit_damage))
            last_skill_damage = last_damage * (1 + crit_rate * crit_damage)

            last_q_skill_damage = last_skill_damage + q_skill_damage

            total_damage = f"기본 공격 데미지: {basic_damage:.2f}\n" \
                           f"E 스킬 데미지: {e_skill_damage:.2f}\n" \
                           f"Q 스킬 데미지: {last_q_skill_damage:2f}"
        
        elif character == "아젠티":
            #캐릭터의 기본 공격, E스킬, Q스킬 계산
            basic_damage = attack * basic_coeff
            e_skill_damage = attack * e_skill_coeff
            q_skill_damage = attack * q_skill_coeff

            # 치명타 계산 (기본 공식: 기본 데미지 * (1 + 치명타 확률 * 치명타 피해))
            basic_damage = basic_damage * (1 + crit_rate * crit_damage)
            e_skill_damage = e_skill_damage * (1 + crit_rate * crit_damage)
            q_skill_damage = q_skill_damage * (1 + crit_rate * crit_damage) + (6 * (attack * 1.02))

            total_damage = f"기본 공격 데미지: {basic_damage:.2f}\n" \
                           f"E 스킬 데미지: {e_skill_damage:.2f}\n" \
                           f"Q 스킬 데미지: {q_skill_damage:.2f}"
        
        elif character == "아케론":
            # 캐릭터의 기본 공격, E스킬 계산
            basic_damage = attack * basic_coeff
            e_skill_damage = attack * e_skill_coeff


            basic_damage = basic_damage * (1 + crit_rate * crit_damage)
            e_skill_damage = e_skill_damage * (1 + crit_rate * crit_damage)
            # Q스킬 계산
            tears_slash_single_damage = attack * 6.126  # 눈물 베기 1회당 단일 피해 + 아즈사카 제거 피해 612.6%
            tears_slash_damage = tears_slash_single_damage * 3  # 눈물 베기 3회
            return_damage = attack * 5.32  # 황천의 귀환 피해 (단일 피해 + 황천의 귀환 532%)

            # 총 Q스킬 데미지 계산
            q_skill_damage = (tears_slash_damage + return_damage) * (1 + crit_rate * crit_damage)

            total_damage = f"기본 공격 데미지: {basic_damage:.2f}\n" \
                        f"E 스킬 데미지: {e_skill_damage:.2f}\n" \
                        f"Q 스킬 데미지: {q_skill_damage:.2f}"


        elif character == "라파":
            #캐릭터의 기본 공격, E스킬, Q스킬 계산
            basic_damage = attack * basic_coeff
            e_skill_damage = attack * e_skill_coeff
            q_skill_damage = attack * q_skill_coeff

            # 치명타 계산 (기본 공식: 기본 데미지 * (1 + 치명타 확률 * 치명타 피해))
            basic_damage = basic_damage * (1 + crit_rate * crit_damage)
            e_skill_damage = e_skill_damage * (1 + crit_rate * crit_damage)
            q_skill_damage = 3 * (q_skill_damage * (1 + crit_rate * crit_damage))

            total_damage = f"기본 공격 데미지: {basic_damage:.2f}\n" \
                           f"E 스킬 데미지: {e_skill_damage:.2f}\n" \
                           f"Q 스킬 사용후 기본 공격 총합 데미지: {q_skill_damage:.2f}"

        else:
            #캐릭터의 기본 공격, E스킬, Q스킬 계산
            basic_damage = attack * basic_coeff
            e_skill_damage = attack * e_skill_coeff
            q_skill_damage = attack * q_skill_coeff

            # 치명타 계산 (기본 공식: 기본 데미지 * (1 + 치명타 확률 * 치명타 피해))
            basic_damage = basic_damage * (1 + crit_rate * crit_damage)
            e_skill_damage = e_skill_damage * (1 + crit_rate * crit_damage)
            q_skill_damage = q_skill_damage * (1 + crit_rate * crit_damage)

            total_damage = f"기본 공격 데미지: {basic_damage:.2f}\n" \
                           f"E 스킬 데미지: {e_skill_damage:.2f}\n" \
                           f"Q 스킬 데미지: {q_skill_damage:.2f}"

        # 결과 표시
        result_label.config(text=f"총 데미지: {total_damage:.2f}" if isinstance(total_damage, float) else total_damage)

    except ValueError:
        result_label.config(text="숫자 값을 입력해 주세요.")

def show_instructions():
    instructions = (
        "붕괴 스타레일 데미지 계산기 사용 방법:\n\n"
        "1. 공격력, 속도, 치명타 피해(%), 치명타 확률(%)을 각각 입력합니다.\n"
        "   - 공격력: 캐릭터의 총 공격력 수치\n"
        "   - 속도: 캐릭터의 속도 수치\n"
        "   - 치명타 피해: 치명타 발생 시 추가 피해를 퍼센트로 입력합니다 (예: 50은 50%).\n"
        "   - 치명타 확률은 100%로 고정되어 있습니다.\n"
        "2. 캐릭터를 선택합니다. 각 캐릭터마다 기본 공격, E스킬, Q스킬의 계수가 다릅니다.\n"
        "3. '데미지 계산' 버튼을 눌러 각 스킬의 데미지를 확인합니다.\n\n"
        "각 스킬의 데미지는 입력된 수치와 선택된 캐릭터의 만렙 스킬의 계수를 바탕으로 계산됩니다.\n"
        "캐릭터의 특성 버프,격파 피해,타 캐릭의 버프등은 포함되지 않습니다.\n"
        "확산 공격은 단일 적 기준 데미지로 적용합니다.\n"
        "속성피해는 그냥 피해로 취급.\n"
        "변신 캐릭터&강화 스킬들은 변신&강화 기준의 스킬 계수로 계산합니다.\n"
        "*****모든 캐릭은 풀돌 기준입니당*****"
    )
    messagebox.showinfo("사용 방법", instructions)

# 스킬 계수 예시 (캐릭터별로 다르게 설정할 수 있음)
# 기본공격, E스킬, Q스킬의 % 계수
skill_coefficients = {
    #개척자
    "개척자(파멸)": (1.1, 1.37, 4.8),  
    "개척자(보존)": (1.20, 1.40, 2.20),  
    "개척자(화합)": (1.10, 1.30, 1.80),  
    #은하열차
    "Mar.7th": (1.1, 0, 1.62),
    "단항": (1.1, 2.86, 4.32),
    "히메코": (1.1, 2.2, 2.48),
    "웰트": (1.1, 0.79, 1.62),
    #스텔라론
    "은랑": (1.1, 2.15, 4.1),
    "카프카":(1.1,1.76,0.88),
    "반디":(2.2,2.2,0),
    #우주정거장
    "아를란":(1.1,2.64,3.45),
    "아스타":(1.1,0.55,0),
    "헤르타":(1.1,1.1,2.16),
    #벨로보그
    "게파드":(1.1,2.2,0),
    "클라라":(1.1,1.32,3.48),
    "서벌":(1.1,1.54,1.94),
    "페라":(1.1,2.31,1.08),
    "삼포":(1.1,0.61,1.72),
    "후크":(1.1,3.08,4.32),
    "제레":(1.1,2.42,4.59),
    "루카":(1.54,1.32,3.56),
    #스타피스 컴퍼니
    "토파즈":(1.1,3.3,3.3),
    "어벤츄린":(1.1,0.27,2.92),
    "제이드":(0.99,1.59,2.64),
    #페나코니
    "미샤":(1.1,2.2,0),
    "갤러거":(1.1,2.75,1.65),
    #선주 나부
    "연경":(1.1,2.42,3.78),
    "청작":(1.1,2.64,2.16),
    "소상":(1.1,2.31,3.45),
    "신경원":(1.1,1.1,2.16),
    "단항·음월":(5.5,0,3.24),
    "경류":(1.1,2.75,3.24),
    "계네빈":(1.1,1.32,1.296),
    "설의":(1.1,1.54,2.7),
    "운리":(1.1,1.32,2.37),
    "비소":(1.1,2.2,7.6),
    "맥택":(1.1,1.65,2.92),
    #은하
    "아젠티":(1.1,1.32,3.02),
    "Dr.레이시오":(1.3,1.87,2.88),
    "블랙스완":(0.66,0.99,1.27),
    "아케론":(1.1,1.76,4.02),
    "부트힐":(2.42,0,4.32),
    "라파":(1.1,1.32,1)
}

# 각 카테고리별 캐릭터 분류
categories = {
    "개척자": ["개척자(파멸)", "개척자(보존)", "개척자(화합)"],
    "은하열차": ["Mar.7th", "단항", "히메코"],
    "스텔라론": ["은랑","카프카","반디"],
    "우주정거장":["아를란","아스타","헤르타"],
    "벨로보그":["게파드","클라라","서벌","페라","삼포","후크","제레","루카"],
    "스타피스 컴퍼니":["토파즈","어벤츄린","제이드"],
    "페나코니":["미샤","갤러거"],
    "선주 나부":["연경","청작","소상","신경원","단항·음월","경류","계네빈","설의","운리","비소","맥택"],
    "은하":["아젠티","Dr.레이시오","블랙스완","아케론","부트힐","라파"]
}

# tkinter 기본 창 설정
root = tk.Tk()
root.title("붕괴 스타레일 데미지 계산기")
root.geometry("400x450")  # 창 크기 조정

# 메인 프레임 생성
main_frame = ttk.Frame(root, padding="10 10 10 10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# 입력란 설정 (공격력, 속도, 치명타 피해)
input_frame = ttk.Frame(main_frame, padding="5 5 5 5")
input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

tk.Label(input_frame, text="공격력:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
entry_attack = tk.Entry(input_frame, width=25)
entry_attack.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="속도:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
entry_speed = tk.Entry(input_frame, width=25)
entry_speed.grid(row=1, column=1, padx=5, pady=5)

tk.Label(input_frame, text="치명타 피해 (%):").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
entry_crit_dmg = tk.Entry(input_frame, width=25)
entry_crit_dmg.grid(row=2, column=1, padx=5, pady=5)

# 치명타 확률을 100%로 고정
tk.Label(input_frame, text="치명타 확률 (100%고정):").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
entry_crit_rate = tk.Entry(input_frame, width=25, state='disabled')
entry_crit_rate.insert(0, "100")  # 기본값 100%
entry_crit_rate.grid(row=3, column=1, padx=5, pady=5)

# 캐릭터 선택 라벨과 메뉴
character_selection_frame = ttk.Frame(main_frame, padding="5 5 5 5")
character_selection_frame.grid(row=4, column=0, sticky=(tk.W, tk.E))

# 캐릭터 선택 텍스트
character_label = tk.Label(character_selection_frame, text="캐릭터 선택:")
character_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

# 카테고리 선택
category_var = tk.StringVar(root)
category_var.set("개척자")  # 기본 카테고리 설정
category_menu = ttk.OptionMenu(character_selection_frame, category_var, "개척자", *categories.keys())
category_menu.grid(row=0, column=1, padx=5, pady=5)

# 캐릭터 선택
character_var = tk.StringVar(root)
character_var.set(categories["개척자"][0])  # 기본 캐릭터 설정
character_menu = ttk.OptionMenu(character_selection_frame, character_var, *categories["개척자"])
character_menu.grid(row=0, column=2, padx=5, pady=5)

# 카테고리 변경 시 캐릭터 메뉴 업데이트 함수
def update_character_menu(*args):
    # 카테고리 선택에 따라 캐릭터 목록 업데이트
    category = category_var.get()
    character_var.set(categories[category][0] if categories[category] else "")
    character_menu['menu'].delete(0, 'end')
    for character in categories[category]:
        character_menu['menu'].add_command(label=character, command=tk._setit(character_var, character))
    
    # 캐릭터를 재선택할 때 입력값을 초기화
    clear_inputs()

# 입력 필드를 초기화하는 함수
def clear_inputs(*args):
    entry_attack.delete(0, tk.END)
    entry_speed.delete(0, tk.END)
    entry_crit_dmg.delete(0, tk.END)
    entry_crit_rate.delete(0, tk.END)
    entry_crit_rate.insert(0, "100")  # 치명타 확률 초기값 100%
    result_label.config(text="결과: ")  # 결과 초기화
    entry_attack.focus_set()

# 캐릭터 선택 시 입력 필드를 초기화
character_var.trace_add("write", clear_inputs)



category_var.trace_add("write", update_character_menu)

# 버튼 생성 (데미지 계산 및 설명)
button_frame = ttk.Frame(main_frame, padding="5 5 5 5")
button_frame.grid(row=5, column=0, sticky=(tk.W, tk.E))

calculate_button = tk.Button(button_frame, text="데미지 계산", command=calculate_damage)
calculate_button.grid(row=0, column=0, padx=5, pady=10)

instruction_button = tk.Button(button_frame, text="설명", command=show_instructions)
instruction_button.grid(row=0, column=1, padx=5, pady=10)

# 결과를 표시할 라벨
result_frame = ttk.Frame(main_frame, padding="5 5 5 5")
result_frame.grid(row=6, column=0, sticky=(tk.W, tk.E))

result_label = tk.Label(result_frame, text="결과: ", anchor="w", justify="left")
result_label.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=5, pady=10)

err_label = tk.Label(result_frame, text="*데미지는 인게임과 차이가 있을 수 있습니다*", anchor="w", justify="left")
err_label.grid(row=1, column=0, sticky=(tk.W, tk.E), padx=5, pady=1)

bottom_text = tk.Label(root, text="세상의 모든 아름다운 것들을 위하여", font=("Arial", 8), fg="#e0e0e0")
bottom_text.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

# 창 실행
root.mainloop()





# import tkinter as tk
# from tkinter import ttk, messagebox


# # 데미지 계산 함수
# def calculate_damage():
#     try:
#         # 사용자 입력 값 읽기
#         attack = float(entry_attack.get())
#         speed = float(entry_speed.get())
#         crit_dmg = float(entry_crit_dmg.get())
#         crit_rate = 100  # 치명타 확률 고정

#         # 선택한 캐릭터의 스킬 계수 가져오기
#         character = character_var.get()
#         if character not in skill_coefficients:
#             result_label.config(text="결과: 캐릭터 정보 없음")
#             return

#         basic, skill_e, skill_q = skill_coefficients[character]

#         # 데미지 계산 (치명타 확률은 항상 100%)
#         basic_damage = attack * (1 + crit_dmg / 100) * basic
#         skill_e_damage = attack * (1 + crit_dmg / 100) * skill_e
#         skill_q_damage = attack * (1 + crit_dmg / 100) * skill_q

#         # 지속 피해와 격파 피해 계산
#         sustain_damage = 0
#         crush_damage = 0

#         if character in sustain_characters:
#             sustain_damage = (skill_e_damage + skill_q_damage) * sustain_time

#         if character in crush_characters:
#             crush_damage = (skill_e_damage + skill_q_damage) * crush_bonus

        

#         # 결과 표시
#         result_label.config(
#             text=(
#                 f"결과:\n"
#                 f"기본공격 데미지: {basic_damage:.2f}\n"
#                 f"E스킬 데미지: {skill_e_damage:.2f}\n"
#                 f"Q스킬 데미지: {skill_q_damage:.2f}\n"
#                 f"지속 피해: {sustain_damage:.2f}\n"
#                 f"격파 피해: {crush_damage:.2f}"
#             )
#         )
#     except ValueError:
#         messagebox.showerror("입력 오류", "공격력, 속도, 치명타 피해는 숫자만 입력해야 합니다.")


# # 사용법 설명 함수
# def show_instructions():
#     instructions = (
#         "붕괴 스타레일 데미지 계산기 사용 방법:\n\n"
#         "1. 공격력, 속도, 치명타 피해(%)를 각각 입력합니다.\n"
#         "2. 캐릭터를 선택한 후 '데미지 계산'을 클릭합니다.\n"
#         "3. 결과는 각 스킬의 데미지로 표시됩니다.\n\n"
#         "* 주의: 계산은 기본적인 계수를 기준으로 하며, 버프나 특성 효과는 포함되지 않습니다."
#     )
#     messagebox.showinfo("사용 방법", instructions)


# # 카테고리 선택에 따른 캐릭터 목록 업데이트
# def update_character_menu(*args):
#     category = category_var.get()
#     characters = categories.get(category, [])
#     character_menu['menu'].delete(0, 'end')
#     for char in characters:
#         character_menu['menu'].add_command(label=char, command=tk._setit(character_var, char))
#     if characters:
#         character_var.set(characters[0])


# # 초기화 함수
# def clear_inputs():
#     entry_attack.delete(0, tk.END)
#     entry_speed.delete(0, tk.END)
#     entry_crit_dmg.delete(0, tk.END)
#     result_label.config(text="결과: ")


# # 지속 피해를 주는 캐릭터 목록
# sustain_characters = ["카프카", "블랙스완", "삼포", "서벌"]
# # 격파 피해를 주는 캐릭터 목록
# crush_characters = ["부트힐", "라파", "반디"]

# # 지속 피해 시간 설정 (초 단위)
# sustain_time = 5  # 예시: 5초 동안 지속되는 피해

# # 격파 피해 계수 설정
# crush_bonus = 1.5  # 예시: 격파 피해 계수 1.5

# # 스킬 계수 데이터
# skill_coefficients = {
#     #개척자
#     "개척자(파멸)": (1.1, 1.37, 4.8),  
#     "개척자(보존)": (1.20, 1.40, 2.20),  
#     "개척자(화합)": (1.10, 1.30, 1.80),  
#     #은하열차
#     "Mar.7th": (1.1, 0, 1.62),
#     "단항": (1.1, 2.86, 4.32),
#     "히메코": (1.1, 2.2, 2.48),
#     "웰트": (1.1, 0.79, 1.62),
#     #스텔라론
#     "은랑": (1.1, 2.15, 4.1),
#     "카프카":(1.1,1.76,0.88),
#     "반디":(2.2,2.2,0),
#     #우주정거장
#     "아를란":(1.1,2.64,3.45),
#     "아스타":(1.1,0.55,0),
#     "헤르타":(1.1,1.1,2.16),
#     #벨로보그
#     "게파드":(1.1,2.2,0),
#     "클라라":(1.1,1.32,3.48),
#     "서벌":(1.1,1.54,1.94),
#     "페라":(1.1,2.31,1.08),
#     "삼포":(1.1,0.61,1.72),
#     "후크":(1.1,3.08,4.32),
#     "제레":(1.1,2.42,4.59),
#     "루카":(1.54,1.32,3.56),
#     #스타피스 컴퍼니
#     "토파즈":(1.1,3.3,3.3),
#     "어벤츄린":(1.1,0.27,2.92),
#     "제이드":(0.99,1.59,2.64),
#     #페나코니
#     "미샤":(1.1,2.2,0),
#     "갤러거":(1.1,2.75,1.65),
#     #선주 나부
#     "연경":(1.1,2.42,3.78),
#     "청작":(1.1,2.64,2.16),
#     "소상":(1.1,2.31,3.45),
#     "신경원":(1.1,1.1,2.16),
#     "단항·음월":(5.5,0,3.24),
#     "경류":(1.1,2.75,3.24),
#     "계네빈":(1.1,1.32,1.296),
#     "설의":(1.1,1.54,2.7),
#     "운리":(1.1,1.32,2.37),
#     "비소":(1.1,2.2,7.6),
#     "맥택":(1.1,1.65,2.92),
#     #은하
#     "아젠티":(1.1,1.32,3.02),
#     "Dr.레이시오":(1.3,1.87,2.88),
#     "블랙스완":(0.66,0.99,1.27),
#     "아케론":(1.1,1.76,4.02),
#     "부트힐":(2.42,0,4.32),
#     "라파":(1.1,1.32,1)
# }

# # 카테고리와 캐릭터 데이터
# categories = {
#     "개척자": ["개척자(파멸)", "개척자(보존)", "개척자(화합)"],
#     "은하열차": ["Mar.7th", "단항", "히메코"],
#     "스텔라론": ["은랑","카프카","반디"],
#     "우주정거장":["아를란","아스타","헤르타"],
#     "벨로보그":["게파드","클라라","서벌","페라","삼포","후크","제레","루카"],
#     "스타피스 컴퍼니":["토파즈","어벤츄린","제이드"],
#     "페나코니":["미샤","갤러거"],
#     "선주 나부":["연경","청작","소상","신경원","단항·음월","경류","계네빈","설의","운리","비소","맥택"],
#     "은하":["아젠티","Dr.레이시오","블랙스완","아케론","부트힐","라파"]
# }

# # tkinter 설정
# root = tk.Tk()
# root.title("붕괴 스타레일 데미지 계산기")
# root.geometry("400x500")

# # 메인 프레임
# main_frame = ttk.Frame(root, padding="10")
# main_frame.pack(fill="both", expand=True)

# # 입력 영역
# input_frame = ttk.LabelFrame(main_frame, text="입력값", padding="10")
# input_frame.pack(fill="x", padx=5, pady=5)

# tk.Label(input_frame, text="공격력:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
# entry_attack = tk.Entry(input_frame, width=20)
# entry_attack.grid(row=0, column=1, padx=5, pady=5)

# tk.Label(input_frame, text="속도:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
# entry_speed = tk.Entry(input_frame, width=20)
# entry_speed.grid(row=1, column=1, padx=5, pady=5)

# tk.Label(input_frame, text="치명타 피해 (%):").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
# entry_crit_dmg = tk.Entry(input_frame, width=20)
# entry_crit_dmg.grid(row=2, column=1, padx=5, pady=5)

# # 캐릭터 선택 영역
# selection_frame = ttk.LabelFrame(main_frame, text="캐릭터 선택", padding="10")
# selection_frame.pack(fill="x", padx=5, pady=5)

# tk.Label(selection_frame, text="카테고리:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
# category_var = tk.StringVar()
# category_menu = ttk.OptionMenu(selection_frame, category_var, "개척자", *categories.keys())
# category_menu.grid(row=0, column=1, padx=5, pady=5)

# tk.Label(selection_frame, text="캐릭터:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
# character_var = tk.StringVar()
# character_menu = ttk.OptionMenu(selection_frame, character_var, "")
# character_menu.grid(row=1, column=1, padx=5, pady=5)

# # 버튼 영역
# button_frame = ttk.Frame(main_frame, padding="10")
# button_frame.pack(fill="x", padx=5, pady=5)

# calculate_button = tk.Button(button_frame, text="데미지 계산", command=calculate_damage)
# calculate_button.pack(side="left", padx=5)

# instruction_button = tk.Button(button_frame, text="설명", command=show_instructions)
# instruction_button.pack(side="right", padx=5)

# # 결과 표시
# result_label = tk.Label(main_frame, text="결과: ", anchor="w", justify="left", wraplength=380)
# result_label.pack(fill="x", padx=5, pady=5)

# # 이벤트 연결
# category_var.trace_add("write", update_character_menu)
# character_var.trace_add("write", clear_inputs)

# # 초기 값 설정
# category_var.set("개척자")

# # 창 실행
# root.mainloop()
