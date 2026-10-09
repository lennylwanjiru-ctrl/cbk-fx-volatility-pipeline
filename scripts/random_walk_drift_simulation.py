import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run_random_walk_simulations():
    print(" Launching Random Walk with Drift Simulation Engine...")
    
    # 1. Simulation Parameters
    n = 1000
    delta = 0.01
    sigma = 1.0
    t = np.arange(1, n + 1)
    
    # Theoretical mean function: mu_t = 0.01 * t
    mean_function = delta * t
    
    # Configure a clean 2x3 subplot matrix for the six simulations
    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(2, 3, figsize=(16, 10), sharex=True, sharey=False)
    axes = axes.flatten()
    
    # Seed for reproducibility while maintaining unique random iterations
    np.random.seed(42)
    
    print(" Simulating paths and computing ordinary least squares lines...")
    for i in range(6):
        # Generate random white noise shocks
        white_noise = np.random.normal(0, sigma, n)
        
        # Construct the random walk with drift: x_t = x_{t-1} + delta + w_t
        drifts = np.full(n, delta)
        x = np.cumsum(drifts + white_noise)
        
        # Fit zero-intercept OLS regression: x_t = beta * t + w_t
        beta_hat = np.sum(t * x) / np.sum(t**2)
        fitted_line = beta_hat * t
        
        # Plot using raw strings to safely handle LaTeX components
        ax = axes[i]
        ax.plot(t, x, color="#1f77b4", alpha=0.6, label=r"Simulated Data ($x_t$)")
        ax.plot(t, mean_function, color="black", linestyle="-", linewidth=2, label=r"True Mean ($\mu_t$)")
        ax.plot(t, fitted_line, color="red", linestyle="--", linewidth=2, label=fr"Fitted Line ($\hat{{\beta}}$={beta_hat:.4f})")
        
        ax.set_title(f"Realization Run #{i+1}", fontsize=11, fontweight="bold")
        
        # Add labels based on subplot position index
        if i >= 3:
            ax.set_xlabel("Time Step (t)")
        if i == 0 or i == 3:
            ax.set_ylabel("Value")
            
        ax.legend(fontsize=9, loc="upper left")

    plt.suptitle("Stochastic Simulation: Random Walk with Drift vs. OLS Estimators", fontsize=14, fontweight="bold", y=0.96)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    
    # 2. Save the final graphic output safely
    output_dir = "documentation"
    os.makedirs(output_dir, exist_ok=True)
    save_path = os.path.join(output_dir, "random_walk_simulations.png")
    plt.savefig(save_path, dpi=300)
    plt.close()
    
    print("\n" + "="*65)
    print(" STOCHASTIC REPLICATED SIMULATIONS COMPLETED SUCCESSFULLY!")
    print(f" Master dashboard layout saved to: '{save_path}'")
    print("=======================================================\n")

if __name__ == "__main__":
    run_random_walk_simulations()