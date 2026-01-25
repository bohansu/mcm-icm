import matplotlib.pyplot as plt
import matplotlib.patches as patches
import 配色工具库 as mcm_colors
import math

def plot_palettes(palettes_dict, filename="palette_preview.png"):
    """
    Generate a figure showing all color palettes.
    """
    n_palettes = len(palettes_dict)
    cols = 2
    rows = math.ceil(n_palettes / cols)
    
    fig, axes = plt.subplots(rows, cols, figsize=(15, rows * 1.5))
    fig.suptitle("MCM/ICM Official Color Palettes (ggsci & SciencePlots)", fontsize=16, y=1.02)
    
    # Flatten axes
    axes = axes.flatten()
    
    for i, (name, colors) in enumerate(palettes_dict.items()):
        ax = axes[i]
        n_colors = len(colors)
        
        # Draw color bars
        for j, color in enumerate(colors):
            rect = patches.Rectangle((j, 0), 1, 1, facecolor=color)
            ax.add_patch(rect)
            
            # Add text label (hex code) if there are few colors, otherwise just index
            text_color = 'white' if j < n_colors else 'black' 
            # Simple brightness check to switch text color could be added here
            
            if n_colors <= 10:
                ax.text(j + 0.5, 0.5, color, ha='center', va='center', color='white', fontsize=8, fontweight='bold', rotation=90)
        
        ax.set_xlim(0, n_colors)
        ax.set_ylim(0, 1)
        ax.set_title(name, fontsize=10, loc='left')
        ax.axis('off')
        
    # Hide unused axes
    for j in range(i + 1, len(axes)):
        axes[j].axis('off')
        
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"Palette preview saved to {filename}")

if __name__ == "__main__":
    # Select some key palettes to visualize
    # We don't visualize all 86 because it's too huge, let's pick the best ones
    
    key_palettes = {
        "NPG_NRC (Nature)": mcm_colors.NPG_NRC,
        "AAAS_DEFAULT (Science)": mcm_colors.AAAS_DEFAULT,
        "NEJM_DEFAULT (New England J. Med)": mcm_colors.NEJM_DEFAULT,
        "LANCET_LANONC (Lancet)": mcm_colors.LANCET_LANONC,
        "JAMA_DEFAULT (JAMA)": mcm_colors.JAMA_DEFAULT,
        "JCO_DEFAULT (J. Clin. Oncology)": mcm_colors.JCO_DEFAULT,
        "IGV_DEFAULT (51 colors for many categories)": mcm_colors.IGV_DEFAULT,
        "UCSCGB_DEFAULT (26 colors)": mcm_colors.UCSCGB_DEFAULT,
        "D3_CATEGORY20 (Web Standard)": mcm_colors.D3_CATEGORY20,
        "D3_CATEGORY10": mcm_colors.D3_CATEGORY10,
        "OBSERVABLE10": mcm_colors.OBSERVABLE_OBSERVABLE10,
        "FLATUI_DEFAULT": mcm_colors.FLATUI_DEFAULT,
        "STAR_TREK": mcm_colors.STARTREK_UNIFORM,
        "RICK_AND_MORTY": mcm_colors.RICKANDMORTY_SCHWIFTY,
        "SIMPSONS": mcm_colors.SIMPSONS_SPRINGFIELD
    }
    
    plot_palettes(key_palettes)
