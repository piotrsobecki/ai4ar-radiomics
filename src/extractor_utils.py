import numpy as np
import logging
from radiomics import featureextractor
import SimpleITK
from joblib import Parallel, delayed

log = logging.getLogger('radiomics')


# Create a feature extraction pipeline as a function that takse a case and returns a dictionary of features
def extract_features(extractor: featureextractor, img:SimpleITK.Image, mask:SimpleITK.Image):
 
    # Correct geometry
    mask.SetOrigin(img.GetOrigin())

    features = extractor.execute(img, mask, label=1)
    
    # Filter by feature name (only radiomics features start with 'original_'), if value is a numpy array and  has only one element, convert to scalar
    features_filtered = {k: v.item() if isinstance(v, np.ndarray) and v.size == 1 else v for k, v in features.items() if k.startswith("original_")}


    # Return the features as a dictionary
    return features_filtered


def extract(dataset, extractor: featureextractor,  jobs, n_jobs=4):
    
    def error_callback(exc, row):
        # Handle the exception and prevent the job from crashing
        print(f'An error occurred while processing {row}: {exc}')
    
    
    def process_row(row):
        try:
                
            # Debug: Process row
            log.debug(f"Debug: Process row: {row}")
            
            # Obtain case    
            case = dataset[str(row['patient_id']).zfill(3)]
            # Debug: Case
            log.debug(f"Debug: Case: {case}")
            
            # Obtain modality image
            modality_img = case.image(row['data_path'], cache=False)
            # Obtain mask image
            mask_img = case.image(row['mask_path'], cache=False)
            # Debug: Images
            log.debug(f"Debug: Modality image: {modality_img} Mask image: {mask_img}")
            
            # Extract features
            features = extract_features(extractor, modality_img.sitk(), mask_img.sitk())
            # Debug: Features
            log.debug(f"Debug: Features: {features}")
            
            # Combine id columns with features
            result = {**row, **features}
            
            # Debug: Result
            log.debug(f"Debug: Result: {result}")
            
            mask_img.clear_image_cache()
            
            
        
        except Exception as e:
            error_callback(e,row)
            result = None
        
        return result
    
    
    return Parallel(n_jobs=n_jobs, verbose=10)(delayed(process_row)(row) for idx, row  in jobs.iterrows())

def construct_feature_extractor(config):
    # Instantiate the extractor
    extractor = featureextractor.RadiomicsFeatureExtractor(**config['init_params'].as_dict())

    # Enable all features
    #extractor.enableAllFeatures()

    # Enable all image types (original image, wavelet, square, log, square root, and exponent)
    extractor.disableAllImageTypes()

    extractor.disableAllFeatures()

    for f in config['features']:
        extractor.enableFeatureClassByName(f)

    for f in config['image_types']:
        extractor.enableImageTypeByName(f)
        
    log.info('Radiomics settings (from config):\n\t', config.as_dict())
    log.debug('\nExtraction parameters:\n\t', extractor.settings)
    log.debug('\nEnabled filters:\n\t', extractor.enabledImagetypes)
    log.debug('\nEnabled features:\n\t', extractor.enabledFeatures)
    
    return extractor
        