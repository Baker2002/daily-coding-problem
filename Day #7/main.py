# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 25, 26]
list_2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
          "w", "x", "y", "z"]

a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26

alphabet = {
    "br": list_1,
    "sl": list_2,
    3: "c",
}

msg = "111"

for num in range(int(len(msg))):
    #print(num)
    fr = alphabet["br"].index(int(msg[num]))
    print(num)
    print(alphabet["sl"][fr])

for num in range(int(len(msg))):
    #print(num)
    fr = f'{alphabet["br"].index(int(msg[num]))}{alphabet["br"].index(int(msg[num+1]))}'

    print(alphabet["sl"][int(fr)])


ab = alphabet["br"].index(int(msg[0]))

