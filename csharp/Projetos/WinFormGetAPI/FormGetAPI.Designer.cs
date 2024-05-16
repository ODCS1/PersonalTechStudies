namespace WinFormGetAPI
{
    partial class FormGetAPI
    {
        /// <summary>
        /// Variável de designer necessária.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Limpar os recursos que estão sendo usados.
        /// </summary>
        /// <param name="disposing">true se for necessário descartar os recursos gerenciados; caso contrário, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Código gerado pelo Windows Form Designer

        /// <summary>
        /// Método necessário para suporte ao Designer - não modifique 
        /// o conteúdo deste método com o editor de código.
        /// </summary>
        private void InitializeComponent()
        {
            this.pnlMain = new System.Windows.Forms.Panel();
            this.lblCep = new System.Windows.Forms.Label();
            this.lblComplemento = new System.Windows.Forms.Label();
            this.lblUf = new System.Windows.Forms.Label();
            this.lblIbge = new System.Windows.Forms.Label();
            this.lblLogradouro = new System.Windows.Forms.Label();
            this.lblBairro = new System.Windows.Forms.Label();
            this.lblCidade = new System.Windows.Forms.Label();
            this.btnRequest = new System.Windows.Forms.Button();
            this.txtURI = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.btnClose = new System.Windows.Forms.Button();
            this.txtBoxCidade = new System.Windows.Forms.TextBox();
            this.txtBoxBairro = new System.Windows.Forms.TextBox();
            this.txtBoxComplemento = new System.Windows.Forms.TextBox();
            this.txtBoxLogradouro = new System.Windows.Forms.TextBox();
            this.txtBoxUf = new System.Windows.Forms.TextBox();
            this.txtBoxCep = new System.Windows.Forms.TextBox();
            this.txtBoxIbge = new System.Windows.Forms.TextBox();
            this.pnlMain.SuspendLayout();
            this.SuspendLayout();
            // 
            // pnlMain
            // 
            this.pnlMain.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.pnlMain.Controls.Add(this.txtBoxIbge);
            this.pnlMain.Controls.Add(this.txtBoxCep);
            this.pnlMain.Controls.Add(this.txtBoxUf);
            this.pnlMain.Controls.Add(this.txtBoxLogradouro);
            this.pnlMain.Controls.Add(this.txtBoxComplemento);
            this.pnlMain.Controls.Add(this.txtBoxBairro);
            this.pnlMain.Controls.Add(this.txtBoxCidade);
            this.pnlMain.Controls.Add(this.lblCep);
            this.pnlMain.Controls.Add(this.lblComplemento);
            this.pnlMain.Controls.Add(this.lblUf);
            this.pnlMain.Controls.Add(this.lblIbge);
            this.pnlMain.Controls.Add(this.lblLogradouro);
            this.pnlMain.Controls.Add(this.lblBairro);
            this.pnlMain.Controls.Add(this.lblCidade);
            this.pnlMain.Controls.Add(this.btnRequest);
            this.pnlMain.Controls.Add(this.txtURI);
            this.pnlMain.Controls.Add(this.label1);
            this.pnlMain.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.pnlMain.Location = new System.Drawing.Point(12, 12);
            this.pnlMain.Name = "pnlMain";
            this.pnlMain.Size = new System.Drawing.Size(415, 302);
            this.pnlMain.TabIndex = 0;
            // 
            // lblCep
            // 
            this.lblCep.AutoSize = true;
            this.lblCep.Location = new System.Drawing.Point(3, 237);
            this.lblCep.Name = "lblCep";
            this.lblCep.Size = new System.Drawing.Size(41, 20);
            this.lblCep.TabIndex = 11;
            this.lblCep.Text = "CEP";
            // 
            // lblComplemento
            // 
            this.lblComplemento.AutoSize = true;
            this.lblComplemento.Location = new System.Drawing.Point(3, 137);
            this.lblComplemento.Name = "lblComplemento";
            this.lblComplemento.Size = new System.Drawing.Size(131, 20);
            this.lblComplemento.TabIndex = 10;
            this.lblComplemento.Text = "COMPLEMENTO";
            // 
            // lblUf
            // 
            this.lblUf.AutoSize = true;
            this.lblUf.Location = new System.Drawing.Point(3, 206);
            this.lblUf.Name = "lblUf";
            this.lblUf.Size = new System.Drawing.Size(31, 20);
            this.lblUf.TabIndex = 9;
            this.lblUf.Text = "UF";
            // 
            // lblIbge
            // 
            this.lblIbge.AutoSize = true;
            this.lblIbge.Location = new System.Drawing.Point(3, 270);
            this.lblIbge.Name = "lblIbge";
            this.lblIbge.Size = new System.Drawing.Size(49, 20);
            this.lblIbge.TabIndex = 8;
            this.lblIbge.Text = "IBGE";
            // 
            // lblLogradouro
            // 
            this.lblLogradouro.AutoSize = true;
            this.lblLogradouro.Location = new System.Drawing.Point(3, 169);
            this.lblLogradouro.Name = "lblLogradouro";
            this.lblLogradouro.Size = new System.Drawing.Size(126, 20);
            this.lblLogradouro.TabIndex = 7;
            this.lblLogradouro.Text = "LOGRADOURO";
            // 
            // lblBairro
            // 
            this.lblBairro.AutoSize = true;
            this.lblBairro.Location = new System.Drawing.Point(3, 108);
            this.lblBairro.Name = "lblBairro";
            this.lblBairro.Size = new System.Drawing.Size(72, 20);
            this.lblBairro.TabIndex = 6;
            this.lblBairro.Text = "BAIRRO";
            // 
            // lblCidade
            // 
            this.lblCidade.AutoSize = true;
            this.lblCidade.Location = new System.Drawing.Point(3, 79);
            this.lblCidade.Name = "lblCidade";
            this.lblCidade.Size = new System.Drawing.Size(71, 20);
            this.lblCidade.TabIndex = 5;
            this.lblCidade.Text = "CIDADE";
            // 
            // btnRequest
            // 
            this.btnRequest.Location = new System.Drawing.Point(340, 20);
            this.btnRequest.Name = "btnRequest";
            this.btnRequest.Size = new System.Drawing.Size(55, 46);
            this.btnRequest.TabIndex = 4;
            this.btnRequest.Text = "Go";
            this.btnRequest.UseVisualStyleBackColor = true;
            this.btnRequest.Click += new System.EventHandler(this.btnRequest_Click);
            // 
            // txtURI
            // 
            this.txtURI.Location = new System.Drawing.Point(15, 40);
            this.txtURI.Name = "txtURI";
            this.txtURI.Size = new System.Drawing.Size(319, 26);
            this.txtURI.TabIndex = 2;
            this.txtURI.Text = "https://opencep.com/v1/13020060";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(15, 17);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(103, 20);
            this.label1.TabIndex = 0;
            this.label1.Text = "Request URI";
            // 
            // btnClose
            // 
            this.btnClose.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnClose.ForeColor = System.Drawing.Color.Red;
            this.btnClose.Location = new System.Drawing.Point(331, 320);
            this.btnClose.Name = "btnClose";
            this.btnClose.Size = new System.Drawing.Size(96, 34);
            this.btnClose.TabIndex = 1;
            this.btnClose.Text = "&Close";
            this.btnClose.UseVisualStyleBackColor = true;
            this.btnClose.Click += new System.EventHandler(this.btnClose_Click);
            // 
            // txtBoxCidade
            // 
            this.txtBoxCidade.Location = new System.Drawing.Point(80, 79);
            this.txtBoxCidade.Name = "txtBoxCidade";
            this.txtBoxCidade.Size = new System.Drawing.Size(315, 26);
            this.txtBoxCidade.TabIndex = 12;
            // 
            // txtBoxBairro
            // 
            this.txtBoxBairro.Location = new System.Drawing.Point(81, 108);
            this.txtBoxBairro.Name = "txtBoxBairro";
            this.txtBoxBairro.Size = new System.Drawing.Size(314, 26);
            this.txtBoxBairro.TabIndex = 13;
            // 
            // txtBoxComplemento
            // 
            this.txtBoxComplemento.Location = new System.Drawing.Point(140, 137);
            this.txtBoxComplemento.Name = "txtBoxComplemento";
            this.txtBoxComplemento.Size = new System.Drawing.Size(255, 26);
            this.txtBoxComplemento.TabIndex = 14;
            // 
            // txtBoxLogradouro
            // 
            this.txtBoxLogradouro.Location = new System.Drawing.Point(130, 169);
            this.txtBoxLogradouro.Name = "txtBoxLogradouro";
            this.txtBoxLogradouro.Size = new System.Drawing.Size(265, 26);
            this.txtBoxLogradouro.TabIndex = 15;
            // 
            // txtBoxUf
            // 
            this.txtBoxUf.Location = new System.Drawing.Point(65, 200);
            this.txtBoxUf.Name = "txtBoxUf";
            this.txtBoxUf.Size = new System.Drawing.Size(330, 26);
            this.txtBoxUf.TabIndex = 16;
            // 
            // txtBoxCep
            // 
            this.txtBoxCep.Location = new System.Drawing.Point(65, 234);
            this.txtBoxCep.Name = "txtBoxCep";
            this.txtBoxCep.Size = new System.Drawing.Size(330, 26);
            this.txtBoxCep.TabIndex = 17;
            // 
            // txtBoxIbge
            // 
            this.txtBoxIbge.Location = new System.Drawing.Point(58, 270);
            this.txtBoxIbge.Name = "txtBoxIbge";
            this.txtBoxIbge.Size = new System.Drawing.Size(337, 26);
            this.txtBoxIbge.TabIndex = 18;
            // 
            // FormGetAPI
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(444, 361);
            this.ControlBox = false;
            this.Controls.Add(this.btnClose);
            this.Controls.Add(this.pnlMain);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Name = "FormGetAPI";
            this.Text = "Get API Request";
            this.pnlMain.ResumeLayout(false);
            this.pnlMain.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Panel pnlMain;
        private System.Windows.Forms.TextBox txtURI;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button btnRequest;
        private System.Windows.Forms.Button btnClose;
        private System.Windows.Forms.Label lblCep;
        private System.Windows.Forms.Label lblComplemento;
        private System.Windows.Forms.Label lblUf;
        private System.Windows.Forms.Label lblIbge;
        private System.Windows.Forms.Label lblLogradouro;
        private System.Windows.Forms.Label lblBairro;
        private System.Windows.Forms.Label lblCidade;
        private System.Windows.Forms.TextBox txtBoxIbge;
        private System.Windows.Forms.TextBox txtBoxCep;
        private System.Windows.Forms.TextBox txtBoxUf;
        private System.Windows.Forms.TextBox txtBoxLogradouro;
        private System.Windows.Forms.TextBox txtBoxComplemento;
        private System.Windows.Forms.TextBox txtBoxBairro;
        private System.Windows.Forms.TextBox txtBoxCidade;
    }
}

