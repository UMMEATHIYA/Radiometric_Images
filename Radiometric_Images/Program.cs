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
            while (true)
            {
                CameraDeviceInfo device = CameraDeviceInfo.Create("192.168.0.11", Interface.Network);
                ThermalCamera cam = new ThermalCamera();
                cam.Connect(device);

                while (!cam.ConnectionStatus.Equals(ConnectionStatus.Connected)) ;
                while (cam.IsGrabbing != true) ;
                ImageBase image = cam.GetImage();
                string datetime = DateTime.Now.ToString("yyyy-dd-M-HH-mm-ss");
                Console.WriteLine(datetime);

                image.SaveSnapshot(@"C:\Users\0012CD744\June_22_radiometric_image\img_20000211_100030_607\img_20000211_100030_607" + datetime + ".raw");


                string imagePath = @"C:\Users\0012CD744\June_22_radiometric_image\img_20000211_100030_607\img_20000211_093249_656" + datetime + ".raw";
                ImageProcessor imageProcesser = new ImageProcessor(imagePath);
                FlirImage flirImage = imageProcesser.FlirImageData;


                string json = imageProcesser.ToJson(flirImage);

                string diretoryPath = Path.GetDirectoryName(imagePath);
                string fileName = Path.GetFileNameWithoutExtension(imagePath);
                string outputFilePath = diretoryPath + "\\" + fileName + ".json";
                File.WriteAllText(outputFilePath, json);
                Console.WriteLine("Data Saved to " + outputFilePath);

                /// Reading the json file///
                string st = File.ReadAllText(outputFilePath);
                Console.WriteLine(st);

                ///Deserialization///
                //var my_obj = JsonConvert.DeserializeObject<ThermalData>(st);
                var my_obj = Newtonsoft.Json.JsonConvert.DeserializeObject<ThermalData>(st);
                ///Extract the thermal data -> JSON Array ///
                ///

                var data = (JArray)JObject.Parse(st)["ThermalData"];
                double[,] myData = new double[320, 240];

                foreach (var item in data)
                {
                    int x = item.Value<int>("X");
                    int z = item.Value<int>("Z");
                    Double temperatureValue = item.Value<Double>("TemperatureValue");
                    Double rawValue = item.Value<Double>("RawValue");


                    myData[x, z] = item.Value<double>("TemperatureValue");
                    Console.WriteLine("[ " + x + " , " + z + " ] = " + myData[x, z]);
                }

                //ConvertToGrayscale convertToGrayscale = new ConvertToGrayscale();
                //convertToGrayscale.ConvertToGrayscale2(myBitmap).Save(@"C:\Users\0012CD744\June_22_radiometric_images\img_20000211_100030_607\img_20000211_100030_607.jpg", System.Drawing.Imaging.ImageFormat.Jpeg);
                //convertToGrayscale.ImageToByteArray(myBitmap);

                //image.SaveSnapshot(@"C:\Users\0012CD744\umme");
                
                System.Threading.Thread.Sleep(30000);
                cam.Disconnect();
            }
        }
    }
}
