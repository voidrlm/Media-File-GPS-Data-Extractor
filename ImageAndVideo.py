import exiftool


def get_gps_data(filepath):
    try:
        with exiftool.ExifToolHelper() as et:
            # Get GPS latitude and longitude metadata
            gps_data = et.get_metadata(
                filepath, ['-gpslatitude', '-gpslongitude'])
            return gps_data
    except exiftool.ExifToolError as e:
        return f"ExifToolError: {e}"
    except FileNotFoundError:
        return f"File not found: {filepath}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


def main():
    # Provide file path here (Can use both image and video files)
    filepath = "./media/image.jpg"

    # Get GPS data and handle errors
    gps_data = get_gps_data(filepath)

    if isinstance(gps_data, str):
        print(f"Error: {gps_data}")
    else:
        print("Latitude " + str(gps_data[0]['Composite:GPSLatitude']))
        print("Longitude " + str(gps_data[0]['Composite:GPSLongitude']))


if __name__ == "__main__":
    main()
