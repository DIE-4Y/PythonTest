/*
 Navicat Premium Data Transfer

 Source Server         : dontreciteenglish
 Source Server Type    : MySQL
 Source Server Version : 80400 (8.4.0)
 Source Host           : localhost:3306
 Source Schema         : dontreciteenglish

 Target Server Type    : MySQL
 Target Server Version : 80400 (8.4.0)
 File Encoding         : 65001

 Date: 05/12/2024 16:06:06
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for app01_poetry
-- ----------------------------
DROP TABLE IF EXISTS `app01_poetry`;
CREATE TABLE `app01_poetry`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `author` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `dynasty` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `content` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of app01_poetry
-- ----------------------------

-- ----------------------------
-- Table structure for app01_similar_words
-- ----------------------------
DROP TABLE IF EXISTS `app01_similar_words`;
CREATE TABLE `app01_similar_words`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `main_character` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `related_characters` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of app01_similar_words
-- ----------------------------

-- ----------------------------
-- Table structure for article
-- ----------------------------
DROP TABLE IF EXISTS `article`;
CREATE TABLE `article`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `author` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `dynasty` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `text` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 41 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of article
-- ----------------------------
INSERT INTO `article` VALUES (1, '黄金缕·妾本钱塘江上住', '司马槱', '〔宋代〕', '妾本钱塘江上住。花落花开，不管流年度。燕子衔将春色去，纱窗几阵黄梅雨。斜插犀梳云半吐，檀板轻敲，唱彻黄金缕。望断行云无觅处，梦回明月生南浦。');
INSERT INTO `article` VALUES (2, '枭将东徙', '刘向', '〔两汉〕', '枭逢鸠。鸠曰：“子将安之？”枭曰：“我将东徙。”鸠曰：“何故？”枭曰：“乡人皆恶我鸣。以故东徙。”鸠曰：“子能更鸣，可矣；不能更鸣，东徙，犹恶子之声。”');
INSERT INTO `article` VALUES (3, '左迁至蓝关示侄孙湘', '韩愈', '〔唐代〕', '一封朝奏九重天，夕贬潮州路八千。欲为圣明除弊事，肯将衰朽惜残年！(欲为一作：本为；圣明一作：圣朝；肯将一作：敢将)云横秦岭家何在？雪拥蓝关马不前。知汝远来应有意，好收吾骨瘴江边。');
INSERT INTO `article` VALUES (4, '送郑少府入辽共赋侠客远从戎', '骆宾王', '〔唐代〕', '边烽警榆塞，侠客度桑乾。柳叶开银镝，桃花照玉鞍。满月临弓影，连星入剑端。不学燕丹客，徒歌易水寒。');
INSERT INTO `article` VALUES (5, '题武关', '杜牧', '〔唐代〕', '碧溪留我武关东，一笑怀王迹自穷。郑袖娇娆酣似醉，屈原憔悴去如蓬。山樯谷堑依然在，弱吐强吞尽已空。今日圣神家四海，戍旗长卷夕阳中。');
INSERT INTO `article` VALUES (6, '殿前欢·畅幽哉', '贯云石', '〔元代〕', '畅幽哉，春风无处不楼台。一时怀抱俱无奈，总对天开。就渊明归去来，怕鹤怨山禽怪，问甚功名在？酸斋是我，我是酸斋。');
INSERT INTO `article` VALUES (7, '一叶落·泪眼注', '朱彝尊', '〔清代〕', '泪眼注，临当去，此时欲住已难住。下楼复上楼，楼头风吹雨。风吹雨，草草离人语。');
INSERT INTO `article` VALUES (8, '哀江南', '孔尚任', '〔清代〕', '　　〔哀江南〕〔北新水令〕山松野草带花挑，猛抬头秣陵重到。残军留废垒，瘦马卧空壕；村郭萧条，城对着夕阳道。　　〔驻马听〕野火频烧，护墓长楸多半焦。山羊群跑，守陵阿监几时逃。鸽翎蝠粪满堂抛，枯枝败叶当阶罩；谁祭扫，牧儿打碎龙碑帽。　　〔沈醉东风〕横白玉八根柱倒，堕红泥半堵墙高。碎琉璃瓦片多，烂翡翠窗棂少。舞丹墀燕雀常朝，直入宫门一路蒿，住几个乞儿饿殍。　　〔折桂令〕问秦淮旧日窗寮，破纸迎风，坏槛当潮，目断魂消。当年粉黛，何处笙箫？罢灯船端阳不闹，收酒旗重九无聊。白鸟飘飘，绿水滔滔，嫩黄花有些蝶飞，新红叶无个人瞧。　　〔沽美酒〕你记得跨青溪半里桥，旧红板没一条。秋水长天人过少，冷清清的落照，剩一树柳弯腰。　　〔太平令〕行到那旧院门，何用轻敲，也不怕小犬哰哰。无非是枯井颓巢，不过些砖苔砌草。手种的花条柳梢，尽意儿采樵；这黑灰是谁家厨灶？　　〔离亭宴带歇指煞〕俺曾见金陵玉殿莺啼晓，秦淮水榭花开早，谁知道容易冰消！眼看他起朱楼，眼看他宴宾客，眼看他楼塌了！这青苔碧瓦堆，俺曾睡风流觉，将五十年兴亡看饱。那乌衣巷不姓王，莫愁湖鬼夜哭，凤凰台栖枭鸟。残山梦最真，旧境丢难掉，不信这舆图换稿！诌一套《哀江南》，放悲声唱到老。');
INSERT INTO `article` VALUES (9, '悲回风', '屈原', '〔先秦〕', '悲回风之摇蕙兮，心冤结而内伤。物有微而陨性兮，声有隐而先倡。夫何彭咸之造思兮，暨志介而不忘！万变其情岂可盖兮，孰虚伪之可长？鸟兽鸣以号群兮，草苴比而不芳。鱼葺鳞以自别兮，蛟龙隐其文章。故荼荠不同亩兮，兰茝幽而独芳。惟佳人之永都兮，更统世以自贶。眇远志之所及兮，怜浮云之相羊。介眇志之所惑兮，窃赋诗之所明。惟佳人之独怀兮，折若椒以自处。曾歔欷之嗟嗟兮，独隐伏而思虑。涕泣交而凄凄兮，思不眠以至曙。终长夜之曼曼兮，掩此哀而不去。寤从容以周流兮，聊逍遥以自恃。伤太息之愍怜兮，气於邑而不可止。糺思心以为纕兮，编愁苦以为膺。折若木以弊光兮，随飘风之所仍。存彷佛而不见兮，心踊跃其若汤。抚珮衽以案志兮，超惘惘而遂行。岁曶曶其若颓兮，时亦冉冉而将至。薠蘅槁而节离兮，芳以歇而不比。怜思心之不可惩兮，证此言之不可聊。宁溘死而流亡兮，不忍此心之常愁。孤子吟而抆泪兮，放子出而不还。孰能思而不隐兮，照彭咸之所闻。登石峦以远望兮，路眇眇之默默。入景响之无应兮，闻省想而不可得。愁郁郁之无快兮，居戚戚而不可解。心鞿羁而不开兮，气缭转而自缔。穆眇眇之无垠兮，莽芒芒之无仪。声有隐而相感兮，物有纯而不可为。邈漫漫之不可量兮，缥绵绵之不可纡。愁悄悄之常悲兮，翩冥冥之不可娱。凌大波而流风兮，讬彭咸之所居。上高岩之峭岸兮，处雌蜺之标颠。据青冥而摅虹兮，遂儵忽而扪天。吸湛露之浮源兮，漱凝霜之雰雰。依风穴以自息兮，忽倾寤以婵媛。冯昆仑以澂雾兮，隐渂山以清江。惮涌湍之礚礚兮，听波声之汹汹。纷容容之无经兮，罔芒芒之无纪。轧洋洋之无从兮，驰委移之焉止？漂翻翻其上下兮，翼遥遥其左右。氾潏潏其前后兮，伴张驰之信期。观炎气之相仍兮，窥烟液之所积。悲霜雪之俱下兮，听潮水之相击。借光景以往来兮，施黄棘之枉策。求介子之所存兮，见伯夷之放迹。心调度而弗去兮，刻著志之无适。曰吾怨往昔之所冀兮，悼来者之悐悐。浮江淮而入海兮，从子胥而自适。望大河之洲渚兮，悲申徒之抗迹。骤谏君而不听兮，重任石之何益？心絓结而不解兮，思蹇产而不释。');
INSERT INTO `article` VALUES (10, '行路难·缚虎手', '贺铸', '〔宋代〕', '缚虎手，悬河口，车如鸡栖马如狗。白纶巾，扑黄尘，不知我辈可是蓬蒿人？衰兰送客咸阳道，天若有情天亦老。作雷颠，不论钱，谁问旗亭美酒斗十千？酌大斗，更为寿，青鬓长青古无有。笑嫣然，舞翩然，当垆秦女十五语如弦。遗音能记秋风曲，事去千年犹恨促。揽流光，系扶桑，争奈愁来一日却为长。');
INSERT INTO `article` VALUES (11, '感旧四首·其二', '黄景仁', '〔清代〕', '唤起窗前尚宿酲，啼鹃催去又声声。丹青旧誓相如札，禅榻经时杜牧情。别后相思空一水，重来回首已三生。云阶月地依然在，细逐空香百遍行。');
INSERT INTO `article` VALUES (12, '悼亡诗三首', '潘岳', '〔魏晋〕', '荏苒冬春谢，寒暑忽流易。之子归穷泉，重壤永幽隔。私怀谁克从，淹留亦何益。僶俛恭朝命，回心反初役。望庐思其人，入室想所历。帏屏无髣髴，翰墨有馀迹。流芳未及歇，遗挂犹在壁。怅恍如或存，回惶忡惊惕。(回惶一作：周惶)如彼翰林鸟，双栖一朝只。如彼游川鱼，比目中路析。春风缘隟来，晨霤承檐滴。寝息何时忘，沉忧日盈积。庶几有时衰，庄缶犹可击。皎皎窗中月，照我室南端。清商应秋至，溽暑随节阑。凛凛凉风升，始觉夏衾单。岂曰无重纩，谁与同岁寒。岁寒无与同，朗月何胧胧。展转盻枕席，长簟竟床空。床空委清尘，室虚来悲风。独无李氏灵，髣髴覩尔容。抚衿长叹息，不觉涕沾胸。沾胸安能已，悲怀从中起。寝兴目存形，遗音犹在耳。上惭东门吴，下愧蒙庄子。赋诗欲言志，此志难具纪。命也可奈何，长戚自令鄙。曜灵运天机，四节代迁逝。凄凄朝露凝，烈烈夕风厉。奈何悼淑俪，仪容永潜翳。念此如昨日，谁知已卒岁。改服从朝政，哀心寄私制。茵帱张故房，朔望临尔祭。尔祭讵几时，朔望忽复尽。衾裳一毁撤，千载不复引。亹亹朞月周，戚戚弥相愍。悲怀感物来，泣涕应情陨。驾言陟东阜，望坟思纡轸。徘徊墟墓间，欲去复不忍。徘徊不忍去，徙倚步踟蹰。落叶委埏侧，枯荄带坟隅。孤魂独茕茕，安知灵与无。投心遵朝命，挥涕强就车。谁谓帝宫远，路极悲有余。');
INSERT INTO `article` VALUES (13, '高山流水·次夫子清风阁落成韵', '顾太清', '〔清代〕', '群山万壑引长风，透林皋、晓日玲珑。楼外绿阴深，凭栏指点偏东。浑河水、一线如虹。清凉极，满谷幽禽啼啸，冷雾溟濛。任海天寥阔，飞跃此身中。云容。看白云苍狗，无心者、变化虚空。细草络危岩，岩花秀媚日承红。清风阁，高凌霄汉，列岫如童。待何年归去，谈笑各争雄。');
INSERT INTO `article` VALUES (14, '咏画扇诗', '鲍子卿', '〔南北朝〕', '细丝本自轻，弱彩何足眄。直为发红颜，谬成握中扇。乍奉长门泣，时承柏梁宴。思妆开已掩，歌容隐而见。但画双黄鹄，莫画孤飞燕。');
INSERT INTO `article` VALUES (15, '汉宫曲', '徐凝', '〔唐代〕', '水色帘前流玉霜，赵家飞燕侍昭阳。掌中舞罢箫声绝，三十六宫秋夜长。');
INSERT INTO `article` VALUES (16, '赠女冠畅师', '秦观', '〔宋代〕', '瞳人剪水腰如束，一幅乌纱裹寒玉。飘然自有姑射姿，回看粉黛皆尘俗。雾阁云窗人莫窥，门前车马任东西。礼罢晓坛春日静，落红满地乳鸦啼。');
INSERT INTO `article` VALUES (17, '夕次盱眙县', '韦应物', '〔唐代〕', '落帆逗淮镇，停舫临孤驿。浩浩风起波，冥冥日沉夕。人归山郭暗，雁下芦洲白。独夜忆秦关，听钟未眠客。');
INSERT INTO `article` VALUES (18, '送僧南归', '简长', '〔宋代〕', '渐老念乡国，先归独羡君。吴山全接汉，江树半藏云。振锡林烟断，添瓶涧月分。重栖上方定，孤狖雪中闻。');
INSERT INTO `article` VALUES (19, '临江仙·再用前韵送祐之弟归浮梁', '辛弃疾', '〔宋代〕', '钟鼎山林都是梦，人间宠辱休惊。只消闲处过平生。酒杯秋吸露，诗句夜裁冰。记取小窗风雨夜，对床灯火多情。问谁千里伴君行。晓山眉样翠，秋水镜般明。');
INSERT INTO `article` VALUES (20, '梅圣俞诗集序', '欧阳修', '〔宋代〕', '　　予闻世谓诗人少达而多穷，夫岂然哉？盖世所传诗者，多出于古穷人之辞也。凡士之蕴其所有，而不得施于世者，多喜自放于山巅水涯之外，见虫鱼草木风云鸟兽之状类，往往探其奇怪，内有忧思感愤之郁积，其兴于怨刺，以道羁臣寡妇之所叹，而写人情之难言。盖愈穷则愈工。然则非诗之能穷人，殆穷者而后工也。　　予友梅圣俞，少以荫补为吏，累举进士，辄抑于有司，困于州县，凡十余年。年今五十，犹从辟书，为人之佐，郁其所蓄，不得奋见于事业。其家宛陵，幼习于诗，自为童子，出语已惊其长老。既长，学乎六经仁义之说，其为文章，简古纯粹，不求苟说于世。世之人徒知其诗而已。然时无贤愚，语诗者必求之圣俞；圣俞亦自以其不得志者，乐于诗而发之，故其平生所作，于诗尤多。世既知之矣，而未有荐于上者。昔王文康公尝见而叹曰：“二百年无此作矣！”虽知之深，亦不果荐也。若使其幸得用于朝廷，作为雅、颂，以歌咏大宋之功德，荐之清庙，而追商、周、鲁颂之作者，岂不伟欤！奈何使其老不得志，而为穷者之诗，乃徒发于虫鱼物类，羁愁感叹之言。世徒喜其工，不知其穷之久而将老也！可不惜哉！　　圣俞诗既多，不自收拾。其妻之兄子谢景初，惧其多而易失也，取其自洛阳至于吴兴以来所作，次为十卷。予尝嗜圣俞诗，而患不能尽得之，遽喜谢氏之能类次也，辄序而藏之。　　其后十五年，圣俞以疾卒于京师，余既哭而铭之，因索于其家，得其遗稿千余篇，并旧所藏，掇其尤者六百七十七篇，为一十五卷。呜呼！吾于圣俞诗论之详矣，故不复云。　　庐陵欧阳修序。');
INSERT INTO `article` VALUES (21, '寿阳曲·云笼月', '马致远', '〔元代〕', '云笼月，风弄铁，两般儿助人凄切。剔银灯欲将心事写，长吁气一声吹灭。');
INSERT INTO `article` VALUES (22, '醉太平·堂堂大元', '佚名', '〔元代〕', '堂堂大元，奸佞专权。开河变钞祸根源，惹红巾万千。官法滥，刑法重，黎民怨。人吃人，钞买钞，何曾见。贼做官，官做贼，混贤愚。哀哉可怜！');
INSERT INTO `article` VALUES (23, '从军行', '卢思道', '〔南北朝〕', '朔方烽火照甘泉，长安飞将出祁连。犀渠玉剑良家子，白马金羁侠少年。平明偃月屯右地，薄暮鱼丽逐左贤。谷中石虎经衔箭，山上金人曾祭天。天涯一去无穷已，蓟门迢递三千里。朝见马岭黄沙合，夕望龙城阵云起。庭中奇树已堪攀，塞外征人殊未还。白雪初下天山外，浮云直向五原间。关山万里不可越，谁能坐对芳菲月。流水本自断人肠，坚冰旧来伤马骨。边庭节物与华异，冬霰秋霜春不歇。长风萧萧渡水来，归雁连连映天没。从军行，军行万里出龙庭，单于渭桥今已拜，将军何处觅功名。');
INSERT INTO `article` VALUES (24, '归雁', '杜甫', '〔唐代〕', '东来万里客，乱定几年归？肠断江城雁，高高向北飞。');
INSERT INTO `article` VALUES (25, '西陵遇风献康乐', '谢惠连', '〔南北朝〕', '我行指孟春，春仲尚未发。趣途远有期，念离情无歇。成装候良辰，漾舟陶嘉月。瞻涂意少悰，还顾情多阙。哲兄感仳别，相送越坰林。饮饯野亭馆，分袂澄湖阴。凄凄留子言，眷眷浮客心。回塘隐舻栧，远望绝形音。靡靡即长路，戚戚抱遥悲。悲遥但自弭，路长当语谁！行行道转远，去去情弥迟。昨发浦阳汭，今宿浙江湄。屯云蔽曾岭，惊风涌飞流。零雨润坟泽，落雪洒林丘。浮氛晦崖巘，积素惑原畴。曲汜薄停旅，通川绝行舟。临津不得济，伫檝阻风波。萧条洲渚际，气色少谐和。西瞻兴游叹，东睇起凄歌。积愤成疢痗，无萱将如何！');
INSERT INTO `article` VALUES (26, '逆旅小子', '方苞', '〔清代〕', '　　戊戌秋九月，余归自塞上，宿石槽。逆旅小子形苦羸，敞布单衣，不袜不履，而主人挞击之甚猛，泣甚悲。叩之东西家，曰“是其兄之孤也。有田一区，畜产什器粗具，恐孺子长而与之分，故不恤其寒饥而苦役之；夜则闭之户外，严风起，弗活矣。”余至京师，再书告京兆尹，宜檄县捕诘，俾乡邻保任而后释之。　　逾岁四月，复过此里，人曰：“孺子果以是冬死，而某亦暴死，其妻子、田宅、畜物皆为他人有矣。”叩以“吏曾呵诘乎？”则未也。　　昔先王以道明民，犹恐顽者不喻，故“以乡八刑纠万民”，其不孝、不弟、不睦、不姻、不任、不恤者，则刑随之，而五家相保，有罪奇邪则相及，所以闭其涂，使民无由动于邪恶也。管子之法，则自乡师以至什伍之长，转相督察，而罪皆及于所司。盖周公所虑者，民俗之偷而已，至管子而又患吏情之遁焉，此可以观世变矣。');
INSERT INTO `article` VALUES (27, '池上二绝', '白居易', '〔唐代〕', '山僧对棋坐，局上竹阴清。映竹无人见，时闻下子声。小娃撑小艇，偷采白莲回。不解藏踪迹，浮萍一道开。');
INSERT INTO `article` VALUES (28, '送韦评事', '王维', '〔唐代〕', '欲逐将军取右贤，沙场走马向居延。遥知汉使萧关外，愁见孤城落日边。');
INSERT INTO `article` VALUES (29, '折桂令·西陵送别', '张可久', '〔元代〕', '画船儿载不起离愁，人到西陵，恨满东州。懒上归鞍，慵开泪眼，怕倚层楼。春去春来，管送别依依岸柳。潮生潮落，会忘机泛泛沙鸥。烟水悠悠，有句相酬，无计相留。');
INSERT INTO `article` VALUES (30, '渡黄河', '范云', '〔南北朝〕', '河流迅且浊，汤汤不可陵。桧楫难为榜，松舟才自胜。空庭偃旧木，荒畴余故塍。不睹行人迹，但见狐兔兴。寄言河上老，此水何当澄。');
INSERT INTO `article` VALUES (31, '咏萤', '虞世南', '〔唐代〕', '的历流光小，飘飖弱翅轻。恐畏无人识，独自暗中明。');
INSERT INTO `article` VALUES (32, '清平乐·检校山园书所见', '辛弃疾', '〔宋代〕', '断崖修竹，竹里藏冰玉。路转清溪三百曲，香满黄昏雪屋。行人系马疏篱，折残犹有高枝。留得东风数点，只缘娇嫩春迟。');
INSERT INTO `article` VALUES (33, '南乡子·好个主人家', '辛弃疾', '〔宋代〕', '好个主人家。不问因由便去嗏。病得那人妆晃了，巴巴。系上裙儿稳也哪。别泪没些些。海誓山盟总是赊。今日新欢须记取，孩儿，更过十年也似他。');
INSERT INTO `article` VALUES (34, '佳人', '杜甫', '〔唐代〕', '绝代有佳人，幽居在空谷。自云良家子，零落依草木。关中昔丧乱，兄弟遭杀戮。官高何足论，不得收骨肉。世情恶衰歇，万事随转烛。夫婿轻薄儿，新人美如玉。合昏尚知时，鸳鸯不独宿。但见新人笑，那闻旧人哭。在山泉水清，出山泉水浊。侍婢卖珠回，牵萝补茅屋。摘花不插发，采柏动盈掬。天寒翠袖薄，日暮倚修竹。');
INSERT INTO `article` VALUES (35, '水龙吟·翠鳌涌出沧溟', '施岳', '〔宋代〕', '翠鳌涌出沧溟，影横栈壁迷烟墅。楼台对起，阑干重凭，山川自古。梁苑平芜，汴堤疏柳，几番晴雨。看天低四远，江空万里，登临处、分吴楚。两岸花飞絮舞。度春风、满城箫鼓。英雄暗老，昏潮晓汐，归帆过橹。淮水东流，塞云北渡，夕阳西去。正凄凉望极，中原路杳，月来南浦。');
INSERT INTO `article` VALUES (36, '留客住·鹧鸪', '曹贞吉', '〔清代〕', '瘴云苦。遍五溪、沙明水碧，声声不断，只劝行人休去。行人今古如织，正复何事，关卿频寄语。空祠废驿，便征衫湿尽，马蹄难驻。风更雨。一发中原，杳无望处。万里炎荒，遮莫摧残毛羽。记否越王春殿，宫女如花，只今惟剩汝。子规声续，想江深月黑，低头臣甫。');
INSERT INTO `article` VALUES (37, '相州昼锦堂记', '欧阳修', '〔宋代〕', '　　仕宦而至将相，富贵而归故乡。此人情之所荣，而今昔之所同也。　　盖士方穷时，困厄闾里，庸人孺子，皆得易而侮之。若季子不礼于其嫂，买臣见弃于其妻。一旦高车驷马，旗旄导前，而骑卒拥后，夹道之人，相与骈肩累迹，瞻望咨嗟；而所谓庸夫愚妇者，奔走骇汗，羞愧俯伏，以自悔罪于车尘马足之间。此一介之士，得志于当时，而意气之盛，昔人比之衣锦之荣者也。　　惟大丞相魏国公则不然：公，相人也，世有令德，为时名卿。自公少时，已擢高科，登显仕。海内之士，闻下风而望余光者，盖亦有年矣。所谓将相而富贵，皆公所宜素有；非如穷厄之人，侥幸得志于一时，出于庸夫愚妇之不意，以惊骇而夸耀之也。然则高牙大纛，不足为公荣；桓圭衮冕，不足为公贵。惟德被生民，而功施社稷，勒之金石，播之声诗，以耀后世而垂无穷，此公之志，而士亦以此望于公也。岂止夸一时而荣一乡哉！　　公在至和中，尝以武康之节，来治于相，乃作“昼锦”之堂于后圃。既又刻诗于石，以遗相人。其言以快恩仇、矜名誉为可薄，盖不以昔人所夸者为荣，而以为戒。于此见公之视富贵为何如，而其志岂易量哉！故能出入将相，勤劳王家，而夷险一节。至于临大事，决大议，垂绅正笏，不动声色，而措天下于泰山之安：可谓社稷之臣矣！其丰功盛烈，所以铭彝鼎而被弦歌者，乃邦家之光，非闾里之荣也。　　余虽不获登公之堂，幸尝窃诵公之诗，乐公之志有成，而喜为天下道也。于是乎书。　　尚书吏部侍郎、参知政事欧阳修记。');
INSERT INTO `article` VALUES (38, '母别子', '白居易', '〔唐代〕', '母别子，子别母，白日无光哭声苦。关西骠骑大将军，去年破虏新策勋。敕赐金钱二百万，洛阳迎得如花人。新人迎来旧人弃，掌上莲花眼中刺。迎新弃旧未足悲，悲在君家留两儿。一始扶行一初坐，坐啼行哭牵人衣。以汝夫妇新燕婉，使我母子生别离。不如林中乌与鹊，母不失雏雄伴雌。应似园中桃李树，花落随风子在枝。新人新人听我语，洛阳无限红楼女。但愿将军重立功，更有新人胜于汝。');
INSERT INTO `article` VALUES (39, '更漏子·菊花残', '晏殊', '〔宋代〕', '菊花残，梨叶堕。可惜良辰虚过。新酒熟，绮筵开。不辞红玉杯。蜀弦高，羌管脆。慢飐舞娥香袂。君莫笑，醉乡人。熙熙长似春。');
INSERT INTO `article` VALUES (40, '青青陵上柏', '佚名', '〔两汉〕', '青青陵上柏，磊磊涧中石。人生天地间，忽如远行客。斗酒相娱乐，聊厚不为薄。驱车策驽马，游戏宛与洛。洛中何郁郁，冠带自相索。长衢罗夹巷，王侯多第宅。两宫遥相望，双阙百余尺。极宴娱心意，戚戚何所迫？');

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id` ASC, `permission_id` ASC) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id` ASC) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id` ASC, `codename` ASC) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 65 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add content type', 4, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (14, 'Can change content type', 4, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (15, 'Can delete content type', 4, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (16, 'Can view content type', 4, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (17, 'Can add session', 5, 'add_session');
INSERT INTO `auth_permission` VALUES (18, 'Can change session', 5, 'change_session');
INSERT INTO `auth_permission` VALUES (19, 'Can delete session', 5, 'delete_session');
INSERT INTO `auth_permission` VALUES (20, 'Can view session', 5, 'view_session');
INSERT INTO `auth_permission` VALUES (21, 'Can add captcha', 6, 'add_captcha');
INSERT INTO `auth_permission` VALUES (22, 'Can change captcha', 6, 'change_captcha');
INSERT INTO `auth_permission` VALUES (23, 'Can delete captcha', 6, 'delete_captcha');
INSERT INTO `auth_permission` VALUES (24, 'Can view captcha', 6, 'view_captcha');
INSERT INTO `auth_permission` VALUES (25, 'Can add user', 7, 'add_user');
INSERT INTO `auth_permission` VALUES (26, 'Can change user', 7, 'change_user');
INSERT INTO `auth_permission` VALUES (27, 'Can delete user', 7, 'delete_user');
INSERT INTO `auth_permission` VALUES (28, 'Can view user', 7, 'view_user');
INSERT INTO `auth_permission` VALUES (29, 'Can add article', 8, 'add_article');
INSERT INTO `auth_permission` VALUES (30, 'Can change article', 8, 'change_article');
INSERT INTO `auth_permission` VALUES (31, 'Can delete article', 8, 'delete_article');
INSERT INTO `auth_permission` VALUES (32, 'Can view article', 8, 'view_article');
INSERT INTO `auth_permission` VALUES (33, 'Can add easy sentence', 9, 'add_easysentence');
INSERT INTO `auth_permission` VALUES (34, 'Can change easy sentence', 9, 'change_easysentence');
INSERT INTO `auth_permission` VALUES (35, 'Can delete easy sentence', 9, 'delete_easysentence');
INSERT INTO `auth_permission` VALUES (36, 'Can view easy sentence', 9, 'view_easysentence');
INSERT INTO `auth_permission` VALUES (37, 'Can add hard sentence', 10, 'add_hardsentence');
INSERT INTO `auth_permission` VALUES (38, 'Can change hard sentence', 10, 'change_hardsentence');
INSERT INTO `auth_permission` VALUES (39, 'Can delete hard sentence', 10, 'delete_hardsentence');
INSERT INTO `auth_permission` VALUES (40, 'Can view hard sentence', 10, 'view_hardsentence');
INSERT INTO `auth_permission` VALUES (41, 'Can add process', 11, 'add_process');
INSERT INTO `auth_permission` VALUES (42, 'Can change process', 11, 'change_process');
INSERT INTO `auth_permission` VALUES (43, 'Can delete process', 11, 'delete_process');
INSERT INTO `auth_permission` VALUES (44, 'Can view process', 11, 'view_process');
INSERT INTO `auth_permission` VALUES (45, 'Can add easy list', 12, 'add_easylist');
INSERT INTO `auth_permission` VALUES (46, 'Can change easy list', 12, 'change_easylist');
INSERT INTO `auth_permission` VALUES (47, 'Can delete easy list', 12, 'delete_easylist');
INSERT INTO `auth_permission` VALUES (48, 'Can view easy list', 12, 'view_easylist');
INSERT INTO `auth_permission` VALUES (49, 'Can add hard list', 13, 'add_hardlist');
INSERT INTO `auth_permission` VALUES (50, 'Can change hard list', 13, 'change_hardlist');
INSERT INTO `auth_permission` VALUES (51, 'Can delete hard list', 13, 'delete_hardlist');
INSERT INTO `auth_permission` VALUES (52, 'Can view hard list', 13, 'view_hardlist');
INSERT INTO `auth_permission` VALUES (53, 'Can add segment', 14, 'add_segment');
INSERT INTO `auth_permission` VALUES (54, 'Can change segment', 14, 'change_segment');
INSERT INTO `auth_permission` VALUES (55, 'Can delete segment', 14, 'delete_segment');
INSERT INTO `auth_permission` VALUES (56, 'Can view segment', 14, 'view_segment');
INSERT INTO `auth_permission` VALUES (57, 'Can add poetry', 15, 'add_poetry');
INSERT INTO `auth_permission` VALUES (58, 'Can change poetry', 15, 'change_poetry');
INSERT INTO `auth_permission` VALUES (59, 'Can delete poetry', 15, 'delete_poetry');
INSERT INTO `auth_permission` VALUES (60, 'Can view poetry', 15, 'view_poetry');
INSERT INTO `auth_permission` VALUES (61, 'Can add similar_words', 16, 'add_similar_words');
INSERT INTO `auth_permission` VALUES (62, 'Can change similar_words', 16, 'change_similar_words');
INSERT INTO `auth_permission` VALUES (63, 'Can delete similar_words', 16, 'delete_similar_words');
INSERT INTO `auth_permission` VALUES (64, 'Can view similar_words', 16, 'view_similar_words');

-- ----------------------------
-- Table structure for captcha
-- ----------------------------
DROP TABLE IF EXISTS `captcha`;
CREATE TABLE `captcha`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(254) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `code` varchar(4) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `email`(`email` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of captcha
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `content_type_id` int NULL DEFAULT NULL,
  `user_id` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id` ASC) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_user_username`(`user_id` ASC) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_user_username` FOREIGN KEY (`user_id`) REFERENCES `user` (`username`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_chk_1` CHECK (`action_flag` >= 0)
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label` ASC, `model` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 17 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (15, 'app01', 'poetry');
INSERT INTO `django_content_type` VALUES (16, 'app01', 'similar_words');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (8, 'book', 'article');
INSERT INTO `django_content_type` VALUES (12, 'book', 'easylist');
INSERT INTO `django_content_type` VALUES (9, 'book', 'easysentence');
INSERT INTO `django_content_type` VALUES (13, 'book', 'hardlist');
INSERT INTO `django_content_type` VALUES (10, 'book', 'hardsentence');
INSERT INTO `django_content_type` VALUES (11, 'book', 'process');
INSERT INTO `django_content_type` VALUES (14, 'book', 'segment');
INSERT INTO `django_content_type` VALUES (4, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (5, 'sessions', 'session');
INSERT INTO `django_content_type` VALUES (6, 'user', 'captcha');
INSERT INTO `django_content_type` VALUES (7, 'user', 'user');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 22 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2024-12-05 15:33:05.441957');
INSERT INTO `django_migrations` VALUES (2, 'contenttypes', '0002_remove_content_type_name', '2024-12-05 15:33:05.538973');
INSERT INTO `django_migrations` VALUES (3, 'auth', '0001_initial', '2024-12-05 15:33:05.959571');
INSERT INTO `django_migrations` VALUES (4, 'auth', '0002_alter_permission_name_max_length', '2024-12-05 15:33:06.048481');
INSERT INTO `django_migrations` VALUES (5, 'auth', '0003_alter_user_email_max_length', '2024-12-05 15:33:06.056353');
INSERT INTO `django_migrations` VALUES (6, 'auth', '0004_alter_user_username_opts', '2024-12-05 15:33:06.065285');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0005_alter_user_last_login_null', '2024-12-05 15:33:06.073195');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0006_require_contenttypes_0002', '2024-12-05 15:33:06.079056');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0007_alter_validators_add_error_messages', '2024-12-05 15:33:06.093099');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0008_alter_user_username_max_length', '2024-12-05 15:33:06.114535');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0009_alter_user_last_name_max_length', '2024-12-05 15:33:06.123411');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0010_alter_group_name_max_length', '2024-12-05 15:33:06.145533');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0011_update_proxy_permissions', '2024-12-05 15:33:06.154079');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0012_alter_user_first_name_max_length', '2024-12-05 15:33:06.163259');
INSERT INTO `django_migrations` VALUES (15, 'user', '0001_initial', '2024-12-05 15:33:06.665891');
INSERT INTO `django_migrations` VALUES (16, 'admin', '0001_initial', '2024-12-05 15:33:06.878277');
INSERT INTO `django_migrations` VALUES (17, 'admin', '0002_logentry_remove_auto_add', '2024-12-05 15:33:06.889505');
INSERT INTO `django_migrations` VALUES (18, 'admin', '0003_logentry_add_action_flag_choices', '2024-12-05 15:33:06.901118');
INSERT INTO `django_migrations` VALUES (19, 'app01', '0001_initial', '2024-12-05 15:33:06.965530');
INSERT INTO `django_migrations` VALUES (20, 'book', '0001_initial', '2024-12-05 15:33:07.420614');
INSERT INTO `django_migrations` VALUES (21, 'sessions', '0001_initial', '2024-12-05 15:33:07.476630');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_session
-- ----------------------------

-- ----------------------------
-- Table structure for easylist
-- ----------------------------
DROP TABLE IF EXISTS `easylist`;
CREATE TABLE `easylist`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `article_id` bigint NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `article_id`(`article_id` ASC) USING BTREE,
  CONSTRAINT `easylist_article_id_106c0cb0_fk_Article_id` FOREIGN KEY (`article_id`) REFERENCES `article` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of easylist
-- ----------------------------

-- ----------------------------
-- Table structure for easysentence
-- ----------------------------
DROP TABLE IF EXISTS `easysentence`;
CREATE TABLE `easysentence`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `text` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of easysentence
-- ----------------------------

-- ----------------------------
-- Table structure for hardlist
-- ----------------------------
DROP TABLE IF EXISTS `hardlist`;
CREATE TABLE `hardlist`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `article_id` bigint NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `article_id`(`article_id` ASC) USING BTREE,
  CONSTRAINT `hardlist_article_id_aa1e190b_fk_Article_id` FOREIGN KEY (`article_id`) REFERENCES `article` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of hardlist
-- ----------------------------

-- ----------------------------
-- Table structure for hardsentence
-- ----------------------------
DROP TABLE IF EXISTS `hardsentence`;
CREATE TABLE `hardsentence`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `text` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `count` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of hardsentence
-- ----------------------------

-- ----------------------------
-- Table structure for poetry
-- ----------------------------
DROP TABLE IF EXISTS `poetry`;
CREATE TABLE `poetry`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `author` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `dynasty` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 41 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of poetry
-- ----------------------------
INSERT INTO `poetry` VALUES (1, '黄金缕·妾本钱塘江上住', '司马槱', '〔宋代〕', '妾本钱塘江上住。花落花开，不管流年度。燕子衔将春色去，纱窗几阵黄梅雨。\n斜插犀梳云半吐，檀板轻敲，唱彻黄金缕。望断行云无觅处，梦回明月生南浦。');
INSERT INTO `poetry` VALUES (2, '枭将东徙', '刘向', '〔两汉〕', '枭逢鸠。鸠曰：“子将安之？”\n枭曰：“我将东徙。”\n鸠曰：“何故？”\n枭曰：“乡人皆恶我鸣。以故东徙。”\n鸠曰：“子能更鸣，可矣；不能更鸣，东徙，犹恶子之声。”');
INSERT INTO `poetry` VALUES (3, '左迁至蓝关示侄孙湘', '韩愈', '〔唐代〕', '一封朝奏九重天，夕贬潮州路八千。\n欲为圣明除弊事，肯将衰朽惜残年！(欲为 一作：本为；圣明 一作：圣朝；肯将 一作：敢将)\n云横秦岭家何在？雪拥蓝关马不前。\n知汝远来应有意，好收吾骨瘴江边。');
INSERT INTO `poetry` VALUES (4, '送郑少府入辽共赋侠客远从戎', '骆宾王', '〔唐代〕', '边烽警榆塞，侠客度桑乾。\n柳叶开银镝，桃花照玉鞍。\n满月临弓影，连星入剑端。\n不学燕丹客，徒歌易水寒。');
INSERT INTO `poetry` VALUES (5, '题武关', '杜牧', '〔唐代〕', '碧溪留我武关东，一笑怀王迹自穷。\n郑袖娇娆酣似醉，屈原憔悴去如蓬。\n山樯谷堑依然在，弱吐强吞尽已空。\n今日圣神家四海，戍旗长卷夕阳中。');
INSERT INTO `poetry` VALUES (6, '殿前欢·畅幽哉', '贯云石', '〔元代〕', '畅幽哉，春风无处不楼台。一时怀抱俱无奈，总对天开。\n就渊明归去来，怕鹤怨山禽怪，问甚功名在？酸斋是我，我是酸斋。');
INSERT INTO `poetry` VALUES (7, '一叶落·泪眼注', '朱彝尊', '〔清代〕', '泪眼注，临当去，此时欲住已难住。下楼复上楼，楼头风吹雨。风吹雨，草草离人语。');
INSERT INTO `poetry` VALUES (8, '哀江南', '孔尚任', '〔清代〕', '　　〔哀江南〕〔北新水令〕山松野草带花挑，猛抬头秣陵重到。残军留废垒，瘦马卧空壕；村郭萧条，城对着夕阳道。\n　　〔驻马听〕野火频烧，护墓长楸多半焦。山羊群跑，守陵阿监几时逃。鸽翎蝠粪满堂抛，枯枝败叶当阶罩；谁祭扫，牧儿打碎龙碑帽。\n　　〔沈醉东风〕横白玉八根柱倒，堕红泥半堵墙高。碎琉璃瓦片多，烂翡翠窗棂少。舞丹墀燕雀常朝，直入宫门一路蒿，住几个乞儿饿殍。\n　　〔折桂令〕问秦淮旧日窗寮，破纸迎风，坏槛当潮，目断魂消。当年粉黛，何处笙箫？ 罢灯船端阳不闹，收酒旗重九无聊。白鸟飘飘，绿水滔滔，嫩黄花有些蝶飞，新红叶无个人瞧。\n　　〔沽美酒〕你记得跨青溪半里桥，旧红板没一条。秋水长天人过少，冷清清的落照，剩一树柳弯腰。\n　　〔太平令〕行到那旧院门，何用轻敲，也不怕小犬哰哰。无非是枯井颓巢，不过些砖苔砌草。手种的花条柳梢，尽意儿采樵；这黑灰是谁家厨灶？\n　　〔离亭宴带歇指煞〕俺曾见金陵玉殿莺啼晓，秦淮水榭花开早，谁知道容易冰消！眼看他起朱楼，眼看他宴宾客，眼看他楼塌了！这青苔碧瓦堆，俺曾睡风流觉，将五十年兴亡看饱。那乌衣巷不姓王，莫愁湖鬼夜哭，凤凰台栖枭鸟。残山梦最真，旧境丢难掉，不信这舆图换稿！诌一套《哀江南》，放悲声唱到老。');
INSERT INTO `poetry` VALUES (9, '悲回风', '屈原', '〔先秦〕', '悲回风之摇蕙兮，心冤结而内伤。\n物有微而陨性兮，声有隐而先倡。\n夫何彭咸之造思兮，暨志介而不忘！\n万变其情岂可盖兮，孰虚伪之可长？\n鸟兽鸣以号群兮，草苴比而不芳。\n鱼葺鳞以自别兮，蛟龙隐其文章。\n故荼荠不同亩兮，兰茝幽而独芳。\n惟佳人之永都兮，更统世以自贶。\n眇远志之所及兮，怜浮云之相羊。\n介眇志之所惑兮，窃赋诗之所明。\n惟佳人之独怀兮，折若椒以自处。\n曾歔欷之嗟嗟兮，独隐伏而思虑。\n涕泣交而凄凄兮，思不眠以至曙。\n终长夜之曼曼兮，掩此哀而不去。\n寤从容以周流兮，聊逍遥以自恃。\n伤太息之愍怜兮，气於邑而不可止。\n糺思心以为纕兮，编愁苦以为膺。\n折若木以弊光兮，随飘风之所仍。\n存彷佛而不见兮，心踊跃其若汤。\n抚珮衽以案志兮，超惘惘而遂行。\n岁曶曶其若颓兮，时亦冉冉而将至。\n薠蘅槁而节离兮，芳以歇而不比。\n怜思心之不可惩兮，证此言之不可聊。\n宁溘死而流亡兮，不忍此心之常愁。\n孤子吟而抆泪兮，放子出而不还。\n孰能思而不隐兮，照彭咸之所闻。\n登石峦以远望兮，路眇眇之默默。\n入景响之无应兮，闻省想而不可得。\n愁郁郁之无快兮，居戚戚而不可解。\n心鞿羁而不开兮，气缭转而自缔。\n穆眇眇之无垠兮，莽芒芒之无仪。\n声有隐而相感兮，物有纯而不可为。\n邈漫漫之不可量兮，缥绵绵之不可纡。\n愁悄悄之常悲兮，翩冥冥之不可娱。\n凌大波而流风兮，讬彭咸之所居。\n上高岩之峭岸兮，处雌蜺之标颠。\n据青冥而摅虹兮，遂儵忽而扪天。\n吸湛露之浮源兮，漱凝霜之雰雰。\n依风穴以自息兮，忽倾寤以婵媛。\n冯昆仑以澂雾兮，隐渂山以清江。\n惮涌湍之礚礚兮，听波声之汹汹。\n纷容容之无经兮，罔芒芒之无纪。\n轧洋洋之无从兮，驰委移之焉止？\n漂翻翻其上下兮，翼遥遥其左右。\n氾潏潏其前后兮，伴张驰之信期。\n观炎气之相仍兮，窥烟液之所积。\n悲霜雪之俱下兮，听潮水之相击。\n借光景以往来兮，施黄棘之枉策。\n求介子之所存兮，见伯夷之放迹。\n心调度而弗去兮，刻著志之无适。\n曰吾怨往昔之所冀兮，悼来者之悐悐。\n浮江淮而入海兮，从子胥而自适。\n望大河之洲渚兮，悲申徒之抗迹。\n骤谏君而不听兮，重任石之何益？\n心絓结而不解兮，思蹇产而不释。');
INSERT INTO `poetry` VALUES (10, '行路难·缚虎手', '贺铸', '〔宋代〕', '缚虎手，悬河口，车如鸡栖马如狗。白纶巾，扑黄尘，不知我辈可是蓬蒿人？衰兰送客咸阳道，天若有情天亦老。作雷颠，不论钱，谁问旗亭美酒斗十千？\n酌大斗，更为寿，青鬓长青古无有。笑嫣然，舞翩然，当垆秦女十五语如弦。遗音能记秋风曲，事去千年犹恨促。揽流光，系扶桑，争奈愁来一日却为长。');
INSERT INTO `poetry` VALUES (11, '感旧四首·其二', '黄景仁', '〔清代〕', '唤起窗前尚宿酲，啼鹃催去又声声。\n丹青旧誓相如札，禅榻经时杜牧情。\n别后相思空一水，重来回首已三生。\n云阶月地依然在，细逐空香百遍行。');
INSERT INTO `poetry` VALUES (12, '悼亡诗三首', '潘岳', '〔魏晋〕', '荏苒冬春谢，寒暑忽流易。\n之子归穷泉，重壤永幽隔。\n私怀谁克从，淹留亦何益。\n僶俛恭朝命，回心反初役。\n望庐思其人，入室想所历。\n帏屏无髣髴，翰墨有馀迹。\n流芳未及歇，遗挂犹在壁。\n怅恍如或存，回惶忡惊惕。(回惶 一作：周惶)\n如彼翰林鸟，双栖一朝只。\n如彼游川鱼，比目中路析。\n春风缘隟来，晨霤承檐滴。\n寝息何时忘，沉忧日盈积。\n庶几有时衰，庄缶犹可击。\n皎皎窗中月，照我室南端。\n清商应秋至，溽暑随节阑。\n凛凛凉风升，始觉夏衾单。\n岂曰无重纩，谁与同岁寒。\n岁寒无与同，朗月何胧胧。\n展转盻枕席，长簟竟床空。\n床空委清尘，室虚来悲风。\n独无李氏灵，髣髴覩尔容。\n抚衿长叹息，不觉涕沾胸。\n沾胸安能已，悲怀从中起。\n寝兴目存形，遗音犹在耳。\n上惭东门吴，下愧蒙庄子。\n赋诗欲言志，此志难具纪。\n命也可奈何，长戚自令鄙。\n曜灵运天机，四节代迁逝。\n凄凄朝露凝，烈烈夕风厉。\n奈何悼淑俪，仪容永潜翳。\n念此如昨日，谁知已卒岁。\n改服从朝政，哀心寄私制。\n茵帱张故房，朔望临尔祭。\n尔祭讵几时，朔望忽复尽。\n衾裳一毁撤，千载不复引。\n亹亹朞月周，戚戚弥相愍。\n悲怀感物来，泣涕应情陨。\n驾言陟东阜，望坟思纡轸。\n徘徊墟墓间，欲去复不忍。\n徘徊不忍去，徙倚步踟蹰。\n落叶委埏侧，枯荄带坟隅。\n孤魂独茕茕，安知灵与无。\n投心遵朝命，挥涕强就车。\n谁谓帝宫远，路极悲有余。');
INSERT INTO `poetry` VALUES (13, '高山流水·次夫子清风阁落成韵', '顾太清', '〔清代〕', '群山万壑引长风，透林皋、晓日玲珑。楼外绿阴深，凭栏指点偏东。浑河水、一线如虹。清凉极，满谷幽禽啼啸，冷雾溟濛。任海天寥阔，飞跃此身中。\n云容。看白云苍狗，无心者、变化虚空。细草络危岩，岩花秀媚日承红。清风阁，高凌霄汉，列岫如童。待何年归去，谈笑各争雄。');
INSERT INTO `poetry` VALUES (14, '咏画扇诗', '鲍子卿', '〔南北朝〕', '细丝本自轻，弱彩何足眄。\n直为发红颜，谬成握中扇。\n乍奉长门泣，时承柏梁宴。\n思妆开已掩，歌容隐而见。\n但画双黄鹄，莫画孤飞燕。');
INSERT INTO `poetry` VALUES (15, '汉宫曲', '徐凝', '〔唐代〕', '水色帘前流玉霜，赵家飞燕侍昭阳。\n掌中舞罢箫声绝，三十六宫秋夜长。');
INSERT INTO `poetry` VALUES (16, '赠女冠畅师', '秦观', '〔宋代〕', '瞳人剪水腰如束，一幅乌纱裹寒玉。\n飘然自有姑射姿，回看粉黛皆尘俗。\n雾阁云窗人莫窥，门前车马任东西。\n礼罢晓坛春日静，落红满地乳鸦啼。');
INSERT INTO `poetry` VALUES (17, '夕次盱眙县', '韦应物', '〔唐代〕', '落帆逗淮镇，停舫临孤驿。\n浩浩风起波，冥冥日沉夕。\n人归山郭暗，雁下芦洲白。\n独夜忆秦关，听钟未眠客。');
INSERT INTO `poetry` VALUES (18, '送僧南归', '简长', '〔宋代〕', '渐老念乡国，先归独羡君。\n吴山全接汉，江树半藏云。\n振锡林烟断，添瓶涧月分。\n重栖上方定，孤狖雪中闻。');
INSERT INTO `poetry` VALUES (19, '临江仙·再用前韵送祐之弟归浮梁', '辛弃疾', '〔宋代〕', '钟鼎山林都是梦，人间宠辱休惊。只消闲处过平生。酒杯秋吸露，诗句夜裁冰。 \n记取小窗风雨夜，对床灯火多情。问谁千里伴君行。晓山眉样翠，秋水镜般明。');
INSERT INTO `poetry` VALUES (20, '梅圣俞诗集序', '欧阳修', '〔宋代〕', '　　予闻世谓诗人少达而多穷，夫岂然哉？盖世所传诗者，多出于古穷人之辞也。凡士之蕴其所有，而不得施于世者，多喜自放于山巅水涯之外，见虫鱼草木风云鸟兽之状类，往往探其奇怪，内有忧思感愤之郁积，其兴于怨刺，以道羁臣寡妇之所叹，而写人情之难言。盖愈穷则愈工。然则非诗之能穷人，殆穷者而后工也。 \n　　予友梅圣俞，少以荫补为吏，累举进士，辄抑于有司，困于州县，凡十余年。年今五十，犹从辟书，为人之佐，郁其所蓄，不得奋见于事业。其家宛陵，幼习于诗，自为童子，出语已惊其长老。既长，学乎六经仁义之说，其为文章，简古纯粹，不求苟说于世。世之人徒知其诗而已。然时无贤愚，语诗者必求之圣俞；圣俞亦自以其不得志者，乐于诗而发之，故其平生所作，于诗尤多。世既知之矣，而未有荐于上者。昔王文康公尝见而叹曰：“二百年无此作矣！”虽知之深，亦不果荐也。若使其幸得用于朝廷，作为雅、颂，以歌咏大宋之功德，荐之清庙，而追商、周、鲁颂之作者，岂不伟欤！奈何使其老不得志，而为穷者之诗，乃徒发于虫鱼物类，羁愁感叹之言。世徒喜其工，不知其穷之久而将老也！可不惜哉！ \n　　圣俞诗既多，不自收拾。其妻之兄子谢景初，惧其多而易失也，取其自洛阳至于吴兴以来所作，次为十卷。予尝嗜圣俞诗，而患不能尽得之，遽喜谢氏之能类次也，辄序而藏之。 \n　　其后十五年，圣俞以疾卒于京师，余既哭而铭之，因索于其家，得其遗稿千余篇，并旧所藏，掇其尤者六百七十七篇，为一十五卷。呜呼！吾于圣俞诗论之详矣，故不复云。 \n　　庐陵欧阳修序。');
INSERT INTO `poetry` VALUES (21, '寿阳曲·云笼月', '马致远', '〔元代〕', '云笼月，风弄铁，两般儿助人凄切。剔银灯欲将心事写，长吁气一声吹灭。');
INSERT INTO `poetry` VALUES (22, '醉太平·堂堂大元', '佚名', '〔元代〕', '堂堂大元，奸佞专权。开河变钞祸根源，惹红巾万千。官法滥，刑法重，黎民怨。人吃人，钞买钞，何曾见。贼做官，官做贼，混贤愚。哀哉可怜！');
INSERT INTO `poetry` VALUES (23, '从军行', '卢思道', '〔南北朝〕', '朔方烽火照甘泉，长安飞将出祁连。\n犀渠玉剑良家子，白马金羁侠少年。\n平明偃月屯右地，薄暮鱼丽逐左贤。\n谷中石虎经衔箭，山上金人曾祭天。\n天涯一去无穷已，蓟门迢递三千里。\n朝见马岭黄沙合，夕望龙城阵云起。\n庭中奇树已堪攀，塞外征人殊未还。\n白雪初下天山外，浮云直向五原间。\n关山万里不可越，谁能坐对芳菲月。\n流水本自断人肠，坚冰旧来伤马骨。\n边庭节物与华异，冬霰秋霜春不歇。\n长风萧萧渡水来，归雁连连映天没。\n从军行，军行万里出龙庭，单于渭桥今已拜，将军何处觅功名。');
INSERT INTO `poetry` VALUES (24, '归雁', '杜甫', '〔唐代〕', '东来万里客，乱定几年归？\n肠断江城雁，高高向北飞。');
INSERT INTO `poetry` VALUES (25, '西陵遇风献康乐', '谢惠连', '〔南北朝〕', '我行指孟春，春仲尚未发。\n趣途远有期，念离情无歇。\n成装候良辰，漾舟陶嘉月。\n瞻涂意少悰，还顾情多阙。\n哲兄感仳别，相送越坰林。\n饮饯野亭馆，分袂澄湖阴。\n凄凄留子言，眷眷浮客心。\n回塘隐舻栧，远望绝形音。\n靡靡即长路，戚戚抱遥悲。\n悲遥但自弭，路长当语谁！\n行行道转远，去去情弥迟。\n昨发浦阳汭，今宿浙江湄。\n屯云蔽曾岭，惊风涌飞流。\n零雨润坟泽，落雪洒林丘。\n浮氛晦崖巘，积素惑原畴。\n曲汜薄停旅，通川绝行舟。\n临津不得济，伫檝阻风波。\n萧条洲渚际，气色少谐和。\n西瞻兴游叹，东睇起凄歌。\n积愤成疢痗，无萱将如何！');
INSERT INTO `poetry` VALUES (26, '逆旅小子', '方苞', '〔清代〕', '　　戊戌秋九月，余归自塞上，宿石槽。逆旅小子形苦羸，敞布单衣，不袜不履，而主人挞击之甚猛，泣甚悲。叩之东西家，曰“是其兄之孤也。有田一区，畜产什器粗具，恐孺子长而与之分，故不恤其寒饥而苦役之；夜则闭之户外，严风起，弗活矣。”余至京师，再书告京兆尹，宜檄县捕诘，俾乡邻保任而后释之。\n　　逾岁四月，复过此里，人曰：“孺子果以是冬死，而某亦暴死，其妻子、田宅、畜物皆为他人有矣。”叩以“吏曾呵诘乎？”则未也。\n　　昔先王以道明民，犹恐顽者不喻，故“以乡八刑纠万民”，其不孝、不弟、不睦、不姻、不任、不恤者，则刑随之，而五家相保，有罪奇邪则相及，所以闭其涂，使民无由动于邪恶也。管子之法，则自乡师以至什伍之长，转相督察，而罪皆及于所司。盖周公所虑者，民俗之偷而已，至管子而又患吏情之遁焉，此可以观世变矣。');
INSERT INTO `poetry` VALUES (27, '池上二绝', '白居易', '〔唐代〕', '山僧对棋坐，局上竹阴清。\n映竹无人见，时闻下子声。\n小娃撑小艇，偷采白莲回。\n不解藏踪迹，浮萍一道开。');
INSERT INTO `poetry` VALUES (28, '送韦评事', '王维', '〔唐代〕', '欲逐将军取右贤，沙场走马向居延。\n遥知汉使萧关外，愁见孤城落日边。');
INSERT INTO `poetry` VALUES (29, '折桂令·西陵送别', '张可久', '〔元代〕', '画船儿载不起离愁，人到西陵，恨满东州。懒上归鞍，慵开泪眼，怕倚层楼。春去春来，管送别依依岸柳。潮生潮落，会忘机泛泛沙鸥。烟水悠悠，有句相酬，无计相留。');
INSERT INTO `poetry` VALUES (30, '渡黄河', '范云', '〔南北朝〕', '河流迅且浊，汤汤不可陵。\n桧楫难为榜，松舟才自胜。\n空庭偃旧木，荒畴余故塍。\n不睹行人迹，但见狐兔兴。\n寄言河上老，此水何当澄。');
INSERT INTO `poetry` VALUES (31, '咏萤', '虞世南', '〔唐代〕', '的历流光小，飘飖弱翅轻。\n恐畏无人识，独自暗中明。');
INSERT INTO `poetry` VALUES (32, '清平乐·检校山园书所见', '辛弃疾', '〔宋代〕', '断崖修竹，竹里藏冰玉。路转清溪三百曲，香满黄昏雪屋。\n行人系马疏篱，折残犹有高枝。留得东风数点，只缘娇嫩春迟。');
INSERT INTO `poetry` VALUES (33, '南乡子·好个主人家', '辛弃疾', '〔宋代〕', '好个主人家。不问因由便去嗏。病得那人妆晃了，巴巴。系上裙儿稳也哪。\n别泪没些些。海誓山盟总是赊。今日新欢须记取，孩儿，更过十年也似他。');
INSERT INTO `poetry` VALUES (34, '佳人', '杜甫', '〔唐代〕', '绝代有佳人，幽居在空谷。\n自云良家子，零落依草木。\n关中昔丧乱，兄弟遭杀戮。\n官高何足论，不得收骨肉。\n世情恶衰歇，万事随转烛。\n夫婿轻薄儿，新人美如玉。\n合昏尚知时，鸳鸯不独宿。\n但见新人笑，那闻旧人哭。\n在山泉水清，出山泉水浊。\n侍婢卖珠回，牵萝补茅屋。\n摘花不插发，采柏动盈掬。\n天寒翠袖薄，日暮倚修竹。');
INSERT INTO `poetry` VALUES (35, '水龙吟·翠鳌涌出沧溟', '施岳', '〔宋代〕', '翠鳌涌出沧溟，影横栈壁迷烟墅。楼台对起，阑干重凭，山川自古。梁苑平芜，汴堤疏柳，几番晴雨。看天低四远，江空万里，登临处、分吴楚。\n两岸花飞絮舞。度春风、满城箫鼓。英雄暗老，昏潮晓汐，归帆过橹。淮水东流，塞云北渡，夕阳西去。正凄凉望极，中原路杳，月来南浦。');
INSERT INTO `poetry` VALUES (36, '留客住·鹧鸪', '曹贞吉', '〔清代〕', '瘴云苦。遍五溪、沙明水碧，声声不断，只劝行人休去。行人今古如织，正复何事，关卿频寄语。空祠废驿，便征衫湿尽，马蹄难驻。\n风更雨。一发中原，杳无望处。万里炎荒，遮莫摧残毛羽。记否越王春殿，宫女如花，只今惟剩汝。子规声续，想江深月黑，低头臣甫。');
INSERT INTO `poetry` VALUES (37, '相州昼锦堂记', '欧阳修', '〔宋代〕', '　　仕宦而至将相，富贵而归故乡。此人情之所荣，而今昔之所同也。\n　　盖士方穷时，困厄闾里，庸人孺子，皆得易而侮之。若季子不礼于其嫂，买臣见弃于其妻。一旦高车驷马，旗旄导前，而骑卒拥后，夹道之人，相与骈肩累迹，瞻望咨嗟；而所谓庸夫愚妇者，奔走骇汗，羞愧俯伏，以自悔罪于车尘马足之间。此一介之士，得志于当时，而意气之盛，昔人比之衣锦之荣者也。\n　　惟大丞相魏国公则不然：公，相人也，世有令德，为时名卿。自公少时，已擢高科，登显仕。海内之士，闻下风而望余光者，盖亦有年矣。所谓将相而富贵，皆公所宜素有；非如穷厄之人，侥幸得志于一时，出于庸夫愚妇之不意，以惊骇而夸耀之也。然则高牙大纛，不足为公荣；桓圭衮冕，不足为公贵。惟德被生民，而功施社稷，勒之金石，播之声诗，以耀后世而垂无穷，此公之志，而士亦以此望于公也。岂止夸一时而荣一乡哉！\n　　公在至和中，尝以武康之节，来治于相，乃作“昼锦”之堂于后圃。既又刻诗于石，以遗相人。其言以快恩仇、矜名誉为可薄，盖不以昔人所夸者为荣，而以为戒。于此见公之视富贵为何如，而其志岂易量哉！故能出入将相，勤劳王家，而夷险一节。至于临大事，决大议，垂绅正笏，不动声色，而措天下于泰山之安：可谓社稷之臣矣！其丰功盛烈，所以铭彝鼎而被弦歌者，乃邦家之光，非闾里之荣也。\n　　余虽不获登公之堂，幸尝窃诵公之诗，乐公之志有成，而喜为天下道也。于是乎书。\n　　尚书吏部侍郎、参知政事欧阳修记。 ');
INSERT INTO `poetry` VALUES (38, '母别子', '白居易', '〔唐代〕', '母别子，子别母，白日无光哭声苦。\n关西骠骑大将军，去年破虏新策勋。\n敕赐金钱二百万，洛阳迎得如花人。\n新人迎来旧人弃，掌上莲花眼中刺。\n迎新弃旧未足悲，悲在君家留两儿。\n一始扶行一初坐，坐啼行哭牵人衣。\n以汝夫妇新燕婉，使我母子生别离。\n不如林中乌与鹊，母不失雏雄伴雌。\n应似园中桃李树，花落随风子在枝。\n新人新人听我语，洛阳无限红楼女。\n但愿将军重立功，更有新人胜于汝。');
INSERT INTO `poetry` VALUES (39, '更漏子·菊花残', '晏殊', '〔宋代〕', '菊花残，梨叶堕。可惜良辰虚过。新酒熟，绮筵开。不辞红玉杯。\n蜀弦高，羌管脆。慢飐舞娥香袂。君莫笑，醉乡人。熙熙长似春。');
INSERT INTO `poetry` VALUES (40, '青青陵上柏', '佚名', '〔两汉〕', '青青陵上柏，磊磊涧中石。\n人生天地间，忽如远行客。\n斗酒相娱乐，聊厚不为薄。\n驱车策驽马，游戏宛与洛。\n洛中何郁郁，冠带自相索。\n长衢罗夹巷，王侯多第宅。\n两宫遥相望，双阙百余尺。\n极宴娱心意，戚戚何所迫？');

-- ----------------------------
-- Table structure for process
-- ----------------------------
DROP TABLE IF EXISTS `process`;
CREATE TABLE `process`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `text` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `count` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of process
-- ----------------------------

-- ----------------------------
-- Table structure for segment
-- ----------------------------
DROP TABLE IF EXISTS `segment`;
CREATE TABLE `segment`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `text` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `sentence_id` bigint NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `segment_sentence_id_3661720e_fk_hardsentence_id`(`sentence_id` ASC) USING BTREE,
  CONSTRAINT `segment_sentence_id_3661720e_fk_hardsentence_id` FOREIGN KEY (`sentence_id`) REFERENCES `hardsentence` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of segment
-- ----------------------------

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `password` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `first_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `username` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `photo` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `name` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`username`) USING BTREE,
  UNIQUE INDEX `email`(`email` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------

-- ----------------------------
-- Table structure for user_groups
-- ----------------------------
DROP TABLE IF EXISTS `user_groups`;
CREATE TABLE `user_groups`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `user_groups_user_id_group_id_40beef00_uniq`(`user_id` ASC, `group_id` ASC) USING BTREE,
  INDEX `user_groups_group_id_b76f8aba_fk_auth_group_id`(`group_id` ASC) USING BTREE,
  CONSTRAINT `user_groups_group_id_b76f8aba_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `user_groups_user_id_abaea130_fk_user_username` FOREIGN KEY (`user_id`) REFERENCES `user` (`username`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `user_user_permissions`;
CREATE TABLE `user_user_permissions`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `user_user_permissions_user_id_permission_id_7dc6e2e0_uniq`(`user_id` ASC, `permission_id` ASC) USING BTREE,
  INDEX `user_user_permission_permission_id_9deb68a3_fk_auth_perm`(`permission_id` ASC) USING BTREE,
  CONSTRAINT `user_user_permission_permission_id_9deb68a3_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `user_user_permissions_user_id_ed4a47ea_fk_user_username` FOREIGN KEY (`user_id`) REFERENCES `user` (`username`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_user_permissions
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
