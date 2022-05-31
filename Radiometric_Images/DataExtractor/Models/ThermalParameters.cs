namespace Radiometric_Images.DataExtractor.Models
{
    internal class ThermalParameters
    {
        public double Altitude { get; set; }
        public double Dop { get; set; }
        public double Latitude { get; set; }
        public double Longitude { get; set; }
        public string MapDatum { get; set; }
        public string Satellites { get; set; }
        public object AtmosphericTemperature { get; internal set; }

        public object Distance { get; set; }
        public double Emissivity { get; internal set; }
        public double ExternalOpticsTemperature { get; internal set; }
        public double ExternalOpticsTransmission { get; internal set; }
        public double ReferenceTemperature { get; internal set; }
        public double ReflectedTemperature { get; internal set; }
        public double RelativeHumidity { get; internal set; }
        public double Transmission { get; internal set; }


    }
}
