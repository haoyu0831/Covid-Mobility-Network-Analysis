from model import *
import powerlaw
from statistics import median
from matplotlib.lines import Line2D
from read_file import *
import matplotlib.pyplot as plt
import geopandas as gpd
import json


# NY NJ PA 5602
# LA 4472
# Chicago 1602
# Dallas 1922
# Houston 3362


class InterMsaG:
    def __init__(self, date, device, dest):#, msa_qc):
        print(date)
        self.date = date
        # self.msa_qc = msa_qc

        self.device_count = device
        self.sum_device = sum(device.values())
        self.g = generate_network(dest)

        self.flux = total_flux(self.g)

        # calculate qc and following features
        self.thresholds = np.arange(0, 1000, 5)

        self.num_g, self.num_sg, self.dev_g, self.dev_sg = calc_g_sg(self.g, self.thresholds, self.device_count)
        index_qc, index_qcb = l_sl_value(self.num_sg)

        self.gc_node_size = self.num_g[index_qc]
        self.qc = self.thresholds[index_qc]
        self.qcb = self.thresholds[index_qcb]
        self.g_perco = generate_network_threshold(self.g, self.qc)
        self.g_perco_1 = generate_network_threshold(self.g, self.qcb)

        self.bottleneck = calc_bottleneck_c(self.g, self.thresholds, self.qc)

        self.indegree = []
        for i in self.g.nodes():
            self.indegree.append(self.g.degree(i))
        self.indegree_median = median(self.indegree)
        self.indegree_25 = np.percentile(self.indegree, 25)
        self.indegree_75 = np.percentile(self.indegree, 75)

        self.edge_w = []
        for i in self.g.edges():
            self.edge_w.append(self.g.edges[i]['weight'])
        self.edge_w_median = median(self.edge_w)
        self.edge_w_25 = np.percentile(self.edge_w, 25)
        self.edge_w_75 = np.percentile(self.edge_w, 75)
        self.edge_w_ave = self.flux / self.g.number_of_nodes()

        dc = list(self.device_count.values())
        self.device_median = median(dc)
        self.device_25 = np.percentile(dc, 25)
        self.device_75 = np.percentile(dc, 75)

        # self.plot_map(self.g_perco, 1)
        # self.plot_map(self.g_perco_1, 0)

    def __eq__(self, other):
        return self.date == other.date

    def plot_g_sg(self):
        plt.figure()
        figure, axis_1 = plt.subplots()

        axis_1.plot(self.thresholds, self.num_sg, color='grey', label='SGC')
        axis_1.axvline(self.qc, linestyle='-.', color='red', label=r'$q_c$')
        axis_1.axvline(self.qcb, linestyle='-.', color='orange', label=r'$q_{c2}$')
        axis_1.set_xlabel('thresholds')
        axis_1.set_ylabel('SGC Component size', color='grey')

        axis_2 = axis_1.twinx()
        axis_2.set_ylabel('GC Component size', color='dodgerblue')
        axis_2.plot(self.thresholds, self.num_g, color='dodgerblue', label='GC')
        lines_1, labels_1 = axis_1.get_legend_handles_labels()
        lines_2, labels_2 = axis_2.get_legend_handles_labels()

        lines = lines_1 + lines_2
        labels = labels_1 + labels_2

        axis_1.legend(lines, labels, loc=0)

        plt.title('Inter MSA ' + self.date.strftime('%m/%d') + ' percolation component size')

        plt.savefig('results/interMSA/' + self.date.strftime('%m_%d') + '_g_sg_size.png')
        return

    def plot_map(self, g, num):
        plt.figure()
        gdf = gpd.read_file('shape_file/tl_2017_us_county/tl_2017_us_county.shp')
        gdf['GEOID'] = gdf['GEOID'].astype(str)
        centroids = gdf['geometry'].centroid
        lons, lats = [list(t) for t in zip(*map(get_xy, centroids))]
        gdf['longitude'] = lons
        gdf['latitude'] = lats
        gdf.to_crs({"init": "epsg:4326"}).plot(color="white", edgecolor="grey", linewidth=0.5, alpha=0.75) #ax=ax
        mx, my = gdf['longitude'].values, gdf['latitude'].values

        node_size = dict()
        for i in self.device_count.keys():
            node_size[i] = self.device_count[i]/100

        pos = dict()
        for i, elem in enumerate(gdf['GEOID']):
            pos[elem] = mx[i], my[i]

        cc = list(nx.connected_components(g))
        cc.sort(key=len, reverse=True)

        largest_cc = g.subgraph(cc[0])
        ax = plt.gca()

        nx.draw_networkx_nodes(largest_cc, pos=pos, node_color='dodgerblue', node_size=1, alpha=1)
        for i, j in largest_cc.edges():
            ax.annotate("",
                        xy=pos[i], xycoords='data',
                        xytext=pos[j], textcoords='data',
                        arrowprops=dict(arrowstyle="-", color='dodgerblue',
                                        shrinkA=5, shrinkB=5,
                                        patchA=None, patchB=None,
                                        connectionstyle="arc3,rad=0.3",
                                        ),
                        )

        s_largest_cc = self.g_perco.subgraph(cc[1])
        nx.draw_networkx_nodes(s_largest_cc, pos=pos, node_color='mediumspringgreen', node_size=1, alpha=1)
        for i, j in s_largest_cc.edges():
            ax.annotate("",
                        xy=pos[i], xycoords='data',
                        xytext=pos[j], textcoords='data',
                        arrowprops=dict(arrowstyle="-", color='mediumspringgreen',
                                        shrinkA=5, shrinkB=5,
                                        patchA=None, patchB=None,
                                        connectionstyle="arc3,rad=0.3",
                                        ),
                        )

        bn = nx.Graph()
        bn.add_edges_from(self.bottleneck)
        nx.draw_networkx_nodes(bn, pos=pos, node_color='r', node_size=1, alpha=1)
        for i, j in bn.edges():
            ax.annotate("",
                        xy=pos[i], xycoords='data',
                        xytext=pos[j], textcoords='data',
                        arrowprops=dict(arrowstyle="-", color='r',
                                        shrinkA=5, shrinkB=5,
                                        patchA=None, patchB=None,
                                        connectionstyle="arc3,rad=0.3",
                                        ),
                        )

        rest = self.g_perco.subgraph(cc[2:])
        nx.draw_networkx_nodes(rest, pos=pos, node_color='silver', node_size=1, alpha=1)
        for i, j in rest.edges():
            ax.annotate("",
                        xy=pos[i], xycoords='data',
                        xytext=pos[j], textcoords='data',
                        arrowprops=dict(arrowstyle="-", color='silver',
                                        shrinkA=5, shrinkB=5,
                                        patchA=None, patchB=None,
                                        connectionstyle="arc3,rad=0.3",
                                        ),
                        )

        # manually add legend
        labels = ['GC', 'SGC', 'Bottleneck', 'Rest']
        colors = ['dodgerblue', 'mediumspringgreen', 'r', 'silver']
        lines = [Line2D([0], [0], color=c, linewidth=3, alpha=0.85) for c in colors]
        plt.legend(lines, labels, fontsize=8, loc=0)
        plt.title('Inter MSA ' + self.date.strftime('%m/%d') + ' map '+str(num))
        plt.savefig('results/interMSA/' + self.date.strftime('%m_%d') + '_map'+str(num)+'.png')

        return

    def plot_hist(self):
        plt.figure()

        fit = powerlaw.Fit(self.edge_w)
        fig2 = fit.plot_pdf(color='peachpuff')

        fit.plot_ccdf(color='royalblue', linewidth=2, ax=fig2)

        fit.power_law.plot_ccdf(color='cornflowerblue', linestyle='--', ax=fig2)
        labels = ['CCDF', 'PDF']
        colors = ['royalblue', 'peachpuff']
        lines = [Line2D([0], [0], color=c, linewidth=2, alpha=0.85) for c in colors]
        plt.legend(lines, labels)
        plt.title('Inter MSA ' + self.date.strftime('%m/%d') + ' CCDF')
        plt.savefig('results/interMSA/' + self.date.strftime('%m_%d') + '_hist.png')
        return

    def plot_g_sg_device(self):
        plt.figure()
        figure, axis_1 = plt.subplots()

        axis_1.plot(self.thresholds, self.dev_sg, color='grey', label='SGC')
        axis_1.axvline(self.qc, linestyle='-.', color='red', label=r'$q_c$')
        axis_1.axvline(self.qcb, linestyle='-.', color='orange', label=r'$q_{c2}$')
        axis_1.set_xlabel('thresholds')
        axis_1.set_ylabel('SGC device count', color='grey')

        axis_2 = axis_1.twinx()
        axis_2.set_ylabel('GC device count', color='dodgerblue')
        axis_2.plot(self.thresholds, self.dev_g, color='dodgerblue', label='GC')
        lines_1, labels_1 = axis_1.get_legend_handles_labels()
        lines_2, labels_2 = axis_2.get_legend_handles_labels()

        lines = lines_1 + lines_2
        labels = labels_1 + labels_2

        axis_1.legend(lines, labels, loc=0)

        plt.title('Inter MSA ' + self.date.strftime('%m/%d') + ' percolation device count')

        plt.savefig('results/interMSA/' + self.date.strftime('%m_%d') + '_g_sg_device.png')
        return

    # def plot_msa_qc(self):
    #     plt.figure()
    #
    #     th = np.arange(1, 75, .5)
    #     remain_msa = []
    #
    #     for i in th:
    #         tmp = 0
    #         for j in self.msa_qc.keys():
    #             if i < self.msa_qc[j]:
    #                 tmp += self.device_count[j]
    #         remain_msa.append(tmp)
    #
    #     plt.plot(th, remain_msa, color='royalblue')
    #     plt.grid(True)
    #     plt.xlabel('Thresholds')
    #     plt.ylabel('device count')
    #
    #     plt.title('Sum of remaining MSAs device count ' + self.date.strftime('%m/%d'))
    #     plt.savefig('results/interMSA/' + self.date.strftime('%m_%d') + '_MSAs_device.png')
    #     return