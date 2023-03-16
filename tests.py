"""Tests to make some huge Gmaps. See README.md for more info."""

from hugegmaps import create_map


def test_calibration():
    """Quick single screenshot of Philly Art Museum for calibration.
    Takes about 10 seconds to run.
    """
    create_map(
        lat_start=39.9644273,
        long_start=-75.1801129,
        number_rows=1,
        number_cols=1,
        scale=0.5,
        sleep_time=0,
        offset_left=0,  # My value: 0.05
        offset_top=0,  # My value: 0.17
        offset_right=0,  # My value: 0.03
        offset_bottom=0,  # My value: 0.09
        outfile='huge_gmap_calibration.png',

    )


def test_small_area():
    """Small 3x3 grid of images to test combining images.
    Takes about 60 seconds to run.
    """
    create_map(
        lat_start=39.9644273,
        long_start=-75.1801129,
        number_rows=3,
        number_cols=3,
        scale=0.2,
        sleep_time=3,
        offset_left=0.05,
        offset_top=0.17,
        offset_right=0.03,
        offset_bottom=0.09,
        outfile='huge_gmap_small_area.png',
    )


def test_philly_high_res():
    """High-res map of Philly. Creates the final version I hung on my wall.
    Takes about 20 minutes to run.
    """
    create_map(
        lat_start=39.9746524,
        long_start=-75.2020434,
        number_rows=16,
        number_cols=8,
        scale=1,
        sleep_time=5,
        offset_left=0.05,
        offset_top=0.17,
        offset_right=0.03,
        offset_bottom=0.09,
        outfile='huge_gmap_high_res.png',
    )
def coumn(fname,csd):
    """Small 3x3 grid of images to test combining images.
    Takes about 60 seconds to run.
    """
    create_map(
        lat_start=17.6014779,
        long_start=78.4638268,
        number_rows=2,
        number_cols=1,
        sleep_time=3,
        offset_left=0.05,
        offset_top=0.17,
        offset_right=0.03,
        offset_bottom=0.09,
        outfile=fname,
        cons_lat=csd
    )

def rws(fname):
    """Small 3x3 grid of images to test combining images.
    Takes about 60 seconds to run.
    """
    create_map(
        lat_start=17.6014779,
        long_start=78.4638268,
        number_rows=2,
        number_cols=2,
        sleep_time=5,
        offset_left=0.05,
        offset_top=0.17,
        offset_right=0.03,
        offset_bottom=0.09,
        outfile=fname,
    )

csd = 0.00000511
coumn(f'cols{csd}.png',csd)
rofs = 0.000005363
#rws(f'test1.png')
