import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_toolkits.basemap import Basemap as Basemap
from matplotlib.lines import Line2D
from model import *

# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
# plt.gcf().autofmt_xdate()

'''
This function is aim to plot number of element of G and SG with changing threshold described in the paper
'''


def plot_g_sg(x, g, sg):

    figure, axis_1 = plt.subplots()

    axis_1.plot(x, g, color='blue', label='1st CC')
    axis_1.set_xlabel('threshold')
    axis_1.set_ylabel('size')

    axis_2 = axis_1.twinx()
    axis_2.plot(x, sg, color='orange', label='2nd CC')
    lines_1, labels_1 = axis_1.get_legend_handles_labels()
    lines_2, labels_2 = axis_2.get_legend_handles_labels()

    lines = lines_1 + lines_2
    labels = labels_1 + labels_2

    axis_1.legend(lines, labels, loc=0)

    plt.title('TX 1/1-1/7 size of cc')

    plt.show()

    return


'''
This function plot the histograph of weights of edges with a logrithmic scale
'''


def plot_hist(g):
    value = list()

    for i in g.edges():
        value.append(g.edges[i]['weight'])

    plt.hist(value, label='number of weights', log=True, bins=1000)
    plt.xscale('log')
    plt.grid(True)
    plt.legend()
    plt.title('NY 1/1-1/7 histogram')
    plt.show()

    return


'''
This function returns latitude and longitude of a point
'''


def get_xy(pt):
    return [pt.x, pt.y]


'''
This function is used to plot a map of network
'''


# def plot_map(g, id):
#     gdf = gpd.read_file('tl_2017_' + str(id) + '_bg/tl_2017_' + str(id) + '_bg.shp')
#     gdf['GEOID'] = gdf['GEOID'].astype(str)
#     centroids = gdf['geometry'].centroid
#     lons, lats = [list(t) for t in zip(*map(get_xy, centroids))]
#     gdf['longitude'] = lons
#     gdf['latitude'] = lats
#     gdf.to_crs({"init": "epsg:4326"}).plot(color="white", edgecolor="grey", linewidth=0.5, alpha=0.75) #ax=ax
#     mx, my = gdf['longitude'].values, gdf['latitude'].values
#
#     pos = dict()
#     for i, elem in enumerate(gdf['GEOID']):
#         pos[elem] = mx[i], my[i]
#
#     nx.draw_networkx(g, pos=pos, node_color='#bebada', with_labels=False, node_size=10)
#
#     plt.show()
#
#     return


'''
This function is used to plot a map with the largest second connected component and bottleneck
'''


# def plot_map_bn(g, bottleneck, bn_weight, id):
#     gdf = gpd.read_file('tl_2017_' + str(id) + '_bg/tl_2017_' + str(id) + '_bg.shp')
#     gdf['GEOID'] = gdf['GEOID'].astype(str)
#     centroids = gdf['geometry'].centroid
#     lons, lats = [list(t) for t in zip(*map(get_xy, centroids))]
#     gdf['longitude'] = lons
#     gdf['latitude'] = lats
#     gdf.to_crs({"init": "epsg:4326"}).plot(color="white", edgecolor="grey", linewidth=0.5, alpha=0.75) #ax=ax
#     mx, my = gdf['longitude'].values, gdf['latitude'].values
#
#     pos = dict()
#     for i, elem in enumerate(gdf['GEOID']):
#         pos[elem] = mx[i], my[i]
#
#     new_g = generate_network_threshold(g, bn_weight)
#
#     cc = list(nx.connected_components(new_g))
#     cc.sort(key=len)
#
#     largest_cc = new_g.subgraph(cc[-1])
#     # pos = nx.circular_layout(largest_cc)
#     # ax = plt.gca()
#     # ax.annotate("",
#     #             xy=pos[0], xycoords='data',
#     #             xytext=pos[1], textcoords='data',
#     #             arrowprops=dict(arrowstyle="-",
#     #                             shrinkA=5, shrinkB=5,
#     #                             patchA=None, patchB=None,
#     #                             connectionstyle="arc3,rad=0.3",
#     #                             ),
#     #             )
#     nx.draw_networkx(largest_cc, pos=pos, node_color='#0080ff', with_labels=False, node_size=.5, edge_color='#0080ff', width=.25)
#
#     s_largest_cc = new_g.subgraph(cc[-2])
#     # pos = nx.circular_layout(s_largest_cc)
#     # ax = plt.gca()
#     # ax.annotate("",
#     #             xy=pos[0], xycoords='data',
#     #             xytext=pos[1], textcoords='data',
#     #             arrowprops=dict(arrowstyle="-",
#     #                             shrinkA=5, shrinkB=5,
#     #                             patchA=None, patchB=None,
#     #                             connectionstyle="arc3,rad=0.3",
#     #                             ),
#     #             )
#     nx.draw_networkx(s_largest_cc, pos=pos, node_color='#32ecab', with_labels=False, node_size=.5, edge_color='#32ecab', width=.25)
#
#     bn = nx.Graph()
#     bn.add_edges_from(bottleneck)
#     # pos = nx.circular_layout(bn)
#     # ax = plt.gca()
#     # ax.annotate("",
#     #             xy=pos[0], xycoords='data',
#     #             xytext=pos[1], textcoords='data',
#     #             arrowprops=dict(arrowstyle="-",
#     #                             shrinkA=5, shrinkB=5,
#     #                             patchA=None, patchB=None,
#     #                             connectionstyle="arc3,rad=0.3",
#     #                             ),
#     #             )
#     nx.draw_networkx(bn, pos=pos, node_color='#f54242', with_labels=False, node_size=3, edge_color='#f65754')
#
#     # manually add legend
#     labels = ['1st CC', '2nd CC', 'Bottleneck']
#     colors = ['#0080ff', '#32ecab', '#f54242']
#     lines = [Line2D([0], [0], color=c, linewidth=3, alpha=0.85) for c in colors]
#     plt.legend(lines, labels, fontsize=8, loc=0)
#     plt.title('CA 1/1-1/7 Map')
#
#     plt.show()
#
#     return


'''
device count
'''


def plot_device(date, y, y_25, y_75, id):
    plt.figure()
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
    plt.plot(date, y, color='k', marker='.')
    plt.fill_between(date, y_25, y_75, color='silver')
    plt.gcf().autofmt_xdate()

    plt.title(id + ' device count')
    if id == 'InterMSA':
        plt.savefig('results/interMSA/device_count.png')
    else:
        plt.savefig('results/' + id + '/device_count.png')

    return


'''
node indegree
'''


def plot_node_indegree(date, y, y_25, y_75, id):
    plt.figure()
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
    plt.plot(date, y, color='k', marker='.')
    plt.fill_between(date, y_25, y_75, color='silver')
    plt.gcf().autofmt_xdate()

    plt.title(id + ' node indegree')
    if id == 'InterMSA':
        plt.savefig('results/interMSA/node_indegree.png')
    else:
        plt.savefig('results/' + id + '/node_indegree.png')

    return


'''
total flux
'''


def plot_flux(x, y, id):
    plt.figure()
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
    plt.plot(x, y, color='k', marker='.')
    plt.gcf().autofmt_xdate()

    plt.title(id + ' total flux')
    if id == 'InterMSA':
        plt.savefig('results/interMSA/total_flux.png')
    else:
        plt.savefig('results/' + id + '/total_flux.png')

    return


'''
qc
'''


def plot_qc(x, y, id):
    plt.figure()
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
    plt.plot(x, y, color='k', marker='.')
    plt.gcf().autofmt_xdate()

    plt.title(id + ' qc')
    if id == 'InterMSA':
        plt.savefig('results/interMSA/qc.png')
    else:
        plt.savefig('results/' + id + '/qc.png')

    return


'''
node size
'''


def plot_node_size(x, y, id):
    plt.figure()
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
    plt.plot(x, y, color='k', marker='.')
    plt.gcf().autofmt_xdate()

    plt.title(id + ' GC node size')
    if id == 'InterMSA':
        plt.savefig('results/interMSA/gc_node_size.png')
    else:
        plt.savefig('results/' + id + '/gc_node_size.png')

    return


'''
Average node weight
'''


def plot_ave_node_w(dates, ave, id):
    plt.figure()
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
    plt.plot(dates, ave, color='k', marker='.')
    plt.gcf().autofmt_xdate()

    plt.title(id + ' Average edge weight')
    if id == 'InterMSA':
        plt.savefig('results/interMSA/ave_node_w.png')
    else:
        plt.savefig('results/' + id + '/ave_node_w.png')

    return


'''
node indegree
'''


def plot_edge_w(date, y, y_25, y_75, id):
    plt.figure()
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
    plt.plot(date, y, color='k', marker='.')
    plt.fill_between(date, y_25, y_75, color='silver')
    plt.gcf().autofmt_xdate()

    plt.title(id + ' edge weight')
    if id == 'InterMSA':
        plt.savefig('results/interMSA/edge_w.png')
    else:
        plt.savefig('results/' + id + '/edge_w.png')

    return


def plot_g_sg_qc(date, qc, qcb, thresholds, num_g, num_sg):
    plt.figure()
    figure, axis_1 = plt.subplots()

    axis_1.axvline(qc, linestyle='-.', color='red', label=r'$q_c$')
    axis_1.axvline(qcb, linestyle='-.', color='orange', label=r'$q_{c2}$')
    axis_1.set_ylabel('GC Component size', color='dodgerblue')
    axis_1.plot(thresholds, num_g, color='dodgerblue', label='GC')
    axis_1.set_xlabel('thresholds')

    axis_2 = axis_1.twinx()
    axis_2.plot(thresholds, num_sg, color='grey', label='SGC')
    axis_2.set_ylabel('SGC Component size', color='grey')

    lines_1, labels_1 = axis_1.get_legend_handles_labels()
    lines_2, labels_2 = axis_2.get_legend_handles_labels()

    lines = lines_1 + lines_2
    labels = labels_1 + labels_2

    axis_1.legend(lines, labels, loc=0)

    plt.title('Inter MSA ' + date.strftime('%m/%d') + ' percolation component size')

    plt.savefig()
    return


'''
Plot map with different qc and weight link
'''

def plot_qc_map(g, qc, color, device_count, pos, q, w, date):
    plt.figure()

    if len(g.nodes()) == 0:
        return

    m = Basemap(
        projection='merc',
        llcrnrlon=-130,
        llcrnrlat=25,
        urcrnrlon=-60,
        urcrnrlat=50,
        lat_ts=0,
        resolution='i',
        suppress_ticks=True)

    m.drawcountries(linewidth=3)
    m.drawstates(linewidth=0.2)
    m.drawcoastlines(linewidth=1)
    m.fillcontinents(alpha=0.3)
    # m.drawcounties(linewidth=0.1)

    x, y = [], []
    for i in pos.keys():
        x.append(pos[i][0])
        y.append(pos[i][1])
    mx, my = m(x, y)
    pos1 = dict()
    for i, j in enumerate(pos.keys()):
        pos1[j] = (mx[i], my[i])

    colors = []
    for i in g.nodes():
        colors.append(color[i])

    cc = list(nx.connected_components(g))
    cc.sort(key=len, reverse=True)
    ax = plt.gca()

    nx.draw_networkx_nodes(G=g, pos=pos1, nodelist=g.nodes(), node_color=colors,
                           node_size=[(device_count[i]/250)**(1/2) for i in g.nodes()])

    g0 = g.subgraph(cc[0])
    for i, j in g0.edges():
        ax.annotate("",
                    xy=pos1[i], xycoords='data',
                    xytext=pos1[j], textcoords='data',
                    arrowprops=dict(arrowstyle="-", color='royalblue',
                                    shrinkA=5, shrinkB=5,
                                    patchA=None, patchB=None,
                                    connectionstyle="arc3,rad=0.3",
                                    ),
                    )
    if len(cc) > 1:
        g1 = g.subgraph(cc[1])
        for i, j in g1.edges():
            ax.annotate("",
                        xy=pos1[i], xycoords='data',
                        xytext=pos1[j], textcoords='data',
                        arrowprops=dict(arrowstyle="-", color='skyblue',
                                        shrinkA=5, shrinkB=5,
                                        patchA=None, patchB=None,
                                        connectionstyle="arc3,rad=0.3",
                                        ),
                        )

    if len(cc) > 2:
        tmp = set()
        for i in cc[2:]:
            if len(i) > 1:
                tmp |= i
        g3 = g.subgraph(tmp)
        for i, j in g3.edges():
            ax.annotate("",
                        xy=pos1[i], xycoords='data',
                        xytext=pos1[j], textcoords='data',
                        arrowprops=dict(arrowstyle="-", color='silver',
                                        shrinkA=5, shrinkB=5,
                                        patchA=None, patchB=None,
                                        connectionstyle="arc3,rad=0.3",
                                        ),
                        )

    labels = ['GC', 'SGC', 'Rest']
    colors = ['royalblue', 'skyblue', 'silver']
    lines = [Line2D([0], [0], color=c, linewidth=2, alpha=0.85) for c in colors]
    plt.tight_layout()
    plt.legend(lines, labels, fontsize=8, loc=4)
    plt.title(date.strftime('%m/%d') + ' ' + qc + '>' + str(q) + ', weight>' + str(w))
    plt.savefig('results/interMSA/'+date.strftime('%m/%d') + '/' + str(qc) + '/' + qc + '_' + str(q) + '_w_' + str(w) + '.png')
    return
