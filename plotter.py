import filetools
import unpack
import vectors

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.neighbors import KernelDensity


def _velocity_pdf(velocities, bandwidth=0.5):
    vel_sq = vectors.magnitudes3(velocities)
    left = round(min(vel_sq), 2)
    right = round(max(vel_sq), 2)
    broadcasted = np.array(vel_sq)[:, np.newaxis]
    kde = KernelDensity(kernel='gaussian',
                        bandwidth=bandwidth).fit(broadcasted)
    domain = np.linspace(left, right, len(vel_sq))[:, np.newaxis]
    log_dens = kde.score_samples(domain)

    return domain, log_dens


def velocity_pdf(velocities, bandwidth=0.1):
    domain, log_dens = _velocity_pdf(velocities, bandwidth)
    fig, ax = plt.subplots(1, 1, sharex=True, sharey=True)
    ax.set_yscale('log')
    ax.plot(domain, np.exp(log_dens))


def velocity_pdf_samples(data_dir, **kwargs):
    confs = filetools.get_conf_files(data_dir)
    fig, ax = plt.subplots(1, 1, sharex=True, sharey=True)

    confs = list(confs)
    df = unpack.DataFile(confs[0]).unpack(numpy=True)
    domain, log_dens = _velocity_pdf(df.vels * df.to_kms)
    ax.set_yscale('log')
    floored = np.clip(np.exp(log_dens), 1e-12, 1e2)   
    ax.plot(domain, floored)

    # df = unpack.DataFile(confs[len(confs) / 4]).unpack(numpy=True)
    # domain, log_dens = _velocity_pdf(df.vels * df.to_kms)
    # ax[0,1].set_yscale('log')
    # floored = np.clip(np.exp(log_dens), 1e-12, 1e2)    
    # ax[0, 1].plot(domain, floored)


    # df = unpack.DataFile(confs[len(confs) / 2]).unpack(numpy=True)
    # domain, log_dens = _velocity_pdf(df.vels * df.to_kms)
    # ax[1,0].set_yscale('log')
    # floored = np.clip(np.exp(log_dens), 1e-12, 1e2)    
    # ax[1, 0].plot(domain, floored)

    # df = unpack.DataFile(confs[3 * len(confs) / 4]).unpack(numpy=True)
    # domain, log_dens = _velocity_pdf(df.vels * df.to_kms)
    # ax[1,1].set_yscale('log')
    # floored = np.clip(np.exp(log_dens), 1e-12, 1e2)    
    # ax[1, 1].plot(domain, floored)


def cumulative_density_profile(data_dir):
    confs = filetools.get_conf_files(data_dir)
    initial = confs[0]
    df = unpack.DataFile(initial).unpack()
    

def mass_v_time(data_dir):
    confs = filetools.get_conf_files(data_dir)
    total_mass = []
    for conf in confs:
        df = unpack.DataFile(conf).unpack()
        total_mass.append(sum(df.masses) * df.to_solar_mass)
    fig, ax = plt.subplots(1, 1, sharex=True, sharey=True)
    ax.set_ylabel('Total Mass (solar masses)')
    ax.set_xlabel('Crossing times')
    ax.plot(total_mass)

def avg_ke_v_time(data_dir):
    confs = filetools.get_conf_files(data_dir)
    avg_kes = []
    for conf in confs:
        df = unpack.DataFile(conf).unpack(numpy=True)
        energies = df.masses * df.to_solar_mass * \
            np.array(vectors.magnitudes3(df.vels, scale=df.to_kms))
        avg_kes.append(sum(energies) / energies.shape[0])
    fig, ax = plt.subplots(1, 1, sharex=True, sharey=True)
    ax.set_xlabel('Crossing times')
    ax.set_ylabel(
        'Average Kinetic Energy Per Particle (solar masses * (km/s)^2')
    ax.plot(avg_kes)


def richest_particle_energy(data_dir):
    confs = filetools.get_conf_files(data_dir)
    richest = []
    for conf in confs:
        df = unpack.DataFile(conf).unpack(numpy=True)
        energies = df.masses * df.to_solar_mass * \
            np.array(vectors.magnitudes3(df.vels, scale=df.to_kms))
        richest.append(max(energies))
    fig, ax = plt.subplots(1, 1)
    ax.set_xlabel('Crossing times')
    ax.set_ylabel('Energy of richest particle (solar masses * (km/s)^2')
    ax.plot(richest)


def closest_sep_v_time(data_dir):
    confs = filetools.get_conf_files(data_dir)
    seps = []
    for conf in confs:
        df = unpack.DataFile(conf).unpack()
        seps.append(df.closest_sep() * df.to_parsecs)
    fig, ax = plt.subplots(1, 1, sharex=True, sharey=True)

    ax.set_yscale('log')
    ax.set_xlabel('Crossing times')
    ax.set_ylabel('Closest pair separation (pc)')
    ax.plot(seps)


def total_energy_v_time(data_dir):
    glo = data_dir + '/global.30'
    data = pd.read_csv(glo, sep='\s+', index_col=False)
    fig, ax = plt.subplots(1, 1)
    ax.plot(data['TIME[NB}'], data['BE(3)'])
