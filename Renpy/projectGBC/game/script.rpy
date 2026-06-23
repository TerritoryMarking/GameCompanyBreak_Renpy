################################################################################
# 캐릭터 정의 (Character Definitions)
################################################################################

define player = Character("주인공")
define kijun = Character("한기준")
define isa = Character("천이사")
define eunbi = Character("황은비")
define hana = Character("백하나")
define solmi = Character("라솔미")
define unknown_char = Character("???")
define daeun = Character("김다은")
define dojin = Character("박도진")
define jaein = Character("신재인")

# 나레이션용 캐릭터
define narrator = Character(None)

################################################################################
# 이미지/효과 정의 (Image and Effect Definitions)
################################################################################

# 캐릭터 스프라이트
image isa_normal = "images/Char/Isa_Normal.png"
image eunbi_normal = "images/Char/Eunbi_Normal.png"
image hana_normal = "images/Char/Hana_Normal.png"
image solmi_normal = "images/Char/Solmi_Normal.png"
image daeun_normal = "images/Char/Daeun_Normal.png"
image kijun_normal = "images/Char/Kijun_Normal.png"
image jaein_normal = "images/Char/Jaein_Normal.png"
image dojin_normal = "images/Char/Dojin_Normal.png"

# 배경 이미지 플레이스홀더
image bg interview_room = "images/BG/MeetingRoom.jpg"
image bg gamjatang_restaurant = "images/BG/Gamjatang.png"
image bg bramun_market = "images/BG/Buramun.png"
image bg university_club_room = "images/BG/ClubRoom.jpg"
image bg hanas_room = "images/BG/HanaRoom.png"
image bg onlizeon = "images/BG/IndieGameBooth.jpg"
image bg company_front = "images/BG/Gobul.jpg" #//추후 변경 필요
image bg gobul = "images/BG/Gobul.jpg"
image bg makgeolli_bar = "images/BG/Makgeoli.jpg" #//추후 변경 필요


# 특수 이미지 플레이스홀더
image sd_keyring = "images/Char/Isa_Normal.png" #//추후 변경 필요
image sd_eunbi_dazed = "images/Char/Eunbi_Normal.png" #//추후 변경 필요
image unity_tilemap = "images/Char/Isa_Normal.png" #//추후 변경 필요
image mineral_dump = "images/Char/Isa_Normal.png" #//추후 변경 필요

# 인스타그램 이미지 예시 (실제 구현 시 여러 이미지 필요)
image is_insta_1 = "image/Char/Isa_Normal.png" #//추후 변경 필요

################################################################################
# 게임 시작 (Game Start)
################################################################################

label start:
    jump scene1_intro

# 1. 1분 자기소개는 아무도 듣지 않아.
label scene1_intro:
    jump s1

# S#1. 26살 2월, 면접 시작…
label s1:
    scene bg interview_room with fade
    "N사 면접장. 긴장감이 맴돈다. 총 3명이 앉아있다. 왼쪽부터 실무자 신재인, 디렉터 박도진, 팀장 한기준 순서대로 앉아 있다."
    "신재인과 한기준은 노트북을, 디렉터는 정면을 보고 있다."
    "이어, 한기준이 노트북에서 정면으로 시선을 옮긴다."
    show jaein_normal at right
    show dojin_normal at truecenter
    show kijun_normal at left
    kijun "안녕하세요."
    player "네, 안녕하십니까."
    kijun "… 자리에 앉으시면 됩니다."
    player "…네!"
    "내 앞의 의자를 밀고 자리에 앉았다."
    "허리 세우고, 손은 책상 아래, 시선은 정면보다 살짝 아래로."
    "옅은 웃음을 유지하기 위해 입꼬리를 억지로 고정시켰다."

    kijun "자, 긴장 푸시고요."
    kijun "먼저 준비해오신 1분 자기소개부터 시작해주시죠."
    "그 말을 듣는 순간, 이상하게도 감자탕 냄새가 떠올랐다."

    hide jaein_normal
    hide dojin_normal
    hide kijun_normal
    jump s2


# S#2. 26살 1월, 이사 누나와 감자탕
label s2:
    scene bg gamjatang_restaurant with fade
    "감자탕집. (낮) 오후 1시 30분. 이미 나온 감자탕은 끓고 있다."
    "N사 면접 보기 한 달 전."
    
    show isa_normal at center
    isa "야, 어차피 1분 자기소개는 아무도 안 들어."
    hide isa_normal
    player "… 뭐?"
    "팔팔 끓는 냄비에서 김이 올라온다."
    "이사 누나는 돼지 등뼈 하나를 앞접시에 건져 올리더니, 집게로 살을 툭툭 발랐다."
    show isa_normal at left
    isa "그래. 어차피 안 들으니까, 그럴듯한 말로 끊기지 않게만 말해."
    hide isa_normal
    player "그게 말이 돼?"
    show isa_normal at left
    isa "음…쩝… 말 되지."
    isa "면접이잖아."
    hide isa_normal
    player "면접이면 오히려 들어야 되는 거 아니야?"
    show isa_normal at left
    "이사 누나는 대답 대신 감자탕 국물을 한 숟갈 떠먹었다."
    isa "캬, 이거지. 진짜 몇 번을 먹어도 감동이 있다. 야."
    hide isa_normal
    player "지금 감자탕 평가할 때야?"
    show isa_normal at left
    isa "누나 오랜만에 휴가야."
    isa "목숨 걸고 먹는 중이니까 방해하지 마."
    isa "이거 먹는 거만 생각하면서 타향만리에서 버텼다고."
    isa "그리고, 이거 내가 사주는 거잖아. 알았으면 끄덕여."
    hide isa_normal
    "나는 고개를 끄덕이며 내 앞접시에 돼지 등뼈 하나를 옮겼다."
    player "네, 감사합니다. 선배님. 맛있게 드십쇼."
    "… 납득이 안 된다. 아까 이 여자는 도대체 나보고 뭐라는 걸까?"
    "내 표정을 봤는지, 이사 누나는 입에 남은 고기를 꿀꺽 삼키고 다시 말했다."
    show isa_normal at left
    isa "그 1분 동안 면접관들은 보통 네 포폴 읽어. 자기소개 시간에."
    hide isa_normal
    player "무슨 말이야…?"
    player "면접 전에 읽어 오는 거 아니야?"
    show isa_normal at left
    isa "… 너 면접관 해봤냐?"
    hide isa_normal
    player "아니."
    show isa_normal at left
    isa "나도 안 해봤어."
    hide isa_normal
    player "…?"
    show isa_normal at left
    isa "그래도 난 직장인은 해봤어."
    isa "회사원한테 제일 없는 게 뭔지 알아?"
    "이사 누나는 뼈를 내려놓고 휴지를 한 장 뽑았다."
    hide isa_normal
    player "… 돈?"
    show isa_normal at left
    isa "그건 너한테 없고. 난 많아."
    "젓가락으로 나를 가리키며 이사 누나는 말했다."
    hide isa_normal
    player "아. 맞네. 그럼 뭐가 부족한데?"
    show isa_normal at left
    isa "시간."
    isa "다들 자기 업무 하느라 바빠."
    isa "지원자 포폴을 처음부터 끝까지 읽어 본다고?"
    isa "여유로운 팀이면 그려러나?"
    hide isa_normal
    player "… 그래도 다 읽고 오겠지."
    player "누군가에겐 목숨이 걸린 일인데."
    show isa_normal at left
    "이사 누나는 잠깐 젓가락을 멈췄다."
    isa "입장이 다른 거지. 뭐."
    hide isa_normal
    "별일 아니라는 듯한 이사 누나의 말에, 나도 모르게 반박했다."
    player "그, 그러면 애초에 자기소개는 왜 해?"
    show isa_normal at left
    isa "그야, 안 시키면 어색하잖아."
    hide isa_normal
    player "진짜 너무하다."
    show isa_normal at left
    isa "진짜라니까."
    "이사 누나는 이제 할 말은 다 했다는 듯, 다음 돼지 등뼈를 자신의 앞접시로 들어 옮겼다."
    isa "아. 그렇다고 해서, 안 외워 가는 건 아니지?"
    hide isa_normal
    player "아무도 안 듣는다며."
    show isa_normal at left
    isa "안 들으니까 외워야지."
    isa "끊기면 그때부터 듣거든."
    hide isa_normal
    player "…"
    show isa_normal at left
    isa "자기소개는 잘해서 붙는 게 아니야."
    isa "망쳐서 떨어지지 않으려고 하는 거지."
    isa "그러니까 이번엔 잘 좀 해봐. 나도 후배한테 얻어먹어보자."
    isa "내 돈 주고 먹는데도 이렇게 맛있는데, 너한테 얻어먹으면 얼마나 맛있겠냐?"
    hide isa_normal
    "장난처럼 말했지만, 이상하게 그 말만큼은 빈말처럼 들리지 않았다."
    player "… 합격하면 다음엔 내가 살게."
    show isa_normal at left
    isa "떨어져도 네가 사."
    hide isa_normal
    player "왜?"
    show isa_normal at left
    "이사 누나는 별일 아니라는 듯 국물을 한 숟갈 떴다."
    isa "그러면 뭐, 천년만년 얻어먹게?"
    hide isa_normal
    "하얀 김 너머로, 입꼬리가 아주 조금 올라가 있었다."
    
    hide isa_normal
    jump s3


# S#3. 26살 2월, 면접장
label s3:
    scene bg interview_room
    "N사 면접장. 자기소개 질문을 받은 현재로 돌아온다."
    "선배가 그렇게 말하긴 했지만, 여전히 믿기지 않는다."
    "아무리 그래도 대기업이잖아. 체계와 규칙이라는 게 있을 거 아냐?"
    "나는 물을 한 모금 마신 뒤, 입을 열었다."

    player "안녕하십니까! 교내 게임개발 동아리에서 세 개의 게임을 개발해 본 지원자 주인공입니다."
    "첫 문장은 무사히 나왔다."
    player "저는 지난 프로젝트에서…"

    play sound "sfx/mouse_click.ogg"
    "딸깍."
    "왼쪽에서 패드를 누르는 소리가 났다."

    play sound "sfx/mouse_click.ogg"
    play sound "sfx/mouse_click.ogg"
    "딸깍, 딸깍."
    "이번엔 오른쪽이었다."
    "가장 왼쪽에 앉은 면접관의 시선이 내 얼굴에서 노트북 화면으로 내려갔다."
    "오른쪽 면접관은 이미 무언가를 스크롤하고 있다."
    "가운데 면접관은 정면을 보고 있지만, 정확히 나를 보고 있는 것 같지는 않다."

    "와."
    "진짜네…"
    player "게임을 만들 때 가장 중요하게 여기는 것은.."
    "입은 계속 움직였다."
    "수백 번 외운 문장은 뇌를 거치지 않고 흘러나왔다."

    "눈앞에서는 세 개의 화면이 빛난다."
    "그 너머에 앉은 사람들은, 내 목소리보다 내 포트폴리오의 페이지를 더 빠르게 넘기고 있었다."
    "아무도 안 듣는다고?"

    player "이 회사에서 함께 유저에게 사랑받는 게임을 만들어보고 싶습니다! 감사합니다!"

    "자기소개가 끝나자, 그제야 화면만 보던 면접관들이 하나둘씩 나를 쳐다봤다."
    "입꼬리를 올려 싱긋 웃어 본다. 어색하진 않으려나."
    "면접관들은 관심이 없는지, 아니면 속아 넘어간 건지 크게 반응하지 않았다."

    kijun "네, 여기 포트폴리오 보면 “STAY”라는 게임을 개발하셨다고 적혀 있는데,"
    kijun "간단히 소개해 주시겠어요?"

    jump scene2_team_building

label scene2_team_building:
    jump s4

# S#4. 24살 9월, 브라문 야시장
label s4:
    scene bg bramun_market with Dissolve(1.0)
    "브라문 야시장 술집 (저녁 노을), 창가 자리에 앉아 주인공과 이사 누나가 술을 마시고 있다. 시끌벅적한 분위기."
    "재작년 여름, 전역하고 얼마 되지 않았을 때였다."
    "잠깐 다녀왔다고 생각했는데, 그 사이에 세상은 이상한 속도로 바뀌어 있었다."

    show isa_normal at left
    player "누나, X 된 거 같아."
    isa "여기 토마토 계란 볶음밥 하나 주세요!"
    player "내 말 듣고 있어?"
    isa "물론이지. X 됐다며. 왠지 그래 보이더라."
    hide isa_normal
    player "AI 이거 뭔가 이상해."
    player "처음 나왔을 땐 그 정도 아니었는데, 이제 나보다 더 작업을 잘해."
    show isa_normal at left
    "이사 누나는 별 반응 없이 간짜장을 젓가락으로 크게 집어 먹었다."
    isa "냠… 음. 야, 이거 맛있다."
    hide isa_normal
    player "…"
    show isa_normal at left
    isa "AI가 네 일자리 뺏을까 봐 무서워?"
    hide isa_normal
    player "어."
    show isa_normal at left
    isa "틀렸어."
    hide isa_normal
    player "뭐가?"
    show isa_normal at left
    isa "이미 뺏겼어."
    hide isa_normal
    player "…"
    show isa_normal at left
    isa "표정 좀 풀어라. 술맛 떨어지게 굴지 말고."
    isa "군대 다녀오기 전에는 진짜 귀여웠는데 어쩌다가 이렇게 까칠해졌냐?"
    isa "…나 처음 봤을 때, 숫기 하나도 없어서 나한테 말도 못 걸고,"
    isa "쩔쩔매는 게 진짜 개쳐귀여웠는데."
    isa "“... 이사님, 이, 이거 언제까지 되나요오오오? 어디가세요오오오?”"
    hide isa_normal
    player "…"
    show isa_normal at left
    "이런 건 반응을 안 해줘야 빠르게 다음 주제로 넘어간다."
    isa "…. 재미없어."
    isa "그게 벌써 몇 년 전이지? 3년은 됐나."
    hide isa_normal
    player "딱 3년 정도 됐지."
    show isa_normal at left
    isa "그때가 엊그제 같은데 벌써 둘 다 복학생 아저씨가 됐네."
    hide isa_normal
    player "아저씨는 무슨."
    show isa_normal at left
    isa "아무튼 옛날엔 활기차고 발랄했는데, 왜 이리 우울해졌냐는 거지."
    hide isa_normal
    player "…"
    show isa_normal at left
    "이사 누나는 나를 보고 머리를 긁적이더니, 결심한 듯 말을 꺼냈다."
    isa "하씨... 이건 말 안 하려고 했는데, 알려줘야겠네."
    isa "사실, 이 누나는 AI에 대한 계획이 다 있어."
    hide isa_normal
    player "… 뭔데?"
    show isa_normal at left
    "솔직히 조금 혹했다."
    "평소에 헛소리만 해도 공부는 잘하는 누나니까,"
    "자기 미래가 걸린 일이라면, 뭔가 생각해둔 게 있지 않을까?"
    isa "알박기."
    hide isa_normal
    player "어…?"
    show isa_normal at left
    isa "졸업하고 빨리 취업해서 회사에 자리 알박아 둘 거야."
    isa "AI가 더 발전하기 전에 하루라도 빨리 노동법의 보호를 받아야 해."
    isa "들어가서 버티고, 아니다 싶으면 그때 이직하면 돼."
    "자신의 계획에 대해 말하는 이사 누나는 그 어느 때보다 진지했다."
    hide isa_normal
    player "애매하게 그럴 듯해서 더 짜치네."
    show isa_normal at left
    isa "원래 어른이란 건 다 짜치는 거야."
    hide isa_normal
    player "그런 건가?"
    show isa_normal at left
    isa "그런 거야."

    "물 소리. 천이사가 주인공 잔에 술을 따른다."
    "내 말을 들은 이사 누나가 내 잔에 한 잔 따라주었다."
    isa "아쉽게 된 일이지. 짠."
    hide isa_normal
    player "짠."
    
    play sound "sfx/glass_clink.ogg"
    "유리와 유리가 부딪히는 소리가 시끄러운 소음 속에 묻혔다."

    "한 시간."
    "두 시간."

    show isa_normal at left
    "AI가 어쩌고, 취업이 어쩌고 하던 이야기는 어느새 식은 간짜장 옆으로 밀려나 있었다."
    isa "그러니까아!!"
    isa "이 허리에서 꼬리로 이어지는 이 라인을 봐봐."
    isa "진짜 미쳤지 않았냐?"
    hide isa_normal
    player "얘는 꼬리 시작 부분이 보통 캐릭터보다 살짝 더 위인 게 킥이라고."
    show isa_normal at left
    isa "그것도 그렇고, 뿔이랑 꼬리 끝에만 핑크색인 게"
    isa "진짜 사람을 미치게 만든다니까."
    hide isa_normal
    player "오우, 엉덩이 보소."
    show isa_normal at left
    "이종족은 캐릭터의 실루엣이 다양해서 개발할 때 좋아."
    isa "… 이 게임은 언제부터 했어?"
    hide isa_normal
    player "전작부터 했지."
    show isa_normal at left
    isa "진짜?"
    "이사 누나의 목소리가 순간 옆 테이블까지 들릴 만큼 커졌다."
    hide isa_normal
    player "목소리 좀 낮춰. 누나."
    player "… 전작은 대학 입학 때부터 했고,"
    player "신작은 오픈부터 계속하고 있어."

    show isa_normal at left
    isa "와!!"
    isa "드디어 친구 찾았다!!!"
    isa "이렇게 오래 하는 사람 처음 봐."
    isa "내 주변엔 다 오픈 때만 하고 접더라고."
    hide isa_normal
    player "아무래도 장르가 마이너하니까… 그렇긴 하지."
    show isa_normal at left
    "전작은 디펜스, 신작은 공장 자동화 게임."
    "둘 다 대중적이라고 하기엔 어려운 장르였다."
    isa "안 되겠다."
    isa "너 오늘 집 못 가."
    hide isa_normal
    player "뭐?"
    show isa_normal at left
    isa "넌 오늘 나랑 씹덕 토크 해야 해."
    hide isa_normal
    "그렇게 말하는 이사 누나는 정말로 반가운 듯했다."
    "상병 때 나온 휴가 이후 6개월 만에 나를 봤을 때보다 더."
    "… 왜 기분이 묘하지?"
    
    show isa_normal at left
    isa "아니다."
    isa "그건 날 잡고 제대로 해야지."
    "이사 누나는 자신의 캘린더를 보여주며 손으로 날짜 여기저기를 가리켰다."
    isa "이날 어때? 안되면 이날은?"
    hide isa_normal
    player "이제 곧 개강인데, 뭐."
    player "누나 학교 나오는 날 불러."
    show isa_normal at left
    isa "그래그래. 자세가 좋아, 아주."
    "이사 누나는 흡족한 듯 고개를 끄덕였다."

    hide isa_normal
    scene black with fade
    "화면 암전. 시간이 흐른다."

    scene bg bramun_market with fade

    show isa_normal at left
    isa "아 맞다."
    isa "너, 혹시 요새 프로젝트 하는 거 있어?"
    hide isa_normal
    player "… 아니? 이제 전역해서 따로 하는 거 없어."
    show isa_normal at left
    isa "그래? 그러면 누나랑 하나 할래?"
    hide isa_normal
    player "갑자기?"
    show isa_normal at left
    isa "갑자기는 무슨."
    isa "생각해 보니까 우리 안 지도 꽤 됐잖아."
    isa "근데, 막상 너랑 제대로 해본 적이 없던 거 같아서."
    hide isa_normal
    player "… 처음 만났을 때, 게임잼 했었잖아."
    show isa_normal at left
    isa "그때 결국 완성 못했잖아."
    "하루 동안 진행되는 게임잼이다보니, 시간이 촉박해서 결국 완성하지 못했었다."
    "이사 누나는 흐트러져 있던 자세를 고쳐 앉더니,"
    "내쪽으로 몸을 살짝 기울였다."
    isa "그러니까, 이번엔 좀 더 본격적으로 해보자 이 말이지."
    hide isa_normal
    player "누나, 아이디어는 있어?"
    show isa_normal at left
    isa "있지."
    hide isa_normal
    player "뭐야?"
    show isa_normal at left
    isa "스타X밸리인데, 배경이 외계 행성이야."
    isa "주인공이 그 행성에 가보니까 다양한 종족들이 돌아다니는 거지."
    isa "수인도 있고, 퍼리도 있고,"
    isa "용족도 있고, 천족도 있고, 마족도 있고."
    isa "농사로 돈 많이 벌어서 걔네들을 꼬시는 게 엔드 컨텐츠인 거야."
    hide isa_normal
    player "진짜 아이디어만 있네…"
    show isa_normal at left
    isa "아무래도 본격적인 기획은 네가 할 거니까."
    hide isa_normal
    player "… 저요?"
    show isa_normal at left
    isa "너 스타X밸리 플탐 천 시간이잖아."
    hide isa_normal
    player "음… 그렇긴 하지."
    show isa_normal at left
    "한때 미친 듯이 했고, 지금도 심심할 때마다 켜곤 한다."
    isa "그러니까."
    isa "그럼 하자! 이종족 좋아하면서 농장 RPG도 좋아하는 사람은 흔치 않다고."
    isa "둘 다 은근 마이너 취향이라서 교집합이 없어서 신작도 잘 안 나와…"
    isa "그래서, 그런 게임 하려면 직접 만들 수밖에 없다고."
    hide isa_normal
    player "그렇다고 그렇게 갑자기 말하면…"
    show isa_normal at left
    isa "왜?"
    hide isa_normal
    player "아무래도 개발 스펙이 큰 편이잖아. 농장 시뮬이면."
    player "작물, 계절, NPC, 호감도, 맵, 상호작용, 이벤트도 있어야 하고."
    player "그냥 해보자고 하기엔 게임 사이즈가 너무 커."
    show isa_normal at left
    isa "술을 아직 덜 먹였나? 왜 아직도 지능이 높지?"
    hide isa_normal
    player "…예?"
    show isa_normal at left
    isa "아냐아냐. 음…"
    isa "그래! 너 내년에 취업할 거잖아."
    hide isa_normal
    player "… 그렇지?"
    show isa_normal at left
    isa "그럼 플젝 하나라도 해야지. 안 그래?"
    hide isa_normal
    player "… 그렇지."
    show isa_normal at left
    "이사 누나의 말이 맞다."
    "게임 회사의 경우, 게임 개발 경험이 있으면 좀 더 유리하니까."
    isa "어차피 해야 하는 거면, 좋아하는 걸로 해."
    isa "하기 싫은 장르, 포폴용으로 억지로 만들다가 터지는 것보다,"
    isa "이종족 농장 RPG 만들다 터지는 게 덜 억울하잖아."
    hide isa_normal
    player "망하는 걸 전제로 말하지 마."
    show isa_normal at left
    isa "말이 그렇다는 거지."
    isa "그래서 할래? 말래? 응응? 하자! 같이 좀 하자!"
    isa "나 이제 같이 이런 얘기 하면서 플젝 할 사람 너밖에 없단 말이야."
    "그 말에는, 평소보다 조금 힘이 빠져 있었다."
    isa "선배들은 다 졸업했고, 동기들은 취업 준비하고 있고."
    isa "요새 동방에 아는 사람 아무도 없어. 같이 하자. 응?"
    hide isa_normal
    "… 아무리 봐도 방금 생각해낸 논리 같은데, 묘하게 빠져나갈 구멍이 없었다."
    "취업하려면 프로젝트가 필요한 것도 사실이고."
    "그리고 무엇보다 이 정도로 말이랑 취향이 통하는 팀원을 구하는 것은 더 어려울 것 같았다."
    player "… 그럼 할까?"
    show isa_normal at left
    isa "하기로 한 거다?"
    "이사 누나는 잔을 들었다."
    "방금 전까지 장난처럼 굴던 얼굴에, 숨기지 못한 기쁨이 묻어 있었다."
    hide isa_normal
    player "… 뭐야. 왜 그렇게 좋아해?"
    show isa_normal at left
    isa "그냥."
    isa "말 통하는 후배가 오랜만에 돌아왔잖아."
    hide isa_normal
    "그 말에 나는 괜히 시선을 피했다."
    "… 취업은 해야 하니까."
    "취업하려면 포트폴리오도 필요하니까."
    "술자리에서 떠밀리듯, 그렇게 프로젝트가 시작되었다."
    
    hide isa_normal
    jump s5

# S#5. 24살 9월, 다음날 동방
label s5:
    scene bg university_club_room with fade
    "대학교 교실, 공대 건물 특유의 쿰쿰한 냄새가 난다."
    play sound "sfx/phone_vibrate.ogg"
    "휴대폰 진동 소리가 울린다."

    "다음 날, 이사 누나에게 연락이 왔다."
    isa "지금 시간 나?"
    player "ㅇㅇ"
    "마침 오늘 수업이 다 끝난 참이었다."
    isa "그러면 동방 와봐. 나도 곧 갈게."
    player "ㅇㅋㅇㅋ"
    "나는 가방을 들고, 자리에서 일어났다."

    "동아리방. 문을 기준으로 가운데는 6인용 테이블, 정면 벽면에는 소파가 놓여 있다."
    "또한 왼쪽 구석에는 커튼이 쳐진 공간이 있다. 커튼 뒷편에는 간의 침대 1개와 비품 박스가 놓여있다."
    "또한 문 바로 옆의 공간에는 사람 둘이 들어갈만한 사물함이 있다."
    
    show eunbi_normal at right
    "동방까지는 금방 왔다."
    "학교가 작아서 그런가."
    "문을 열고 안으로 들어서자, 낯선 여성 한 명이 6인용 테이블 왼쪽 구석에 앉아 있었다."
    "누구지? 동아리 신입 부원인가?"

    "그런데 분위기가 묘했다."
    "내 발소리를 듣자마자 그녀의 어깨가 작게 튀었다."
    "시선은 이쪽을 향했다가, 곧바로 테이블 아래로 떨어졌다."
    "단지, 손가락만 가방 끈 위에서 조심스럽게 꼼지락거리고 있었다."

    "뭘 하고 싶은 거지?"
    "… 화장실에라도 가고 싶은 건가?"
    "마치 누가 허락도 안 했는데 몰래 들어온 사람처럼 보였다."
    hide eunbi_normal
    player "안녕하세요!"
    show eunbi_normal at right
    unknown_char "아…안!녕하세요…"
    hide eunbi_normal
    player "…"
    show eunbi_normal at right
    unknown_char "…"
    "대화가 끝났다."
    unknown_char "……."
    "보통이라면 여기서 각자 핸드폰을 보면 된다."
    "동방은 원래 많은 사람이 오가기도 하고, 모르는 사람이 있을 수도 있으니까."
    "그런데 저 사람은 그 자세 그대로 멈춰있었다."
    "그렇다고 이쪽을 똑바로 보는 것도 아니었다."
    
    "힐끔."

    "눈이 마주치기 직전에, 다시 시선이 내려간다."
    unknown_char "………"
    hide eunbi_normal
    "제발 절 무시하고 할 일을 해주세요."
    "그렇게 생각했지만, 그쪽에서 먼저 나를 무시하지 못하고 있었다."
    "그렇게 애매하게 신경을 쓰면, 나도 신경 쓰인단 말이야…"
    "아, 무슨 말을 해야하지."
    "나도 이런 상황을 능숙하게 넘기는 타입은 아닌데."

    "어떻게든 어색함을 풀기 위해 스몰토크 거리를 찾던 도중,"
    "마침 그녀의 가방에 달린 키링이 눈에 띄었다."
    
    hide eunbi_normal
    show sd_keyring at center with moveinright
    "키링 이미지. 작은 뿔과 용 꼬리가 달린 SD 캐릭터. 발 밑에는 해파리 촉수 같은 것이 꿈틀거리듯 감겨있다. 한 손에는 피 묻은 가위를 들고 있다."
    pause 3.0
    hide sd_keyring with moveoutright

    player "어?"
    "나도 모르게 목소리가 튀어나왔다."
    player "그 키링. 혹시 “말촉” 작가님 굿즈 아니에요?"
    "말촉. 풀네임 ‘말랑 촉수’."
    "인터넷에 인외 중심의 호러 만화와 스케치를 올리는 작가다."
    "그림체는 둥글고 귀여운 편인데,"
    "내용은 이상할 정도로 잔인하고 불길하다."
    "그리고 가끔 작가 본인만 아는 신화 체계 같은 걸"
    "스케치 옆에 악필로 빽빽하게 적어놓는 취향도 있다."
    "나만 아는 줄 알았는데, 동지가 있었구나…!"
    player "저도 그 작가님 그림 좋아하거든요."
    show eunbi_normal at right
    "나는 가벼운 아이스브레이킹을 목적으로 말을 건넸다."
    "그런데 그 말을 들은 사람의 반응이… 예상을 한참 빗나갔다."
    unknown_char "히익…!"
    unknown_char "아, 그, 저, 그러니까…!"
    unknown_char "이, 이거는…!"
    "내 앞에 여성분은 말까지 절하며 당황해했다."
    hide eunbi_normal
    "아."
    "그러니까… 이건 그거지?"
    "내 취향을 처음 보는 사람에게 들켜서 부끄러운 느낌."
    "내가 겪어봐서 안다."
    "이럴 땐, 오히려 질문을 한 사람이 더 강하게 나가야 한다."
    "이게 ‘오타쿠를 향한 일반인의 순박하고 잔혹한 질문’이 아니라,"
    "나도 같은 쪽 인간이라서 한 말이란 걸 증명해야 한다."

    player "이 작가님을 제가 진짜 좋아하거든요!"
    player "인X타도 팔로우 했어요."
    show eunbi_normal at right
    unknown_char "…!! 아.. 그…네…"
    unknown_char "좋아…하시는 구나.."
    hide eunbi_normal
    "아직 부족한가?"
    "어떻게 더 어필을 하지?"
    player "개인적으로 이 작가님 콘 중에 <초괴수카구야공주콘> 있잖아요."
    player "그거 진짜 귀엽지 않아요?"
    show eunbi_normal at right
    unknown_char "그, 그거.. 네..!"
    unknown_char "아…아니에요…"
    hide eunbi_normal
    "나는 핸드폰을 켜 말촉 작가님의 블로그를 켰다."
    player "아, 그리고 이거는 보셨어요?"
    player "가장 최근에 올리신 단편인데, 진짜 말도 안 돼요."
    "사는 게 질려 죽길 원하는 뱀파이어와 무엇이든 죽여주는 살인청부업자 인간."
    "이런 관계성을 도대체 어떻게 생각해내는 걸까요?"
    show eunbi_normal at right
    unknown_char "으아아…."
    hide eunbi_normal
    "…?"
    "내 앞에 있는 사람이 뭔가 반응이 이상하다."
    show eunbi_normal at right
    "동공은 지진이라도 난 듯 사정없이 흔들렸고,"
    "가방은 어느새 조그만한 등 뒤로 숨겨져 있었다."
    "금방이라도 울 것 같은 표정으로 덜덜 떨기 시작한다."
    hide eunbi_normal
    player "아, 아니… 기분 나쁘셨다면 죄송해요."
    player "그냥, 좋아하는 작가라서…"
    show eunbi_normal at right
    unknown_char "아, 아, 아니에요! 그게 아니라…"
    unknown_char "으아아… 감사합니다…{size=-10}(작은 글씨){/size}"
    hide eunbi_normal
    "뭐지?"
    "내가 잘못한 건가…?"
    "순식간에 큰 잘못을 저지른 쓰레기가 된 것 같은 기분에 식은땀이 흐르려던 찰나,"
    "타이밍 좋게 동방 문이 벌컥 열렸다."

    show isa_normal at left
    isa "오, 둘 다 일찍 왔네?"
    isa "인사들은 나눴어?"
    "구원자처럼 등장한 이사 누나는 아주 자연스럽게 나와 여자분에게 손을 흔들었다."

    hide isa_normal
    player "어? 아는 사람이야?"
    show isa_normal at left
    isa "… 우리 팀인데?"
    hide isa_normal
    player "…네?"
    show isa_normal at left
    isa "인사해. 이쪽은 앞으로 우리 게임 아트를 맡아줄 황은비."
    show eunbi_normal at right
    isa "그리고 은비야, 이쪽은 어제 말했던 그 기획자."
    "이사 누나는 씩 웃으며 덧붙였다."
    isa "참고로 이 친구도 너 못지않게 인외 좋아해."
    isa "팀원 잘 데려왔지?"
    eunbi "힉…!"
    eunbi "그, 그런 식으로 말하면…!"
    "황은비라는 분은 얼굴이 터질 듯 달아오르더니,"
    "갑자기 자리에서 벌떡 일어났다."
    eunbi "저, 저 먼저 가볼게요!"
    eunbi "죄송합니다!"

    "다다다다다 뛰어나가는 소리."
    hide eunbi_normal

    "황은비씨는 인사조차 제대로 마치지 못한 채,"
    "동방 문을 박차고 도망쳤다."

    player "… 어떡하지?"
    isa "왜?"
    player "내가 뭔가 크게 잘못한 거 같은데…"
    "나는 이사 누나가 오기 전에 있었던 일을 말했다."
    "모든 이야기를 들은 이사 누나는…"
    isa "아하하하하."
    isa "진짜 그렇게 말했어?"
    hide isa_normal
    player "… 거기서 내가 가만히 있었으면 은비 씨 진짜 수치스러웠을걸."
    player "누나는 안당해봤어?"
    player "일반인의 순박한 질문?"
    show isa_normal at left
    isa "아하하하하하. 진짜 넌 최고다. 진짜로. 핳하하."
    "이사 누나는 내 말에 더 크게 웃었다."
    "뭐가 그렇게 웃긴 걸까…?"
    "… 잠시 뒤, 이사 누나가 진정하고 말을 건넸다."
    isa "그게 문제가 아니라, 그냥 상황이 웃겨서 그래."
    isa "넌 잘했어."
    isa "은비가 부끄럼이 좀 많아서 그래. 냅둬, 금방 적응할 거야."
    hide isa_normal
    player "진짜지?"
    show isa_normal at left
    isa "응."
    isa "아마 지금쯤 복도쯤에서 자기 가방 끌어안고 죽고 싶어하고 있을 걸?"
    hide isa_normal
    player "… 괜찮은 거 맞지?"
    show isa_normal at left
    isa "부끄럽다고 사람 안 죽어."
    hide isa_normal
    player "아 근데, 누나 친구 없다면서. 어디서 사람 구한 거야?"
    show isa_normal at left
    isa "난 학교에 친구 많아. 친구는 네가 없는 거지."
    "이사 누나는 나에게 혀를 내밀었다."
    "선배만 아니였어도…"
    hide isa_normal
    player "…"
    show isa_normal at left
    isa "아무튼, 이제 사람도 모아놨으니까, 일정 짜고 작업 시작하자."
    hide isa_normal
    player "카톡방 만드는 김에 깃까지 파줘."
    player "난 노션 세팅해야함."
    show isa_normal at left
    isa "깃까지 판 김에 저녁도 먹자. 감자탕 먹을래?"
    hide isa_normal
    player "싫어. 지난 주에도 먹었잖아."
    show isa_normal at left
    isa "감자탕은 쿨타임 없어."
    hide isa_normal
    "그날은 치킨을 먹고 돌아갔다."

    hide isa_normal
    jump s6

label scene3_get_closer:
    jump s6

# S#6. 24살 10월, 동아리방
label s6:
    scene bg university_club_room with fade
    "그렇게 천이사, 은비, 주인공 세 사람은 개발을 시작한다."
    show isa_normal at left
    show eunbi_normal at right
    "동아리방, 황은비, 천이사, 주인공 순서대로 자리에 앉아 있다."

    isa "하아아아아암… 농사 기본 시스템 1차 올렸어. 확인 좀 해줘."
    "저녁 5시, 우렁찬 기지개소리와 함께 커밋이 올라왔다."
    hide isa_normal
    hide eunbi_normal
    player "굿굿. 바로 확인해볼게."
    show isa_normal at left
    isa "분량이 꽤 있어서 저녁 먹기 전까지는 다 못 볼 걸?"
    isa "저녁 먹고 천천히 보셈."
    hide isa_normal
    player "하긴 그렇긴 하네."
    "농사 1차는 작물 심기, 밭 갈기, 물 주기 & 마르기, 자라기 등등 체크할 게 꽤 있는 편이다."
    player "근데, 나 오늘은 과제해야해서 저녁 이후에 못 봐."
    player "내일 봐도 돼?"
    show isa_normal at left
    isa "어. 문제 없을 듯? 다른 거 하고 있지 뭐. 번들 시스템 건드리고 있을까?"
    hide isa_normal
    show eunbi_normal at right
    player "좋지. 아 그러면 은비님, 지난 번에 부탁드렸던 번들에 들어가는 아이템들 어디까지 진행됐어요?"
    
    "프로젝트가 시작된 지 한 달 정도 지난 지금."
    "신생 팀 치고 놀랍게도 손발이 매우 잘 맞고 있다."
    "따로 부탁하지 않았는데도, 여유 시간이 나면 동방으로 와 작업하는 팀원들."
    "심지어 작업 중 이해가 안 가는 부분이 있으면 명확히 물어보고, 더 나은 아이디어도 제안한다."
    "이런 말도 안되는 유니콘 같은 팀에 감사하며 살고 있지만…"
    "딱 하나 고민인 점이 있다면,"

    player "… 은비님?"
    eunbi "히…히익….!!! 그… 네… 오늘 밤까지는 드릴 수 있을 거 같아요…"
    player "아… 천천히 주셔도 돼요. 일정 확인하려고만 하는 거라서요."
    hide eunbi_normal
    
    "은비님이 날 무서워하는 거…?"
    
    "10분 후,"

    show isa_normal at left
    isa "그러면, 저녁 먹기 전까지 한 시간 정도 남았으니까,"
    isa "내가 어제 밤에 생각한 개쩌는 아이디어 들어볼래?"
    hide isa_normal
    player "… 어, 해봐."
    show eunbi_normal at right
    eunbi "… 네. 들려주세요."
    hide eunbi_normal
    show isa_normal at left
    isa "마을에 축제가 열려."
    isa "주민들은 모두 신나서 각자의 방식으로 축제를 즐기고 있지."
    isa "어린 용족들은 군집 비행으로 마을 하늘을 날아다니고,"
    isa "다람쥐 노인들은 길거리의 주민들에게 꽃 한 송이씩 나눠주고 있어."
    hide isa_normal
    player "뻔해서 좋네."
    show isa_normal at left
    isa "그렇게 다같이 축제의 하이라이트인 ‘번영식’을 기다리는데,"
    isa "시장님의 가발이 도난당하는 사건이 발생한 거야."
    isa "유저는 마을 사람 중에 범인이 누구일 지 추리하는 거지."
    hide isa_normal
    player "… 왜 유저한테 탐정을 맡겨? 얼마 전에 이사온 사람이 제일 유력한 용의자가 아냐?"
    show isa_normal at left
    isa "어… 그거까지는 생각 안했는데?"
    isa "그냥 시장님의 가발이 도난당했으면 했어."
    hide isa_normal
    player "…"
    show isa_normal at left
    isa "솔직히 재밌잖아."
    hide isa_normal
    player "그렇긴 해."
    show eunbi_normal at right
    eunbi "…"
    hide eunbi_normal
    player "그러면, ‘유저에게 왜 탐정을 맡기는 지’만 설득시키면 되네."
    player "음… 어떻게 하면 유저가 추리를 하게 되지?"
    "잠시 침묵. 어려운 질문에 다들 고민하고 있다."
    show eunbi_normal at right
    eunbi "부끄러워서…"
    "먼저 입을 뗀 건 은비님이었다."
    hide eunbi_normal
    show isa_normal at left
    isa "조금만 더 크게 말해봐. 은비야."
    hide isa_normal
    show eunbi_normal at right
    eunbi "시장이 일 크게 만들고 싶지 않아서요...!"
    eunbi "누가 자기가 대머리인 걸 말하고 싶겠어요…"
    hide eunbi_normal
    player "그러면 본인이 직접 조사하지 않을까요?"
    show eunbi_normal at right
    eunbi "…"
    "은비님은 날 보더니, 잠시 숨을 고른 뒤 대답했다."
    eunbi "마을 축제가 한창이라 조사할 시간이 없는 거죠."
    eunbi "그러면 소문을 퍼뜨릴 친구가 없는 이방인인 유저에게 요청하지 않을까요?"
    hide eunbi_normal
    
    "다들 고민하다가 이내 서로 눈이 마주친다."

    player "그럼 진행할까요?"
    show isa_normal at left
    isa "난 좋아."
    hide isa_normal
    show eunbi_normal at right
    eunbi "… 네."
    hide eunbi_normal
    
    player "그러면 탐색 시스템은 어떻게 가져가지?"
    player "마을 사람들을 탐문해도 다들 답을 잘 안해주는 게 더 자연스러운데…"
    show isa_normal at left
    isa "TRPG 시스템처럼 확률에 따라 결정되게 만들면 되잖아."
    isa "주사위 굴려서 운 좋으면 단서 획득 성공하고 운 안 좋으면 실패하게."
    hide isa_normal
    "그러면, 단서 몇 개는 얻고 몇 개는 모르니까. 추리가 작동하잖아."
    player "나 TRPG 안해봤는데…?"
    "게임 기획을 하다보니, 들어도 보고, 시스템에 호기심도 생겼지만, 해볼 사람도, 판이나 환경 만들기도 어려워 관심은 있지만 해본 적은 없다."
    player "누나는 TRPG 해봤어?"
    show isa_normal at left
    isa "나도 안 해봤는데? 그냥 유튜브에서 봤어."
    hide isa_normal
    player "… 그래."
    show isa_normal at left
    isa "TRPG 시스템이 있으면, 왠지 미국 너드 개발자가 3년 동안 혼자 개발해서 출시한 게임 같기도 하고."
    hide isa_normal
    show eunbi_normal at right
    eunbi "…."
    hide eunbi_normal
    player "흠… 한 번 룰북이라도 읽어보고 싶은데, 나무위키에 치면 나오려나?"
    show eunbi_normal at right
    eunbi "…!"
    hide eunbi_normal
    show isa_normal at left
    isa "나무위키는 거짓말 안해."
    hide isa_normal
    
    "며칠 뒤, 책을 빌려주게 되는 황은비."
    
    hide isa_normal
    hide eunbi_normal
    jump s7

# S#7. 24살 10월, 3일 뒤.
label s7:
    scene bg university_club_room
    "룰북을 옆에 펴 놓고, 게임 레퍼로 확인 중에 있는데, 은비님이 힐끔힐끔 쳐다본다."
    "… 또 이 패턴이야?"

    player "시간 괜찮으면… 같이 해볼래요?"
    eunbi "… 네!? 저요??"
    player "빌려주시기도 했고, 기획에 써보려면 직접 해보는 게 나을 거 같아서요."
    player "… 혼자서는 감이 안 잡히는 부분들이 있기도 하고요."
    eunbi "… 그래도."
    eunbi "처음 해본 사람이랑은 안해서요."
    player "아, 그러시구나."
    eunbi "아! 아니!! 그게 아니라…!"
    eunbi "세부 룰이나, 설명할 부분들이 많아서 초심자가 하기엔 어려운 거라서요…!"
    player "며칠 동안 룰북 읽어봤어서 어느 정도 익숙해지긴 했어요."
    player "그리고 제가 모르는 부분이 있으면, 그건 알려주시면서 하면 되지 않을까요?"
    player "… 괜찮죠?"
    eunbi "… 네…"

    scene black with fade
    "간단한 두 명이서 하는 추리 TRPG였다."
    "플레이어는 탐정이 되어서, NPC들을 심문하고, 범인을 찾는 형태."
    "확실히 혼자서 룰 북을 볼 때보다는 훨씬 더 빠르게 이해할 수 있었다."
    
    scene bg university_club_room # Or some other TRPG background
    
    eunbi "로즈 아가씨, 혹시 지난 새벽 3시쯤에 어떤 일을 하셨는지요?"
    "이렇게 물어보면, 룰 북에 따라서 가능한 답변을 하면 되는 구나…"

    eunbi "당신 아까 가스파드 백작이라고 했어."
    eunbi "백작가의 경비병이 자기가 지키는 백작의 이름도 똑바로 몰라?"
    eunbi "어디서 굴러먹던 놈이야?"
    player "어… 어?"

    "그냥 레퍼런스 삼아서 한 번 해본 건데…"
    "… 왜이리 몰입하셨지."

    player "그렇게, 뱀파이어는 줄을 타고 도망치고, 당신은 저택에서 빠져나왔습니다."
    eunbi "아까 주사위 때문에 못 봤던 그 단서 뭐였어요?"

    eunbi "… 그건 그렇고…"
    player "어? … 뭐 또 추가할 게 있어요?"
    eunbi "… 왜 말 안 놔요…?"
    player "응?"
    eunbi "이사 언니랑은 말 편하게 하면서,"
    eunbi "왜… 저랑은 말 안 놔요?"
    eunbi "… 안 지 한 달이나 됐으면서…"
    player "…? 놓으면 돼?"
    eunbi "…!!"
    eunbi "…. 네. 선배."
    jump s8
    
# S#8. 25살 2월, 천이사의 탈주
label s8:
    scene bg university_club_room
    show isa_normal at left
    show eunbi_normal at right
    "동아리방. (낮) 이사, 은비, 주인공이 각자 화면을 보며 작업을 하고 있다."

    isa "맵 프리팹은 여기서 땡겨오면 돼. 지금 일단 더미 넣어놨거든? 확인해봐."
    "잠깐의 로딩 이후, 이사 누나가 작업한 곳을 확인했다."

    show unity_tilemap at center with dissolve
    "유니티 타일맵, 흰 네모에 붉은 글씨로 ‘조약돌’, ‘잔디’라 적힌 타일이 여러 개 배치된 이미지."
    pause 3
    hide unity_tilemap

    player "확인했어, 누나. 은비야, 지형 바닥 타일 리소스는 언제까지 돼?"
    eunbi "방금 다 만들긴 했는데요… 잘 어울리는 지 모르겠어서요."
    player "그럼 일단 푸시해줘봐. 넣어보고 안 예쁘면 그때 고치자."
    eunbi "네, 그러면 일단 작업하던 거 바로 깃에 올릴게요."

    "대화가 끝나자, 다시 처음처럼 각자 화면을 보며 작업을 했다."
    isa "아, 맞다. 주인공아."
    player "또 벌써 작업 끝낸 게 있어? 누나?"
    isa "그건 아니고, 나 내일부터 플젝 참여 못한다."
    player "…네? 방금 뭐라고…?"
    isa "해외 회사 면접 붙었거든. 다음 주부터 캘리포니아다."
    player "…네???"
    player "그럼 저랑 은비는 어떻게 하고요?"
    isa "그래, 이제부터 네가 이 팀의 팀장이다."
    
    hide isa_normal
    hide eunbi_normal
    
    scene black with fade
    # play music "path/to/upbeat_music.ogg" # Placeholder
    show is_insta_1 at center with dissolve
    pause 2
    
    "경쾌한 음악, 이사의 인스타그램 이미지. 야자수가 보이는 캘리포니아 해변에서 칵테일을 들고 있는 천이사 사진이 차례대로 업로드 된다."

    player "오늘은 흑인 누나랑 친해졌구나? 이사 누나. 보기 좋네…"
    "프로젝트 ‘STAY’의 지주였던 이사 누나는, 동방에서의 그 한마디를 남기고 팀을 떠났다."
    "입사 전까지 집도 알아보고 여러 절차도 밟아야 한다고 바쁘다고 했던 그녀는,"
    "막상 캘리포니아에 도착한 날부터 하루도 빠짐없이 인스타에 놀고 있는 사진을 올렸다."
    
    # stop music fadeout 1.0
    # play music "path/to/sad_music.ogg" # Placeholder
    
    "음울한 음악, 화면 절반으로 나눈 이미지. 좌측에는 아무 주석 없는 코드 / 우측에는 눈의 초점이 사라진 멘헤라 은비."
    "그러나, 이사 누나의 무책임을 탓할 새도 없었다."
    "그가 남긴 자리엔 아무 주석도 쓰지 않은 코드와… 함께 버려진 아트 담당 황은비 뿐이었으니까."

    jump s10

# S#10. 신입생 환영회 (과거)
label s10:
    scene bg makgeolli_bar with fade
    show eunbi_normal at right with dissolve
    "막걸리싸롱 (밤) 삼겹살 냄새와 소주 냄새가 뒤섞인 시끄러운 신입생 환영회 술자리. 주인공과 은비는 구석 테이블에 앉아 영혼이 나간 표정으로 잔을 채우고 있다."
    "이사 누나가 캘리포니아로 도망친 지 딱 한 달 반쯤 지났다."
    player "이번엔 이틀 만에 도망쳤나? 신기록 갱신이네."
    eunbi "…그 언니는 왜 주석을 한 개도 안 달아놔서… 그리고, 새로 온 프로그래머 오빠는 바쁘신가 보네요… 톡을 안 보시는 구나.."

    "그동안 은비와 나는 이사 누나의 후임자를 찾아 다녔다."
    "하지만, 이사 누나의 복잡하고 기괴한 코드 덕분에, 후임 프로그래머를 구하는 건 불가능에 가까웠다."
    "동아리에서 코딩 좀 한다는 지인들에게 바짓가랑이를 붙잡고 부탁해봤지만, 다들 일주일을 버티지 못하고 도망쳤다."
    "나같아도 주석 없는 남의 코드를 바탕으로 개발하기 보다는 그냥 다른 팀 가서 새로운 프로젝트 하나 하지 않을까… 싶다."
    "다 버리고 처음부터 하기엔 6개월이나 개발해서 버리긴 아깝고, 그대로 두기엔 아무도 원하지 않는 프로젝트."
    "그게 탈주한 이사 누나가 우리에게 남긴 것이었다."

    player "은비야. 그동안 고생했어."
    player "너도 그 성격에 처음 보는 사람에게 말 걸고, 부탁하느라 힘들었잖아."
    player "그냥 오늘 털고, 끝내자."
    eunbi "싫어요…이 …이대로 끝나는 건 싫어요."
    "은비가 이정도로 크게 감정표현을 하는 건 처음이라, 솔직히 당황했다. 그러나…"
    player "방법이 있어야지.. 다른 사람이 온다고 달라질 거 같지도 않고."
    "평소 아무리 흐물거리던 인간이여도, G사 붙은 사람의 코드다."
    "단순히 주석이 달리지 않았다라기보단 그 복잡성이 가장 큰 문제였다."
    "타인과 일하는 것을 상정하지 않았다보니, 오버엔지니어링, 자신만 이해하는 코드 흐름으로 가득 차 있었다."
    player "왜 게임 코드에서 예술을 하고 있는 거야. 미친 사람."
    
    "은비와 둘이서 소주나 까며 진짜 프로젝트의 종말을 선언한 그 순간, 옆 테이블에서 한 명이 나에게 말을 걸었다."

    show hana_normal at center
    unknown_char "저기요. 아까부터 어쩌다 보니 들었는데, 혹시 개발자 구해요?"
    player "…아. 괜찮아요. 이젠 안 구해서요."
    unknown_char "에이, 옆에서 다 들었는데, 제가 해볼래요."
    unknown_char "개발자들 다 도망쳤다면서요. 제가 해내면 이 팀에 구세주 같은 거 아니에요?"
    player "…그렇죠. 네."
    "도망친 개발자가 열 명이 넘어간 지금, 구세주 같은 건 없다고 확신한다."
    unknown_char "어차피 다른 방법도 없잖아요. 제가 할게요."

    "술이 잔뜩 취해 쫑알거리는 목소리를 들으니, 안 그래도 쓰린 속이 더 얹히는 기분이었다."
    "술맛도 떨어졌고, 일단 이 시끄러운 입을 막는 게 우선이라는 생각이 들었다."

    player "이름이 뭐에요?"
    hana "… 백하나요."
    player "번호 줘요."
    hana "어… 왜요..!!"
    "눈 앞에 보이는 여자는 조금 당황한 듯 되물었다."
    player "할 수 있다면서요."
    "나는 속의 울분을 꾹꾹 참고 최대한 감정 섞이지 않은 말투로 말을 건넸다."
    "백하나는 이내 얌전히 내게 번호를 건넸다."

    play sound "sfx/phone_vibrate.ogg"
    "하나의 휴대폰에서 진동이 울린다."
    "잠시 뒤, 하나의 휴대폰에 진동이 울렸다."
    player "메일 보내주시면 깃 초대해드릴게요."
    hana "아… 네. 잠시만요. 지금 보내드렸어요."
    "하나가 잠시 핸드폰을 만지작 거리더니만 메일 주소를 보내주었다."
    "주소를 확인한 나는 하나에게 프로젝트의 깃 링크를 던져주었다."
    "어차피 이틀 뒤면 얘도 연락을 끊을 거니까."
    "지금 당장은 입을 다물어줬으면… 하고 보냈다."

    jump s12

# S#12. 하나의 방 (과거)
label s12:
    scene bg hanas_room with fade
    "자취방 책상. (새벽) 모니터의 푸른 빛이 하나의 얼굴을 비추고 있다. 책상 위에는 다 마신 몬스터 캔 3개와 전공 서적이 어지럽게 널려 있다. 화면에는 천이사(1024)이 작성한 수천 줄의 C# 코드가 띄워져 있다."
    "술자리에서 그가 건네준 프로젝트의 코드는 거대한 콘크리트 벽이었다."
    hana "… 이게 뭐야?"
    "코드를 본 첫 날, 하나는 자신의 컨디션을 의심했다."
    "둘째 날, 쓸데 없는 오버엔지니어링에 전임자를 욕했다."
    "셋째, 넷째 날, 아무 것도 이해할 수 없었다."
    "넷째 날까지 하나는 총합 약 10시간 정도 잤다."
    "… 자러 갈까? 그렇지만, 할 수 있다고 당당히 쫑알거렸던 술자리가 계속 떠올랐다."
    hana "… 술 좀 적당히 마실 걸. 평소에 안하던 짓을 왜 했을까."
    
    "고등학교 시절에 고난이도 수학 문제를 풀어본 적이 있는가?"
    "종종, 정답률 1%% 이하인 수능 수학 문제들이 출제된다."
    "그런 문제를 본 어떤 학생은 30분 정도 고민하고 답을 적어낸다."
    "어떤 학생은 2시간 정도 충분히 고민하고 답을 적어낸다."
    "그리고 어떤 학생은 풀릴 때까지 하루든 이틀이든 멈추지 않고 마음껏 낭비한다."
    "그런 낭비벽 있는 학생은 그게 딱히 좋아서 하는 행위가 아니다."
    "단지, 그러지 않으면 안되기 때문에."

    "안타깝게도 하나가 그런 사람이다."
    "스스로를 갉아먹고, 피곤하게 만들고, 다른 효율적인 행위를 한다는 선택지를 없앤다."
    
    "그럼에도 불구하고 하나가 그렇게 사는 이유는 아름다움 하나다."
    "문제가 가진 복잡함의 출처가 출제자의 악의와 기만으로 구성된 것이 아니라 자신이 발견한 수학 자체가 가지는 아름다움의 편린을 나눠주고 싶다는 의지라는 것을 알게 된다면,"
    "어디 사는 지, 어떻게 생겼는 지도 모르는 수학 교수의 마음이 전해진다면,"
    "그제서야 이 모든 과정이 혼자 끙끙거리던 시간이 아니라 누군가와 함께라는 것을 알게 된다."

    "그런 아름다움과 고양감이 하나의 자취방에서 다시 재현되었다."
    "하나는 얽히고설킨 코드 속에서 딱 한 블록, 완벽하게 맞물려 돌아가는 객체 지향의 흐름을 이해했다."
    "수많은 코드 중 고작 한 블록이었지만, 하나는 온몸에 소름이 돋았다."
    
    hana "…대박."
    "욕을 하면서 읽을 때는 몰랐는데, 구조를 깨닫고 보니 소름 끼치도록 정교했다."
    "오기가 생긴다. 이 미친 천재가 짜놓은 판을 내 손으로 분석해내고 말겠다는 개발자로서의 자존심이 건드려진다."
    
    "자리에서 벌떡 일어나는 소리."
    "하나는 자리에서 일어나, 냉장고로 향했다."
    hana "한 캔 더 까야겠네."
    "하나는 차가운 몬스터 캔의 탭을 소리 나게 젖히며 다시 모니터 앞으로 앉았다."

    jump s13
    
# S#13. 동아리 방 (과거)
label s13:
    scene bg university_club_room with fade
    "동아리방. (낮) 신환회로부터 일주일이 지난 날. 오후의 햇살이 창문으로 들어오고 있다. 주인공은 책상에 앉아 노트북을 켜고, 은비는 태블릿으로 의미 없는 선만 긋고 있다."
    player "아, 습관."
    "과제를 하기 위해 노트북 로딩이 끝나자 마자, 나도 모르게 엔진을 켰다."
    "은비와는 끝내기로 지난 주에 말은 했지만, 일주일 내내 습관처럼 켜곤 했다."
    "죽은 자식 불X 만지기가 이런 느낌일까."

    show sd_eunbi_dazed at right with dissolve
    "은비 멍한 상태 SD 이미지, 태블릿에 그냥 의미없이 선만 찍찍 긋는다."
    "이런 마음이 나만 있는 것은 아닌지, 은비도 상태가 좋진 않다."
    "동아리 내에서 안된다면, 동아리 밖에서 찾아봐야 하나…"
    "아예 모르는 사람이랑 작업하는 건 쉽지 않은데."
    "동아리 밖이라고 사실 잘한다는 보장도 없고, 왠지 돈을 줘야할 거 같다. 안하려고 했는데..."
    "… 그건 그렇고 정말로 은비를 저렇게 냅둬도 되는 걸까?"
    hide sd_eunbi_dazed

    play sound "sfx/door_open.ogg" # Placeholder
    "쾅 하는 소리, 은비가 깜짝 놀란다."
    "동방에 누가 들어왔다."
    show hana_normal at center with moveinleft
    hana "허억 허억 허억.. 저기, 자리 남아요?"
    player "…어 네?"
    hana "그 프로젝트, 자리 있냐고요."
    player "… 집 가서 깃 확인해보셨어요?"

    "근거 없는 자신감인 줄로만 알았던 하나의 눈은, 일주일 동안 잠을 못 자서 퀭해져 있었다. 하지만 그 눈빛만큼은 이상할 정도로 확신에 차 있었다."
    
    hana "전임자가 천이사 선배라고 했죠? 이사 선배 코드 확인했어요."
    player "… 이사 누나꺼 얼마나 이해했어요?"
    "나는 물어보면서 백하나의 눈을 마주쳤다."
    "퀭한 눈, 내려온 다크서클. 처음 봤을 때는 안 그랬는데…?"
    "하나는 잠시 고민하다가 입을 열었다."
    hana "솔직히, 모든 걸 이해하진 못해서 퍼센트로 표현은 못하는데, 어느 정도는 이해했어요."
    hana "작업은 들어갈 수 있는 정도? 물론 어떤 걸 시키느냐에 따라 다르긴 할 텐데…"
    "다시 백하나의 눈을 봤다. 멍청해보이고 시끄러웠던 첫인상과는 뭔가 달라보였다."

    player "… 지금 시간 나요?"
    hana "…네? 아, 지금이면 괜찮아요."
    player "팀원 셋 다 있는 김에, 협업 기본 세팅도 하고 일정도 짜보려고요."
    "하나는 내 옆자리에 앉으며 말했다."
    hana "안 그래도 노트북 들고 왔어."
    player "? … 말이 짧으시네요?"
    hana "이제 팀이잖아. 어차피 친해질텐데, 시간 아끼자."
    eunbi "(심기불편하게 하나를 쳐다보며)…"
    "사람 잘못 본 거 같다. 미친 사람이다."
    player "편한 대로 하세요. 아니, 편한 대로 해."
    "그래도… 시간 아끼면 좋긴 하니까."
    hana "그래서 이게 무슨 게임이야?"
    player "… 그러니까, 이게 이종족이 사는 행성 시골에서 스타X밸리 하는 건데, 게임의 핵심 재미 포인트가…"
    "그 뒤로 2시간 동안 하나에게 전반적인 프로젝트 설명을 했다."


    "s14끝"
    "데모는 여기까지"

    return
