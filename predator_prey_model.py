import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

class PredatorPreySimulation:
    def __init__(self, master):
        self.master = master
        master.title("Predator-Prey Simulation")

        # Simulation parameters
        self.alpha = tk.DoubleVar(value=0.1)
        self.beta = tk.DoubleVar(value=0.02)
        self.delta = tk.DoubleVar(value=0.01)
        self.gamma = tk.DoubleVar(value=0.1)
        self.prey_initial = tk.DoubleVar(value=40)
        self.predator_initial = tk.DoubleVar(value=9)
        self.T = tk.DoubleVar(value=200)
        self.dt = tk.DoubleVar(value=0.1)

        # Create GUI components
        self.create_widgets()
        
    def create_widgets(self):
        # Parameters frame
        params_frame = tk.Frame(self.master)
        params_frame.pack(side=tk.LEFT, padx=10, pady=10)
        
        # Alpha parameter
        tk.Label(params_frame, text="Alpha (prey growth rate):").grid(row=0, column=0, sticky=tk.W)
        tk.Entry(params_frame, textvariable=self.alpha).grid(row=0, column=1)

        # Beta parameter
        tk.Label(params_frame, text="Beta (predation rate):").grid(row=1, column=0, sticky=tk.W)
        tk.Entry(params_frame, textvariable=self.beta).grid(row=1, column=1)

        # Delta parameter
        tk.Label(params_frame, text="Delta (predator increase rate):").grid(row=2, column=0, sticky=tk.W)
        tk.Entry(params_frame, textvariable=self.delta).grid(row=2, column=1)

        # Gamma parameter
        tk.Label(params_frame, text="Gamma (predator death rate):").grid(row=3, column=0, sticky=tk.W)
        tk.Entry(params_frame, textvariable=self.gamma).grid(row=3, column=1)

        # Prey initial population
        tk.Label(params_frame, text="Initial prey population:").grid(row=4, column=0, sticky=tk.W)
        tk.Entry(params_frame, textvariable=self.prey_initial).grid(row=4, column=1)

        # Predator initial population
        tk.Label(params_frame, text="Initial predator population:").grid(row=5, column=0, sticky=tk.W)
        tk.Entry(params_frame, textvariable=self.predator_initial).grid(row=5, column=1)

        # Total time
        tk.Label(params_frame, text="Total time:").grid(row=6, column=0, sticky=tk.W)
        tk.Entry(params_frame, textvariable=self.T).grid(row=6, column=1)

        # Time step
        tk.Label(params_frame, text="Time step:").grid(row=7, column=0, sticky=tk.W)
        tk.Entry(params_frame, textvariable=self.dt).grid(row=7, column=1)

        # Start simulation button
        start_button = tk.Button(params_frame, text="Start Simulation", command=self.start_simulation)
        start_button.grid(row=8, columnspan=2, pady=10)

        # Save results button
        save_button = tk.Button(params_frame, text="Save Results", command=self.save_results)
        save_button.grid(row=9, columnspan=2, pady=10)

        # Plot frame
        plot_frame = tk.Frame(self.master)
        plot_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=plot_frame)
        self.canvas.get_tk_widget().pack()

    def start_simulation(self):
        alpha = self.alpha.get()
        beta = self.beta.get()
        delta = self.delta.get()
        gamma = self.gamma.get()
        prey_initial = self.prey_initial.get()
        predator_initial = self.predator_initial.get()
        T = self.T.get()
        dt = self.dt.get()

        time = np.arange(0, T, dt)
        prey_population = np.zeros(len(time))
        predator_population = np.zeros(len(time))

        prey_population[0] = prey_initial
        predator_population[0] = predator_initial

        for t in range(1, len(time)):
            prey_population[t] = prey_population[t-1] + (alpha * prey_population[t-1] - beta * prey_population[t-1] * predator_population[t-1]) * dt
            predator_population[t] = predator_population[t-1] + (delta * prey_population[t-1] * predator_population[t-1] - gamma * predator_population[t-1]) * dt

        self.plot_results(time, prey_population, predator_population)

    def plot_results(self, time, prey_population, predator_population):
        self.ax.clear()
        self.ax.plot(time, prey_population, label='Prey Population')
        self.ax.plot(time, predator_population, label='Predator Population')
        self.ax.legend()
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Population')
        self.ax.set_title('Predator-Prey Simulation')
        self.ax.grid(True)
        self.canvas.draw()

    def save_results(self):
        alpha = self.alpha.get()
        beta = self.beta.get()
        delta = self.delta.get()
        gamma = self.gamma.get()
        prey_initial = self.prey_initial.get()
        predator_initial = self.predator_initial.get()
        T = self.T.get()
        dt = self.dt.get()

        time = np.arange(0, T, dt)
        prey_population = np.zeros(len(time))
        predator_population = np.zeros(len(time))

        prey_population[0] = prey_initial
        predator_population[0] = predator_initial

        for t in range(1, len(time)):
            prey_population[t] = prey_population[t-1] + (alpha * prey_population[t-1] - beta * prey_population[t-1] * predator_population[t-1]) * dt
            predator_population[t] = predator_population[t-1] + (delta * prey_population[t-1] * predator_population[t-1] - gamma * predator_population[t-1]) * dt

        np.savetxt('simulation_results.csv', np.column_stack((time, prey_population, predator_population)),
                   delimiter=',', header='Time,Prey Population,Predator Population', comments='')

if __name__ == "__main__":
    root = tk.Tk()
    app = PredatorPreySimulation(root)
    root.mainloop()
