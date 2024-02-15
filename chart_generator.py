import io
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors

def generate_chart(lang_stats: dict) -> io.StringIO:
    cmap = cm.get_cmap('Blues')
    norm = mcolors.Normalize(vmin=0, vmax=len(lang_stats))
    colors = cmap(norm(range(len(lang_stats))))
    
    data = [(lang, stats['percentage']) for lang, stats in lang_stats.items()]
    data_sorted = sorted(data, key=lambda x: x[1], reverse=True)
    
    labels, sizes = zip(*data_sorted)

    fig, ax = plt.subplots(figsize=(6, 4), facecolor="#20232a")
    wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=180, colors=colors)

    plt.setp(texts, fontsize=8, color='#5AA5E7', fontweight='bold')
    plt.setp(autotexts, fontsize=8, color="#20232a")

    ax.axis('equal')
    svg_buf = io.StringIO()
    plt.savefig(svg_buf, format='svg', bbox_inches='tight')
    svg_buf.seek(0)
    plt.close(fig)
    return svg_buf
