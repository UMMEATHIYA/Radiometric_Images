using System;
using System.Drawing;
using System.Windows.Forms;

namespace Radiometric_Images
{
    public partial class Form2 : Form
    {
        //private ThermalImageFile th;
        private PictureBox p;

        public Form2()
        {
            InitializeComponent();
        }

        private void Form2_Load(object sender, EventArgs e)
        {
            PictureBox picture = new PictureBox
            {
                Name = "pictureBox",
                Size = new Size(100, 50),
                Location = new Point(14, 17)
            };
            p.Controls.Add(picture);
            picture.ImageLocation = @"C:\Users\0012CD744\Downloads\images_new\img_20000115_101918_464.jpg";
        }
    }
}
