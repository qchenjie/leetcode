s = "PAYPALISHIRING"


class Solution():
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1:
            return s
        # ret: ['P','AP','Y'] 这样的形式,他后面是不断地这样的+进去
        ret = [""] * min(len(s), num_rows)
        curr_row, going_down = 0, False
        for c in s:
            ret[curr_row] += c
            # 在首行或者是末行 就要开始转
            if curr_row == 0 or curr_row == num_rows - 1:
                going_down = not going_down
            if going_down:
                curr_row += 1
            else:
                curr_row -= 1
        # 拼接组合
        for i in range(1, len(ret)):
            ret[0] += ret[i]

        return ret[0]


if __name__ == '__main__':
    chen = Solution()
    print(chen.convert(s, 3))
