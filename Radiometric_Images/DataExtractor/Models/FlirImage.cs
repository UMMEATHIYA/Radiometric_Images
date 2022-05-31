using System;
using System.Collections.Generic;

namespace Radiometric_Images.DataExtractor.Models
{
    internal class FlirImage
    {
        public CameraInfo CameraInfo { get; set; }
        public CompassInfo CompassInfo { get; set; }
        public DateTime DateTaken { get; set; }
        public string Description { get; set; }
        public GpsInfo GpsInfo { get; set; }
        public int Height { get; set; }
        public int MaxSignalValue { get; set; }
        public int MinSignalValue { get; set; }
        public int Precision { get; set; }
        public Enums.TemperatureUnit TemperatureUnit { get; set; }
        public ThermalParameters ThermalParameters { get; set; }
        public IList<ThermalData> ThermalData { get; set; }
        public string Title { get; set; }
        public int Width { get; set; }
    }
}
