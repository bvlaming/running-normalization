import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format="%(asctime)s %(name)-4s: %(module)-4s :%(levelname)-8s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

LOGGER = logging.getLogger(__name__)

LOGGER.info("begin data loading")
# steps:
# load data from websites (quite possibly, multiple websites with different parsing/context)
# create a few data classes that we parse into
# store them in some way, somewhere (locally? mongo? postgres?)


# once we have the data, we can do actual normalization work
# this is logic that we need to think through

k = "abcdefdgh"
first_index = k.find("d")

first_part = k[:first_index + 1]
remainder = k[first_index + 1:]

result = first_part[::-1] + remainder
LOGGER.info(first_index)
LOGGER.info(first_part)
LOGGER.info(remainder)
LOGGER.info(result)