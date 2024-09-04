from django.core.exceptions import ValidationError

# validate pagination query for GET countries endpoint 
def validate_query(offset, limit):
    try:
        int_offset = int(offset)
        if int_offset < 0:
            raise ValidationError("Offset must be greater than or equal to 0.")
    except ValueError:
        raise ValidationError("Offset must be an integer.")

    if limit is not None:
        try:
            int_limit = int(limit)
            if int_limit < 0:
                raise ValidationError("Limit must be greater than or equal to 0.")
        except ValueError:
            raise ValidationError("Limit must be an integer.")