from typing import Union

MAXIMUM_TEMPERATURE = 800
MINIMUM_NEUTRONS_EMITTED = 500
MAXIMUM_PRODUCT = 500000

EFFICIENCY_STATUS = {
    "green": 80,
    "orange": 60,
    "red": 30,
    "black": 0,
}

SAFETY_STATUS = ["DANGER", "NORMAL", "LOW"]
SAFETY_THRESHOLD = 0.10


def is_criticality_balanced(
    temperature: Union[int, float], neutrons_emitted: Union[int, float]
) -> bool:
    """Verify criticality is balanced.

    :param temperature: temperature value (integer or float)
    :param neutrons_emitted: number of neutrons emitted per second (integer or float)
    :return:  boolean True if conditions met, False if not

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """

    return (
        temperature < MAXIMUM_TEMPERATURE
        and neutrons_emitted > MINIMUM_NEUTRONS_EMITTED
        and temperature * neutrons_emitted < MAXIMUM_PRODUCT
    )


def reactor_efficiency(
    voltage: Union[int, float],
    current: Union[int, float],
    theoretical_max_power: Union[int, float],
) -> str:
    """Assess reactor efficiency zone.

    :param voltage: voltage value (integer or float)
    :param current: current value (integer or float)
    :param theoretical_max_power: power that corresponds to a 100% efficiency (integer or float)
    :return: str one of 'green', 'orange', 'red', or 'black'

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """

    efficiency = voltage * current / theoretical_max_power * 100

    for status, minimum in EFFICIENCY_STATUS.items():
        if efficiency >= minimum:
            return status

    raise RuntimeError("This code line should be unreachable.")


def fail_safe(
    temperature: Union[int, float],
    neutrons_produced_per_second: Union[int, float],
    threshold: Union[int, float],
) -> str:
    """Assess and return status code for the reactor.

    :param temperature: value of the temperature (integer or float)
    :param neutrons_produced_per_second: neutron flux (integer or float)
    :param threshold: threshold (integer or float)
    :return: str one of: 'LOW', 'NORMAL', 'DANGER'

    - `temperature * neutrons per second` < 90% of `threshold` == 'LOW'
    - `temperature * neutrons per second` +/- 10% of `threshold` == 'NORMAL'
    - `temperature * neutrons per second` is not in the above-stated ranges ==  'DANGER'
    """

    criticality = temperature * neutrons_produced_per_second
    interval = threshold * SAFETY_THRESHOLD
    boundaries = [threshold + interval, threshold - interval, 0]

    for status, boundary in zip(SAFETY_STATUS, boundaries):
        if criticality >= boundary:
            return status

    raise RuntimeError("This code line should be unreachable.")
