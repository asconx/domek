namespace Domek
{
    public partial class MainPage : ContentPage
    {

        int polubieniaCount = 1;
        public MainPage()
        {
            InitializeComponent();
           

        }

        private void OnCounterClicked(object sender, EventArgs e)
        {
            polubieniaCount++;
            polubienia.Text = $"{polubieniaCount} Polubienia";


        }
        private void Delete(object sender, EventArgs e)
        {
            
            if (polubieniaCount > 1)
            {
                polubieniaCount--;
                polubienia.Text = $"{polubieniaCount} Polubienia";
            }


        }
    }

}
