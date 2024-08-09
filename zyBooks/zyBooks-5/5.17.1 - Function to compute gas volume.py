gas_const = 8.3144621

''' Your solution goes here '''
def compute_gas_volume(p,t,m):
    V = (m * gas_const * t ) / p
    return V

gas_pressure = float(input())
gas_moles = float(input())
gas_temperature = float(input())
gas_volume = 0.0

gas_volume = compute_gas_volume(gas_pressure, gas_temperature, gas_moles)
print('Gas volume:', gas_volume, 'm^3')