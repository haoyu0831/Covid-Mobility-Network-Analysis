from plot import *
from whole_network import *
import time

'''
This function is to generate file names with multiple dates
'''


def generate_file_name(num):
    names = []
    for i in range(1, num+1):
        tmp = 'data/01/0'+str(i)+'/2020-01-0'+str(i)+'-social-distancing.csv.gz'
        names.append(tmp)

    return names


if __name__ == '__main__':
    date = dt.date(2020,3,21)
    while date < dt.date(2020,8,1):
        tmp = Nation(date)
        # device_count, dest, MSA_dest = read_files_whole(date)
        # tmp1 = InterMsaG(date, dest, device_count)
        tmp1 = InterMsaG(tmp.date, tmp.dest, tmp.device_count)
        # tmp.plot_map(tmp.g_perco)
        # tmp.plot_g_sg()
        # tmp.plot_g_sg_c()
        # tmp.plot_g_sg_device()
        # tmp.plot_hist()
        tmp1.plot_w_qc_perco()
        msa = ['35620', '31080', '16980', '19100', '26420', '47900', '33100', '37980', '12060', '38060']
        # tmp = Nation(date)
        # tmp.interMSA.plot_msa_qc()
        # tmp.interMSA.plot_map(tmp.interMSA.g_perco)
        # tmp.interMSA.plot_g_sg()
        # tmp.interMSA.plot_g_sg_c()
        # tmp.interMSA.plot_g_sg_device()
        # tmp.interMSA.plot_hist()
        # tmp.interMSA.plot_qc_map()
        # for i in msa:
        #     print(i, len(tmp.MSAs[i].g.nodes()), tmp.MSAs[i].flux/len(tmp.MSAs[i].g.nodes()))
        #     tmp.MSAs[i].plot_g_sg()
        #     tmp.MSAs[i].plot_g_sg_c()
        date += dt.timedelta(days=5)
    # start = dt.date(2020, 9, 8)
    # end = dt.date(2020, 9, 9)
    #
    # tmp = start
    #
    # msa = ['35620', '31080', '16980', '19100', '26420', '47900', '33100', '37980', '12060', '38060']
    # msa_p = ['interMSA', '35620', '31080', '16980', '19100', '26420', '47900', '33100', '37980', '12060', '38060']
    # dates = []
    # datas = dict()
    # for i in msa_p:
    #     datas[i] = {'edge_w': [], 'edge_w_25': [], 'edge_w_75': [],
    #                 'qc': [],
    #                 'ave': [],
    #                 'n_size': [],
    #                 'flux': [],
    #                 'n_in': [], 'n_in_25': [], 'n_in_75': [],
    #                 'd': [], 'd_25': [], 'd_75': []}
    # while tmp < end:
    #     dates.append(tmp)
    #     nation = Nation(tmp)
    #
    #     nation.interMSA.plot_hist()
    #     nation.interMSA.plot_g_sg()
    #     nation.interMSA.plot_g_sg_device()
    #     # nation.interMSA.plot_msa_qc()
    #
    #     datas['interMSA']['edge_w'].append(nation.interMSA.edge_w_median)
    #     datas['interMSA']['edge_w_25'].append(nation.interMSA.edge_w_25)
    #     datas['interMSA']['edge_w_75'].append(nation.interMSA.edge_w_75)
    #     datas['interMSA']['qc'].append(nation.interMSA.qc)
    #     datas['interMSA']['ave'].append(nation.interMSA.edge_w_ave)
    #     datas['interMSA']['n_size'].append(nation.interMSA.gc_node_size)
    #     datas['interMSA']['flux'].append(nation.interMSA.flux)
    #     datas['interMSA']['n_in'].append(nation.interMSA.indegree_median)
    #     datas['interMSA']['n_in_25'].append(nation.interMSA.indegree_25)
    #     datas['interMSA']['n_in_75'].append(nation.interMSA.indegree_75)
    #     datas['interMSA']['d'].append(nation.interMSA.device_median)
    #     datas['interMSA']['d_25'].append(nation.interMSA.device_25)
    #     datas['interMSA']['d_75'].append(nation.interMSA.device_75)
    #
    #     # for i in msa:
    #     #     nation.MSAs[i].plot_hist()
    #     #     nation.MSAs[i].plot_g_sg()
    #     #     nation.MSAs[i].plot_g_sg_device()
    #     #     # nation.MSAs[i].plot_map()
    #     #
    #     #     datas[i]['edge_w'].append(nation.interMSA.edge_w_median)
    #     #     datas[i]['edge_w_25'].append(nation.interMSA.edge_w_25)
    #     #     datas[i]['edge_w_75'].append(nation.interMSA.edge_w_75)
    #     #     datas[i]['qc'].append(nation.interMSA.qc)
    #     #     datas[i]['ave'].append(nation.interMSA.edge_w_ave)
    #     #     datas[i]['n_size'].append(nation.interMSA.gc_node_size)
    #     #     datas[i]['flux'].append(nation.interMSA.flux)
    #     #     datas[i]['n_in'].append(nation.interMSA.indegree_median)
    #     #     datas[i]['n_in_25'].append(nation.interMSA.indegree_25)
    #     #     datas[i]['n_in_75'].append(nation.interMSA.indegree_75)
    #     #     datas[i]['d'].append(nation.interMSA.device_median)
    #     #     datas[i]['d_25'].append(nation.interMSA.device_25)
    #     #     datas[i]['d_75'].append(nation.interMSA.device_75)
    #
    #
    #     tmp += dt.timedelta(days=7)

    # for i in msa_p:
    #     plot_edge_w(dates, datas[i]['edge_w'], datas[i]['edge_w_25'], datas[i]['edge_w_75'], i)
    #     plot_qc(dates, datas[i]['qc'], i)
    #     plot_ave_node_w(dates, datas[i]['ave'], i)
    #     plot_node_size(dates, datas[i]['n_size'], i)
    #     plot_flux(dates, datas[i]['flux'], i)
    #     plot_node_indegree(dates, datas[i]['n_in'], datas[i]['n_in_25'], datas[i]['n_in_75'], i)
    #     plot_device(dates, datas[i]['d'], datas[i]['d_25'], datas[i]['d_75'], i)
    #     break

    # ds = [dt.date(2020,1,15), dt.date(2020,3,23), dt.date(2020,5,15), dt.date(2020,7,15), dt.date(2020,9,15)]
    #
    # for i in ds:
    #     nation = Nation(i)
    #     with open("nations/"+i.strftime('%m_%d')+'.json', "x") as out:
    #         json.dump(nation.interMSA.cc, out)

    # tmp = dt.date(2020,3,1)
    # dates=[]
    # qc=[]
    # qc0 = []
    # qc1=[]
    # qca=[]
    # qca0=[]
    # qca1=[]
    # qcf=[]
    # qcf0=[]
    # qcf1=[]
    #
    # while tmp < dt.date(2020,6,18):
    #     dates.append(tmp)
    #     df = pd.read_csv(qc_str(tmp))
    #     qc.append(np.percentile(df['qc'], 50))
    #     qc0.append(np.percentile(df['qc'], 25))
    #     qc1.append(np.percentile(df['qc'], 75))
    #     qca.append(np.percentile(df['qca'], 50))
    #     qca0.append(np.percentile(df['qca'], 25))
    #     qca1.append(np.percentile(df['qca'], 75))
    #     qcf.append(np.percentile(df['qcf'], 50))
    #     qcf1.append(np.percentile(df['qcf'], 75))
    #     qcf0.append(np.percentile(df['qcf'], 25))
    #     tmp+=dt.timedelta(days=1)
    #
    # plt.figure()
    # plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
    # plt.plot(dates, qcf, color='k', label=r'$q_{cf}$')
    # plt.axvline(dt.date(2020,3,13), linestyle='-.', color='red', label='National Emergency')
    # plt.fill_between(dates, qcf0, qcf1, color='silver')
    # plt.gcf().autofmt_xdate()
    # plt.legend()
    #
    # plt.title('March MSA\'s qcf median')
    # plt.savefig('results/interMSA/03/qcf.png')
