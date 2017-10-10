import struct
import numpy as np


class DataFile(object):

    def __init__(self, fname):
        self.fname = fname
        self.unpacked = False

    def unpack(self, numpy=False):

        if self.unpacked:
            return

        with open(self.fname, 'rb') as f:
            data = f.read()

        head, tail = 0, 28
        header1 = struct.unpack('7i', data[head:tail])
        ntot = header1[1]
        nk = header1[4]

        head, tail = tail, tail + nk * 4
        header2 = struct.unpack('{}f'.format(nk), data[head:tail])

        head, tail = tail, tail + ntot * 4

        masses = struct.unpack('{}f'.format(ntot), data[head:tail])

        head, tail = tail, tail + ntot * 4

        rhos = struct.unpack('{}f'.format(ntot), data[head:tail])

        head, tail = tail, tail + ntot * 4

        xns = struct.unpack('{}f'.format(ntot), data[head:tail])

        head, tail = tail, tail + ntot * 12

        pos = struct.unpack('{}f'.format(3 * ntot), data[head:tail])

        head, tail = tail, tail + ntot * 12

        vels = struct.unpack('{}f'.format(3 * ntot), data[head:tail])

        self.header1 = self._parseHeaderOne(header1)
        self.header2 = self._parseHeaderTwo(header2)
        self.masses = masses
        self.rhos = rhos
        self.xns = xns
        self.pos = pos
        self.vels = vels
        self.unpacked = True

        if numpy:
            self.header1 = np.array(self.header1)
            self.header2 = np.array(self.header2)
            self.masses = np.array(self.masses)
            self.rhos = np.array(self.rhos)
            self.xns = np.array(self.xns)
            self.pos = np.array(self.pos)
            self.vels = np.array(self.vels)

        return self._init_units()

    def _parseHeaderOne(self, header1):
        return {'ntot': header1[1], 'nk': header1[4]}

    def _parseHeaderTwo(self, header2):
        assert len(header2) >= 19
        return {'time[nb]': header2[0],
                'npairs': header2[1],
                'rbar': header2[2],
                'zmbar': header2[3],
                'rtide': header2[4],
                'tidal4': header2[5],
                'rdens': (header2[6], header2[7], header2[8]),
                'time/tcr': header2[9],
                'tscale': header2[10],
                'vstar': header2[11],
                'rc': header2[12],
                'nc': header2[13],
                'vc': header2[14],
                'rhom': header2[15],
                'cmax': header2[16],
                'rscale': header2[17],
                'rsmin': header2[18],
                'dmin1': header2[19]}

    def _init_units(self):

        self.to_parsecs = self.header2['rbar']
        self.to_solar_mass = self.header2['zmbar']
        self.to_kms = self.header2['vstar']
        self.to_myr = self.header2['tscale']

        self.to_sim_length = 1. / self.to_parsecs
        self.to_sim_mass = 1. / self.to_solar_mass
        self.to_sim_v = 1. / self.to_kms

        return self

    def closest_sep(self):
        if not self.unpacked:
            self.unpack()
        return self.header2[19]
