from direct.showbase.PythonUtil import invertDictLossless

messageDirector = {
	'OTP_SERVER_ROOT_DO_ID': 4007,
	'CHANNEL_CLIENT_BROADCAST': 4014,
	'BAD_CHANNEL_ID': 0,
	'BAD_ZONE_ID': 0,
	'BAD_DO_ID': 0,
	'CONTROL_MESSAGE': 4001,
	'CONTROL_SET_CHANNEL': 2001,
	'CONTROL_REMOVE_CHANNEL': 2002,
	'CONTROL_SET_CON_NAME': 2004,
	'CONTROL_SET_CON_URL': 2005,
	'CONTROL_ADD_RANGE': 2008,
	'CONTROL_REMOVE_RANGE': 2009,
	'CONTROL_ADD_POST_REMOVE': 2010,
	'CONTROL_CLEAR_POST_REMOVE': 2011 }

MsgDirectorTypes = invertDictLossless(messageDirector)
globals().update(messageDirector)