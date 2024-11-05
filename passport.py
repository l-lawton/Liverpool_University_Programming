from datetime import datetime

class Passport:
    """A class representing a digital passport with travel tracking capabilities.

    This class implements a digital passport system that stores personal information
    and tracks travel history through country visit stamps.

    Attributes:
        first_name (str): First name of the passport holder
        last_name (str): Last name of the passport holder
        dob (datetime.date): Date of birth of the passport holder
        country (str): Country of birth of the passport holder
        exp_date (datetime.date): Expiration date of the passport
    """

    # Class variable to track passport numbers
    _passport_counter = 0

    def __init__(self, first_name, last_name, dob, country, exp_date):
        """Initialize a new passport with personal information.

        Args:
            first_name (str): First name of the passport holder
            last_name (str): Last name of the passport holder
            dob (str): Date of birth in ISO format (YYYY-MM-DD)
            country (str): Country of birth
            exp_date (str): Expiration date in ISO format (YYYY-MM-DD)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.dob = datetime.fromisoformat(dob).date()
        self.country = country
        self.exp_date = datetime.fromisoformat(exp_date).date()
        self._visited_countries = {}
        self._passport_id = Passport._passport_counter
        Passport._passport_counter += 1

    def is_valid(self):
        """Check if the passport is currently valid based on expiration date.

        Returns:
            bool: True if passport has not expired, False otherwise
        """
        return datetime.now().date() < self.exp_date

    def summary(self):
        """Generate a human-readable summary of the passport information.

        Returns:
            str: Summary string including holder details and validity status
        """
        validity = "valid" if self.is_valid() else "invalid"
        return (f"This passport belongs to {self.first_name} {self.last_name}, "
                f"born on {self.dob} in {self.country}. It is {validity}.")

    def check_data(self, first_name, last_name, dob, country):
        """Verify if provided data matches passport data and passport is valid.

        Args:
            first_name (str): First name to verify
            last_name (str): Last name to verify
            dob (str): Date of birth in ISO format to verify
            country (str): Country to verify

        Returns:
            bool: True if all data matches and passport is valid, False otherwise
        """
        check_dob = datetime.fromisoformat(dob).date()
        return (
            self.first_name == first_name
            and self.last_name == last_name
            and self.dob == check_dob
            and self.country == country
            and self.is_valid()
        )

    def stamp(self, country):
        """Record a visit to a country if different from passport country.

        Args:
            country (str): Name of country being visited
        """
        if country != self.country:
            self._visited_countries[country] = self._visited_countries.get(country, 0) + 1

    def countries_visited(self):
        """Get list of all countries visited.

        Returns:
            list: List of country names that have been stamped
        """
        return list(self._visited_countries.keys())

    def times_visited(self, country):
        """Get the number of visits to a specific country.

        Args:
            country (str): Name of country to check

        Returns:
            int: Number of times the country has been visited
        """
        return self._visited_countries.get(country, 0)

    def sum_square_visits(self):
        """Calculate sum of squared visit counts for all visited countries.

        Returns:
            int: Sum of squares of visit counts
        """
        return sum(count * count for count in self._visited_countries.values())

    def passport_number(self):
        """Get the unique passport identification number.

        Returns:
            int: Passport ID number
        """
        return self._passport_id