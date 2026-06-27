#!/usr/bin/env python3
"""
Rewrite all lesson notes:
1. Keep only EN explanations (remove CN where EN exists)
2. Rewrite EN for clarity
3. Add missing example sentences
"""

import re, os

BASE = os.path.dirname(os.path.abspath(__file__))

def esc(s):
    return s.replace('\\', '\\\\').replace("'", "\\'").replace('"', '\u201c')


# ============================================================
# Note data for all 12 lessons
# Format: {lesson_num: {note_index: (title, body)}}
# title = bold grammar name
# body = EN explanation + examples
# ============================================================

def N(lesson, index, title, body):
    """Register a note replacement."""
    if lesson not in note_data:
        note_data[lesson] = {}
    note_data[lesson][index] = (title, body)

note_data = {}

# --- L1 ---
N(1, 1,
   '**[1] 越来越 (yuèláiyuè) \u2014 more and more**',
   '"越来越" means "more and more" or "increasingly". It indicates that the degree of something grows over time. It is followed by an adjective or a verb that expresses a change.\n'
   '① 天气越来越凉快。 (The weather is getting cooler and cooler.)\n'
   '② 汉语越来越难。 (Chinese is getting harder and harder.)\n'
   '③ 他越来越喜欢中国。 (He likes China more and more.)')

N(1, 2,
   '**[2] 是……的 (shì...de) \u2014 emphasizing time, place, manner, or agent**',
   '"是……的" is used to emphasize the time, place, manner, or person who did something. The action must be something that has already happened.\n'
   'Structure: 是 + [emphasized part] + Verb + 的\n'
   '① 他是今年3月到北京的。 (emphasizes time \u2192 He arrived in Beijing in March this year.)\n'
   '② 这本书是在外文书店买的。 (emphasizes place \u2192 I bought this book at the Foreign Language Bookstore.)\n'
   '③ 教室里的灯不是田中开的，是飞龙开的。 (emphasizes agent \u2192 It was Feilong who turned on the light, not Tanaka.)')

N(1, 3,
   '**[3] 先……然后…… (xiān...ránhòu...) \u2014 first...then...**',
   '"先" and "然后" work together to show the sequence of two events. The first clause (with 先) happens first, and the second clause (with 然后) happens after.\n'
   '① 我要先在这儿学习半年，然后在中国工作。 (I will first study here for six months, then work in China.)\n'
   '② 先吃饭，然后去看电影。 (Eat first, then go see a movie.)\n'
   '③ 你先打电话问问，然后再决定。 (Call and ask first, then decide.)')

N(1, 4,
   '**[4] 一边……一边…… (yìbiān...yìbiān...) \u2014 doing two things at the same time**',
   'Two "一边" are used together to indicate doing two actions at the same time. The verbs must be actions that the person can control.\n'
   '① 妈妈一边做饭，一边跟客人聊天儿。 (Mom chats with the guest while cooking.)\n'
   '② 飞龙一边弹吉他，一边唱歌。 (Feilong sings while playing the guitar.)\n'
   '③ 不要一边走路一边看手机。 (Dont look at your phone while walking.)\n'
   'NB: The verbs must be voluntary actions. It would be wrong to say "他一边受表扬，一边脸红了" since receiving praise and blushing are not both voluntary.')

N(1, 5,
   '**[5] 一……也/都+不/没…… \u2014 emphasizing total negation**',
   'This structure is used to emphasize a strong negation. "一" is followed by a measure word (with or without a noun). "也" or "都" can be used before "不" or "没".\n'
   '① 马克来中国以前没学过汉语，一个汉字也/都不认识。 (Mark had never studied Chinese before coming to China \u2014 he didnt know a single character.)\n'
   '② 我一口也没吃。 (I didnt eat even one bite.)\n'
   '③ 教室里一个人都没有。 (There isnt a single person in the classroom.)\n'
   'Optionally, "连" can be placed before "一" for extra emphasis.')

N(1, 6,
   '**[6] 为了 (wèile) \u2014 in order to; for the purpose of**',
   '"为了" is usually placed at the beginning of the first clause to indicate a purpose or goal. The second clause explains the action taken to achieve that goal.\n'
   '① 为了让女儿专心工作，老人每天去女儿家里帮助做家务。 (In order to let his daughter focus on work, the old man goes to her home every day to help with housework.)\n'
   '② 为了学好汉语，她每天练习两个小时。 (In order to learn Chinese well, she practices for two hours every day.)\n'
   'Sometimes the action is stated first, followed by "是为了": 他每天跑步，是为了身体健康。 (He runs every day in order to be healthy.)')

# --- L2 ---
N(2, 1,
   '**[1] 又……又…… (yòu...yòu...) \u2014 both...and...**',
   '"又……又……" connects two adjectives or verbs to indicate that two qualities or actions exist at the same time.\n'
   '① 这家饭馆儿的饭菜又好吃又便宜。 (This restaurants food is both tasty and cheap.)\n'
   '② 她男朋友又高又帅。 (Her boyfriend is both tall and handsome.)\n'
   '③ 他又想学汉语，又想学日语。 (He wants to study both Chinese and Japanese.)')

N(2, 2,
   '**[2] 一……就…… (yī...jiù...) \u2014 as soon as; once...then...**',
   'The pattern "一 + Verb₁ + 就 + Verb₂" means "as soon as A happens, B happens". It indicates that the second action follows the first very closely in time.\n'
   '① 我一看汉语菜单就头疼。 (My head hurts as soon as I look at a Chinese menu.)\n'
   '② 他一回家就打开电视。 (He turns on the TV as soon as he gets home.)\n'
   '③ 她一说汉语就脸红。 (She blushes as soon as she speaks Chinese.)')

N(2, 3,
   '**[3] 挺 + Adj (tǐng) \u2014 quite; pretty; rather**',
   '"挺" is an adverb meaning "quite", "pretty", or "rather". It is similar to "很" but is more colloquial and softer in tone. "挺 + Adj" is often followed by "的" at the end of the sentence.\n'
   '① 挺好吃的。 (Its pretty tasty.)\n'
   '② 这个电影挺有意思的。 (This movie is quite interesting.)\n'
   '③ 今天挺冷的，多穿一点儿吧。 (Its pretty cold today \u2014 wear more clothes.)')

N(2, 4,
   '**[4] Verb + 得了/不了 (de liǎo/bù liǎo) \u2014 able/unable to**',
   '"得了" and "不了" are placed after a verb to indicate whether something can or cannot be done. "得了" = can/able to, "不了" = cannot/unable to.\n'
   'Possible meanings:\n'
   '(1) Able to finish/manage: 这么多菜，我一个人吃不了。 (So many dishes \u2014 I cant eat them all alone.)\n'
   '(2) Can/cannot due to circumstances: 明天我有事，去不了了。 (I have something to do tomorrow \u2014 I cant go.)\n'
   '① 这些生词我记住了。 (I memorized these new words.) [result complement]\n'
   '② 这些生词太多，我记不住。 (Too many new words \u2014 I cant memorize them.) [potential complement]')

N(2, 5,
   '**[5] 越……越…… (yuè...yuè...) \u2014 the more...the more...**',
   '"越……越……" indicates that as the degree of the first action/state increases, the degree of the second also increases accordingly.\n'
   '① 我觉得汉语越学越有意思。 (The more I study Chinese, the more interesting it becomes.)\n'
   '② 雨越下越大。 (The rain is getting heavier and heavier.)\n'
   '③ 她越跑越快。 (She runs faster and faster.)')

N(2, 6,
   '**[6] 就是 (jiùshì) \u2014 concessive "but"; the only problem is...**',
   '"就是" can introduce a concession or a minor drawback. It is similar to "but" or "the only problem is...". It usually follows a positive statement.\n'
   '① 这件衣服很好看，就是有一点点贵。 (This clothing looks great \u2014 the only problem is its a bit expensive.)\n'
   '② 这个手机不错，就是电池不太好。 (This phone is nice \u2014 its just that the battery isnt great.)\n'
   '③ 他很聪明，就是不太努力。 (Hes very smart \u2014 the only thing is he doesnt work hard enough.)')

# --- L3 ---
N(3, 1,
   '**[1] (你)这是……? \u2014 asking what someone is doing**',
   '"(你)这是……?" is a common way to ask what someone is currently doing. It often carries a tone of curiosity or friendly inquiry.\n'
   '① 你这是去哪儿？ (Where are you going?)\n'
   '② 你这是干什么？ (What are you doing?)\n'
   '③ 你这是怎么了？ (Whats wrong with you? / What happened?)')

N(3, 2,
   '**[2] 原来……怪不得…… (yuánlái...guàibude...) \u2014 now I understand why...**',
   'This pair expresses a sudden realization. "原来" introduces the reason, and "怪不得" introduces the situation that now makes sense. The speaker finally understands something that was puzzling before.\n'
   '① 原来是这样，怪不得这几天我经常看见你在校园里转。 (So thats it \u2014 no wonder Ive been seeing you around campus these days.)\n'
   '② 原来他病了，怪不得没来上课。 (So he was sick \u2014 no wonder he didnt come to class.)\n'
   '③ 原来她是中国人，怪不得汉语说得这么好。 (So shes Chinese \u2014 no wonder she speaks Chinese so well.)')

N(3, 3,
   '**[3] 什么 (shénme) \u2014 "whatever" meaning (not a question)**',
   '"什么" can be used not as a question word, but to mean "whatever" or "any". In this usage, it is usually followed by "都" or "也" for emphasis.\n'
   '① "什么" here doesnt ask what there is \u2014 it means "whatever you need, the campus has it".\n'
   '② 他什么都吃。 (He eats everything.)\n'
   '③ 我什么都不知道。 (I dont know anything.)\n'
   '④ 今天他去商店了，可是什么都没买。 (He went to the store today but didnt buy anything.)\n'
   'Other question words like "谁", "哪儿" can be used in the same pattern.')

N(3, 4,
   '**[4] 这么 + Adj \u2014 to such a degree; so...**',
   '"这么" (or "那么") can be placed before an adjective or auxiliary verb to indicate a high degree. It adds vividness and often carries a slight sense of surprise or exaggeration.\n'
   '① 想不到你已经这么熟悉了！ (I didnt expect you to be THIS familiar already!)\n'
   '② 想不到北京的夏天这么热！ (I never expected Beijings summer to be THIS hot!)\n'
   '③ 生词这么多，今天学不完了。 (There are so many new words \u2014 we cant finish learning them today.)')

N(3, 5,
   '**[5] 不但……而且…… (búdàn...érqiě...) \u2014 not only...but also...**',
   'In the pattern "不但……而且……", the clause after "而且" adds further information that goes beyond the first clause or provides additional details. When the subject is the same, it goes BEFORE "不但".\n'
   '① 里边不但有吃的、喝的，而且有穿的、用的，东西很全。 (Not only are there things to eat and drink, but also clothes and daily necessities \u2014 its very complete.)\n'
   '② 她不但喜欢唱歌，而且唱得很好。 (She not only likes singing, but also sings well.)\n'
   '③ 我不但去过故宫，而且去过三次。 (Ive not only been to the Forbidden City, but Ive been three times.)')

N(3, 6,
   '**[6] 为的是 (wèi de shì) \u2014 the purpose is to; in order to**',
   '"为的是" works the same as "是为了" to indicate the purpose or aim of doing something. It is placed after stating the action, explaining why it was done.\n'
   '① 他们努力学习，为的是以后能找到一个好工作。 (They study hard in order to find a good job in the future.)\n'
   '② 大家现在努力工作，为的是以后生活得更好。 (Everyone works hard now so that life will be better in the future.)\n'
   '③ 麦克努力工作，为的是挣更多的钱买房、买车。 (Mike works hard to earn more money to buy a house and a car.)')

# --- L4 ---
N(4, 1,
   '**[1] 才 (cái) \u2014 indicating a small quantity**',
   '"才" is an adverb that indicates a small amount. When used before a verb + quantity, it means "only" or "merely", suggesting the speaker thinks the quantity is less than expected.\n'
   '① 他一天才吃了两顿饭。 (He only ate two meals in a whole day \u2014 thats very little.)\n'
   '② 我才学了三个月汉语。 (Ive only studied Chinese for three months.)\n'
   '③ 这个房间才十平方米。 (This room is only ten square meters.)')

N(4, 2,
   '**[2] 偏偏 (piānpiān) \u2014 contrary to expectations**',
   '"偏偏" is an adverb indicating that something happens contrary to ones wishes or expectations. It often conveys disappointment or frustration.\n'
   '① 下午我学习的时候，他偏偏要睡觉！ (In the afternoon when Im studying, he just has to sleep!)\n'
   '② 好不容易到周末了，偏偏下起雨来。 (I finally made it to the weekend, and of course it had to rain.)\n'
   '③ 大家都同意了，他偏偏反对。 (Everyone agreed, but he just had to oppose it.)')

N(4, 3,
   '**[3] 既……也/又…… (jì...yě/yòu...) \u2014 both...and...; neither...nor...**',
   '"既……也/又……" connects two verbs or adjectives to indicate that two qualities or situations exist simultaneously. Use "也" for a milder tone and "又" for a stronger one.\n'
   '① 她既没说同意，也没说不同意。 (She neither agreed nor disagreed.)\n'
   '② 他既聪明又努力。 (He is both smart and hardworking.)\n'
   '③ 这件衣服既便宜又好看。 (This piece of clothing is both cheap and nice-looking.)')

N(4, 4,
   '**[4] 能 (néng) vs. 会 (huì) \u2014 expressing ability**',
   '"能" means "can" \u2014 having the ability, condition, or permission to do something. "会" means "know how to" \u2014 a skill learned through practice.\n'
   '① 我会说汉语。 (I can speak Chinese \u2014 I know how to.)\n'
   '② 我不能去，明天有事。 (I cant go \u2014 I have something to do tomorrow.)\n'
   '③ 学了汉字才能看书。 (Only after learning characters can one read books.) [能 = objective possibility]')

N(4, 5,
   '**[5] 怎么 + Verb + 得/不 + Complement \u2014 rhetorical "how can"**',
   '"怎么" in this structure is a rhetorical question meaning "how can/how could". It implies the speaker believes something is impossible or unreasonable.\n'
   '① 天天睡不好，怎么能有精神？ (If you cant sleep well every day, how can you have energy?)\n'
   '② 不练习，怎么能学好汉语？ (If you dont practice, how can you learn Chinese well?)\n'
   '③ 这么贵的手机，我怎么买得起？ (Such an expensive phone \u2014 how could I afford it?)')

N(4, 6,
   '**[6] 不是……吗？(bú shì...ma) \u2014 rhetorical question**',
   '"不是……吗？" is a rhetorical question pattern. The speaker uses it to point out something obvious, expecting agreement. It translates to "Isnt it...?" or "Dont you...?"\n'
   '① 咱们的宿舍楼不是临街吗？ (Isnt our dormitory building facing the street? \u2014 It obviously is.)\n'
   '② 你不是中国人吗？怎么不会用筷子？ (Arent you Chinese? How come you cant use chopsticks?)\n'
   '③ 你不是说过要来吗？ (Didnt you say you would come?)')

N(4, 7,
   '**[7] 或者……或者…… (huòzhě...huòzhě...) \u2014 either...or...**',
   '"或者……或者……" presents two or more alternatives in declarative sentences. For questions, use "还是" instead.\n'
   '① 你或者想办法换个房间，或者快点儿习惯新环境。 (Either find a way to change rooms, or quickly get used to the new environment.)\n'
   '② 周末我或者看书，或者看电影。 (On weekends I either read or watch a movie.)\n'
   '③ 你或者坐地铁去，或者打车去。 (You can either take the subway or take a taxi.)')

N(4, 8,
   '**[8] 再说吧 (zàishuō ba) \u2014 lets talk about it later**',
   '"再说吧" means not wanting to discuss or decide something now, but to deal with it later when the time is right. "再" means "later/further", "说" means "discuss".\n'
   '① 今天太晚了，明天再说吧。 (Its too late today. Lets talk about it tomorrow.)\n'
   '② A: 你打算什么时候结婚？ B: 以后再说吧。 (A: When do you plan to get married? B: Well see later.)\n'
   '③ 你先找工作，其他的事以后再说。 (Find a job first; well worry about other things later.)')

# --- L5 ---
N(5, 1,
   '**[1] 差不多 (chàbuduō) \u2014 almost; nearly; about the same**',
   '"差不多" means "almost", "nearly", or "about the same". It indicates a small difference between two things \u2014 they are close but not exactly the same. It can also be used before quantities.\n'
   '① 咱们俩差不多高。 (The two of us are about the same height.)\n'
   '② 这两个餐厅的价格差不多。 (The prices at these two restaurants are about the same.)\n'
   '③ 教室里坐了差不多20人。 (There are almost 20 people sitting in the classroom.)')

N(5, 2,
   '**[2] 比 (bǐ) \u2014 comparative structure**',
   'The preposition "比" is used to make comparisons: A + 比 + B + Adjective + (Difference). The "Difference" can be a quantity or words like "得多", "多了", "一点儿".\n'
   '① 香山比天坛近一些。 (Fragrant Hills is a bit closer than the Temple of Heaven.)\n'
   '② 他比我高得多。 (He is much taller than me.)\n'
   '③ 今天比昨天冷多了。 (Today is much colder than yesterday.)')

N(5, 3,
   '**[3] 腻 (nì) \u2014 to be tired of; fed up with**',
   '"腻" describes the feeling of being tired of something because you have done it too many times or had too much of it. Commonly used for food, activities, or entertainment.\n'
   '① 天天吃方便面，我都吃腻了。 (Eating instant noodles every day \u2014 Im sick of them.)\n'
   '② 这首歌我听了好多遍，都听腻了。 (Ive listened to this song so many times \u2014 Im tired of it.)\n'
   '③ 同一个电影看三遍，你不腻吗？ (Watching the same movie three times \u2014 dont you get tired of it?)')

N(5, 4,
   '**[4] 要是 (yàoshì) \u2014 if; in case (hypothetical)**',
   '"要是" is a conjunction used in the first clause to introduce a hypothesis. "就", "那", or "那么" often appears in the second clause to introduce the result.\n'
   '① 明天要是下雨，我们就不去了。 (If it rains tomorrow, we wont go.)\n'
   '② 要是你不来，那我也不去了。 (If youre not coming, then Im not going either.)\n'
   '③ 要是你有时间，我们就一起去。 (If you have time, lets go together.)')

N(5, 5,
   '**[5] 千万 (qiānwàn) \u2014 must; be sure to; by all means**',
   '"千万" expresses "must" or "be sure to". It is used when urging someone earnestly or expressing a strong wish. Usually followed by "要" or a negative expression.\n'
   '① 明天的晚会你千万要来呀。 (You absolutely must come to tomorrows party.)\n'
   '② 你千万别忘了带护照。 (Dont forget to bring your passport \u2014 whatever you do!)\n'
   '③ 千万别告诉他这个消息。 (Be sure NOT to tell him this news.)')

N(5, 6,
   '**[6] 因为……所以…… (yīnwèi...suǒyǐ...) \u2014 because...therefore...**',
   'The most common structure for expressing cause and effect. "因为" introduces the reason, and "所以" introduces the result.\n'
   '① 那是因为故宫在市区，沿途都是热闹的地方，所以很容易堵车。 (Thats because the Forbidden City is downtown and the route is full of busy areas, so traffic jams are common.)\n'
   '② 因为下雨，所以比赛取消了。 (Because it rained, the match was cancelled.)\n'
   '③ 因为他很努力，所以进步很快。 (Because he works hard, hes improving quickly.)')

N(5, 7,
   '**[7] 再说 (zàishuō) \u2014 moreover; besides; furthermore**',
   '"再说" (as a conjunction) is used in spoken Chinese to give a further reason or add new supporting arguments. It usually appears at the beginning of the second sentence.\n'
   '① 再说，飞龙骑车的技术不高，他不敢骑车去。 (Besides, Feilongs cycling skills arent good \u2014 he doesnt dare to ride there.)\n'
   '② 这本书没什么意思，再说你已经有一本差不多的书了，别买了。 (This book isnt interesting \u2014 besides, you already have a similar one. Dont buy it.)\n'
   '③ 我们是好朋友，不用客气。再说，互相帮忙是应该的。 (Were good friends \u2014 no need to be polite. Besides, helping each other is only right.)')

N(5, 8,
   '**[8] 再 + 说 (zài + shuō) \u2014 to talk about it later**',
   '"再 + 说" literally means "to talk (about it) later". One doesnt want to do or decide something now, but will do so when the right time comes.\n'
   '① 先找工作吧，其他的事以后再说。 (Find a job first \u2014 well talk about other things later.)\n'
   '② 今天太晚了，明天再说吧。 (Its too late today. Lets talk about it tomorrow.)\n'
   '③ 你先找地方住下，工作的事过几天再说。 (Find a place to stay first \u2014 well talk about work in a few days.)\n'
   'NB: Note the difference from "再说" (conjunction, meaning "besides/moreover") vs. "再+说" (adverb+verb, meaning "talk about later").')

# --- L6 ---
N(6, 1,
   '**[1] 早 (zǎo) \u2014 already; a long time ago**',
   '"早" placed before a verb emphasizes that the action happened a long time ago or much earlier than expected. "了" often appears at the end of the sentence.\n'
   '① 他早走了。 (He left a long time ago.)\n'
   '② 我早就知道了。 (Ive known for a long time.)\n'
   '③ 你早说呀！ (Why didnt you say so earlier!)')

N(6, 2,
   '**[2] Verb + 什么 + Noun + 呀 \u2014 rhetorical rejection**',
   'This structure is a rhetorical way of saying the action is unnecessary. It implies "There is no need to...!" Commonly used in spoken Chinese to politely decline.\n'
   '① 带什么礼物呀！ (You dont need to bring any gifts!)\n'
   '② 客气什么呀！ (No need to be polite!)\n'
   '③ 谢什么呀，这是应该的。 (No need to thank me \u2014 its my pleasure.)')

N(6, 3,
   '**[3] 该 (gāi) \u2014 should; ought to; its time to**',
   '"该" as an auxiliary verb means "should" or "its time to (do something)". It can also indicate something is likely to happen under normal circumstances.\n'
   '① 该做饭了。 (Its time to cook.)\n'
   '② 都八点了，该上课了。 (Its already 8 oclock \u2014 time for class.)\n'
   '③ 你该休息一下。 (You should take a rest.)')

N(6, 4,
   '**[4] 如果 (rúguǒ) \u2014 if (formal)**',
   '"如果" is similar to "要是" in meaning (both mean "if"), but "如果" is more formal and often used in writing. "那么", "就" etc. often appear in the second clause.\n'
   '① 如果明天下雨，我们就不去了。 (If it rains tomorrow, we wont go.)\n'
   '② 如果你有时间，那我们就一起去吧。 (If you have time, then lets go together.)\n'
   '③ 如果遇到问题，就给老师打电话。 (If you run into problems, call the teacher.)')

N(6, 5,
   '**[5] 其实 (qíshí) \u2014 actually; in fact; as a matter of fact**',
   '"其实" is used to introduce the real situation, often correcting a misunderstanding or revealing something unexpected.\n'
   '① 其实，去中国人家里做客，带什么礼物都可以。 (Actually, when visiting a Chinese home, any gift is fine.)\n'
   '② 其实他不想去，只是不好意思说。 (Actually, he doesnt want to go \u2014 hes just too embarrassed to say it.)\n'
   '③ 你以为很难？其实很容易。 (You think its hard? Actually, its very easy.)')

N(6, 6,
   '**[6] 什么 (shénme) \u2014 indefinite reference ("some" or "any")**',
   '"什么" can be used before a noun to refer to something indefinite or unspecific. It translates to "some sort of" or "any". It can sometimes be omitted without changing the meaning.\n'
   '① 买点儿什么水果吧。 (Buy some fruit or other.)\n'
   '② 他好像有什么心事。 (He seems to have something on his mind.)\n'
   '③ 我饿了，想吃点儿什么。 (Im hungry \u2014 I want to eat something.)')

# --- L7 ---
N(7, 1,
   '**[1] 好 (hǎo) \u2014 as a result complement**',
   '"好" used as a result complement after a verb indicates that the action has been completed to a satisfactory degree \u2014 done properly, done well, or ready.\n'
   '① 做好准备再出发。 (Prepare well before setting out.)\n'
   '② 你说好了吗？ (Have you finished saying what you needed to say?)\n'
   '③ 菜做好了。 (The food is ready/cooked.)')

N(7, 2,
   '**[2] 除了……(以外) (chúle...yǐwài) \u2014 except; besides; in addition to**',
   'This preposition phrase has two meanings:\n'
   '(1) "除了A以外，B都……" means "except for A, all B..." (excluding A):\n'
   '① 除了星期天以外，我每天都去图书馆。 (I go to the library every day except Sunday.)\n'
   '(2) "除了A以外，B也/还……" means "besides A, B also..." (including A):\n'
   '② 除了故宫以外，我们还去了颐和园。 (Besides the Forbidden City, we also went to the Summer Palace.)')

N(7, 3,
   '**[3] 说实话 (shuō shíhuà) \u2014 to tell the truth; honestly**',
   '"说实话" is a common conversational phrase used at the beginning of a sentence to indicate the speaker is about to express an honest opinion.\n'
   '① 说实话，我对烤肉也很有兴趣。 (To be honest, Im also very interested in BBQ.)\n'
   '② 说实话，我不太喜欢这个电影。 (To be honest, I dont really like this movie.)\n'
   '③ 说实话，你的汉语说得很好。 (To be honest, your Chinese is very good.)')

N(7, 4,
   '**[4] Interrogative Pronouns as Referentials \u2014 哪儿/谁/什么 + 都/也**',
   'When interrogative pronouns like "哪儿", "谁", "什么" are used with "都" or "也", they take on a referential meaning: "wherever", "whoever", "whatever".\n'
   '① 哪儿 + Quantifier: 你哪儿都可以去。 (You can go anywhere you want.)\n'
   '② 第一个"哪儿"表示任何地方，第二个"哪儿"指同一个地方。去哪儿吃都可以。 (Wherever you want to eat is fine.)\n'
   '③ 他什么都吃。 (He eats everything.)')

N(7, 5,
   '**[5] Other interrogative pronouns in the same pattern**',
   'Other question words can also be used in the same referential pattern with "都/也".\n'
   '① 谁想去都可以。 (Anyone who wants to go can.)\n'
   '② 哪天都行。 (Any day is fine.)\n'
   '③ 怎么去都可以。 (However you get there is fine.)')

N(7, 6,
   '**[6] 既……又…… (jì...yòu...) \u2014 both...and...**',
   '"既……又……" connects two structures of the same type to indicate two qualities or situations exist simultaneously. Stronger tone than "既……也……".\n'
   '① 这个公园既漂亮又安静。 (This park is both beautiful and quiet.)\n'
   '② 他既会说汉语，又会说英语。 (He can speak both Chinese and English.)\n'
   '③ 这件衣服既便宜又实用。 (This piece of clothing is both cheap and practical.)')

N(7, 7,
   '**[7] 既……也…… (jì...yě...) \u2014 both...and... (lighter tone)**',
   '"既……也……" is similar to "既……又……" but has a milder tone. "也" introduces supplementary or further explanation.\n'
   '① 他既有经验，也有能力。 (He has both experience and ability.)\n'
   '② 这里交通既方便，环境也好。 (Transportation here is convenient, and the environment is also good.)')

N(7, 8,
   '**[8] 等……就…… (děng...jiù...) \u2014 once...then...**',
   '"等……就……" means "once something happens, then something else will happen". Used for future events. "等" is similar to "when" or "once".\n'
   '① 等你去了，你就知道了。 (Once you go, you will understand.)\n'
   '② 等我有钱了，我就去旅行。 (When I have money, I will travel.)\n'
   '③ 等他来了，我们就开始。 (Once he arrives, we will start.)')

# --- L8 ---
N(8, 1,
   '**[1] 急着 (jí zhe) \u2014 anxiously; in a hurry to**',
   '"急着 + Verb" means to be in a hurry to do something urgently. The verb after "急着" indicates what the person is anxious to do.\n'
   '① 早上我急着去教室，忘了带钥匙。 (I was in a hurry to get to the classroom this morning and forgot my keys.)\n'
   '② 我急着要出去，没时间跟你聊天。 (Im in a rush to go out \u2014 no time to chat.)\n'
   '③ 他一进门就急着问："你看见老王了吗？" (As soon as he came in, he anxiously asked: "Have you seen Old Wang?")\n'
   'NB: Compare with "笑着回答" (answer while smiling) and "坐着上课" (sit while attending class) \u2014 these describe the state while doing something, not urgency.')

N(8, 2,
   '**[2] ……的话 (de huà) \u2014 if (colloquial)**',
   '"……的话" is a hypothetical clause marker. It can be used alone or together with "如果", "要是", "假如" before it. Common in spoken Chinese.\n'
   '① 急着穿的话，两天也行。 (If you need it urgently, two days is fine too.)\n'
   '② 你去不了的话，可以让别人去。 (If you cant go, you can send someone else.)\n'
   '③ 明天不下雨的话，我们就去长城。 (If it doesnt rain tomorrow, we will go to the Great Wall.)')

N(8, 3,
   '**[3] 特别是 (tèbié shì) \u2014 especially; particularly**',
   '"特别是" highlights the most prominent or notable item in a group. A noun or verb usually follows.\n'
   '① 我喜欢运动，特别是游泳。 (I like sports, especially swimming.)\n'
   '② 这个餐厅的菜都好吃，特别是烤鸭。 (All the dishes at this restaurant are delicious, especially the roast duck.)\n'
   '③ 她喜欢小动物，特别是小猫。 (She likes small animals, especially kittens.)')

N(8, 4,
   '**[4] 稍微 (shāowēi) \u2014 slightly; a little; briefly**',
   '"稍微" means "a little bit" or "slightly", indicating a small degree or quantity.\n'
   '(1) 稍微 + Verb (verb often reduplicated, or with "一", or followed by "一会儿/一些/一下"):\n'
   '① 老师马上就来，你们稍微等一等。 (The teacher will be here soon \u2014 wait a moment.)\n'
   '② 这个问题你稍微想一想就能回答。 (Think about this question a bit and you will be able to answer it.)\n'
   '(2) 稍微 + Adj/Verb + 一点儿/一些:\n'
   '③ 请稍微大声一点儿。 (Please speak a bit louder.)')

N(8, 5,
   '**[5] 趟 (tàng) \u2014 measure word for round trips**',
   '"趟" is a verbal measure word used for one complete round trip \u2014 going somewhere and coming back. Together with a numeral, it functions as a complement of frequency.\n'
   '① 我出去一趟。 (Im going out for a bit.)\n'
   '② 我去过北京两趟。 (Ive been to Beijing twice \u2014 round trips.)\n'
   '③ 他昨天跑了三趟银行。 (He went to the bank three times yesterday.)')

N(8, 6,
   '**[6] Adj + 多了 \u2014 much more (showing big difference)**',
   '"Adjective + 多了" means the difference is big. It expresses a change or comparison. The object of comparison is often stated, but if not, it is implied by context.\n'
   '① 老百姓的生活的确方便多了。 (Peoples lives are indeed much more convenient.)\n'
   '② 这孩子比以前胖多了。 (This child is much chubbier than before.)\n'
   '③ 跟大商场比，有的东西在网上买便宜多了。 (Compared to big shopping malls, some things are much cheaper online.)')

N(8, 7,
   '**[7] 拿……来说 (ná...lái shuō) \u2014 take...for example**',
   '"拿……来说" is a common way to give an example. A noun, noun phrase, or verb phrase can be placed between "拿" and "来说".\n'
   '① 就拿吃饭来说吧，现在比以前方便多了。 (Take eating for example \u2014 it is much more convenient now than before.)\n'
   '② 我们班每个人都有自己的爱好，拿李钟文来说吧，他是个电脑迷。 (Everyone in our class has their own hobbies. Take Li Zhongwen \u2014 he is a computer fanatic.)\n'
   '③ 不同地方的人有不同的口味，拿四川菜来说，特点是辣。 (People from different places have different tastes. Take Sichuan food \u2014 its characteristic is spiciness.)')

# --- L9 ---
N(9, 1,
   '**[1] 要不 (yàobù) \u2014 otherwise; how about**',
   '"要不" has two main uses:\n'
   '(1) Meaning "otherwise" \u2014 expressing what would happen if something were not done:\n'
   '① 这么晚了，赶快回家吧，要不家里会不放心的。 (Its late \u2014 hurry home, otherwise your family will worry.)\n'
   '② 赶快走，要不就赶不上火车了。 (Hurry up, or you will miss the train.)\n'
   '(2) Making a suggestion \u2014 "how about...":\n'
   '③ 要不这样吧，我正好要买电脑，我陪你去一趟。 (How about this \u2014 I happen to need to buy a computer, I will go with you.)\n'
   '④ 要不咱们坐出租车去吧，打车快一点儿。 (How about we take a taxi \u2014 it is faster.)')

N(9, 2,
   '**[2] 正好 (zhènghǎo) \u2014 just right; just in time; happen to**',
   '"正好" means "just right", "happen to", or "coincidentally". It describes a perfect fit in time, quantity, or circumstance.\n'
   '① 我正好要买电脑，我陪你去一趟。 (I happen to need to buy a computer \u2014 I will go with you.)\n'
   '② 这件衣服大小正好。 (This piece of clothing is just the right size.)\n'
   '③ 你来得正好，我们正找你呢。 (You have come just in time \u2014 we were looking for you.)')

N(9, 3,
   '**[3] 多 (duō) \u2014 indicating an approximate number**',
   '"多" is placed after numerals or measure words to indicate an approximate number. The position of "多" depends on the number structure.\n'
   '① 他只想要个一千多的。 (He only wants one that is a bit over 1,000 RMB.)\n'
   '② 教室里有二十多个学生。 (There are more than 20 students in the classroom.)\n'
   '③ 他等了三个多小时。 (He waited for over three hours.)')

N(9, 4,
   '**[4] 听说 (tīngshuō) \u2014 I have heard that; someone told me**',
   '"听说" literally means "hear-speak" \u2014 it introduces information obtained from others. The source may be specific or unknown. Functions like "I hear that..." or "apparently...".\n'
   '① 听说附近新开了个批发市场。 (I hear there is a new wholesale market opened nearby.)\n'
   '② 听说你要去中国留学，真的吗？ (I heard you are going to study in China \u2014 is it true?)\n'
   '③ 听说这部电影很好看。 (I have heard this movie is very good.)')

N(9, 5,
   '**[5] 真不用……了 (zhēn búyòng...le) \u2014 truly no need to**',
   '"真不用……了" means "truly there is no need to...". It is used to politely persuade someone that an action is unnecessary.\n'
   '① 你真不用去了，那儿我去过。 (You really dont need to go \u2014 I have been there.)\n'
   '② 你真不用客气。 (You really dont need to be so polite.)\n'
   '③ 这真不用谢，举手之劳。 (There is really no need to thank me \u2014 it was nothing.)')

N(9, 6,
   '**[6] 不如 (bùrú) \u2014 not as good as; had better**',
   '"不如" compares two things and indicates the latter is better. "A不如B + Adjective" means "A is not as (adjective) as B". It can also suggest "it would be better to...".\n'
   '① 东西真不如大商场的好。 (The things there really arent as good as those in big shopping malls.)\n'
   '② 他的汉语不如你好。 (His Chinese is not as good as yours.)\n'
   '③ 与其坐公交车，不如打车去。 (Rather than taking the bus, it is better to take a taxi.)')

# --- L10 ---
N(10, 1,
   '**[1] 怎么 + Verb + 都 + (不/没) \u2014 no matter how**',
   '"怎么 + Verb + 都 + 不/没..." means "no matter how one tries, the result doesnt change". Expresses frustration that despite all efforts, something cant be achieved.\n'
   '① 可像我这样的人怎么减肥都没用。 (But for someone like me, no matter how I try to lose weight, it doesnt work.)\n'
   '② 他怎么学都学不会。 (No matter how hard he studies, he cant learn it.)\n'
   '③ 这东西怎么修都修不好。 (No matter how you fix it, this thing just wont work.)')

N(10, 2,
   '**[2] 谁/哪儿/什么/怎么 + 也/都 \u2014 universal reference**',
   'An emphatic structure meaning "(no matter) who/where/what/how". The question word + "也/都" covers all possibilities.\n'
   '① 谁也不知道。 (Nobody knows.)\n'
   '② 我哪儿都不想去。 (I dont want to go anywhere.)\n'
   '③ 他什么都能吃。 (He can eat anything.)\n'
   '④ 怎么劝都没用。 (No matter how you persuade him, its useless.)')

N(10, 3,
   '**[3] 太 + Adj + 了 (tài...le) \u2014 too; extremely**',
   '"太 + Adjective + 了" means "too (adjective)", "extremely (adjective)", or "(adjective) to excess". Can be positive or negative depending on the adjective.\n'
   '① 你说得太绝对了吧？ (What you said is too absolute, isnt it?)\n'
   '② 太好了！ (Great! / Wonderful!)\n'
   '③ 太多了，吃不了。 (Too much \u2014 I cant eat it all.)')

N(10, 4,
   '**[4] 一天比一天 (yì tiān bǐ yì tiān) \u2014 day by day**',
   '"一天比一天" means "day by day" or "more and more each day". Describes a progressive increase or decrease over time.\n'
   '① 那你说为什么现在的胖子一天比一天多？ (Then tell me, why are there more and more fat people every day?)\n'
   '② 天气一天比一天暖和了。 (The weather is getting warmer day by day.)\n'
   '③ 他的汉语一天比一天进步。 (His Chinese is improving day by day.)')

N(10, 5,
   '**[5] 既然 (jìrán) \u2014 since; now that**',
   '"既然" introduces a reason/fact that is already established. The second clause explains the logical conclusion. "就" is often used in the second clause.\n'
   '① 既然吃药也没用，那就算了。 (Since taking medicine doesnt work either, lets just forget it.)\n'
   '② 既然你已经决定了，我就不劝你了。 (Since you have already decided, I wont try to persuade you.)\n'
   '③ 既然大家都来了，我们就开始吧。 (Since everyones here, lets start.)')

N(10, 6,
   '**[6] 万一 (wànyī) \u2014 just in case; in the event that**',
   '"万一" introduces an unlikely but possible situation \u2014 something one hopes wont happen but prepares for just in case. Often used when warning or being cautious.\n'
   '① 万一让我爱人知道了，就麻烦了。 (If my spouse finds out, it will be trouble.)\n'
   '② 带上伞吧，万一下雨呢。 (Bring an umbrella, just in case it rains.)\n'
   '③ 万一他不同意，我们怎么办？ (What if he doesnt agree? What should we do?)')

N(10, 7,
   '**[7] 一 + Verb + 就是 + Quantity/Time \u2014 once started, it lasts for...**',
   'This structure indicates that the action, once started, lasts for a surprisingly long time or involves a large quantity.\n'
   '① 一玩儿就是好几个小时。 (Once he starts playing, it is for several hours straight.)\n'
   '② 一睡就是半天。 (Once he falls asleep, it is for half a day.)\n'
   '③ 一买就是一大堆。 (Once he starts buying, it is a whole pile of stuff.)')

# --- L11 ---
N(11, 1,
   '**[1] 够 + Adj + 的/了 (gòu) \u2014 quite; very; enough to be**',
   '"够" is used before adjectives, often followed by "的", "了", or "的了". It means "quite", "very", or "reaching a certain degree".\n'
   '① 这双鞋够大的。 (These shoes are quite big.)\n'
   '② 已经够便宜的了，别讲价了。 (It is already cheap enough \u2014 dont bargain.)\n'
   '③ 我够累了，想休息一下。 (Im quite tired \u2014 I want to rest.)')

N(11, 2,
   '**[2] A是A (A shì A) \u2014 concession (A is A, but...)**',
   '"A是A" indicates concession. It admits something is true, then introduces a contrasting point with "可是", "不过", or "就是".\n'
   '① 好是好，不过够贵的。 (Good is good, but it is quite expensive.)\n'
   '② 他胖是胖，可是动作挺灵活。 (Hes chubby, but his movements are quite agile.)\n'
   '③ 这个手机好是好，就是太贵了。 (This phone is nice and all, but it is too expensive.)')

N(11, 3,
   '**[3] 最好 (zuìhǎo) \u2014 had better; it is best to**',
   '"最好" is an idiomatic expression meaning "it is best to" or "had better". It indicates the most ideal choice or suggestion.\n'
   '① 你最好多练习口语。 (You had better practice speaking more.)\n'
   '② 现在老师快下班了，你最好明天去。 (The teacher is about to leave \u2014 you had better go tomorrow.)\n'
   '③ 买东西最好比一比价格。 (When shopping, it is best to compare prices.)\n'
   'NB: In "我们班玛丽的口语最好", "最好" is the superlative of "好" (the best), which is different from the idiomatic "最好" meaning "had better".')

N(11, 4,
   '**[4] ……什么的 (shénme de) \u2014 ...and so on**',
   '"……什么的" is used in enumerations. Before "什么的", there can be one or more items. It means "etc." or "and so on". Common in spoken Chinese.\n'
   '① 牌子、包装什么的，差不多就可以。 (Brand, packaging, and so on \u2014 just good enough is fine.)\n'
   '② 她的书包里装满了口红、粉饼、眉笔什么的。 (Her bag is full of lipstick, powder, eyebrow pencils, and such.)\n'
   '③ 周末我喜欢看看书、听听音乐什么的。 (On weekends I like to read, listen to music, and so on.)')

N(11, 5,
   '**[5] ……吧，……吧，…… \u2014 listing options with hesitation**',
   'In this pattern, "吧" at the end of each clause presents an option, followed by a reason against it. The overall feeling is "hesitation" or "cant decide".\n'
   '① 相信自己吧，自己不可能什么都是行家；相信广告吧，那么多广告又不知道应该相信哪一个；相信商店、售货员吧，他们在你买以前态度都挺好，等你买完以后就不一定了。 (If I trust myself... but I cant be an expert at everything. If I trust ads... but there are so many. If I trust the shop assistants... they are friendly before I buy.)\n'
   '② 去吧，没时间；不去吧，又可惜。 (If I go... I dont have time. If I dont go... it would be a waste.)')

N(11, 6,
   '**[6] 只要……就…… (zhǐyào...jiù...) \u2014 as long as...then...**',
   '"只要……就……" is used in conditional sentences. "只要" introduces a sufficient condition, and "就" introduces the result. Means "as long as X, then Y".\n'
   '① 只要差不多，就觉得行了。 (As long as it is roughly okay, they think it is fine.)\n'
   '② 只要努力，就一定能成功。 (As long as you work hard, you will definitely succeed.)\n'
   '③ 只要不下雨，我们就去。 (As long as it doesnt rain, we will go.)')

N(11, 7,
   '**[7] 因此 (yīncǐ) \u2014 therefore; consequently**',
   '"因此" introduces a result or conclusion. The preceding sentence may use "由于" to indicate the reason. "因此" can be placed before or after the subject.\n'
   '① 我跟他在一起很多年了，因此非常了解他。 (I have been with him for many years, so I know him very well.)\n'
   '② 雪融化时吸收热量，气温因此会下降。 (When snow melts, it absorbs heat, so the temperature drops.)\n'
   '③ 由于我们做了充分的准备，因此这次旅行很顺利。 (Because we made full preparations, this trip went very smoothly.)')

# --- L12 ---
N(12, 1,
   '**[1] 以为 (yǐwéi) \u2014 to have thought (mistakenly)**',
   '"以为" indicates someone made a judgment or assumption, but later found out it was wrong. Different from "认为" (to think/believe), which doesnt imply the judgment is wrong.\n'
   '① 我以为他走了，原来他还在。 (I thought he had left, but he is still here.)\n'
   '② 我以为今天星期二呢。 (I thought today was Tuesday.)\n'
   '③ 别以为学习汉语很容易，其实挺难的。 (Dont think learning Chinese is easy \u2014 it is actually quite hard.)')

N(12, 2,
   '**[2] 这么 + Verb + 着 (zhème...zhe) \u2014 doing/thinking this way**',
   '"这么+Verb+着" indicates "doing the verb in this way" or "thinking/feeling this way". The "着" indicates a continuous state.\n'
   '① 大家都这么想来着。 (Everyone was thinking the same way.)\n'
   '② 你别这么看着我。 (Dont look at me like that.)\n'
   '③ 他一直这么想着，但没说出来。 (He kept thinking this way, but didnt say it out loud.)')

N(12, 3,
   '**[3] 说起 (shuōqǐ) \u2014 speaking of; talking about**',
   '"说起" means "to mention" or "to talk about". It introduces a topic or brings up a subject in conversation.\n'
   '① 说起他来，我常常觉得他有点儿奇怪。 (Speaking of him, I often feel he is a bit strange.)\n'
   '② 说起中国的美食，三天三夜也说不完。 (Speaking of Chinese cuisine \u2014 you could not finish talking about it in three days and nights.)\n'
   '③ 一说到旅游，他就特别兴奋。 (Whenever the topic of travel comes up, he gets very excited.)')

N(12, 4,
   '**[4] 光 (guāng) \u2014 only; merely; just**',
   '"光" is an adverb meaning "only" or "just". It limits the scope of what is being talked about. Similar to "只" but more colloquial.\n'
   '① 光听你说他的好话，他没有缺点吗？ (I only hear you say good things about him \u2014 doesnt he have any faults?)\n'
   '② 光说不做可不行。 (Just talking without doing wont work.)\n'
   '③ 光学习不休息，会累坏的。 (Only studying without rest \u2014 you will wear yourself out.)')

N(12, 5,
   '**[5] 可不是嘛 (kě bú shì ma) \u2014 exactly!; you said it!**',
   '"可不是嘛" is a colloquial expression used to strongly agree with what someone just said. Means "exactly!" or "you said it!"\n'
   '① 可不是嘛！他学习特别认真。 (You said it! He studies very seriously.)\n'
   '② 可不是嘛！今天真冷。 (Exactly! It is really cold today.)\n'
   '③ 可不是嘛！我也这么觉得。 (You said it! I think so too.)')

N(12, 6,
   '**[6] 说不定 (shuōbudìng) \u2014 maybe; perhaps; who knows**',
   '"说不定" means "maybe", "perhaps", or "you never know". It expresses uncertainty about a future possibility. Can be placed at the beginning or middle of a sentence.\n'
   '① 说不定他已经忘记了。 (Maybe he has already forgotten.)\n'
   '② 明天说不定会下雨。 (It might rain tomorrow \u2014 you never know.)\n'
   '③ 你好好儿解释，说不定她就能原谅你。 (If you explain it properly, maybe she will forgive you.)')


# ============================================================
# Application
# ============================================================

def build_note_html(note_num, title, body):
    """Build the HTML for a single note."""
    body_html = body.replace('\n', '<br>\n')
    return f'''<div class="row notes" id="n{note_num}"><div class="nt-title">{title}</div>
<div class="nt">{body_html}</div>
</div>'''


def process_lesson(num):
    """Replace all notes in a lesson HTML."""
    if num not in note_data:
        print(f'L{num}: no note data, skipping')
        return

    fp = os.path.join(BASE, f'jichushang/l{num}/index.html')
    if not os.path.exists(fp):
        print(f'L{num}: HTML not found')
        return

    html = open(fp, encoding='utf-8').read()

    notes_start = html.find('<div class="sec">&#128221; Notes</div>')
    if notes_start < 0:
        print(f'L{num}: no notes section')
        return

    notes_end = html.find('<div class="pm-overlay"', notes_start)
    if notes_end < 0:
        notes_end = html.find('<script>', notes_start)

    note_data_for_lesson = note_data[num]
    new_notes_html = '<div class="sec">&#128221; Notes</div>'
    for n_num in sorted(note_data_for_lesson.keys()):
        data = note_data_for_lesson[n_num]
        new_notes_html += build_note_html(n_num, data[0], data[1])

    new_html = html[:notes_start] + new_notes_html + html[notes_end:]

    old_count = len(re.findall(r'<div class="row notes"', html))
    new_count = len(re.findall(r'<div class="row notes"', new_html))

    if old_count != new_count:
        print(f'L{num}: WARNING! Notes count mismatch: {old_count} -> {new_count}')
        return

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f'L{num}: Updated {old_count} notes')


if __name__ == '__main__':
    for num in sorted(note_data.keys()):
        process_lesson(num)
    print('\nDone!')
