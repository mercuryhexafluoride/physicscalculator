import math

def display_menu():
    print("Kinematics Calculator")
    print("Select the variable you want to solve for:")
    print("1. Final velocity (v)")
    print("2. Initial velocity (u)")
    print("3. Displacement (s)")
    print("4. Time (t)")
    print("5. Acceleration (a)")
    print("6. Exit")

def solve_final_velocity():
    u = float(input("Enter the initial velocity (u) in m/s: "))
    a = float(input("Enter the acceleration (a) in m/s²: "))
    t = float(input("Enter the time (t) in seconds: "))
    v = u + a * t
    print(f"Final velocity (v) = {v:.4f} m/s")

def solve_initial_velocity():
    v = float(input("Enter the final velocity (v) in m/s: "))
    a = float(input("Enter the acceleration (a) in m/s²: "))
    t = float(input("Enter the time (t) in seconds: "))
    u = v - a * t
    print(f"Initial velocity (u) = {u:.4f} m/s")

def solve_displacement():
    u = float(input("Enter the initial velocity (u) in m/s: "))
    v = float(input("Enter the final velocity (v) in m/s: "))
    t = float(input("Enter the time (t) in seconds: "))
    s = ((u + v) / 2) * t
    print(f"Displacement (s) = {s:.4f} m")

def solve_time():
    u = float(input("Enter the initial velocity (u) in m/s: "))
    v = float(input("Enter the final velocity (v) in m/s: "))
    a = float(input("Enter the acceleration (a) in m/s²: "))
    if a != 0:
        t = (v - u) / a
        print(f"Time (t) = {t:.4f} seconds")
    else:
        print("Acceleration cannot be zero for this calculation.")

def solve_acceleration():
    u = float(input("Enter the initial velocity (u) in m/s: "))
    v = float(input("Enter the final velocity (v) in m/s: "))
    t = float(input("Enter the time (t) in seconds: "))
    if t != 0:
        a = (v - u) / t
        print(f"Acceleration (a) = {a:.4f} m/s²")
    else:
        print("Syntax Error: value = 0")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            solve_final_velocity()
        elif choice == "2":
            solve_initial_velocity()
        elif choice == "3":
            solve_displacement()
        elif choice == "4":
            solve_time()
        elif choice == "5":
            solve_acceleration()
        elif choice == "6":
            print("Exiting the calculator")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
