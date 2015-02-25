
class BaseInvoice:
	def __init__(self, projectId, projectSecret):
		"""Create a new instance of BaseInvoice

		Keyword argument:
		projectId -- id of the ProcessOut's project
		projectSecret -- secret of the ProcessOut's project
		"""
		self._host          = 'https://api.processout.com/v1'
		self._projectId     = projectId
		self._projectSecret = projectSecret

		self._enableCoupon = False
		self._returnUrl    = None
		self._cancelUrl    = None
		self._notifyUrl    = None
		self._custom       = None

	@property
	def host(self):
		"""Get the ProcessOut's host"""
		return self._host

	@property
	def projectId(self):
		"""Get the ProcessOut's project id"""
		return self._projectId

	@property
	def projectSecret(self):
		"""Get the ProcessOut's project secret"""
		return self._projectSecret

	@property
	def enableCoupon(self):
		"""Determine if coupons are enabled on the invoice"""
		return self._enableCoupon

	@enableCoupon.setter
	def enableCoupon(self, value):
		"""Set if coupons are enabled on the invoice

		Keyword argument:
		value -- True: coupons enabled; False: disabled
		"""
		self._enableCoupon = value

	@property
	def returnUrl(self):
		"""Get the return URL"""
		return self._returnUrl

	@returnUrl.setter
	def returnUrl(self, value):
		"""Set the return URL

		Keyword argument:
		value -- new return URL
		"""
		self._returnUrl = value

	@property
	def cancelUrl(self):
		"""Get te cancel URL"""
		return self._cancelUrl

	@cancelUrl.setter
	def cancelUrl(self, value):
		"""Set the cancel URL

		Keyword argument:
		value -- new cancel URL
		"""
		self._cancelUrl = value

	@property
	def notifyUrl(self):
		"""Get the notify URL (used for callbacks)"""
		return self._notifyUrl

	@notifyUrl.setter
	def notifyUrl(self, value):
		"""Set the notify URL (used for callbacks)

		Keyword argument:
		value -- new notify URL
		"""
		self._notifyUrl = value

	@property
	def custom(self):
		"""Get the custom field value"""
		return self._custom

	@custom.setter
	def custom(self, value):
		"""Set the custom field value

		Keyword argument:
		value -- new custom field value
		"""
		self._custom = value


	def _generateData(self):
		"""Generate the data used during the ProcessOut's request"""
		return {
			'enabled_coupon': self.enableCoupon,
			'return_url':     self.returnUrl,
			'cancel_url':     self.cancelUrl,
			'notify_url':     self.notifyUrl,
			'custom':         self.custom
		}