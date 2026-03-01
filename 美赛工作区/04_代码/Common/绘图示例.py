import matplotlib.pyplot as plt
import numpy as np
import 配色工具库 as mcm_colors

def plot_demo():
    # 1. Use the helper to load Nature style
    # This automatically finds '样式配置文件/期刊样式/nature.mplstyle'
    mcm_colors.use_nature_style()
    
    # 2. Setup data
    x = np.linspace(0, 10, 20)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.sin(x) + np.cos(x)
    
    # 3. Create figure (Nature standard width is often 89mm or 183mm, converted to inches)
    # The style file already sets a default size, but we can override it.
    fig, ax = plt.subplots()
    
    # 4. Plot using NPG colors (automatically cycled because we called use_nature_style)
    # Or we can explicitly use colors from the list
    ax.plot(x, y1, label='Model A', marker='o')
    ax.plot(x, y2, label='Model B', marker='s')
    ax.plot(x, y3, label='Observation', marker='^')
    
    # 5. Add labels and legend
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude (a.u.)')
    ax.set_title('Demo of Nature Style + NPG Colors')
    ax.legend()
    
    # 6. Save
    output_file = 'demo_nature_plot.pdf'
    plt.savefig(output_file)
    print(f"Demo plot saved to {output_file}")

    # --- Demo 2: High-Dimensional Data with IGV Palette ---
    plt.figure()
    mcm_colors.use_style('ieee') # Switch to IEEE style
    
    # Reset color cycle to IGV (51 colors)
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=mcm_colors.IGV_DEFAULT)
    
    for i in range(15): # Plot 15 lines
        plt.plot(x, y1 + i*0.2, label=f'Group {i}')
    
    plt.title('High-Dimensional Data (IGV Palette)')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.legend(ncol=3, fontsize=6)
    plt.savefig('demo_igv_plot.pdf')
    print("Demo IGV plot saved to demo_igv_plot.pdf")

if __name__ == "__main__":
    plot_demo()
