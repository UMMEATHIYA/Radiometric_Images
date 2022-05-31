namespace Radiometric_Images.DataExtractor.Models
{
    internal class CameraInfo
    {
        public string Filter { get; set; }
        public double Fov { get; set; }
        public string Lens { get; set; }
        public string Model { get; set; }
        public double RangeMin { get; set; }
        public double RangeMax { get; set; }
        public string SerialNumber { get; set; }
    }
}
