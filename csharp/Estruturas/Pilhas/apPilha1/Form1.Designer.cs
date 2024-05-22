namespace apPilha1
{
  partial class FrmPilhas
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
      this.txtExpressao = new System.Windows.Forms.TextBox();
      this.btnAnalisar = new System.Windows.Forms.Button();
      this.chkBalanceada = new System.Windows.Forms.CheckBox();
      this.dgvPilha = new System.Windows.Forms.DataGridView();
      ((System.ComponentModel.ISupportInitialize)(this.dgvPilha)).BeginInit();
      this.SuspendLayout();
      // 
      // label1
      // 
      this.label1.AutoSize = true;
      this.label1.Location = new System.Drawing.Point(13, 13);
      this.label1.Name = "label1";
      this.label1.Size = new System.Drawing.Size(88, 20);
      this.label1.TabIndex = 0;
      this.label1.Text = "Expressão:";
      // 
      // txtExpressao
      // 
      this.txtExpressao.Font = new System.Drawing.Font("Courier New", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
      this.txtExpressao.Location = new System.Drawing.Point(108, 10);
      this.txtExpressao.Name = "txtExpressao";
      this.txtExpressao.Size = new System.Drawing.Size(334, 26);
      this.txtExpressao.TabIndex = 1;
      this.txtExpressao.Enter += new System.EventHandler(this.txtExpressao_Enter);
      // 
      // btnAnalisar
      // 
      this.btnAnalisar.Location = new System.Drawing.Point(17, 42);
      this.btnAnalisar.Name = "btnAnalisar";
      this.btnAnalisar.Size = new System.Drawing.Size(92, 32);
      this.btnAnalisar.TabIndex = 2;
      this.btnAnalisar.Text = "Analisar";
      this.btnAnalisar.UseVisualStyleBackColor = true;
      this.btnAnalisar.Click += new System.EventHandler(this.btnAnalisar_Click);
      // 
      // chkBalanceada
      // 
      this.chkBalanceada.AutoSize = true;
      this.chkBalanceada.Location = new System.Drawing.Point(142, 50);
      this.chkBalanceada.Name = "chkBalanceada";
      this.chkBalanceada.Size = new System.Drawing.Size(122, 24);
      this.chkBalanceada.TabIndex = 3;
      this.chkBalanceada.Text = "Balanceada?";
      this.chkBalanceada.UseVisualStyleBackColor = true;
      // 
      // dgvPilha
      // 
      this.dgvPilha.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
      this.dgvPilha.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
      this.dgvPilha.Location = new System.Drawing.Point(17, 89);
      this.dgvPilha.Name = "dgvPilha";
      this.dgvPilha.Size = new System.Drawing.Size(425, 70);
      this.dgvPilha.TabIndex = 4;
      // 
      // FrmPilhas
      // 
      this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.None;
      this.ClientSize = new System.Drawing.Size(454, 171);
      this.Controls.Add(this.dgvPilha);
      this.Controls.Add(this.chkBalanceada);
      this.Controls.Add(this.btnAnalisar);
      this.Controls.Add(this.txtExpressao);
      this.Controls.Add(this.label1);
      this.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
      this.Name = "FrmPilhas";
      this.Text = "Tratamento de Pilhas";
      ((System.ComponentModel.ISupportInitialize)(this.dgvPilha)).EndInit();
      this.ResumeLayout(false);
      this.PerformLayout();

    }

    #endregion

    private System.Windows.Forms.Label label1;
    private System.Windows.Forms.TextBox txtExpressao;
    private System.Windows.Forms.Button btnAnalisar;
    private System.Windows.Forms.CheckBox chkBalanceada;
    private System.Windows.Forms.DataGridView dgvPilha;
  }
}

