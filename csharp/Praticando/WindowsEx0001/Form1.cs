﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsEx0001
{
    public partial class Form1 : Form
    {
        int num = 0;
        public Form1()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void btn_Click(object sender, EventArgs e)
        {
            if (num % 2 == 0)
            {
                lblMsg.Text = "Você Clicou!";
            }else 
            {
                lblMsg.Text = "";
            }

            num++;
            
        }
    }
}
