"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional),
    diameter in kilometers (optional - sometimes unknown), and whether it's
    marked as potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """

    def __init__(self, pde: str, **info):
        """Create a new `NearEarthObject`.

        :parameters:
            pde: string
                The primary designation of the NEO
            info: keyword arguments
                Additional information about the NEO such as name, diameter,
                hazardous, etc.
        """
        # Assign information from the arguments passed to the constructor
        # onto attributes named `designation`, `name`, `diameter`, and
        # `hazardous`. You should coerce these values to their appropriate data
        # type and handle any edge cases, such as a empty name being
        # represented by `None`and a missing diameter being represented by
        # `float('nan')`.
        self.designation = str(pde)
        self.name = info.get('name')
        if self.name:
            self.name = str(self.name)
        self.diameter = float(info.get('diameter', 'nan'))
        self.hazardous = bool(info.get('hazardous', False))

        # Create an empty initial collection of linked approaches.
        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        if self.name:
            return self.designation + ' ' + self.name
        else:
            return self.designation

    def __str__(self):
        """Return `str(self)`."""
        # Return a human-readable string representation.
        if self.hazardous:
            tobe = 'is'
        else:
            tobe = 'is not'
        return f"A NearEarthObject with full name {self.fullname}. " \
            f"It has a diameter of {self.diameter:.2f} km and \
                {tobe} hazardous."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of \
            this object."""
        return f"NearEarthObject(designation={self.designation!r}, \
            name={self.name!r}, " \
            f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})"


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach
    to Earth, such as the date and time (in UTC) of closest approach, the
    nominal approach distance in astronomical units, and the relative approach
    velocity in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initially, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """

    def __init__(self, time, distance, velocity, _designation: str):
        """Create a new `CloseApproach`.

        :parameters:
            time : string
                NASA-formatted calendar date/time description using the English
                locale's month names.
            distance : string or float
                Nominal approach distance in au of the NEU to Earth at the
                closest point.
            velocity : string or float
                Velocity in km/s of the NEO relative to Earth at the closest
                point.
            _designation: string
                Primary designation of the NEO in place of a NearEarthObject
                typed object.
        """
        self._designation = str(_designation)
        if time:
            self.time = cd_to_datetime(time)
        else:
            self.time = None
        self.distance = float(distance)
        self.velocity = float(velocity)

        # Create an attribute for the referenced NEO, originally None.
        self.neo = None

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach
        time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default
        representation includes seconds - significant figures that don't exist
        in our input data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        return datetime_to_str(self.time)

    def __str__(self):
        """Return `str(self)`."""
        # Return a human-readable string representation.
        return f"A CloseApproach by {self._designation} at {self.time_str}, \
            at a distance of {self.distance:.2f} au " \
            f"and a velocity of {self.velocity:.2f}"

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of \
            this object."""
        return f"CloseApproach(time={self.time_str!r}, \
            distance={self.distance:.2f}, " \
            f"velocity={self.velocity:.2f}, neo={self.neo!r})"
