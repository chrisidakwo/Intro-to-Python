Instructions
1. Update the VehicleStock.txt file to include data for vans and trucks, just like there is for cars. Don't remove the header lines for vans and trucks, that is, the lines that looks as such:

#VANS#
make-model,kmltrs,num-passengers,vin

#TRUCKS#
kmltrs,length,num-rooms,vin

Just append your data below the lines as comma-delimited strings.


2. The method "__populate_vehicles(self.__vehicle_info_file)" is not properly reading information of the car from the text file. You can consider rewriting the method or improving it to enable reading cars, vans, and trucks information from the text file. The method can be found on line 66 in "system_interface.py"