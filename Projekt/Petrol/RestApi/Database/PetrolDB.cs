using Microsoft.EntityFrameworkCore;
using RestApi.Database.Entities;

namespace RestApi.Database
{
    public class PetrolDB : DbContext
    {
        public PetrolDB(DbContextOptions options) : base(options)
        {
        }

        public DbSet<PetrolEntity> Petrol { get; set; }
        // public DbSet<PersonEntity> Person { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);
            // var personEntity = modelBuilder.Entity<PersonEntity>();
            // personEntity.ToTable("Person");
            // personEntity.Property(p => p.ID).IsRequired();


            var petrolEntity = modelBuilder.Entity<PetrolEntity>();
            petrolEntity.ToTable("Petrol");
            petrolEntity.Property(p => p.ID).IsRequired();
        }
    }
}