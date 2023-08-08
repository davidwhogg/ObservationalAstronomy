
fig = plt.figure(figsize=[10., 4.3])
ax = fig.add_subplot(1, 1, 1)

xmajor_ticks = np.arange(0, 3., 0.5)
xminor_ticks = np.arange(0, 3., 0.1)

ymajor_ticks = np.arange(0, 1.5, 0.5)
yminor_ticks = np.arange(0, 1.5, 0.1)

ax.set_xticks(xmajor_ticks)
ax.set_xticks(xminor_ticks, minor=True)
ax.set_yticks(ymajor_ticks)
ax.set_yticks(yminor_ticks, minor=True)

# And a corresponding grid
ax.grid(which='both')

ax.set_xlim([0., 2.8])
ax.set_ylim([0., 1.2])

ax.set_xlabel('u-g')
ax.set_ylabel('g-r')

plt.savefig('colorcolor.eps')
plt.show()
