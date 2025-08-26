import pandas as pd
import time

# --- Decorator Implementation ---
def execution_logger(func):
    """A decorator to log function execution time."""
    def wrapper(*args, **kwargs):
        print(f"Executing function: '{func.__name__}'...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' finished in {end_time - start_time:.4f} seconds.")
        return result
    return wrapper

# --- OOPS Implementation ---
class House:
    """A class to represent a single house, with a decorated method."""
    def __init__(self, house_data):
        self.id = house_data['Id']
        self.area = house_data['Area']
        self.bedrooms = house_data['Bedrooms']
        self.bathrooms = house_data['Bathrooms']
        self.floors = house_data['Floors']
        self.year_built = house_data['YearBuilt']
        self.location = house_data['Location']
        self.condition = house_data['Condition']
        self.garage = house_data['Garage']
        self.price = house_data['Price']

    def __repr__(self):
        return (f"House(Id={self.id}, Area={self.area}, "
                f"Bedrooms={self.bedrooms}, Price={self.price})")

    @execution_logger
    def get_price_per_area(self):
        """Calculates the price per unit area."""
        time.sleep(0.01)  # Simulate a task to show decorator timing
        if self.area > 0:
            return self.price / self.area
        return 0

# --- Iterator Implementation ---
class HouseCollection:
    """A collection of House objects that is also an iterator."""
    def __init__(self, dataframe):
        self.houses = [House(row) for _, row in dataframe.iterrows()]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.houses):
            result = self.houses[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

# --- Generator Implementation ---
def house_generator(file_path):
    """A generator function to yield House objects from a CSV file."""
    df_chunk = pd.read_csv(file_path, chunksize=1)
    for chunk in df_chunk:
        yield House(chunk.iloc[0])

# --- Demonstration ---
if __name__ == '__main__':
    # Load the data
    file_path = 'House Price Prediction Dataset.csv'
    df = pd.read_csv(file_path)

    # Demonstrate OOPS and Iterators
    print("--- Demonstrating OOPS and Iterators ---")
    house_collection = HouseCollection(df)
    for i, house in enumerate(house_collection):
        if i < 3:
            print(f"House {house.id}: Price per area = ${house.get_price_per_area():.2f}")
        else:
            break

    # Demonstrate Generators
    print("\n--- Demonstrating Generators ---")
    gen = house_generator(file_path)
    for i, house in enumerate(gen):
        if i < 3:
            print(f"House {house.id}: Price per area = ${house.get_price_per_area():.2f}")
        else:
            break
