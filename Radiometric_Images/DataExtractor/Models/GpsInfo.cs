namespace Radiometric_Images.DataExtractor.Models
{
    internal class GpsInfo
    {
        public double Altitude { get; set; }
        public double Dop { get; set; }
        public double Latitude { get; set; }
        public double Longitude { get; set; }
        public string MapDatum { get; set; }
        public string Satellites { get; set; }
    }
}
