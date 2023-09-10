# import tkinter as tk
# from tkinter import ttk
# from geopy.geocoders import Nominatim
# import math
#
# class GPSNavigator:
#     def __init__(self):
#         self.geolocator = Nominatim(user_agent="gps_navigator")
#         self.current_location = None
#         self.destination = None
#
#     def set_current_location(self, location):
#         self.current_location = location
#
#     def set_destination(self, address):
#         self.destination = self.geolocator.geocode(address)
#
#     def calculate_bearing(self):
#         if self.current_location and self.destination:
#             # Calculate bearing using GPS coordinates
#             lat1, lon1 = self.current_location.latitude, self.current_location.longitude
#             lat2, lon2 = self.destination.latitude, self.destination.longitude
#             dlat = math.radians(lat2 - lat1)
#             dlon = math.radians(lon2 - lon1)
#             y = math.sin(dlon) * math.cos(math.radians(lat2))
#             x = math.cos(math.radians(lat1)) * math.sin(math.radians(lat2)) - math.sin(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.cos(dlon)
#             initial_bearing = math.atan2(y, x)
#             initial_bearing = math.degrees(initial_bearing)
#             bearing = (initial_bearing + 360) % 360
#             return bearing
#         return None
#
# def calculate_button_click():
#     current_location = current_location_entry.get()
#     destination = destination_entry.get()
#
#     navigator.set_current_location(navigator.geolocator.geocode(current_location))
#     navigator.set_destination(destination)
#     bearing = navigator.calculate_bearing()
#
#     if bearing is not None:
#         result_label.config(text=f"Bearing: {bearing:.2f} degrees")
#     else:
#         result_label.config(text="Error calculating bearing")
#
# # Initialize GPS Navigator
# navigator = GPSNavigator()
#
# # Create GUI
# root = tk.Tk()
# root.title("GPS Navigator")
#
# # Define GUI elements
# current_location_label = ttk.Label(root, text="Current Location:")
# current_location_entry = ttk.Entry(root)
# destination_label = ttk.Label(root, text="Destination:")
# destination_entry = ttk.Entry(root)
# calculate_button = ttk.Button(root, text="Calculate Bearing", command=calculate_button_click)
# result_label = ttk.Label(root, text="")
#
# # Layout GUI elements
# current_location_label.pack()
# current_location_entry.pack()
# destination_label.pack()
# destination_entry.pack()
# calculate_button.pack()
# result_label.pack()
#
# root.mainloop()
