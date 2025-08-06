# Characterising radio sources in the SMC using citizen science and optical spectroscopy

MsC has been finished.


Here are the column names and a short description of what data they contain. The columns are from the
REDTEST.csv file in the Citizen Science folder.
• The first column has no name, but it is an index column added by Python during the table creation
process.
• subject id: The identification number of the subject image from the Zooniverse database.
• data.yes: # of responses indicating the radio source seems to have an associated optical source).
• data.no: # of responses indicating the radio source does not seem to have an associated optical source.
• data.the-radio-source-is-showing-extended-morphology: # of responses indicating the radio
source contours show extended morphology beyond the beam size
• data.yes-there-seem-to-be-associated-regions-close-to-the-central-source: # of responses that
indicate a structured extended radio source morphology.
• data.yes-it-looks-like-a-radio-point-source: # of responses indicating a radio point source mor-
phology from the contours.
• data.no-nearby-marked-regions-seem-associated-with-the-central-source: # of responses in-
dicating a compact extended morphology.
• multi-source: Python generated column recording the # of responses that indicate the associated
optical source could be one of many close-by sources.
• homogeneous: Python generated column recording the # of responses that indicate the associated
optical source looks like a homogeneously luminous gas-like region.
• point-star: Python generated column recording the # of responses that indicate the associated optical
source looks like a star or dot.
• oddORnot-sure: Python generated column recording the # of responses that indicate the associated
optical source has an odd shape that does not match the other options.
• core-in-diffuse: Python generated column recording the # of responses that indicate the associated
optical source looks like a bright core surrounded by a diffuse gassy region.
• Sum: This was an internal confirmation value to check if the number of associated optical sources
matches the number of responses regarding the optical source morphology.
• Total Class: Total # of classifications for the subject image.
• multiFrac: Fraction of classifications that indicated more than one optical source could be the associ-
ated optical counterpart to the radio emission.
• homoFrac: Fraction of classifications that indicated a homogeneously diffuse optical counterpart.
69
• pointFrac: Fraction of classifications that indicated a star or point-like optical counterpart.
• unsureOddFrac: Fraction of classifications that indicated and oddly shaped or uncertain optical
counterpart morphology.
• coreFrac: Fraction of classifications that indicated an optical morphology with a bright core and diffuse
gas-like emission around it.
• ext radFrac: Fraction of classifications that indicated an extended radio source morphology.
• point radFrac: Fraction of classifications that indicate a radio point source morphology.
• flag rad point: 1 if > 80 per cent agreement between classifiers that the radio source is a point source.
• flag rad extended: 1 if > 80 per cent agreement between classifiers that the radio source is an
extended source.
• flag rad unsure: 1 if there is < 80 per cent agreement on either the radio point or extended flags.
• flag optical counterpart: 1 if > 80 per cent agreement between classifiers that an associated optical
source is present.
• metadata: contains a “.json” string recording the file name of the subject as uploaded by the project
creator.
• locations: contains a “.json” string with the image URL inside.
• classifications count: Zooniverse recorded count of classification for the subject.
• Filename: Extracted file name as uploaded by the project creator from the “metadata” column.
• LCurl: URL extracted from the “locations” column
