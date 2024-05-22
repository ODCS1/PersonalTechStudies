namespace Horario
{
    partial class Formulario
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
            this.label1 = new System.Windows.Forms.Label();
            this.lblHoras = new System.Windows.Forms.Label();
            this.btn_addUmMinuto = new System.Windows.Forms.Button();
            this.btnAdicionarUmSegundo = new System.Windows.Forms.Button();
            this.btnDiminuirUmSegundo = new System.Windows.Forms.Button();
            this.btnDiminuirUmMinuto = new System.Windows.Forms.Button();
            this.btnFechar = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(70, 41);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(221, 82);
            this.label1.TabIndex = 0;
            this.label1.Text = "Horário";
            this.label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.label1.Click += new System.EventHandler(this.label1_Click);
            // 
            // lblHoras
            // 
            this.lblHoras.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblHoras.Location = new System.Drawing.Point(333, 41);
            this.lblHoras.Name = "lblHoras";
            this.lblHoras.Size = new System.Drawing.Size(206, 82);
            this.lblHoras.TabIndex = 1;
            this.lblHoras.Text = "00:00:00";
            this.lblHoras.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.lblHoras.Click += new System.EventHandler(this.lblHoras_Click);
            // 
            // btn_addUmMinuto
            // 
            this.btn_addUmMinuto.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btn_addUmMinuto.Location = new System.Drawing.Point(58, 153);
            this.btn_addUmMinuto.Name = "btn_addUmMinuto";
            this.btn_addUmMinuto.Size = new System.Drawing.Size(95, 54);
            this.btn_addUmMinuto.TabIndex = 2;
            this.btn_addUmMinuto.Text = "+60";
            this.btn_addUmMinuto.UseVisualStyleBackColor = true;
            this.btn_addUmMinuto.Click += new System.EventHandler(this.btn_addUmMinuto_Click);
            // 
            // btnAdicionarUmSegundo
            // 
            this.btnAdicionarUmSegundo.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnAdicionarUmSegundo.Location = new System.Drawing.Point(196, 153);
            this.btnAdicionarUmSegundo.Name = "btnAdicionarUmSegundo";
            this.btnAdicionarUmSegundo.Size = new System.Drawing.Size(95, 54);
            this.btnAdicionarUmSegundo.TabIndex = 3;
            this.btnAdicionarUmSegundo.Text = "+1";
            this.btnAdicionarUmSegundo.UseVisualStyleBackColor = true;
            this.btnAdicionarUmSegundo.Click += new System.EventHandler(this.btnAdicionarUmSegundo_Click);
            // 
            // btnDiminuirUmSegundo
            // 
            this.btnDiminuirUmSegundo.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnDiminuirUmSegundo.Location = new System.Drawing.Point(333, 153);
            this.btnDiminuirUmSegundo.Name = "btnDiminuirUmSegundo";
            this.btnDiminuirUmSegundo.Size = new System.Drawing.Size(95, 54);
            this.btnDiminuirUmSegundo.TabIndex = 4;
            this.btnDiminuirUmSegundo.Text = "-1";
            this.btnDiminuirUmSegundo.UseVisualStyleBackColor = true;
            this.btnDiminuirUmSegundo.Click += new System.EventHandler(this.btnDiminuirUmSegundo_Click);
            // 
            // btnDiminuirUmMinuto
            // 
            this.btnDiminuirUmMinuto.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnDiminuirUmMinuto.Location = new System.Drawing.Point(460, 153);
            this.btnDiminuirUmMinuto.Name = "btnDiminuirUmMinuto";
            this.btnDiminuirUmMinuto.Size = new System.Drawing.Size(95, 54);
            this.btnDiminuirUmMinuto.TabIndex = 5;
            this.btnDiminuirUmMinuto.Text = "-60";
            this.btnDiminuirUmMinuto.UseVisualStyleBackColor = true;
            this.btnDiminuirUmMinuto.Click += new System.EventHandler(this.btnDiminuirUmMinuto_Click);
            // 
            // btnFechar
            // 
            this.btnFechar.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnFechar.Location = new System.Drawing.Point(58, 263);
            this.btnFechar.Name = "btnFechar";
            this.btnFechar.Size = new System.Drawing.Size(497, 61);
            this.btnFechar.TabIndex = 6;
            this.btnFechar.Text = "Fechar";
            this.btnFechar.UseVisualStyleBackColor = true;
            this.btnFechar.Click += new System.EventHandler(this.btnFechar_Click);
            // 
            // Formulario
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(584, 361);
            this.Controls.Add(this.btnFechar);
            this.Controls.Add(this.btnDiminuirUmMinuto);
            this.Controls.Add(this.btnDiminuirUmSegundo);
            this.Controls.Add(this.btnAdicionarUmSegundo);
            this.Controls.Add(this.btn_addUmMinuto);
            this.Controls.Add(this.lblHoras);
            this.Controls.Add(this.label1);
            this.MaximizeBox = false;
            this.Name = "Formulario";
            this.Text = "Horario";
            this.Load += new System.EventHandler(this.Formulario_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label lblHoras;
        private System.Windows.Forms.Button btn_addUmMinuto;
        private System.Windows.Forms.Button btnAdicionarUmSegundo;
        private System.Windows.Forms.Button btnDiminuirUmSegundo;
        private System.Windows.Forms.Button btnDiminuirUmMinuto;
        private System.Windows.Forms.Button btnFechar;
    }
}

