store = {}
store['args']={'num_inference_samples': 100, 'available_sample_k': 10, 'initial_samples': [38043, 40091, 17418, 2094, 39879, 3133, 5011, 40683, 54379, 24287, 9849, 59305, 39508, 39356, 8758, 52579, 13655, 7636, 21562, 41329], 'seed': 661442, 'type': 'AcquisitionFunction.bald', 'acquisition_method': 'AcquisitionMethod.independent', 'experiment_description': 'Reproduce b1, 5, 10 k10, 100 and default initial samples, no initial samples for all methods with BALD. (No culling!)', 'batch_size': 64, 'scoring_batch_size': 512, 'test_batch_size': 512, 'validation_set_size': 1024, 'early_stopping_patience': 3, 'epochs': 30, 'epoch_samples': 5056, 'target_accuracy': 0.96, 'target_num_acquired_samples': 300, 'log_interval': 20, 'min_remaining_percentage': 100, 'min_candidates_per_acquired_item': 20, 'dataset': 'DatasetEnum.mnist', 'experiment_task_id': 'mnist_independent_bald_k100_b10_661442', 'experiments_laaos': './experiment_configs/big_repro_b10_k100/configs.py', 'no_cuda': False, 'quickquick': False, 'initial_samples_per_class': 2, 'initial_percentage': 100, 'reduce_percentage': 0}
store['cmdline']=['./src/ignite_mnist.py', '--experiment_task_id=mnist_independent_bald_k100_b10_661442', '--experiments_laaos=./experiment_configs/big_repro_b10_k100/configs.py']
store['iterations']=[]
store['initial_samples']=[38043, 40091, 17418, 2094, 39879, 3133, 5011, 40683, 54379, 24287, 9849, 59305, 39508, 39356, 8758, 52579, 13655, 7636, 21562, 41329]
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.6438, 'nll': 2.795591404854656}, 'chosen_samples': [59669, 54511, 59106, 33788, 20206, 24439, 7394, 23323, 46050, 34850], 'chosen_samples_score': [1.177735894263059, 1.1685824077335512, 1.1600849635809432, 1.1575732927506706, 1.14908239979634, 1.1338618417889625, 1.1315815493928163, 1.1306213080972205, 1.1305393988831551, 1.1280944275994682], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 14.09212072200171, 'batch_acquisition_elapsed_time': 65.69378898099967})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.7075, 'nll': 1.9122236044769287}, 'chosen_samples': [19350, 25309, 35030, 24248, 49157, 49896, 17700, 49324, 29462, 28662], 'chosen_samples_score': [1.1568061599451704, 1.1327214191165327, 1.1306008624773316, 1.1264643522421363, 1.1258553400016549, 1.1182755383666776, 1.1181567310153853, 1.114164869495681, 1.1097206040800658, 1.1080329549096843], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 10.134099811999477, 'batch_acquisition_elapsed_time': 65.55781137000304})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.7595, 'nll': 1.3766789033356905}, 'chosen_samples': [56469, 23331, 5512, 53432, 47652, 3791, 41620, 27878, 45515, 37653], 'chosen_samples_score': [1.0197341525144774, 1.004524117601621, 0.9976647459545437, 0.9730417849591655, 0.9705223553841795, 0.9700140216198988, 0.9649305107739676, 0.9610090096205243, 0.948663732041946, 0.9461596747213418], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 10.226175204996252, 'batch_acquisition_elapsed_time': 65.27124121599627})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.7657, 'nll': 1.2580702861801387}, 'chosen_samples': [44404, 31926, 55064, 1272, 11668, 42709, 17494, 25341, 19641, 4767], 'chosen_samples_score': [0.9804075949360659, 0.9032124031791087, 0.9020213332989806, 0.9015138906562244, 0.8894010813732864, 0.8844836497509706, 0.8730061510206933, 0.8562161322129669, 0.8536327029740939, 0.8529287809119154], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 9.94110415999603, 'batch_acquisition_elapsed_time': 65.63646969600086})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.7621, 'nll': 1.1771939460351466}, 'chosen_samples': [39204, 27473, 29904, 12906, 15472, 47028, 40719, 47365, 12327, 20050], 'chosen_samples_score': [0.8599298578644342, 0.8480591859338267, 0.8354513455251201, 0.8319046303742922, 0.8315863363957875, 0.8308458482279998, 0.825165493623626, 0.8212119531732724, 0.819807897073545, 0.8179607228321121], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 10.196437755999796, 'batch_acquisition_elapsed_time': 65.41008129200054})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.7564, 'nll': 1.1649825422579052}, 'chosen_samples': [12696, 323, 5316, 20001, 56567, 21396, 56212, 56627, 26563, 19178], 'chosen_samples_score': [0.7665230747331084, 0.7567594619395263, 0.7553959771678429, 0.7508653097944651, 0.7440919242967423, 0.737899960454111, 0.7371468789596303, 0.7302759415952449, 0.7293071456978699, 0.7286765130365882], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 10.250055212993175, 'batch_acquisition_elapsed_time': 65.28374613899359})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.8267, 'nll': 0.9040705632489918}, 'chosen_samples': [42020, 21880, 58560, 55503, 46476, 16286, 42363, 16298, 1241, 24692], 'chosen_samples_score': [0.8988900317482936, 0.8919295194497926, 0.8811135785201635, 0.8747048038524533, 0.865926785218121, 0.8652534683496913, 0.8558631914280175, 0.8502569408557161, 0.8485066727549415, 0.8475648221018385], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 10.159491005004384, 'batch_acquisition_elapsed_time': 65.63490175899642})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.8456, 'nll': 0.9047751595470905}, 'chosen_samples': [46447, 54573, 14139, 48349, 26132, 6348, 40702, 49539, 4784, 23406], 'chosen_samples_score': [1.0830956134636602, 1.0784978185567387, 1.074100333004453, 1.0692715464835771, 1.065893268606136, 1.0629403528026158, 1.0494203554340769, 1.03830025097046, 1.0318226037888734, 1.02974270108528], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 13.737978694000049, 'batch_acquisition_elapsed_time': 65.39532159599912})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.8396, 'nll': 0.9584077818532585}, 'chosen_samples': [45801, 7891, 26791, 6428, 19685, 26115, 31847, 15258, 3742, 48495], 'chosen_samples_score': [1.0939034515510149, 1.0307516162487993, 1.017736963049984, 1.0124798734737723, 1.0065501791642482, 1.0035715448466322, 1.0029991413654136, 0.9971364779784164, 0.9959518663952526, 0.9946203342315034], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 13.610374800002319, 'batch_acquisition_elapsed_time': 64.75385083400033})
store['iterations'].append({'num_epochs': 5, 'test_metrics': {'accuracy': 0.8836, 'nll': 0.7074412251769305}, 'chosen_samples': [34524, 42479, 40708, 25986, 55330, 48681, 57300, 20641, 21395, 44438], 'chosen_samples_score': [0.9392125092958314, 0.9264482576628744, 0.9258911177240163, 0.9232895373995695, 0.9082374565377394, 0.9075711978668127, 0.9062882853645259, 0.894969405330897, 0.8934879424071409, 0.8859684747041516], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 11.354509675998997, 'batch_acquisition_elapsed_time': 65.10545686499972})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.8915, 'nll': 0.7003868802701234}, 'chosen_samples': [12934, 42078, 17756, 49137, 7803, 56191, 13827, 33222, 37361, 811], 'chosen_samples_score': [1.0625030882823836, 1.0365296960264458, 1.0346855620901878, 1.029570931614069, 1.0169648347576765, 1.0147957844758944, 1.013638138630803, 1.012623493376029, 1.0116420619143534, 1.0111983215895184], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 17.508446015002846, 'batch_acquisition_elapsed_time': 65.21170584500214})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.8975, 'nll': 0.6501717173292639}, 'chosen_samples': [22083, 20002, 44853, 52169, 40589, 6944, 55513, 11737, 22741, 14901], 'chosen_samples_score': [1.0418173832416349, 1.038064272080514, 1.0279046421892497, 1.0186442758227288, 1.0078080712939985, 1.0055827733335627, 1.0013017018623174, 0.997906710788144, 0.9974205907288319, 0.9871447286678726], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 13.51973630500288, 'batch_acquisition_elapsed_time': 65.61783083699993})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.8925, 'nll': 0.7078353623732329}, 'chosen_samples': [49354, 40678, 59747, 17079, 35232, 28512, 44736, 2000, 8532, 12497], 'chosen_samples_score': [1.1058083550592457, 1.1016687128164484, 1.0545881941446766, 1.05274390910146, 1.0361455251788758, 1.020363952506006, 1.0190550776276206, 1.0068504225251629, 1.0016336852959977, 0.9994657595634173], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 15.572490906000894, 'batch_acquisition_elapsed_time': 65.58890389199951})
store['iterations'].append({'num_epochs': 5, 'test_metrics': {'accuracy': 0.8767, 'nll': 0.7094501106938125}, 'chosen_samples': [13030, 59433, 52294, 28102, 11711, 54316, 26072, 22824, 49060, 11154], 'chosen_samples_score': [0.8370176021755243, 0.8312725344774422, 0.8175589068405533, 0.806327841318213, 0.8062759827665353, 0.79802161762089, 0.7949906950690907, 0.7848596281619358, 0.7842543213325877, 0.7809434604160875], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 12.0973328580003, 'batch_acquisition_elapsed_time': 65.50004369899398})
store['iterations'].append({'num_epochs': 5, 'test_metrics': {'accuracy': 0.8906, 'nll': 0.6683418556895258}, 'chosen_samples': [55485, 3810, 25590, 34597, 38549, 43619, 40892, 42220, 10887, 12345], 'chosen_samples_score': [0.9161478496829567, 0.8883664689316049, 0.872731831942137, 0.8714202107332517, 0.8702426688026481, 0.8699350064223051, 0.8697788012313354, 0.8661429620422558, 0.8644777103718049, 0.8632807425375137], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 11.750170642997546, 'batch_acquisition_elapsed_time': 65.43164339499344})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.8878, 'nll': 0.654462292941749}, 'chosen_samples': [1674, 40530, 57728, 21023, 59294, 49658, 49064, 19362, 17958, 8443], 'chosen_samples_score': [0.9674383677340608, 0.9423195765654079, 0.9378430046675541, 0.9286770879922566, 0.9223872461114264, 0.9157498465247601, 0.9119929135009248, 0.8919857993822147, 0.8795073279095647, 0.8786977176306726], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 15.193486361997202, 'batch_acquisition_elapsed_time': 65.48483946600027})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.9063, 'nll': 0.6096737575686575}, 'chosen_samples': [47132, 4360, 33055, 14405, 34406, 8339, 36072, 1423, 34803, 54885], 'chosen_samples_score': [0.9631940186071889, 0.9068678351959756, 0.8974450016403612, 0.8878291679137058, 0.8862143915925622, 0.8791985694992022, 0.8717512941462191, 0.8682712140470781, 0.8664984713146089, 0.863065091537972], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 13.772473402001197, 'batch_acquisition_elapsed_time': 65.28920866700355})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.9111, 'nll': 0.5986437890856264}, 'chosen_samples': [13031, 32747, 34429, 47587, 37383, 5600, 20869, 4468, 5175, 1075], 'chosen_samples_score': [0.9707168576157251, 0.9483676846426389, 0.9299191145758501, 0.9265739607673471, 0.9093540146849779, 0.9071740477650879, 0.9017361617456846, 0.9015873810526691, 0.8986863085571555, 0.8966172708324118], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 15.41877101600403, 'batch_acquisition_elapsed_time': 65.38004985899897})
store['iterations'].append({'num_epochs': 9, 'test_metrics': {'accuracy': 0.9289, 'nll': 0.5337584410991074}, 'chosen_samples': [17712, 53358, 22783, 10884, 12986, 43126, 26444, 39546, 35864, 5842], 'chosen_samples_score': [1.0725657811848515, 1.0293604102459541, 1.002920315022576, 1.000559595251565, 0.9996386663525723, 0.9987254850475189, 0.9966297053096841, 0.9962841282410039, 0.9951560923871671, 0.9895703270573312], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 19.523697144002654, 'batch_acquisition_elapsed_time': 65.19330962400272})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.9258, 'nll': 0.5170331984193921}, 'chosen_samples': [46613, 32776, 4822, 1160, 52218, 42428, 42112, 59339, 22139, 37469], 'chosen_samples_score': [1.0187845245365446, 0.9708550993882397, 0.9628173607938021, 0.9579564980512488, 0.9493614479188305, 0.9480937243517077, 0.9354337191728245, 0.9294332492397924, 0.917970543328288, 0.9112834466968006], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 17.533752652001567, 'batch_acquisition_elapsed_time': 65.10705329000484})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.9166, 'nll': 0.5734129609236718}, 'chosen_samples': [28491, 52514, 33505, 24722, 21668, 11693, 51832, 8390, 45079, 168], 'chosen_samples_score': [0.826534990056804, 0.8246385542115618, 0.8056946659803159, 0.8054656828760826, 0.8001185710248659, 0.7906919885172388, 0.7890584544152485, 0.7884865209481162, 0.7858161817334328, 0.7818536697259417], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 13.449701393998112, 'batch_acquisition_elapsed_time': 65.00895132499863})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.9341, 'nll': 0.46949114823621513}, 'chosen_samples': [35401, 36000, 49525, 8847, 5774, 28633, 13149, 50086, 34765, 43042], 'chosen_samples_score': [0.8745463929677754, 0.862958468114201, 0.859412225474812, 0.8423353838869376, 0.8346176758193924, 0.8316486681841474, 0.8282323946518204, 0.8220855368825225, 0.8191705783498844, 0.8151006408441345], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 14.839002879001782, 'batch_acquisition_elapsed_time': 64.99694147500122})
store['iterations'].append({'num_epochs': 10, 'test_metrics': {'accuracy': 0.9387, 'nll': 0.46930332227760546}, 'chosen_samples': [8887, 42787, 5013, 45121, 7282, 1642, 52140, 15276, 56347, 59013], 'chosen_samples_score': [1.0807610964191179, 1.027911308443461, 0.9771497540037493, 0.9603273692577374, 0.9508220771700171, 0.9490261110491712, 0.9485211900242434, 0.9470722031176289, 0.9449229537730989, 0.9431019681174001], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 21.166111775004538, 'batch_acquisition_elapsed_time': 64.84093237100024})
store['iterations'].append({'num_epochs': 13, 'test_metrics': {'accuracy': 0.948, 'nll': 0.44484454125952727}, 'chosen_samples': [15460, 21150, 10256, 36230, 49242, 32417, 23551, 9608, 28783, 2381], 'chosen_samples_score': [1.0689930388413875, 1.0493948567716478, 1.041006674343012, 1.0362283761432902, 1.0354273060802734, 1.027764558831636, 1.0193387944238586, 1.0145850373739982, 1.0116376567318395, 1.0009501799278753], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 26.624073841005156, 'batch_acquisition_elapsed_time': 64.79309489599837})
store['iterations'].append({'num_epochs': 9, 'test_metrics': {'accuracy': 0.9511, 'nll': 0.4149655387926698}, 'chosen_samples': [42415, 12651, 20190, 33812, 51764, 31757, 3470, 16787, 27880, 52686], 'chosen_samples_score': [1.0350268678409889, 0.9541804866532505, 0.9524643451883161, 0.9461691100709799, 0.9399308456142037, 0.9333837380367516, 0.9304092383654388, 0.9261743687386684, 0.9260786695764686, 0.9206744332868549], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 19.234617813002842, 'batch_acquisition_elapsed_time': 65.11369561700121})
store['iterations'].append({'num_epochs': 9, 'test_metrics': {'accuracy': 0.9489, 'nll': 0.45188487715560194}, 'chosen_samples': [33338, 32047, 13969, 57714, 44123, 29361, 12305, 19188, 12184, 43176], 'chosen_samples_score': [1.0374612623436603, 1.0008831761887835, 0.9942341170341059, 0.9912228247184336, 0.9601400740336565, 0.9471608141177953, 0.9392211600923588, 0.938177508060319, 0.9206380504111353, 0.9151822369835756], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 18.941440255002817, 'batch_acquisition_elapsed_time': 65.26802317400143})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.9454, 'nll': 0.44281340414535997}, 'chosen_samples': [41602, 49656, 10260, 13729, 57523, 45911, 42703, 8447, 32814, 53116], 'chosen_samples_score': [0.900050168437611, 0.8688764846961299, 0.8575155044012454, 0.8561486611317501, 0.8477005737733823, 0.8455238981188531, 0.8417208013210316, 0.841116852523336, 0.8335369610732908, 0.8316503759569609], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 15.799470532998384, 'batch_acquisition_elapsed_time': 65.32674619099998})
store['iterations'].append({'num_epochs': 10, 'test_metrics': {'accuracy': 0.9518, 'nll': 0.4289513225716353}, 'chosen_samples': [56662, 46412, 26850, 32880, 52894, 19089, 56454, 10028, 43043, 5370], 'chosen_samples_score': [1.028856151095579, 0.9964653578395372, 0.9841552955857119, 0.9616589493246651, 0.9481613309893546, 0.9419578950931945, 0.9392870903159599, 0.9370561128842358, 0.9324548714160275, 0.9322162942846768], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 21.128262197002186, 'batch_acquisition_elapsed_time': 64.9429891960026})