"""
Recipes available to data with tags ['MAROONX', 'SCI']
Default is "reduce".
"""

recipe_tags = set(['MAROONX', 'SCI'])

def reduce(p):
    """
    This recipe processes MAROON-X science echelle spectrum, (1) it traces
    and identifies the fibers and orders in a 2D processed flat and
    (2) performs both regular (aka 'box') and optimum extraction
    to produce 1D extracted spectra for 2D input spectra.

    Tracing and identifying fibers and orders is done on a
    (preferably background subtracted) 2D processed flat.  This step
    needs to be done only once per flat and the results can be
    applied to all subsequent flux extraction steps for other data.
    The routine allows to specify which fibers are illuminated by
    flat light to minimize wrong order/fiber identification.

    Box extraction is the simple summation of all spatial pixels
    in a given fiber/order combination. Optimal extraction is per
    default only applied to fibers illuminated with flat (F)
    and science (O) input.

    TODO: Once the Static and Dynamic wavecal recipes have been created, an additional
    set of parameters in this recipe should be added to request the calibration
    frame produced by the dynamic wavecal recipe and utilize it to perform a
    drift corrected wavelength calibration for the science frame fibers.
    Parameters
    ----------
    p : PrimitivesCORE object
        A primitive set matching the recipe_tags.
    """

    p.prepare()
    p.checkArm()
    p.addDQ()  # just placeholder until MX is in caldb
    p.overscanCorrect()
    p.correctImageOrientation()
    p.addVAR(read_noise=True,poisson_noise=True)
    # get and save wavelength solution (either static reference or frame's unique sim cal solved)
    p.darkSubtraction()
    p.extractStripes()  # gets relevant flat and dark to cut out frame's spectra TODO Skip dark for fiber 5
    p.optimalExtraction()  # does 2D to 1D conversion of cut out spectra (only for fibers 2,3,4)
    # TODO: perform echelle peak fitting on fiber 5
    # TODO: Get wavelength solution from dynamic wavecal recipe
    # TODO: Take Fiber 5 peak positions and 
    p.storeProcessedScience(suffix='_reduced')
    return

_default = reduce

def makeStripeExtractionCheck(p):
    """
    This recipe is utilized to check the stripe extraction that is made
    in the normal processing of a science frame
    Parameters
    ----------
    p : PrimitivesCORE object
        A primitive set matching the recipe_tags.
    Returns
    -------
    creates test frames with FITS-formated stripe extractions meta-info (normally not saved)
    unit test will independently preform stripe extraction and compare results
    """
    p.prepare()
    p.checkArm()
    p.addDQ()  # just placeholder until MX is in caldb
    p.overscanCorrect()
    p.correctImageOrientation()
    p.addVAR(read_noise=True,poisson_noise=True)
    # get and save wavelength solution (either static reference or frame's unique sim cal solved)
    p.darkSubtraction()
    p.extractStripes(test_extraction=True)  # gets relevant flat and dark to cut out frame's spectra
    p.storeProcessedScience(suffix='_test_stripes')