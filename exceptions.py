class ServiceError(Exception):
    pass

class UserNotFoundError(ServiceError):
    pass

class ProductNotFoundError(ServiceError):
    pass

class OrderNotFoundError(ServiceError):
    pass

class InvalidQuantityError(ServiceError):
    pass