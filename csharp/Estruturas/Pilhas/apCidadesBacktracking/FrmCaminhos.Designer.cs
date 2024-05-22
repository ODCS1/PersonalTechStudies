namespace apCidadesBacktracking
{
  partial class FrmCaminhos
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
      this.btnAbrirArquivo = new System.Windows.Forms.Button();
      this.label1 = new System.Windows.Forms.Label();
      this.txtOrigem = new System.Windows.Forms.TextBox();
      this.txtDestino = new System.Windows.Forms.TextBox();
      this.label2 = new System.Windows.Forms.Label();
      this.groupBox1 = new System.Windows.Forms.GroupBox();
      this.rbLigacao = new System.Windows.Forms.RadioButton();
      this.rbDistancia = new System.Windows.Forms.RadioButton();
      this.btnBuscar = new System.Windows.Forms.Button();
      this.label3 = new System.Windows.Forms.Label();
      this.dgvPilha = new System.Windows.Forms.DataGridView();
      this.dgvGrafo = new System.Windows.Forms.DataGridView();
      this.label4 = new System.Windows.Forms.Label();
      this.lsbMovimentos = new System.Windows.Forms.ListBox();
      this.dlgAbrir = new System.Windows.Forms.OpenFileDialog();
      this.groupBox1.SuspendLayout();
      ((System.ComponentModel.ISupportInitialize)(this.dgvPilha)).BeginInit();
      ((System.ComponentModel.ISupportInitialize)(this.dgvGrafo)).BeginInit();
      this.SuspendLayout();
      // 
      // btnAbrirArquivo
      // 
      this.btnAbrirArquivo.Location = new System.Drawing.Point(5, 10);
      this.btnAbrirArquivo.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
      this.btnAbrirArquivo.Name = "btnAbrirArquivo";
      this.btnAbrirArquivo.Size = new System.Drawing.Size(112, 32);
      this.btnAbrirArquivo.TabIndex = 0;
      this.btnAbrirArquivo.Text = "Abrir Arquivo";
      this.btnAbrirArquivo.UseVisualStyleBackColor = true;
      this.btnAbrirArquivo.Click += new System.EventHandler(this.btnAbrirArquivo_Click);
      // 
      // label1
      // 
      this.label1.AutoSize = true;
      this.label1.Location = new System.Drawing.Point(162, 18);
      this.label1.Name = "label1";
      this.label1.Size = new System.Drawing.Size(61, 18);
      this.label1.TabIndex = 1;
      this.label1.Text = "Origem:";
      // 
      // txtOrigem
      // 
      this.txtOrigem.Location = new System.Drawing.Point(229, 15);
      this.txtOrigem.Name = "txtOrigem";
      this.txtOrigem.Size = new System.Drawing.Size(45, 24);
      this.txtOrigem.TabIndex = 2;
      // 
      // txtDestino
      // 
      this.txtDestino.Location = new System.Drawing.Point(362, 15);
      this.txtDestino.Name = "txtDestino";
      this.txtDestino.Size = new System.Drawing.Size(45, 24);
      this.txtDestino.TabIndex = 4;
      // 
      // label2
      // 
      this.label2.AutoSize = true;
      this.label2.Location = new System.Drawing.Point(295, 18);
      this.label2.Name = "label2";
      this.label2.Size = new System.Drawing.Size(63, 18);
      this.label2.TabIndex = 3;
      this.label2.Text = "Destino:";
      // 
      // groupBox1
      // 
      this.groupBox1.Controls.Add(this.rbDistancia);
      this.groupBox1.Controls.Add(this.rbLigacao);
      this.groupBox1.Location = new System.Drawing.Point(165, 51);
      this.groupBox1.Name = "groupBox1";
      this.groupBox1.Size = new System.Drawing.Size(318, 55);
      this.groupBox1.TabIndex = 5;
      this.groupBox1.TabStop = false;
      this.groupBox1.Text = "Tipo de Grafo";
      // 
      // rbLigacao
      // 
      this.rbLigacao.AutoSize = true;
      this.rbLigacao.Location = new System.Drawing.Point(19, 24);
      this.rbLigacao.Name = "rbLigacao";
      this.rbLigacao.Size = new System.Drawing.Size(139, 22);
      this.rbLigacao.TabIndex = 0;
      this.rbLigacao.TabStop = true;
      this.rbLigacao.Text = "Apenas Ligações";
      this.rbLigacao.UseVisualStyleBackColor = true;
      // 
      // rbDistancia
      // 
      this.rbDistancia.AutoSize = true;
      this.rbDistancia.Location = new System.Drawing.Point(174, 24);
      this.rbDistancia.Name = "rbDistancia";
      this.rbDistancia.Size = new System.Drawing.Size(129, 22);
      this.rbDistancia.TabIndex = 1;
      this.rbDistancia.TabStop = true;
      this.rbDistancia.Text = "Com distâncias";
      this.rbDistancia.UseVisualStyleBackColor = true;
      // 
      // btnBuscar
      // 
      this.btnBuscar.Location = new System.Drawing.Point(430, 15);
      this.btnBuscar.Name = "btnBuscar";
      this.btnBuscar.Size = new System.Drawing.Size(75, 27);
      this.btnBuscar.TabIndex = 6;
      this.btnBuscar.Text = "Buscar";
      this.btnBuscar.UseVisualStyleBackColor = true;
      this.btnBuscar.Click += new System.EventHandler(this.btnBuscar_Click);
      // 
      // label3
      // 
      this.label3.AutoSize = true;
      this.label3.Location = new System.Drawing.Point(2, 107);
      this.label3.Name = "label3";
      this.label3.Size = new System.Drawing.Size(40, 18);
      this.label3.TabIndex = 7;
      this.label3.Text = "Pilha";
      // 
      // dgvPilha
      // 
      this.dgvPilha.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
      this.dgvPilha.Location = new System.Drawing.Point(5, 128);
      this.dgvPilha.Name = "dgvPilha";
      this.dgvPilha.Size = new System.Drawing.Size(526, 83);
      this.dgvPilha.TabIndex = 8;
      // 
      // dgvGrafo
      // 
      this.dgvGrafo.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
      this.dgvGrafo.Location = new System.Drawing.Point(5, 235);
      this.dgvGrafo.Name = "dgvGrafo";
      this.dgvGrafo.Size = new System.Drawing.Size(526, 287);
      this.dgvGrafo.TabIndex = 10;
      // 
      // label4
      // 
      this.label4.AutoSize = true;
      this.label4.Location = new System.Drawing.Point(2, 214);
      this.label4.Name = "label4";
      this.label4.Size = new System.Drawing.Size(46, 18);
      this.label4.TabIndex = 9;
      this.label4.Text = "Grafo";
      this.label4.Click += new System.EventHandler(this.label4_Click);
      // 
      // lsbMovimentos
      // 
      this.lsbMovimentos.FormattingEnabled = true;
      this.lsbMovimentos.ItemHeight = 18;
      this.lsbMovimentos.Location = new System.Drawing.Point(5, 529);
      this.lsbMovimentos.Name = "lsbMovimentos";
      this.lsbMovimentos.Size = new System.Drawing.Size(526, 148);
      this.lsbMovimentos.TabIndex = 11;
      // 
      // FrmCaminhos
      // 
      this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 18F);
      this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
      this.ClientSize = new System.Drawing.Size(538, 683);
      this.Controls.Add(this.lsbMovimentos);
      this.Controls.Add(this.dgvGrafo);
      this.Controls.Add(this.label4);
      this.Controls.Add(this.dgvPilha);
      this.Controls.Add(this.label3);
      this.Controls.Add(this.btnBuscar);
      this.Controls.Add(this.groupBox1);
      this.Controls.Add(this.txtDestino);
      this.Controls.Add(this.label2);
      this.Controls.Add(this.txtOrigem);
      this.Controls.Add(this.label1);
      this.Controls.Add(this.btnAbrirArquivo);
      this.Font = new System.Drawing.Font("Microsoft Sans Serif", 11F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
      this.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
      this.Name = "FrmCaminhos";
      this.Text = "Busca de caminhos entre cidades";
      this.groupBox1.ResumeLayout(false);
      this.groupBox1.PerformLayout();
      ((System.ComponentModel.ISupportInitialize)(this.dgvPilha)).EndInit();
      ((System.ComponentModel.ISupportInitialize)(this.dgvGrafo)).EndInit();
      this.ResumeLayout(false);
      this.PerformLayout();

    }

    #endregion

    private System.Windows.Forms.Button btnAbrirArquivo;
    private System.Windows.Forms.Label label1;
    private System.Windows.Forms.TextBox txtOrigem;
    private System.Windows.Forms.TextBox txtDestino;
    private System.Windows.Forms.Label label2;
    private System.Windows.Forms.GroupBox groupBox1;
    private System.Windows.Forms.RadioButton rbDistancia;
    private System.Windows.Forms.RadioButton rbLigacao;
    private System.Windows.Forms.Button btnBuscar;
    private System.Windows.Forms.Label label3;
    private System.Windows.Forms.DataGridView dgvPilha;
    private System.Windows.Forms.DataGridView dgvGrafo;
    private System.Windows.Forms.Label label4;
    private System.Windows.Forms.ListBox lsbMovimentos;
    private System.Windows.Forms.OpenFileDialog dlgAbrir;
  }
}

