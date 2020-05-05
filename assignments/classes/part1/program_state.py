import state
s = state.State('Alaska', 'Juneau', 700000)

s.record_births(150)
s.record_deaths(10)

s.display()
print(s.get_local_time())
