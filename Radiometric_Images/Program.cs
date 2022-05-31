using Flir.Atlas.Image;
using Flir.Atlas.Live.Device;
using Flir.Atlas.Live.Discovery;
using Radiometric_Images.DataExtractor;
using Radiometric_Images.DataExtractor.Models;
using System;
using System.IO;

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

            image.SaveSnapshot(@"C:\Users\0012CD744\radiometric_images\img_20000120_115221_193\img_20000120_115221_193.raw");

            string imagePath = @"C:\Users\0012CD744\radiometric_images\img_20000120_115221_193\img_20000120_115221_193.raw";

            ImageProcessor imageProcesser = new ImageProcessor(imagePath);
            FlirImage flirImage = imageProcesser.FlirImageData;

            string json = imageProcesser.ToJson(flirImage);


            string diretoryPath = Path.GetDirectoryName(imagePath);
            string fileName = Path.GetFileNameWithoutExtension(imagePath);
            string outputFilePath = diretoryPath + "\\" + fileName + ".json";
            File.WriteAllText(outputFilePath, json);
            Console.WriteLine("Data Saved to " + outputFilePath);
            image.SaveSnapshot(@"C:\Users\0012CD744\umme");
            cam.Disconnect();
        }
    }
}