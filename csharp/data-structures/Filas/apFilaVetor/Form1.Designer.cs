namespace apFilaVetor
{
  partial class FrmFilaVetor
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
      this.txtNome = new System.Windows.Forms.TextBox();
      this.label1 = new System.Windows.Forms.Label();
      this.lsbFila = new System.Windows.Forms.ListBox();
      this.btnEnfileirar = new System.Windows.Forms.Button();
      this.btnRetirar = new System.Windows.Forms.Button();
      this.SuspendLayout();
      // 
      // txtNome
      // 
      this.txtNome.Location = new System.Drawing.Point(78, 28);
      this.txtNome.Name = "txtNome";
      this.txtNome.Size = new System.Drawing.Size(100, 20);
      this.txtNome.TabIndex = 0;
      // 
      // label1
      // 
      this.label1.AutoSize = true;
      this.label1.Location = new System.Drawing.Point(27, 28);
      this.label1.Name = "label1";
      this.label1.Size = new System.Drawing.Size(38, 13);
      this.label1.TabIndex = 1;
      this.label1.Text = "Nome:";
      // 
      // lsbFila
      // 
      this.lsbFila.FormattingEnabled = true;
      this.lsbFila.Location = new System.Drawing.Point(30, 83);
      this.lsbFila.Name = "lsbFila";
      this.lsbFila.Size = new System.Drawing.Size(148, 199);
      this.lsbFila.TabIndex = 2;
      // 
      // btnEnfileirar
      // 
      this.btnEnfileirar.Location = new System.Drawing.Point(204, 28);
      this.btnEnfileirar.Name = "btnEnfileirar";
      this.btnEnfileirar.Size = new System.Drawing.Size(75, 23);
      this.btnEnfileirar.TabIndex = 3;
      this.btnEnfileirar.Text = "Enfileirar";
      this.btnEnfileirar.UseVisualStyleBackColor = true;
      this.btnEnfileirar.Click += new System.EventHandler(this.btnEnfileirar_Click);
      // 
      // btnRetirar
      // 
      this.btnRetirar.Location = new System.Drawing.Point(298, 26);
      this.btnRetirar.Name = "btnRetirar";
      this.btnRetirar.Size = new System.Drawing.Size(75, 23);
      this.btnRetirar.TabIndex = 4;
      this.btnRetirar.Text = "Retirar";
      this.btnRetirar.UseVisualStyleBackColor = true;
      this.btnRetirar.Click += new System.EventHandler(this.btnRetirar_Click);
      // 
      // FrmFilaVetor
      // 
      this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
      this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
      this.ClientSize = new System.Drawing.Size(644, 317);
      this.Controls.Add(this.btnRetirar);
      this.Controls.Add(this.btnEnfileirar);
      this.Controls.Add(this.lsbFila);
      this.Controls.Add(this.label1);
      this.Controls.Add(this.txtNome);
      this.Name = "FrmFilaVetor";
      this.Text = "Filas com vetores linear e circular";
      this.Load += new System.EventHandler(this.FrmFilaVetor_Load);
      this.ResumeLayout(false);
      this.PerformLayout();

    }

    #endregion

    private System.Windows.Forms.TextBox txtNome;
    private System.Windows.Forms.Label label1;
    private System.Windows.Forms.ListBox lsbFila;
    private System.Windows.Forms.Button btnEnfileirar;
    private System.Windows.Forms.Button btnRetirar;
  }
}

