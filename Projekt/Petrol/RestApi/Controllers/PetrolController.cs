using Microsoft.AspNetCore.Mvc;
using RestApi.Database;
using RestApi.Database.Entities;
using System.Text.Json;

namespace RestApi.Controllers;

[ApiController]
[Route("[controller]")]
public class PetrolController : ControllerBase
{
    private readonly PetrolDB db;

    public PetrolController(PetrolDB db)
    {
        this.db = db;
    }
    
    [HttpGet]
    public IActionResult Get()
    {
        var petrol = db.Petrol.ToList();
        return Ok(petrol);

    }

    [HttpGet("{id}")]
    public async Task<ActionResult<PetrolEntity>> GetPetrolItem(int id)
    {
        var litres = db.Petrol.Where(l => l.ID == id).First();
        return Ok(litres.Litres);
    }

    [HttpPut("{id}")]
    public void Put(int id, [FromBody] int li)
    {
        var entity = db.Petrol.Where(p => p.ID == id).First();
        entity.Litres = li;

        db.SaveChanges();

    }

    [HttpGet("/auth/{card}/{key}")]
    public IActionResult Get(string card, string key)
    {
        try{
            var auth = db.Petrol.Where(c => c.CardId == card ).Where(k => k.CardKey == key).First();
            return Ok(auth.ID);
            
        }
        catch(System.InvalidOperationException exept){
            return Ok("ERR");
        }

        
    }

    [HttpPut("/new")]    
    public void Put([FromBody] PetrolEntity newPet)
    {
        // {"firstName":"Test","lastName":"Testowy","cardId":"868581146633","cardKey":"test","litres":2137}
        db.Petrol.Add(newPet);
        db.SaveChanges();

    }
}
