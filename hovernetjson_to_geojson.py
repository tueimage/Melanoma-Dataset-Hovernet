import glob
import os
import json
import geojson
import argparse

# Define the classification dictionary for cell types
classification_dict_1 = {"name": "cell_lymphocyte", "color": [0, 0, 255]}
classification_dict_2 = {"name": "cell_tumor", "color": [255, 0, 0]}
classification_dict_3 = {"name": "cell_stroma", "color": [0, 0, 255]}
classification_dict_4 = {"name": "cell_other", "color": [50, 50, 50]}
classification_dict_5 = {"name": "cell_other", "color": [250, 200, 0]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert JSON annotations to GeoJSON format.")
    parser.add_argument("annotations_path", type=str, help="Path to the directory containing JSON annotations.")

    args = parser.parse_args()
    annotations_path = args.annotations_path

    # Iterate over the JSON files in the folder
    for file_name in glob.glob(os.path.join(annotations_path, "*.json")):

        # Load the JSON data from file
        with open(file_name) as f:
            data = json.load(f)

            # Transform the JSON to a GeoJSON
            geojson_data = geojson.FeatureCollection([
                geojson.Feature(
                    geometry=geojson.Polygon([data['nuc'][key]['contour']]),
                    properties={
                        'type': data['nuc'][key]['type'],
                        'type_prob': data['nuc'][key]['type_prob']
                    }
                ) for key in data['nuc']
            ])

            # Close polygon of GEOJSON to make it readable in QUpath and change annotations 
            # Iterate through each feature
            for feature in geojson_data['features']:
                # Get the last coordinate of the polygon and append it to the coordinates array
                start_point = feature['geometry']['coordinates'][0][0]
                feature['geometry']['coordinates'][0].append(start_point),

                if feature['properties']['type'] == 1:
                    feature['properties']['classification'] = classification_dict_1
                    del feature['properties']['type']

                elif feature['properties']['type'] == 2:
                    feature['properties']['classification'] = classification_dict_2
                    del feature['properties']['type']

                elif feature['properties']['type'] == 3:
                    feature['properties']['classification'] = classification_dict_3
                    del feature['properties']['type']

                elif feature['properties']['type'] == 4:
                    feature['properties']['classification'] = classification_dict_4
                    del feature['properties']['type']

                elif feature['properties']['type'] == 5:
                    feature['properties']['classification'] = classification_dict_5
                    del feature['properties']['type'] 
        
            # Write the GeoJSON data to file
            with open (file_name.replace('.json', '_cell.geojson'), 'w') as write_file:
                json.dump(geojson_data, write_file)

            print (file_name, "has been converted to GEOJSON")

# Run the script with the following command:
# python Hovernetjson_to_GEOJSON.py /path/to/annotations