namespace RestApi.Database.Entities
{
    public class PetrolEntity
    {
        public int ID { get; set; }
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public string CardId { get; set; }
        public string CardKey { get; set; }        
        private int _litres = 0;
        public int Litres { 
            get; set;
        //    get { return _litres; }
      //      set { 
    //            if ( value == null ) 
  //                  _litres = 0;
//                else _litres = value;
        }
    }
}