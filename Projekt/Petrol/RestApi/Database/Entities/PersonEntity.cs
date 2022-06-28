namespace RestApi.Database.Entities
{
    public class PersonEntity
    {
        public int ID { get; set; }
        public int FirstName { get; set; }
        public int LastName { get; set; }
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