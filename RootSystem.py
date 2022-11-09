import numpy as np


class RootSystem:
    def __init__(self, rang=1, alg_type='A1'):
        self.rang = rang
        self.alg_type = alg_type
        self.srs = self.find_simple_roots()
        self.roots = self.get_roots()

    def get_rang(self):
        return self.rang

    def find_simple_roots(self):
        basic_srs = {'r=1;alg_type=A1': [[1, 0]],
                     'r=2;alg_type=A2': [[1, 0],
                                         [np.cos(2*np.pi/3), np.sin(2*np.pi/3)]],
                     'r=2;alg_type=B2': [[1, 0],
                                         [np.sqrt(2)*np.cos(3*np.pi/4), np.sqrt(2)*np.sin(3*np.pi/4)]],
                     'r=2;alg_type=C2': [[1, 0],
                                         [np.sqrt(2)*np.cos(3*np.pi/4), np.sqrt(2)*np.sin(3*np.pi/4)]],
                     'r=2;alg_type=D2': [[1, 0],
                                         [0, 2]],
                     'r=2;alg_type=G2': [[1, 0],
                                         [np.sqrt(3)*np.cos(5*np.pi/6), np.sqrt(3)*np.sin(5*np.pi/6)]]}

        key = 'r={};alg_type={}'.format(self.rang, self.alg_type)
        try:
            # print(basic_srs[key])
            return basic_srs[key]
        except KeyError:
            print("Now we can build ony for next algebras: A1, A2, B2/C2, D2, G2")
            raise SystemExit(1)

    def get_series_len(self, u1, u2):
        return round(-2*(np.dot(u1, u2)/(np.dot(u1, u1))))

    def get_simple_roots_serie(self, u1, u2):
        if not (self.rang == 1):
            serie = []
            len_of_ser = self.get_series_len(u1, u2)
            for i in range(1, len_of_ser + 1):
                serie.append((np.array(u2) + i * np.array(u1)).tolist())
            return serie
        else:
            return []

    def get_symmetrical_root(self, ax_vect, ref_vec):
        sym_vec = np.array(ax_vect) * 2 * np.dot(ref_vec, ax_vect)/np.dot(ax_vect, ax_vect) - np.array(ref_vec)
        return sym_vec.tolist()

    def get_roots(self):
        roots = []
        serie = self.get_simple_roots_serie(self.srs[0], self.srs[len(self.srs) - 1])
        for vec in serie:
            roots.append(vec)
            roots.append(self.get_symmetrical_root(self.srs[0], vec))
            roots.append(self.get_symmetrical_root(self.srs[1], vec))
        for sr in self.srs:
            roots.append(sr)
        for i in range(len(roots)):
            roots.append((-np.array(roots[i])).tolist())
        root_set = []
        for root in roots:
            if not (root in root_set):
                root_set.append(root)
        for i in range(self.rang):
            root_set.append(self.srs[i])

        return root_set


def check():
    test_ex = RootSystem(2, alg_type='G2')
    print(test_ex.roots)


if __name__ == "__main__":
    check()
