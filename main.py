import RootSystem as Rs
import DiagramPlot as Dp
import matplotlib.pyplot as plt
import numpy as np


def main():

    # All in one run:

    # fig = []
    # rs = []
    # dp = []
    #
    # tog = ['A1', 'A2', 'B2', 'C2', 'D2', 'G2']
    # rank = [1, 2, 2, 2, 2, 2]
    #
    # for i , alg in enumerate(tog):
    #     rs.append(Rs.RootSystem(rang=rank[i], alg_type=alg))
    #     figs, ax = plt.subplots()
    #     fig.append(ax)
    #     plt.rcParams.update({'figure.figsize': (5, 5)})
    #     dp.append(Dp.DiagramPlot(ax))
    #     ax.grid(True, which='both')
    #     ax.set_ylim(-5, 5)
    #     ax.set_xlim(-5, 5)
    #     srs_x = []
    #     srs_y = []
    #     srs_u = []
    #     srs_v = []
    #     col_r = []
    #     for vec in rs[len(rs) - 1].roots:
    #         srs_x.append(0.)
    #         srs_y.append(0.)
    #         srs_u.append(vec[0])
    #         srs_v.append(vec[1])
    #         col_r.append('black')
    #     for j in range(rs[i].rang):
    #         col_r[len(col_r) - 1 - j] = 'red'
    #     srs_data = [srs_x, srs_y, srs_u, srs_v]
    #     dp[len(dp) - 1].draw_roots(srs_data, color=col_r)
    #     # dp[len(dp) - 1].draw_lines()
    #     # dp[len(dp) - 1].darw_points(rs[i].roots)
    #     print(rs[i].roots)
    #     # plt.savefig('algebra_{}.pdf'.format(alg))
    # plt.show()

    alg = 'G2'
    fig = plt.figure(figsize=(5, 5))
    srs_x = []
    srs_y = []
    srs_u = []
    srs_v = []
    col_r = []
    rs = Rs.RootSystem(rang=2, alg_type=alg)
    for vec in rs.roots:
        srs_x.append(0.)
        srs_y.append(0.)
        srs_u.append(vec[0])
        srs_v.append(vec[1])
        col_r.append('black')
    for j in range(rs.rang):
        col_r[len(col_r) - 1 - j] = 'red'
    srs_data = [srs_x, srs_y, srs_u, srs_v]
    dp = Dp.DiagramPlot(plt)
    dp.draw_roots(srs_data, color=col_r)
    points = rs.roots
    num_points = len(points)
    new_points = []
    for i in range(num_points):
        for p in rs.roots:
            new_points.append((np.array(p) + np.array(points[i])).tolist())
    for j in new_points:
        if not (j in points):
            points.append(j)

    dp.draw_points(points)
    plt.show()


if __name__ == "__main__":
    main()
