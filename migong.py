import argparse, time, os
from random import choice, randint
from support.files.picture import PICTURE


class MAZE:
    CMD = "maze"
    WALLDEPTH = 10

    class MODEL:
        RBKT = 0
        PRIM = 1
        RDVS = 2
        CALC = 3
        MAXVAL = 3

    class DIRECT:
        UP = 0
        DOWN = 1
        LEFT = 2
        RIGHT = 3

    PADDING = 10
    COLOR_EMT = ["#434343", "#FFFFFF", "#3C78D8", "#FFFFFF"]

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.table = None
        self.times = [0, 0]
        # self.screen = SCREEN(column * 10 + MAZE.PADDING * 2)
        self.picture = PICTURE(size=20)

    def create(self, model=MODEL.RBKT):
        def getWallRules(row, column):
            kptwall = [MAZE.DIRECT.UP, MAZE.DIRECT.RIGHT, MAZE.DIRECT.DOWN, MAZE.DIRECT.LEFT]
            index = row * self.column + column
            if (index < self.column): kptwall.remove(MAZE.DIRECT.UP)
            if ((index % self.column + 1) == self.column): kptwall.remove(MAZE.DIRECT.RIGHT)
            if (index + self.column >= self.row * self.column): kptwall.remove(MAZE.DIRECT.DOWN)
            if (index % self.column == 0): kptwall.remove(MAZE.DIRECT.LEFT)
            return kptwall

        def newTable(row, column):
            tables = []
            index = 0
            for r in range(self.row):
                columns = []
                for c in range(self.column):
                    room = {"id": index, "row": r, "column": c}
                    room["wid"] = getWallRules(r, c)
                    columns.append(room)
                    index += 1
                tables.append(columns)
            return tables

        def connectNeighbor(room, wid, broken=True):
            row = room["row"]
            column = room["column"]
            if (wid == MAZE.DIRECT.UP):
                wid = MAZE.DIRECT.DOWN
                row -= 1
            elif (wid == MAZE.DIRECT.RIGHT):
                wid = MAZE.DIRECT.LEFT
                column += 1
            elif (wid == MAZE.DIRECT.DOWN):
                wid = MAZE.DIRECT.UP
                row += 1
            elif (wid == MAZE.DIRECT.LEFT):
                wid = MAZE.DIRECT.RIGHT
                column -= 1
            neighbor = self.table[row][column]
            if (broken): neighbor["wid"].remove(wid)
            return neighbor

        def getValidWalls(room, lst):
            ret = []
            for wid in room["wid"]:
                neighbor = connectNeighbor(room, wid, False)
                if (neighbor not in lst): ret.append(wid)
            return ret

        def brokenWall(room, historyLst, reachLst):
            walls = getValidWalls(room, reachLst)
            if (walls):
                wid = choice(walls)
                room["wid"].remove(wid)
                neighbor = connectNeighbor(room, wid)
                reachLst.append(neighbor)
                if (model == MAZE.MODEL.PRIM): historyLst.append(neighbor)
                if (model == MAZE.MODEL.RBKT): historyLst.append(room)
                if (model == MAZE.MODEL.RBKT): return brokenWall(neighbor, historyLst, reachLst)
            return not not walls

        def excludeNoWallRoom(lst, refLst):
            for room in lst.copy():
                if (not getValidWalls(room, refLst)): lst.remove(room)

        self.model = model
        if (model == MAZE.MODEL.CALC): model = MAZE.MODEL.PRIM
        reachableRooms = []
        viewHistoryRooms = []
        self.table = newTable(self.row, self.column)
        start = time.perf_counter()
        if (model == MAZE.MODEL.RDVS):
            pass
        else:
            room = self.table[0][0]
            reachableRooms.append(room)
            if (model == MAZE.MODEL.PRIM): viewHistoryRooms.append(room)
            while (len(reachableRooms) < (self.row * self.column)):
                ret = brokenWall(room, viewHistoryRooms, reachableRooms)
                if (model == MAZE.MODEL.PRIM):
                    excludeNoWallRoom(viewHistoryRooms, reachableRooms)
                    if (viewHistoryRooms):
                        room = choice(viewHistoryRooms)
                    else:
                        break
                if (model == MAZE.MODEL.RBKT): room = viewHistoryRooms.pop()
            self.times[0] = time.perf_counter() - start
        self.__findRoute()

    def __findRoute(self):
        def getMiniFValueArray(lst1, lst2):
            f1 = self.row * self.column
            f2 = f1
            mini = None
            if (lst1): f1 = lst1[0]["f"]
            if (lst2): f2 = lst2[0]["f"]
            if (f1 <= f2):
                mini = lst1[0]
                lst1.pop(0)
                autoRemoveSameIdRoom(mini["id"], lst2)
            else:
                mini = lst2[0]
                lst2.pop(0)
            return mini

        def autoRemoveSameIdRoom(id, lst):
            for room in lst.copy():
                if (room["id"] == id): lst.remove(room)

        def getReachableNeighbor(room):
            lst = []
            if (MAZE.DIRECT.UP not in room["wid"]): calcF(room, -1, 0, lst)
            if (MAZE.DIRECT.RIGHT not in room["wid"]): calcF(room, 0, 1, lst)
            if (MAZE.DIRECT.DOWN not in room["wid"]): calcF(room, 1, 0, lst)
            if (MAZE.DIRECT.LEFT not in room["wid"]): calcF(room, 0, -1, lst)
            lst.sort(key=(lambda x: x["f"]))
            return lst

        def calcF(room, offsetRow, offsetColumn, lst):
            row = room["row"] + offsetRow
            column = room["column"] + offsetColumn
            if (row < 0 or column < 0): return
            if (row >= self.row or column >= self.column): return
            nextRoom = self.table[row][column].copy()
            nextRoom["step"] = room["step"] + 1
            nextRoom["f"] = self.column + self.row - column - row - 1 + room["step"]
            nextRoom["parent"] = room["id"]
            lst.append(nextRoom)

        def isReached(closeLst):
            ret = False
            for room in closeLst:
                if (room["id"] == self.row * self.column - 1):
                    ret = True
                    break
            return ret

        def getDirectFlag(lastRoomId, currentRoomId):
            r1 = lastRoomId // self.column
            c1 = lastRoomId % self.column
            r2 = currentRoomId // self.column
            c2 = currentRoomId % self.column
            if (r1 > r2):
                flag = MAZE.DIRECT.UP
            elif (r1 < r2):
                flag = MAZE.DIRECT.DOWN
            elif (c1 > c2):
                flag = MAZE.DIRECT.LEFT
            else:
                flag = MAZE.DIRECT.RIGHT
            return flag

        def track(table):
            room = table[-1]
            self.table[room["row"]][room["column"]]["flag"] = MAZE.DIRECT.RIGHT
            parentId = room["parent"]
            while (parentId):
                for parent in table:
                    if (parent["id"] == parentId):
                        self.table[parent["row"]][parent["column"]]["flag"] = getDirectFlag(parentId, room["id"])
                        room = parent
                        parentId = room["parent"]
                        break
            self.table[0][0]["flag"] = getDirectFlag(0, room["id"])

        def removeClosedRoom(lst1, lst2):
            lst = lst1.copy()
            for r in lst1:
                for c in lst2:
                    if (r["id"] == c["id"]): lst.remove(r)
            return lst

        start = time.perf_counter()
        openList = []
        closeList = []
        room = self.table[0][0].copy()
        room["step"] = 0
        room["f"] = self.column + self.row - 1
        closeList.append(room)
        while (not isReached(closeList)):
            lst = getReachableNeighbor(room)
            lst = removeClosedRoom(lst, closeList)
            if (len(lst) == 0 and len(openList) == 0): break
            room = getMiniFValueArray(lst, openList)
            openList.extend(lst)
            openList.sort(key=(lambda x: x["f"]))
            closeList.append(room)
        track(closeList)
        self.times[1] = time.perf_counter() - start

    def get(self, *, route=False, fmt="img"):
        def drawRoom(x, y, room):
            if (self.model == MAZE.MODEL.CALC):
                x, y = self.picture.drawEllipse(x + MAZE.WALLDEPTH * 2, y + MAZE.WALLDEPTH * 2, MAZE.WALLDEPTH * 2,
                                                width=2)
                x -= MAZE.WALLDEPTH // 2
                y -= MAZE.WALLDEPTH // 2
            else:
                self.picture.drawRectangle(x, y, MAZE.WALLDEPTH * 3, MAZE.WALLDEPTH * 3, fill="black")
                self.picture.drawRectangle(x + MAZE.WALLDEPTH, y + MAZE.WALLDEPTH, MAZE.WALLDEPTH, MAZE.WALLDEPTH,
                                           fill="white")
                if (MAZE.DIRECT.LEFT not in room["wid"]): self.picture.drawRectangle(x, y + MAZE.WALLDEPTH,
                                                                                     MAZE.WALLDEPTH, MAZE.WALLDEPTH,
                                                                                     fill="white")
                if (MAZE.DIRECT.RIGHT not in room["wid"]): self.picture.drawRectangle(x + MAZE.WALLDEPTH * 2,
                                                                                      y + MAZE.WALLDEPTH,
                                                                                      MAZE.WALLDEPTH, MAZE.WALLDEPTH,
                                                                                      fill="white")
                if (MAZE.DIRECT.UP not in room["wid"]): self.picture.drawRectangle(x + MAZE.WALLDEPTH, y,
                                                                                   MAZE.WALLDEPTH, MAZE.WALLDEPTH,
                                                                                   fill="white")
                if (MAZE.DIRECT.DOWN not in room["wid"]): self.picture.drawRectangle(x + MAZE.WALLDEPTH,
                                                                                     y + MAZE.WALLDEPTH * 2,
                                                                                     MAZE.WALLDEPTH, MAZE.WALLDEPTH,
                                                                                     fill="white")
                x += MAZE.WALLDEPTH
                y += MAZE.WALLDEPTH
            room["pos"] = (x, y)

        def drawMaze(startX, startY, width, height):
            x = startX
            y = startY
            firstLine = True
            for row in self.table:
                if (self.model == MAZE.MODEL.CALC):
                    linex, liney = self.picture.calcEllipsePoint(x + MAZE.WALLDEPTH * 2, y + MAZE.WALLDEPTH * 2,
                                                                 MAZE.WALLDEPTH * 2, width=2)
                    linex -= MAZE.WALLDEPTH // 2
                    liney -= MAZE.WALLDEPTH // 2
                    self.picture.drawRectangle(linex, liney, width - MAZE.WALLDEPTH * 4, MAZE.WALLDEPTH, fill="gray")
                for room in row:
                    if (self.model == MAZE.MODEL.CALC and firstLine):
                        linex, liney = self.picture.calcEllipsePoint(x + MAZE.WALLDEPTH * 2, y + MAZE.WALLDEPTH * 2,
                                                                     MAZE.WALLDEPTH * 2, width=2)
                        linex -= MAZE.WALLDEPTH // 2
                        liney -= MAZE.WALLDEPTH // 2
                        self.picture.drawRectangle(linex, liney, MAZE.WALLDEPTH, height - MAZE.WALLDEPTH * 4,
                                                   fill="gray")
                    drawRoom(x, y, room)
                    x += MAZE.WALLDEPTH * 2
                    if (self.model == MAZE.MODEL.CALC): x += MAZE.WALLDEPTH * 4
                firstLine = False
                x = startX
                y += MAZE.WALLDEPTH * 2
                if (self.model == MAZE.MODEL.CALC): y += MAZE.WALLDEPTH * 4

        def fillRoute():
            x = 0
            y = 0
            for row in self.table:
                for room in row:
                    if ("flag" in room):
                        x = room["pos"][0]
                        y = room["pos"][1]
                        if (self.model == MAZE.MODEL.CALC):
                            x += MAZE.WALLDEPTH // 2
                            y += MAZE.WALLDEPTH // 2
                            self.picture.drawEllipse(x, y, MAZE.WALLDEPTH * 2, width=2, fill="red")
                        else:
                            self.picture.drawRectangle(x, y, MAZE.WALLDEPTH, MAZE.WALLDEPTH, fill="red")
                            if (room["flag"] == MAZE.DIRECT.UP): self.picture.drawRectangle(x, y - MAZE.WALLDEPTH,
                                                                                            MAZE.WALLDEPTH,
                                                                                            MAZE.WALLDEPTH, fill="red")
                            if (room["flag"] == MAZE.DIRECT.LEFT): self.picture.drawRectangle(x - MAZE.WALLDEPTH, y,
                                                                                              MAZE.WALLDEPTH,
                                                                                              MAZE.WALLDEPTH,
                                                                                              fill="red")
                            if (room["flag"] == MAZE.DIRECT.DOWN): self.picture.drawRectangle(x, y + MAZE.WALLDEPTH,
                                                                                              MAZE.WALLDEPTH,
                                                                                              MAZE.WALLDEPTH,
                                                                                              fill="red")
                            if (room["flag"] == MAZE.DIRECT.RIGHT): self.picture.drawRectangle(x + MAZE.WALLDEPTH, y,
                                                                                               MAZE.WALLDEPTH,
                                                                                               MAZE.WALLDEPTH,
                                                                                               fill="red")

        def fillRandomCalc(target):
            method = randint(0, 1)
            calc = ""
            for row in self.table:
                for room in row:
                    firstNum = randint(1, 10)
                    if ("flag" in room):
                        if (method): secondNum = target - firstNum
                        if (not method): secondNum = target + firstNum
                    else:
                        if (method): secondNum = randint(1, 10)
                        if (not method): secondNum = randint(firstNum, 10)
                    if (method):
                        if (secondNum >= 0):
                            calc = "{}+{}".format(firstNum, secondNum)
                        else:
                            calc = "{}{}".format(firstNum, secondNum)
                    if (not method): calc = "{}-{}".format(secondNum, firstNum)
                    self.picture.drawText(room["pos"][0] - MAZE.WALLDEPTH, room["pos"][1], calc, color="black",
                                          fontsize=13)

        def fillBoarder(x, y, width, height, roomSize, route):
            self.picture.drawRectangle(x, y, width, MAZE.WALLDEPTH, fill="black")
            self.picture.drawRectangle(x, y, MAZE.WALLDEPTH, height, fill="black")
            self.picture.drawRectangle(x + width, y, MAZE.WALLDEPTH, height, fill="black")
            self.picture.drawRectangle(x, y + height, width, MAZE.WALLDEPTH, fill="black")
            fillcolor = "white"
            if (route): fillcolor = "red"
            self.picture.drawRectangle(self.table[0][0]["pos"][0] - MAZE.WALLDEPTH, self.table[0][0]["pos"][1],
                                       MAZE.WALLDEPTH, MAZE.WALLDEPTH, fill=fillcolor)
            self.picture.drawRectangle(self.table[-1][-1]["pos"][0] + MAZE.WALLDEPTH, self.table[-1][-1]["pos"][1],
                                       MAZE.WALLDEPTH, MAZE.WALLDEPTH, fill=fillcolor)

        def calcMazeSize():
            roomSize = 3
            if (self.model == MAZE.MODEL.CALC): roomSize = 5
            width = self.column * (roomSize - 1) * MAZE.WALLDEPTH
            height = self.row * (roomSize - 1) * MAZE.WALLDEPTH
            if (self.model == MAZE.MODEL.CALC):
                width += (self.column - 1) * MAZE.WALLDEPTH * 2
                height += (self.row - 1) * MAZE.WALLDEPTH * 2
            return width, height, roomSize

        desc = "基于 {} 算法".format(self.getAlgorithmName())
        if (route): desc = "{} 迷宫的寻路结果".format(self.getAlgorithmName())
        if (self.model == MAZE.MODEL.CALC):
            target = randint(5, 20)
            desc = "沿着答案等于 {} 的圆圈绘制出走出迷宫的路线".format(target)
            leftImgSize = self.picture.calcImageSize(os.path.join(os.path.dirname(__file__), "res/img/sm01.png"), 0.3)
            rightImgSize = self.picture.calcImageSize(os.path.join(os.path.dirname(__file__), "res/img/sm02.png"), 0.5)
        mazeWidth, mazeHeight, roomSize = calcMazeSize()
        imgWidth = max(self.picture.getTextWidth(desc), mazeWidth) + MAZE.PADDING * 4
        imgHeight = mazeHeight + MAZE.PADDING * 9 + self.picture.getFontHeight() * 2
        if (self.model == MAZE.MODEL.CALC):
            imgWidth += leftImgSize[0] + rightImgSize[0]
            imgHeight += rightImgSize[1]
        imgWidth = int(imgWidth)
        imgHeight = int(imgHeight)
        self.picture.createCanvas(imgWidth, imgHeight)
        x, y = self.picture.drawText(MAZE.PADDING, MAZE.PADDING, desc, color="black")
        mazeY = y + (MAZE.PADDING * 5)
        mazeX = (imgWidth - mazeWidth) // 2
        # if(self.model == MAZE.MODEL.CALC): mazeY += leftImgSize[1]//3
        drawMaze(mazeX, mazeY, mazeWidth, mazeHeight)
        if (route): fillRoute()
        if (self.model == MAZE.MODEL.CALC):
            fillRandomCalc(target)
            self.picture.drawImage(os.path.join(os.path.dirname(__file__), "res/img/sm01.png"), 0.3,
                                   mazeX - leftImgSize[0], mazeY - leftImgSize[1] // 4)
            self.picture.drawImage(os.path.join(os.path.dirname(__file__), "res/img/sm02.png"), 0.5, mazeX + mazeWidth,
                                   mazeHeight - rightImgSize[1] // 4)
        else:
            fillBoarder(mazeX, mazeY, mazeWidth, mazeHeight, roomSize, route)
        time = self.times[0]
        if (route): time = self.times[1]
        desc = "共消耗 {:.6f} CPU 时间".format(time)
        self.picture.drawText(MAZE.PADDING, mazeHeight + self.picture.getFontHeight() + MAZE.PADDING * 8, desc,
                              color="gray")
        if (fmt.lower() == "img"): self.picture.show()
        if (fmt.lower() == "html"): desc = self.picture.getHttpImg()
        return desc

    def getAlgorithmName(self):
        name = "默认"
        if (self.model == MAZE.MODEL.RBKT): name = "深度优先"
        if (self.model == MAZE.MODEL.PRIM): name = "随机PRIM"
        if (self.model == MAZE.MODEL.RDVS): name = "递归分割"
        if (self.model == MAZE.MODEL.CALC): name = "算术迷宫"
        return name

    def generate(model, row, column, fmt="html"):
        maze = MAZE(row, column)
        maze.create(model)
        result = []
        result.append(maze.get(fmt=fmt))
        if (model != MAZE.MODEL.CALC): result.append(maze.get(route=True, fmt=fmt))
        return result

    def parseParams(args):
        parser = argparse.ArgumentParser(prog="maze", exit_on_error=False, allow_abbrev=False)
        parser.add_argument("--model", type=int, default=1)
        parser.add_argument("--row", type=int, default=10)
        parser.add_argument("--column", type=int, default=10)
        try:
            params = parser.parse_args(args)
        except:
            params = parser.parse_args("")
        return params
