import sys
from math import dist
import numpy as np
import csv

#pathOne = ['R8','U5','L5','D3']
#pathTwo = ['U7','R6','D4','L4']
pathOne = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
pathTwo = ['U62','R66','U55','R34','D71','R55','D58','R83']
#pathOne = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
#pathTwo = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']
#pathOne = ['U4','R3']
#pathTwo = ['R1','U3','R2','D1','L1','U3','R1','D2','L2']
#pathOne = ['R1009', 'U263', 'L517', 'U449', 'L805', 'D78', 'L798', 'D883', 'L777', 'D562', 'R652', 'D348', 'R999', 'D767', 'L959', 'U493', 'R59', 'D994', 'L225', 'D226', 'R634', 'D200', 'R953', 'U343', 'L388', 'U158', 'R943', 'U544', 'L809', 'D785', 'R618', 'U499', 'L476', 'U600', 'L452', 'D693', 'L696', 'U764', 'L927', 'D346', 'L863', 'D458', 'L789', 'U268', 'R586', 'U884', 'L658', 'D371', 'L910', 'U178', 'R524', 'U169', 'R973', 'D326', 'R483', 'U233', 'R26', 'U807', 'L246', 'D711', 'L641', 'D75', 'R756', 'U365', 'R203', 'D377', 'R624', 'U430', 'L422', 'U367', 'R547', 'U294', 'L916', 'D757', 'R509', 'D332', 'R106', 'D401', 'L181', 'U5', 'L443', 'U197', 'R406', 'D829', 'R878', 'U35', 'L958', 'U31', 'L28', 'D362', 'R188', 'D582', 'R358', 'U750', 'R939', 'D491', 'R929', 'D513', 'L541', 'U418', 'R861', 'D639', 'L917', 'U582', 'R211', 'U725', 'R711', 'D718', 'L673', 'U921', 'L157', 'U83', 'L199', 'U501', 'L66', 'D993', 'L599', 'D947', 'L26', 'U237', 'L981', 'U833', 'L121', 'U25', 'R641', 'D372', 'L757', 'D645', 'R287', 'U390', 'R274', 'U964', 'R288', 'D209', 'R109', 'D364', 'R983', 'U715', 'L315', 'U758', 'R36', 'D500', 'R626', 'U893', 'L840', 'U716', 'L606', 'U831', 'L969', 'D643', 'L300', 'D838', 'R31', 'D751', 'L632', 'D702', 'R468', 'D7', 'L169', 'U149', 'R893', 'D33', 'R816', 'D558', 'R152', 'U489', 'L237', 'U415', 'R434', 'D472', 'L198', 'D874', 'L351', 'U148', 'R761', 'U809', 'R21', 'D25', 'R586', 'D338', 'L568', 'U20', 'L157', 'U221', 'L26', 'U424', 'R261', 'D227', 'L551', 'D754', 'L90', 'U110', 'L791', 'U433', 'R840', 'U323', 'R240', 'U124', 'L723', 'D418', 'R938', 'D173', 'L160', 'U293', 'R773', 'U204', 'R192', 'U958', 'L472', 'D703', 'R556', 'D168', 'L263', 'U574', 'L845', 'D932', 'R165', 'D348', 'R811', 'D834', 'R960', 'U877', 'R935', 'D141', 'R696', 'U748', 'L316', 'U236', 'L796', 'D566', 'R524', 'U449', 'R378', 'U480', 'L79', 'U227', 'R867', 'D185', 'R474', 'D757', 'R366', 'U153', 'R882', 'U252', 'R861', 'U900', 'R28', 'U381', 'L845', 'U642', 'L849', 'U352', 'R134', 'D294', 'R788', 'D406', 'L693', 'D697', 'L433', 'D872', 'R78', 'D364', 'R240', 'U995', 'R48', 'D681', 'R727', 'D825', 'L583', 'U44', 'R743', 'D929', 'L616', 'D262', 'R997', 'D15', 'R575', 'U341', 'R595', 'U889', 'R254', 'U76', 'R962', 'D944', 'R724', 'D261', 'R608', 'U753', 'L389', 'D324', 'L569', 'U308', 'L488', 'D358', 'L695', 'D863', 'L712', 'D978', 'R149', 'D177', 'R92']
#pathTwo = ['L1003', 'D960', 'L10', 'D57', 'R294', 'U538', 'R867', 'D426', 'L524', 'D441', 'R775', 'U308', 'R577', 'D785', 'R495', 'U847', 'R643', 'D895', 'R448', 'U685', 'L253', 'U312', 'L312', 'U753', 'L89', 'U276', 'R799', 'D923', 'L33', 'U595', 'R400', 'U111', 'L664', 'D542', 'R171', 'U709', 'L809', 'D713', 'L483', 'U918', 'L14', 'U854', 'L150', 'D69', 'L158', 'D500', 'L91', 'D800', 'R431', 'D851', 'L798', 'U515', 'L107', 'U413', 'L94', 'U390', 'L17', 'U221', 'L999', 'D546', 'L191', 'U472', 'L568', 'U114', 'L913', 'D743', 'L713', 'D215', 'L569', 'D674', 'L869', 'U549', 'L789', 'U259', 'L330', 'D76', 'R243', 'D592', 'L646', 'U880', 'L363', 'U542', 'L464', 'D955', 'L107', 'U473', 'R818', 'D786', 'R852', 'U968', 'R526', 'D78', 'L275', 'U891', 'R480', 'U991', 'L981', 'D391', 'R83', 'U691', 'R689', 'D230', 'L217', 'D458', 'R10', 'U736', 'L317', 'D145', 'R902', 'D428', 'R344', 'U334', 'R131', 'D739', 'R438', 'D376', 'L652', 'U304', 'L332', 'D452', 'R241', 'D783', 'R82', 'D317', 'R796', 'U323', 'R287', 'D487', 'L302', 'D110', 'R233', 'U631', 'R584', 'U973', 'L878', 'D834', 'L930', 'U472', 'R120', 'U78', 'R806', 'D21', 'L521', 'U988', 'R251', 'D817', 'R44', 'D789', 'R204', 'D669', 'R616', 'D96', 'R624', 'D891', 'L532', 'U154', 'R438', 'U469', 'R785', 'D431', 'R945', 'U649', 'R670', 'D11', 'R840', 'D521', 'L235', 'D69', 'L551', 'D266', 'L454', 'U807', 'L885', 'U590', 'L647', 'U763', 'R449', 'U194', 'R68', 'U809', 'L884', 'U962', 'L476', 'D648', 'L139', 'U96', 'L300', 'U351', 'L456', 'D202', 'R168', 'D698', 'R161', 'U834', 'L273', 'U47', 'L8', 'D157', 'L893', 'D200', 'L454', 'U723', 'R886', 'U92', 'R474', 'U262', 'L190', 'U110', 'L407', 'D723', 'R786', 'D786', 'L572', 'D915', 'L904', 'U744', 'L820', 'D663', 'R205', 'U878', 'R186', 'U247', 'L616', 'D386', 'R582', 'U688', 'L349', 'D399', 'R702', 'U132', 'L276', 'U866', 'R851', 'D633', 'R468', 'D263', 'R678', 'D96', 'L50', 'U946', 'R349', 'D482', 'R487', 'U525', 'R464', 'U977', 'L499', 'D187', 'R546', 'U708', 'L627', 'D470', 'R673', 'D886', 'L375', 'U616', 'L503', 'U38', 'L775', 'D8', 'L982', 'D556', 'R159', 'U680', 'L124', 'U777', 'L640', 'D607', 'R248', 'D671', 'L65', 'D290', 'R445', 'U778', 'L650', 'U679', 'L846', 'D1', 'L769', 'U659', 'R734', 'D962', 'R588', 'U178', 'R888', 'D753', 'R223', 'U318', 'L695', 'D586', 'R430', 'D61', 'R105', 'U801', 'R953', 'U721', 'L856', 'U769', 'R937', 'D335', 'R895']
#pathOne = ['R997', 'U849', 'R349', 'U641', 'R581', 'D39', 'R285', 'U139', 'R455', 'D346', 'L965', 'D707', 'R393', 'D302', 'L263', 'U58', 'R950', 'U731', 'R858', 'D748', 'R302', 'U211', 'R588', 'D441', 'L153', 'D417', 'R861', 'U775', 'R777', 'U204', 'R929', 'U868', 'L62', 'U163', 'R841', 'D214', 'L648', 'U626', 'R501', 'D751', 'L641', 'D961', 'L23', 'D430', 'L73', 'D692', 'R49', 'U334', 'L601', 'U996', 'R444', 'D658', 'R633', 'D30', 'L861', 'D811', 'R10', 'D394', 'R9', 'U227', 'L848', 'U420', 'L378', 'D622', 'L501', 'U397', 'R855', 'U369', 'R615', 'U591', 'L674', 'D166', 'L181', 'U61', 'L224', 'U463', 'L203', 'U594', 'R93', 'U614', 'L959', 'U198', 'L689', 'D229', 'L674', 'U255', 'R843', 'D382', 'R538', 'U923', 'L960', 'D775', 'L879', 'U97', 'R137', 'U665', 'L340', 'D941', 'L775', 'D57', 'R852', 'D167', 'R980', 'U704', 'L843', 'U989', 'L611', 'D32', 'L724', 'D790', 'L32', 'U984', 'L39', 'U671', 'L994', 'U399', 'R475', 'D85', 'L322', 'D936', 'R117', 'D261', 'R705', 'D696', 'L523', 'D433', 'L239', 'U477', 'L247', 'D465', 'R560', 'D902', 'L589', 'U682', 'R645', 'U376', 'L989', 'D121', 'L215', 'U514', 'R519', 'U407', 'L218', 'D444', 'R704', 'D436', 'L680', 'U759', 'R937', 'U400', 'R533', 'D860', 'R782', 'D233', 'R840', 'D549', 'L508', 'U380', 'L992', 'U406', 'L213', 'D403', 'L413', 'D532', 'L429', 'U186', 'R262', 'U313', 'L913', 'U873', 'L838', 'D882', 'R851', 'U70', 'R185', 'D131', 'R945', 'D595', 'L330', 'U446', 'R88', 'D243', 'L561', 'D952', 'R982', 'D395', 'L708', 'U459', 'L82', 'D885', 'L996', 'U955', 'L406', 'U697', 'L183', 'U266', 'L878', 'D839', 'R843', 'D891', 'R118', 'U772', 'R590', 'D376', 'L500', 'U370', 'R607', 'D12', 'L310', 'D436', 'L602', 'D365', 'R886', 'U239', 'L471', 'D418', 'L122', 'U18', 'R879', 'D693', 'R856', 'U848', 'L657', 'D911', 'L63', 'U431', 'R41', 'U752', 'R919', 'U323', 'L61', 'D263', 'L370', 'D85', 'R929', 'D213', 'R350', 'U818', 'R458', 'D912', 'R509', 'U394', 'L734', 'U49', 'R810', 'D87', 'L870', 'U658', 'R499', 'U550', 'L402', 'U244', 'L112', 'U859', 'R836', 'U951', 'R222', 'D944', 'L691', 'D731', 'R742', 'D52', 'R984', 'D453', 'L514', 'U692', 'R812', 'U35', 'L844', 'D177', 'L110', 'D22', 'R61', 'U253', 'R618', 'D51', 'R163', 'U835', 'R704', 'U148', 'R766', 'U297', 'R457', 'D170', 'L104', 'D441', 'R330', 'D330', 'R989', 'D538', 'R668', 'D811', 'R62', 'D67', 'L470', 'D526', 'R788', 'U376', 'R708', 'U3', 'R961']
#pathTwo = ['L1009', 'D381', 'R970', 'U429', 'L230', 'D909', 'R516', 'D957', 'R981', 'U609', 'L480', 'D139', 'L861', 'U168', 'L48', 'U620', 'R531', 'D466', 'L726', 'D380', 'R977', 'D454', 'L318', 'D397', 'R994', 'U402', 'L77', 'U93', 'L359', 'D72', 'R968', 'D956', 'L174', 'D22', 'R218', 'U619', 'R593', 'U32', 'L154', 'U55', 'L169', 'U415', 'L171', 'U666', 'R617', 'U109', 'L265', 'U773', 'R541', 'D808', 'L797', 'U478', 'R731', 'U379', 'R311', 'D137', 'L806', 'U298', 'R362', 'D458', 'L254', 'D539', 'R700', 'U853', 'R246', 'D588', 'L28', 'U203', 'L432', 'U946', 'R663', 'D408', 'R974', 'U59', 'L683', 'D36', 'L139', 'U738', 'L780', 'U414', 'L401', 'D93', 'R212', 'D973', 'L710', 'U892', 'L357', 'D177', 'R823', 'D4', 'R46', 'D924', 'L235', 'D898', 'R67', 'U220', 'L592', 'U87', 'R94', 'U584', 'R979', 'D843', 'L299', 'D648', 'L491', 'U360', 'R824', 'D245', 'L944', 'D24', 'R616', 'U975', 'L4', 'U42', 'L984', 'U181', 'R902', 'D835', 'L687', 'D413', 'L767', 'U632', 'L754', 'U270', 'R413', 'U51', 'L825', 'D377', 'L596', 'U960', 'L378', 'U706', 'L859', 'D708', 'L156', 'D991', 'L814', 'U351', 'R923', 'D749', 'L16', 'D651', 'R20', 'D86', 'R801', 'U811', 'L228', 'U161', 'L871', 'U129', 'R215', 'U235', 'L784', 'U896', 'R94', 'U145', 'R822', 'U494', 'R248', 'D98', 'R494', 'U156', 'L495', 'U311', 'R66', 'D873', 'L294', 'D620', 'L885', 'U395', 'R778', 'D227', 'R966', 'U756', 'L694', 'D707', 'R983', 'D950', 'R706', 'D730', 'R415', 'U886', 'L465', 'D622', 'L13', 'D938', 'R324', 'D464', 'R723', 'U804', 'R942', 'D635', 'L729', 'D317', 'L522', 'U469', 'R550', 'D141', 'R302', 'U999', 'L642', 'U509', 'R431', 'D380', 'R18', 'D676', 'R449', 'D759', 'L495', 'U901', 'R1', 'D745', 'L655', 'U449', 'L439', 'D818', 'R55', 'D541', 'R420', 'U764', 'L426', 'D176', 'L520', 'U3', 'L663', 'D221', 'L80', 'D449', 'L987', 'U349', 'L71', 'U632', 'L887', 'D231', 'R655', 'D208', 'R698', 'D639', 'R804', 'U616', 'R532', 'U846', 'R363', 'D141', 'R659', 'U470', 'L798', 'U144', 'L675', 'U483', 'L944', 'U380', 'L329', 'U72', 'L894', 'D130', 'R53', 'U109', 'R610', 'U770', 'R778', 'U493', 'R972', 'D340', 'L866', 'U980', 'L305', 'D812', 'R130', 'D954', 'R253', 'D33', 'L912', 'U950', 'L438', 'D680', 'R891', 'U725', 'R171', 'D587', 'R549', 'D367', 'L4', 'U313', 'R522', 'D128', 'L711', 'D405', 'L769', 'D496', 'L527', 'U373', 'R725', 'D261', 'L268', 'D939', 'L902', 'D58', 'L858', 'D190', 'L442']

# Function to get max coord value
# axis must be X or Y
def GetMaxAxis(path, axis):
    max_coord = 0
    cur = 0
    if axis == 'X':
        for point in path:
            if(point[0] == 'R'):
                cur += int(point[1:])
                max_coord = max(max_coord, cur)
            elif(point[0] == 'L'):
                cur -= int(point[1:])
                max_coord = max(max_coord, cur)
    elif axis == 'Y':
        for point in path:
            if(point[0] == 'U'):
                cur += int(point[1:])
                max_coord = max(max_coord, cur)
            elif(point[0] == 'D'):
                cur -= int(point[1:])
                max_coord = max(max_coord, cur)
    return max_coord

def InitGrid(x, y):
    grid = np.zeros((x,y))
    return grid

# Returns a new grid with the path
# pathNum is the integer representation of the path (i.e. pathOne is 1)
def AddPathToGrid(path, grid, pathNum, o):
    curHead = [0,0]
    curHead[0] = o[0]
    curHead[1] = o[1]
    print(curHead)
    for point in path:
        if(point[0] == 'R'):
            for x in range(int(point[1:])):
                curHead[0] += 1
                grid[curHead[0]][curHead[1]] += pathNum
        if(point[0] == 'L'):
            for x in range(int(point[1:]), 0, -1):
                curHead[0] -= 1
                grid[curHead[0]][curHead[1]] += pathNum
        if(point[0] == 'U'):
            for y in range(int(point[1:])):
                curHead[1] += 1
                grid[curHead[0]][curHead[1]] += pathNum
        if(point[0] == 'D'):
            for y in range(int(point[1:]), 0, -1):
                curHead[1] -= 1
                grid[curHead[0]][curHead[1]] += pathNum

def GridIntersectionPoints(g):
    points = []
    x = g.shape[0]
    y = g.shape[1]
    for i in range(x):
        for j in range(y):
            if g[i][j] == 3:
                points.append((i,j))
    return points

# Requires the grid as an argument
def ManhattenDistance(g, o):
    # Don't have a grid over 4 million in any direction
    min_dist = 4000000
    # Find the points of intersection
    intersect_points = GridIntersectionPoints(g)
    for point in intersect_points:
        #min_dist = min(min_dist, point[0] + point[1])
        min_dist = min(min_dist, abs((point[0] - o[0]) + (point[1] - o[1])))
    return min_dist

def PrintToFile(g,x,y):
    row = []
    with open("graph.csv", 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        for i in range(x):
            for j in range(y):
                row.append(str(g[i][j]))
            csvwriter.writerow(row)
            row = []

# Get the max x and y for the grid
x = max(GetMaxAxis(pathOne, 'X'), GetMaxAxis(pathTwo, 'X'))
y = max(GetMaxAxis(pathOne, 'Y'), GetMaxAxis(pathTwo, 'Y'))

print("X: " + str(x))
print("Y: " + str(y))

# Initialize the grid
grid = InitGrid(x + 1,y + 1)
origin = [int((x + 1)/2),int((y + 1)/2)]


AddPathToGrid(pathOne, grid, 1, origin)
AddPathToGrid(pathTwo, grid, 2, origin)
#PrintToFile(grid,x,y)
print("##### Grid prints with X and Y inverted -- thanks python #####")
#print(grid)
print("##### Intersection Points #####")
#print(GridIntersectionPoints(grid))
print("##### ManhattenDistance #####")
print(ManhattenDistance(grid, origin))
