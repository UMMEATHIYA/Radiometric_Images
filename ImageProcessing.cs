using Flir.Atlas.Live;
using Flir.Atlas.Live.Device;
using Flir.Atlas.Image;
using Flir.Atlas.Live.Discovery;
namespace MyNamespace
{
    class Program
    {
        static void Main(string[] args)
        {
            CameraDeviceInfo device = CameraDeviceInfo.Create("192.168.0.11", Interface.Network);
            ThermalCamera cam = new ThermalCamera();
            cam.Connect(device);
            while (!cam.ConnectionStatus.Equals(ConnectionStatus.Connected)) ;
            while (cam.IsGrabbing != true) ;
            ImageBase image = cam.GetImage();
            image.SaveSnapshot(@"C:\Users\0012CD744\shiva");
            cam.Disconnect();
        }
    }
}