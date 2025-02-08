import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

class RubberBandSimulator:
    def __init__(self):
        self.rest_length = 1.0
        self.k = 1.0  # spring constant
        self.damping = 0.1
        
    def force_series(self, displacement):
        """Calculate force for rubber bands in series"""
        # Each rubber band takes half the displacement
        individual_displacement = displacement / 2
        return self.k * individual_displacement
    
    def force_parallel(self, displacement):
        """Calculate force for rubber bands in parallel"""
        # Forces add up
        return 2 * self.k * displacement
    
    def force_combined(self, displacement):
        """Calculate force for rubber bands in both series and parallel"""
        # Combination of series and parallel effects
        series_force = self.force_series(displacement)
        parallel_force = self.force_parallel(displacement/2)
        return (series_force + parallel_force) / 2

    def simulate_pull(self, arrangement, max_displacement=2.0, steps=100):
        """Simulate pulling the rubber band arrangement"""
        displacements = np.linspace(0, max_displacement, steps)
        forces = np.zeros_like(displacements)
        
        for i, d in enumerate(displacements):
            if arrangement == 'series':
                forces[i] = self.force_series(d)
            elif arrangement == 'parallel':
                forces[i] = self.force_parallel(d)
            else:  # combined
                forces[i] = self.force_combined(d)
                
        return displacements, forces

    def plot_comparison(self):
        """Plot force-length relationships for all arrangements"""
        displacements, forces_series = self.simulate_pull('series')
        _, forces_parallel = self.simulate_pull('parallel')
        _, forces_combined = self.simulate_pull('combined')
        
        plt.figure(figsize=(10, 6))
        plt.plot(displacements, forces_series, 'b-', label='Series')
        plt.plot(displacements, forces_parallel, 'r-', label='Parallel')
        plt.plot(displacements, forces_combined, 'g-', label='Combined')
        
        plt.xlabel('Displacement (normalized)')
        plt.ylabel('Force (normalized)')
        plt.title('Force-Length Relationships for Different Rubber Band Arrangements')
        plt.legend()
        plt.grid(True)
        plt.show()

    def interactive_demo(self):
        """Run an interactive demonstration"""
        print("\nRubber Band Arrangement Simulator")
        print("================================")
        
        while True:
            print("\nSelect arrangement:")
            print("1. Series")
            print("2. Parallel")
            print("3. Combined")
            print("4. Show comparison plot")
            print("5. Exit")
            
            choice = input("\nEnter choice (1-5): ")
            
            if choice == '5':
                break
            elif choice == '4':
                self.plot_comparison()
                continue
                
            arrangement = {
                '1': 'series',
                '2': 'parallel',
                '3': 'combined'
            }.get(choice)
            
            if arrangement:
                print(f"\nSimulating {arrangement} arrangement...")
                displacement = float(input("Enter displacement (0-2): "))
                
                if arrangement == 'series':
                    force = self.force_series(displacement)
                    print("\nSeries Arrangement Analysis:")
                    print("- Lower force output")
                    print("- Greater total displacement")
                    print("- Similar to muscle sarcomeres in series")
                    print("- Favors velocity over force")
                    
                elif arrangement == 'parallel':
                    force = self.force_parallel(displacement)
                    print("\nParallel Arrangement Analysis:")
                    print("- Higher force output")
                    print("- Less total displacement")
                    print("- Similar to parallel muscle fibers")
                    print("- Favors force over velocity")
                    
                else:
                    force = self.force_combined(displacement)
                    print("\nCombined Arrangement Analysis:")
                    print("- Balanced force-displacement relationship")
                    print("- Moderate force and displacement")
                    print("- Most similar to actual muscle architecture")
                    print("- Combines advantages of both arrangements")
                
                print(f"\nCalculated force: {force:.2f}")
                time.sleep(1)

if __name__ == "__main__":
    simulator = RubberBandSimulator()
    simulator.interactive_demo()
