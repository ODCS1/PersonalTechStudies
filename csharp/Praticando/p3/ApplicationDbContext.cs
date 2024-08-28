using Microsoft.EntityFrameworkCore;



public class ApplicationDbContext : DbContext{

public DbSet<Produto> Produtos {get; set;}


protected override void OnConfiguring(DbContextOptionsBuilder options) => options.UseSqlServer("Server=regulus;Database=BD23505;UserId=BD23505;Password=BD23505;MultipleActiveResultSets=true;Encrypt=YES;TrustServerCertificate=YES");


}

