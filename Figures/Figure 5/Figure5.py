import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os
import pandas as pd
import sys

cud_palette = [
    '#0101fd',  # Blue
    '#E69F00',  # Orange
    '#000000',  # Black
    '#ff0101',   # Red
    '#0072B2',  # Blue
    '#D55E00',  # Vermilion
    '#CC79A7',  # Reddish Purple
    '#F95C99',  # Reddish Pink
    '#999999',  # Gray
    '#CC61B0',  # Pink
    '#F95C99',  # Reddish Pink
]

markers = ['s', 'o', '^', 'X', 'p', 'P']

fig, ((ax1, ax2, ax7), (ax3, ax4, ax8), (ax5, ax6, ax9)) = plt.subplots(ncols=3, nrows=3, figsize=(10,10))
fig.subplots_adjust(wspace=0.45, hspace=0.6)
plt.suptitle("Random bipartite", fontsize=18, y=0.96)

# -------------------------------------------------------------------------------------------------------------------------------------------------

# probability
df = pd.read_pickle(os.path.join(sys.path[0], f"data/random_bipartite_probability.pkl"))

ax2.errorbar(df['p_connection'], df['LV_app'], yerr=(df['LV_app'] - df['LV_app_CI_lower'], df['LV_app_CI_upper'] - df['LV_app']), marker=markers[0], color=cud_palette[0], capsize=3)
ax2.scatter([], [], label='LV', marker=markers[0], color=cud_palette[0])

ax2.errorbar(df['p_connection'], df['greedy_app'], yerr=(df['greedy_app'] - df['greedy_app_CI_lower'], df['greedy_app_CI_upper'] - df['greedy_app']), marker=markers[2], color=cud_palette[2], capsize=3)
ax2.scatter([], [], label='MDG', marker=markers[2], color=cud_palette[2])

ax2.errorbar(df['p_connection'], df['rpp_app'], yerr=(df['rpp_app'] - df['rpp_app_CI_lower'], df['rpp_app_CI_upper'] - df['rpp_app']), marker=markers[3], color=cud_palette[3], capsize=3)
ax2.scatter([], [], label='RPP', marker=markers[3], color=cud_palette[3])

ax2.errorbar(df['p_connection'], df['luby_app'], yerr=(df['luby_app'] - df['luby_app_CI_lower'], df['luby_app_CI_upper'] - df['luby_app']), marker=markers[4], color=cud_palette[4], capsize=3)
ax2.scatter([], [], label='Luby', marker=markers[4], color=cud_palette[4])

ax2.errorbar(df['p_connection'], df['blelloch_app'], yerr=(df['blelloch_app'] - df['blelloch_app_CI_lower'], df['blelloch_app_CI_upper'] - df['blelloch_app']), marker=markers[5], color=cud_palette[5], capsize=3)
ax2.scatter([], [], label='Blelloch', marker=markers[5], color=cud_palette[5])

ax2.errorbar(df['p_connection'], df['continuation_app'], yerr=(df['continuation_app'] - df['continuation_app_CI_lower'], df['continuation_app_CI_upper'] - df['continuation_app']), marker=markers[1], color=cud_palette[1], capsize=3)
ax2.scatter([], [], label='CLV', marker=markers[1], color=cud_palette[1])

# ax2.legend()
ax2.set_xlabel('p')
ax2.set_ylabel('Approximation factor')
ax2.set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], ['0.0', '0.2', '0.4', '0.6', '0.8', '1.0'])
# ax2.set_yticks([0.60, 0.70, 0.80, 0.90, 1.0], ['0.60', '0.70', '0.80', '0.90', '1.00'])

# -------------------------------------------------------------------------------------------------------------------------------------------------

# size - sparse - performance
df = pd.read_pickle(os.path.join(sys.path[0], f"data/random_bipartite_size_sparse_performance.pkl"))

ax3.errorbar(df['size'], df['LV_app'], yerr=(df['LV_app'] - df['LV_app_CI_lower'], df['LV_app_CI_upper'] - df['LV_app']), marker=markers[0], color=cud_palette[0], capsize=3)
ax3.scatter([], [], label='LV', marker=markers[0], color=cud_palette[0])

ax3.errorbar(df['size'], df['greedy_app'], yerr=(df['greedy_app'] - df['greedy_app_CI_lower'], df['greedy_app_CI_upper'] - df['greedy_app']), marker=markers[2], color=cud_palette[2], capsize=3)
ax3.scatter([], [], label='MDG', marker=markers[2], color=cud_palette[2])

ax3.errorbar(df['size'], df['rpp_app'], yerr=(df['rpp_app'] - df['rpp_app_CI_lower'], df['rpp_app_CI_upper'] - df['rpp_app']), marker=markers[3], color=cud_palette[3], capsize=3)
ax3.scatter([], [], label='RPP', marker=markers[3], color=cud_palette[3])

ax3.errorbar(df['size'], df['luby_app'], yerr=(df['luby_app'] - df['luby_app_CI_lower'], df['luby_app_CI_upper'] - df['luby_app']), marker=markers[4], color=cud_palette[4], capsize=3)
ax3.scatter([], [], label='Luby', marker=markers[4], color=cud_palette[4])

ax3.errorbar(df['size'], df['blelloch_app'], yerr=(df['blelloch_app'] - df['blelloch_app_CI_lower'], df['blelloch_app_CI_upper'] - df['blelloch_app']), marker=markers[5], color=cud_palette[5], capsize=3)
ax3.scatter([], [], label='Blelloch', marker=markers[5], color=cud_palette[5])

ax3.errorbar(df['size'], df['continuation_app'], yerr=(df['continuation_app'] - df['continuation_app_CI_lower'], df['continuation_app_CI_upper'] - df['continuation_app']), marker=markers[1], color=cud_palette[1], capsize=3)
ax3.scatter([], [], label='CLV', marker=markers[1], color=cud_palette[1])

# ax3.legend()
ax3.set_xlabel('Size (n)')
ax3.set_ylabel('Approximation factor')
ax3.set_xticks([0, 50, 100, 150, 200], ['0', '50', '100', '150', '200'])
# ax3.set_yticks([0.70, 0.80, 0.90, 1.0], ['0.70', '0.80', '0.90', '1.00'])

# -------------------------------------------------------------------------------------------------------------------------------------------------

# size - dense - performance
df = pd.read_pickle(os.path.join(sys.path[0], f"data/random_bipartite_size_dense_performance.pkl"))

ax5.errorbar(df['size'], df['LV_app'], yerr=(df['LV_app'] - df['LV_app_CI_lower'], df['LV_app_CI_upper'] - df['LV_app']), marker=markers[0], color=cud_palette[0], capsize=3)
ax5.scatter([], [], label='LV', marker=markers[0], color=cud_palette[0])

ax5.errorbar(df['size'], df['greedy_app'], yerr=(df['greedy_app'] - df['greedy_app_CI_lower'], df['greedy_app_CI_upper'] - df['greedy_app']), marker=markers[2], color=cud_palette[2], capsize=3)
ax5.scatter([], [], label='MDG', marker=markers[2], color=cud_palette[2])

ax5.errorbar(df['size'], df['rpp_app'], yerr=(df['rpp_app'] - df['rpp_app_CI_lower'], df['rpp_app_CI_upper'] - df['rpp_app']), marker=markers[3], color=cud_palette[3], capsize=3)
ax5.scatter([], [], label='RPP', marker=markers[3], color=cud_palette[3])

ax5.errorbar(df['size'], df['luby_app'], yerr=(df['luby_app'] - df['luby_app_CI_lower'], df['luby_app_CI_upper'] - df['luby_app']), marker=markers[4], color=cud_palette[4], capsize=3)
ax5.scatter([], [], label='Luby', marker=markers[4], color=cud_palette[4])

ax5.errorbar(df['size'], df['blelloch_app'], yerr=(df['blelloch_app'] - df['blelloch_app_CI_lower'], df['blelloch_app_CI_upper'] - df['blelloch_app']), marker=markers[5], color=cud_palette[5], capsize=3)
ax5.scatter([], [], label='Blelloch', marker=markers[5], color=cud_palette[5])

ax5.errorbar(df['size'], df['continuation_app'], yerr=(df['continuation_app'] - df['continuation_app_CI_lower'], df['continuation_app_CI_upper'] - df['continuation_app']), marker=markers[1], color=cud_palette[1], capsize=3)
ax5.scatter([], [], label='CLV', marker=markers[1], color=cud_palette[1])

# ax5.legend()
ax5.set_xlabel('Size (n)')
ax5.set_ylabel('Approximation factor')
ax5.set_xticks([0, 50, 100, 150, 200], ['0', '50', '100', '150', '200'])
# ax5.set_yticks([0.60, 0.70, 0.80, 0.90, 1.00], ['0.60', '0.70', '0.80', '0.90', '1.00'])

# -------------------------------------------------------------------------------------------------------------------------------------------------

# histogram
df = pd.read_pickle(os.path.join(sys.path[0], f"data/random_bipartite_histogram.pkl"))

uniform = np.array((df['count_uniform'])) / sum(list(df['count_uniform']))
lv = np.array(df['count_LV']) / sum(list(df['count_LV']))

bars1 = ax1.bar(list(df['value']), uniform, label='Uniform', alpha=0.7, color=cud_palette[3], hatch='//')
bars2 = ax1.bar(list(df['value']), lv, label='LV', alpha=0.7, color=cud_palette[0], hatch='\\\\')

# ax1.legend()
ax1.set_xlabel(r'$|S|$')
ax1.set_ylabel('Frequency')
ax1.set_xticks([16, 20, 24, 28, 32], ['16', '20', '24', '28', '32'])
ax1.set_ylim(0, 0.7)
ax1.legend(loc='lower left')

# Manually define position and size for the inset plot
inset_x = 0.175
inset_y = 0.79
inset_width = 0.08
inset_height = 0.082

ax_inset = fig.add_axes([inset_x, inset_y, inset_width, inset_height])

ax_inset.bar(list(df['value']), uniform, label='Uniform', alpha=0.7, color=cud_palette[3], hatch='//')
ax_inset.bar(list(df['value'][lv>0]), lv[lv>0], label='LV', alpha=0.7, color=cud_palette[0], hatch='\\\\')

ax_inset.set_yscale('log')
ax_inset.set_xticks([16, 20, 24, 28, 32], ['16', '20', '24', '28', '32'])
ax_inset.set_yticks([ 10**-4, 10**-3, 10**-2 , 10**-1 ], [ r'$10^{-4}$', r'$10^{-3}$', r'$10^{-2}$', r'$10^{-1}$' ])
ax_inset.set_ylim(0, 0.6)

# -------------------------------------------------------------------------------------------------------------------------------------------------

# size - sparse - efficiency
df = pd.read_pickle(os.path.join(sys.path[0], f"data/random_bipartite_size_sparse_efficiency.pkl"))

ax4.plot(df['size'], df['LV_eff'], marker=markers[0], color=cud_palette[0])
ax4.scatter([], [], label='LV', marker=markers[0], color=cud_palette[0])

ax4.plot(df['size'], df['greedy_eff'], marker=markers[2], color=cud_palette[2])
ax4.scatter([], [], label='MDG', marker=markers[2], color=cud_palette[2])

ax4.plot(df['size'], df['rpp_eff'], marker=markers[3], color=cud_palette[3])
ax4.scatter([], [], label='RPP', marker=markers[3], color=cud_palette[3])

ax4.plot(df['size'], df['luby_eff'], marker=markers[4], color=cud_palette[4])
ax4.scatter([], [], label='Luby', marker=markers[4], color=cud_palette[4])

ax4.plot(df['size'], df['blelloch_eff'], marker=markers[5], color=cud_palette[5])
ax4.scatter([], [], label='Blelloch', marker=markers[5], color=cud_palette[5])

ax4.plot(df['size'], df['continuation_eff'], marker=markers[1], color=cud_palette[1])
ax4.scatter([], [], label='CLV', marker=markers[1], color=cud_palette[1])

# ax4.legend()
ax4.set_xlabel('Size (n)')
ax4.set_ylabel('Percentage MIS')
ax4.set_xticks([0, 50, 100, 150, 200], ['0', '50', '100', '150', '200'])
# ax4.set_yticks([0.0, 0.25, 0.50, 0.75, 1.00], ['0.00', '0.25', '0.50', '0.75', '1.00'])

# -------------------------------------------------------------------------------------------------------------------------------------------------

# size - dense - efficiency
df = pd.read_pickle(os.path.join(sys.path[0], f"data/random_bipartite_size_dense_efficiency.pkl"))

ax6.plot(df['size'], df['LV_eff'], marker=markers[0], color=cud_palette[0])
ax6.scatter([], [], label='LV', marker=markers[0], color=cud_palette[0])

ax6.plot(df['size'], df['greedy_eff'], marker=markers[2], color=cud_palette[2])
ax6.scatter([], [], label='MDG', marker=markers[2], color=cud_palette[2])

ax6.plot(df['size'], df['rpp_eff'], marker=markers[3], color=cud_palette[3])
ax6.scatter([], [], label='RPP', marker=markers[3], color=cud_palette[3])

ax6.plot(df['size'], df['luby_eff'], marker=markers[4], color=cud_palette[4])
ax6.scatter([], [], label='Luby', marker=markers[4], color=cud_palette[4])

ax6.plot(df['size'], df['blelloch_eff'], marker=markers[5], color=cud_palette[5])
ax6.scatter([], [], label='Blelloch', marker=markers[5], color=cud_palette[5])

ax6.plot(df['size'], df['continuation_eff'], marker=markers[1], color=cud_palette[1])
ax6.scatter([], [], label='CLV', marker=markers[1], color=cud_palette[1])

# ax6.legend()
ax6.set_xlabel('Size (n)')
ax6.set_ylabel('Percentage MIS')
ax6.set_xticks([0, 50, 100, 150, 200], ['0', '50', '100', '150', '200'])
# ax4.set_yticks([0.0, 0.25, 0.50, 0.75, 1.00], ['0.00', '0.25', '0.50', '0.75', '1.00'])

# -------------------------------------------------------------------------------------------------------------------------------------------------

# ax7.legend(loc='center', fontsize=14)
ax7.scatter([], [], label='LV', marker=markers[0], color=cud_palette[0])
ax7.scatter([], [], label='CLV', marker=markers[1], color=cud_palette[1])
ax7.scatter([], [], label='MDG', marker=markers[2], color=cud_palette[2])
ax7.scatter([], [], label='RPP', marker=markers[3], color=cud_palette[3])
ax7.scatter([], [], label='Luby', marker=markers[4], color=cud_palette[4])
ax7.scatter([], [], label='Blelloch', marker=markers[5], color=cud_palette[5])
ax7.legend(loc='center', fontsize=14)
ax7.spines['top'].set_visible(False)
ax7.spines['right'].set_visible(False)
ax7.spines['bottom'].set_visible(False)
ax7.spines['left'].set_visible(False)
ax7.set_xticks([])
ax7.set_yticks([])
ax7.set_xlabel('')
ax7.set_ylabel('')

# -------------------------------------------------------------------------------------------------------------------------------------------------

# size - sparse - worstcase
df = pd.read_pickle(os.path.join(sys.path[0], f"data/random_bipartite_size_sparse_worst_case.pkl"))

ax8.plot(df['size'], df['LV_wc'], marker=markers[0], color=cud_palette[0])
ax8.scatter([], [], label='LV', marker=markers[0], color=cud_palette[0])

ax8.plot(df['size'], df['greedy_wc'], marker=markers[2], color=cud_palette[2])
ax8.scatter([], [], label='MDG', marker=markers[2], color=cud_palette[2])

ax8.plot(df['size'], df['rpp_wc'], marker=markers[3], color=cud_palette[3])
ax8.scatter([], [], label='RPP', marker=markers[3], color=cud_palette[3])

ax8.plot(df['size'], df['luby_wc'], marker=markers[4], color=cud_palette[4])
ax8.scatter([], [], label='Luby', marker=markers[4], color=cud_palette[4])

ax8.plot(df['size'], df['blelloch_wc'], marker=markers[5], color=cud_palette[5])
ax8.scatter([], [], label='Blelloch', marker=markers[5], color=cud_palette[5])

ax8.plot(df['size'], df['continuation_wc'], marker=markers[1], color=cud_palette[1])
ax8.scatter([], [], label='CLV', marker=markers[1], color=cud_palette[1])

# ax8.legend()
ax8.set_xlabel('Size (n)')
ax8.set_ylabel('Worst-case')
ax8.set_xticks([0, 50, 100, 150, 200], ['0', '50', '100', '150', '200'])
# ax8.set_yticks([0.40, 0.60, 0.80, 1.00], ['0.40', '0.60', '0.80', '1.00'])

# -------------------------------------------------------------------------------------------------------------------------------------------------

# size - dense - worstcase
df = pd.read_pickle(os.path.join(sys.path[0], f"data/random_bipartite_size_dense_worst_case.pkl"))

ax9.plot(df['size'], df['LV_wc'], marker=markers[0], color=cud_palette[0])
ax9.scatter([], [], label='LV', marker=markers[0], color=cud_palette[0])

ax9.plot(df['size'], df['greedy_wc'], marker=markers[2], color=cud_palette[2])
ax9.scatter([], [], label='MDG', marker=markers[2], color=cud_palette[2])

ax9.plot(df['size'], df['rpp_wc'], marker=markers[3], color=cud_palette[3])
ax9.scatter([], [], label='RPP', marker=markers[3], color=cud_palette[3])

ax9.plot(df['size'], df['luby_wc'], marker=markers[4], color=cud_palette[4])
ax9.scatter([], [], label='Luby', marker=markers[4], color=cud_palette[4])

ax9.plot(df['size'], df['blelloch_wc'], marker=markers[5], color=cud_palette[5])
ax9.scatter([], [], label='Blelloch', marker=markers[5], color=cud_palette[5])

ax9.plot(df['size'], df['continuation_wc'], marker=markers[1], color=cud_palette[1])
ax9.scatter([], [], label='CLV', marker=markers[1], color=cud_palette[1])

# ax9.legend()
ax9.set_xlabel('Size (n)')
ax9.set_ylabel('Worst-case')
ax9.set_xticks([0, 50, 100, 150, 200], ['0', '50', '100', '150', '200'])
# ax9.set_yticks([0.2, 0.3, 0.4, 0.5, 0.6, 0.7], ['0.2', '0.3', '0.4', '0.5', '0.6', '0.7'])

# -------------------------------------------------------------------------------------------------------------------------------------------------

numbers = [ 'a', 'b', 'c' ]
for index, ax in enumerate([ ax1, ax2, ax7 ]):
    if index == 0:
        ax.text(0.5, 1.05, f'({numbers[index]}) ' + r'$n=60$', ha='center', transform=ax.transAxes, fontsize=12)    
        # ax.legend(loc='lower left', fontsize=8)
    elif index == 1:
        ax.text(0.5, 1.05, f'({numbers[index]})', ha='center', transform=ax.transAxes, fontsize=12)
        # ax.legend(loc='lower left', fontsize=8, ncol=2)
    else:
        ax.text(0.5, 1.05, f'({numbers[index]})', ha='center', transform=ax.transAxes, fontsize=12)
    
    ax.tick_params(axis='x', labelsize=12)
    ax.tick_params(axis='y', labelsize=12)
    ax.set_xlabel( ax.get_xlabel(), fontsize=12)
    ax.set_ylabel( ax.get_ylabel(), fontsize=12)
    
numbers = [ 'd', 'e', 'f' ]
for index, ax in enumerate([ ax3, ax4, ax8 ]):
    ax.text(0.5, 1.05, f'({numbers[index]}) ' + r'$p = \log(n/2) / (n/2)$', ha='center', transform=ax.transAxes, fontsize=12)    
    ax.tick_params(axis='x', labelsize=12)
    ax.tick_params(axis='y', labelsize=12)
    ax.set_xlabel( ax.get_xlabel(), fontsize=12)
    ax.set_ylabel( ax.get_ylabel(), fontsize=12)
    # ax.legend(loc='lower left', fontsize=8, ncol=2)
    
numbers = [ 'g', 'h', 'i' ]
for index, ax in enumerate([ ax5, ax6, ax9 ]):
    ax.text(0.5, 1.05, f'({numbers[index]}) ' + r'$p = 1/2$', ha='center', transform=ax.transAxes, fontsize=12)    
    ax.tick_params(axis='x', labelsize=12)
    ax.tick_params(axis='y', labelsize=12)
    ax.set_xlabel( ax.get_xlabel(), fontsize=12)
    ax.set_ylabel( ax.get_ylabel(), fontsize=12)
    # ax.legend(loc='lower left', fontsize=8, ncol=2)

plt.savefig(os.path.join(sys.path[0], 'Figure5.pdf'), transparent=True, dpi=900, bbox_inches='tight')
plt.show()