namespace Radiometric_Images.DataExtractor.Models
{
    internal class ThermalData
    {
        internal int Y;

        //public double Altitude { get; set; }
        //public double Dop { get; set; }
        //public double Latitude { get; set; }
        //public double Longitude { get; set; }
        //public string MapDatum { get; set; }
        //public string Satellites { get; set; }
        public int X { get; internal set; }

        public int Z { get; internal set; }
        public double TemperatureValue { get; internal set; }
        public double RawValue { get; internal set; }
        public Enums.TemperatureUnit TemperatureUnit { get; internal set; }
    }
}
