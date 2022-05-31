using Flir.Atlas.Image;
using Newtonsoft.Json;
using Radiometric_Images.DataExtractor.Models;
using System;
using System.Collections.Generic;
using System.Drawing;

namespace Radiometric_Images.DataExtractor
{
    internal class ImageProcessor
    {
        private readonly FlirImage _flirImageData;

        public ImageProcessor()
        {
        }

        public ImageProcessor(string imageFilePath)
        {
            FlirImageFile = new ThermalImageFile(imageFilePath);
            _flirImageData = ProcessImage(FlirImageFile);
        }

        public ThermalImageFile FlirImageFile { get; }

        public FlirImage FlirImageData
        {
            get { return _flirImageData; }
        }

        private FlirImage ProcessImage(ThermalImageFile thermalImage)
        {
            FlirImage flirImageData = new FlirImage
            {
                DateTaken = thermalImage.DateTaken,
                Description = thermalImage.Description,
                Height = thermalImage.Height,
                MaxSignalValue = thermalImage.MaxSignalValue,
                MinSignalValue = thermalImage.MinSignalValue,
                Precision = thermalImage.Precision,
                TemperatureUnit = (Enums.TemperatureUnit)Enum.Parse(typeof(Enums.TemperatureUnit),
                    thermalImage.TemperatureUnit.ToString()),
                Width = thermalImage.Width,
                ThermalData = ExtractTemperatureReadings(thermalImage),
                Title = thermalImage.Title
            };

            if (thermalImage.CameraInformation != null)
                flirImageData.CameraInfo = new CameraInfo
                {
                    Filter = thermalImage.CameraInformation.Filter,
                    Fov = thermalImage.CameraInformation.Fov,
                    Lens = thermalImage.CameraInformation.Lens,
                    Model = thermalImage.CameraInformation.Model,
                    RangeMax = thermalImage.CameraInformation.Range.Maximum,
                    RangeMin = thermalImage.CameraInformation.Range.Minimum,
                    SerialNumber = thermalImage.CameraInformation.SerialNumber
                };

            if (thermalImage.CompassInformation != null)
                flirImageData.CompassInfo = new Models.CompassInfo
                {
                    Degrees = thermalImage.CompassInformation.Degrees,
                    Pitch = thermalImage.CompassInformation.Pitch,
                    Roll = thermalImage.CompassInformation.Roll
                };

            //if (thermalImage.GpsInformation != null)
            //    flirImageData.GpsInfo = new GpsInfo
            //    {
            //        Altitude = thermalImage.GpsInformation.Altitude,
            //        Dop = thermalImage.GpsInformation.Dop,
            //        Latitude = thermalImage.GpsInformation.Latitude,
            //        Longitude = thermalImage.GpsInformation.Longitude,
            //        MapDatum = thermalImage.GpsInformation.MapDatum,
            //        Satellites = thermalImage.GpsInformation.Satellites
            //    };

            if (thermalImage.ThermalParameters != null)
                flirImageData.ThermalParameters = new ThermalParameters
                {
                    AtmosphericTemperature = thermalImage.ThermalParameters.AtmosphericTemperature,
                    Distance = thermalImage.ThermalParameters.Distance,
                    Emissivity = thermalImage.ThermalParameters.Emissivity,
                    ExternalOpticsTemperature = thermalImage.ThermalParameters.ExternalOpticsTemperature,
                    ExternalOpticsTransmission = thermalImage.ThermalParameters.ExternalOpticsTransmission,
                    ReferenceTemperature = thermalImage.ThermalParameters.ReferenceTemperature,
                    ReflectedTemperature = thermalImage.ThermalParameters.ReflectedTemperature,
                    RelativeHumidity = thermalImage.ThermalParameters.RelativeHumidity,
                    Transmission = thermalImage.ThermalParameters.Transmission
                };

            return flirImageData;
        }

        private IList<ThermalData> ExtractTemperatureReadings(ThermalImageFile thermalImage)
        {
            IList<ThermalData> thermalData = new List<ThermalData>();

            // Load Raw PixelData
            double[,] rawThermalData = thermalImage.ImageProcessing.GetPixelsArray();

            for (int z = 0; z <= thermalImage.Size.Height - 1; z++)
                for (int x = 0; x <= thermalImage.Size.Width - 1; x++)
                {
                    // Get ThermalValue from Image
                    ThermalValue thermalValue = thermalImage.GetValueAt(new Point(x, z));

                    // Build Data Object and Add to ThermalData List
                    thermalData.Add(new ThermalData
                    {
                        X = x,
                        Z = z,
                        RawValue = rawThermalData[z, x],
                        TemperatureValue = thermalValue.Value,
                        TemperatureUnit = (Enums.TemperatureUnit)Enum.Parse(typeof(Enums.TemperatureUnit),
                            thermalImage.TemperatureUnit.ToString())
                    });
                }

            return thermalData;
        }

        public string ToJson(FlirImage flirImageData)
        {
            return JsonConvert.SerializeObject(flirImageData);
        }
    }
}
