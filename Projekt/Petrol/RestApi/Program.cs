using Microsoft.EntityFrameworkCore;
using RestApi.Database;
using RestApi.Database.Entities;
var builder = WebApplication.CreateBuilder(args);

// Add services to the container.

builder.Services.AddControllers();
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

builder.Services.AddDbContext<PetrolDB>(options => 
{
    var cs = builder.Configuration.GetConnectionString("PetrolDB");
    var test = "Server=tcp:petrol.database.windows.net,1433;Initial Catalog=petrol;Persist Security Info=False;User ID=tst;Password=test123@#;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;";
    options.UseSqlServer(test);
    //options.UseSqlServer(cs);
});

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

app.Run();
