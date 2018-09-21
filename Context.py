from typing import Union

class Context:

    """
    A class used to represent a JSON-LD context in Sage annotations land.
    TODO: add type hinting/checking/validation for iterables

    Attributes
    ----------
    name : str
        a unique name for this context; bookkeeping purposes    
    schemas : list
        a list of schemas to which this context refers for mapping purposes; each schema is a dictionary 
    vocab : string
        a JSON-LD vocabulary IRI (e.g. "http://schema.org/")
    things: list
        a list of things defined in the schemas we refer to 
        Note: the containment of a Thing part of this context into a schema part of this context
        is not programmatically


    Methods
    -------
    getName()
        get this context name
    getSchemas()
        get this context schemas
    getVocabs()
        get this context vocabularies
    getThings()
        get this context Things 
    setName(name)
        set this context name
    setSchemas(schemas)
        set this context schemas
    setVocab(vocab)
        set this context vocab
    setThings()
        set this context Things
    addThing(Thing)
        add a Thing to this context Things
    addSchema(schema)
        add a schema to this context schemas
    removeSchema(schemaName)
        remove a schema from this context schemas (by schema name)
    removeThing(thingName)
        remove a Thing from this context things (by Thing name)
    toJSONLD()
        serialize this context to a JSON-LD file
    """     

    def __init__(self, name, schemas = None, things = None, vocab = None):
        """
        Parameters
        ----------
        name : str, required
            a unique name for this context; bookkeeping purposes    
        schemas : list, optional
            a list of schemas to which this context refers for mapping purposes; each schema is a dictionary 
            {
                "schemaName":"schema IRI" #e.g. "schema":"http://schema.org/
            }
            e.g. schemaName is used as a shorthand for schemas in context term mapping (see JSON-LD documentation)
            Might want to encapsulate schema in its own object representation...
        vocab : str, optional
            a JSON-LD vocabulary IRI (e.g. "http://schema.org/")
        things: list, optional
            a list of things defined in the schemas we refer to 
            Note: the containment of a Thing part of this context into a schema part of this context
            is not programmatically
        """
        
        self.name = name
        self.schemas = schemas
        self.things = things
        self.vocab = vocab

    ### 
    # Accessors 
    ###
    def getName(self) -> str:
        """
        Raises
        ------
        NotImplementedError 
            If no name has been defined. 
        """

        if self.name is None:
            raise NotImplementedError("A context must have been provided with a name")

        return self.name


    def getSchemas(self) -> Union[list, None]:

        return self.schemas
    
    
    def getVocab(self) -> Union[str, None]:

        return self.vocab
    
    
    def getThings(self) -> Union[list, None]:

        return self.things

    
    ### 
    # Mutators 
    ###
    
    def setName(self, name: str) -> str:
        """
        Raises
        ------
        NotImplementedError 
            If no name is provided. 
        """
        
        self.name = name
        
        if self.name is None:
            raise NotImplementedError("Need to pass name to this context!")

        return self.name
    
    
    def setSchemas(self, schemas: list) -> Union[list, None]:
        
        self.schemas = schemas 
        
        return self.schemas
   

    def setVocab(self, vocab: str) -> Union[str, None]:
        
        self.vocab = vocab
        
        return self.vocab
    
    
    def setThings(self, things: list) -> Union[list, None]:
        
        self.things = things
        
        return self.things


    def addThing(self, thing: Thing) -> Union(list, None):
        """Gets a Thing to add; looks for it in existing list of things;
           if the thing is already present return None; otherwise add the Thing 
           and return the updated list of things
        """
        if thing in self.things:
            return None 

        self.things.append(thing)

        return self.things
    
    
    def addSchema(self, schema: dict) -> Union(list, None):
        """Gets a schema to add; looks for it in existing list of schemas;
           if the schema is already present return None; otherwise adds the schema 
           and return the updated list of schemas
        """
        
        # check if schema name is in existing schemas
        
        if schema in self.schemas:
            return None

        self.schemas.append(schema)

        return self.schemas
    
   
    def removeSchema(self, schema: dict) -> Union(list, None):
        """Gets a schema to remove; looks for it in existing list of schemas;
           if the schema is not already present return None; otherwise removes the schema 
           and return the updated list of schemas
        """
        
        # check if schema name is in existing schemas

        if not schema in self.schemas:
            return None

        self.schemas.remove(schema)

        return self.schemas


   def removeThing(self, thing: Thing) -> Union(list, None):
        """Gets a Thing to remove; looks for it in existing list of things;
           if the thing is not already present return None; otherwise remove the Thing 
           and return the updated list of things
        """
        
        if not thing in self.things:
            return None
        
        self.things.remove(thing)
        
        return self.things

    
    ###
    # Serializers
    ###
    
    
    def toJSONLD(self) -> dict:
        """Generate a valid JSON-LD context from this Context schemas, things and vocabularies 
        (assuming schema, things and vocabularies have been properly defined; not trying 
        to enforce JSON-LD standards) 
        """

        context = {}
        

        for schema in self.schemas:
            context[schema.getName()] = schema.getIRI()
        
   
        context["@vocab"] = self.vocab

        for thing in self.things:
            # add things properly (only add keys that are present, etc.)
       
        

        return self.sourceSchema["name"] + ":" + self.name
   

