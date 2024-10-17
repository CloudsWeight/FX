from fed import Fed
fed = Fed()

def test_fxs():
	data = fed.fxs()
	assert fed.status_code == 200

