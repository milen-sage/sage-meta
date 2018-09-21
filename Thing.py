from typing import Union

class Thing:

    """
    A class used to represent a Thing in Sage annotations land.
    TODO: add type hinting/checking/validation for iterables

    Attributes
    ----------
    sourceSchema : Schema
        a Schema indicating the source schema name (e.g. unique name of the resource containing the definition of this thing) 
        and corresponding schema IRI prefix (e.g. http://schema.org/)
    thingType : str
        a string indicating the type of Thing (e.g. another Thing defined in a schema)
        additional types could be added via the additionalType relationship (see. class Relationships)
    name : str
        a string indicating the name of this Thing (i.e. what is this thing more precisely - Chair, Table, Melanoma, ...)
        note: references to existing schema can be added to the name like so: 'sage.cancer:Melanoma' is the name of Melanoma 
        defined in the sage.cancer schema; the name follows json-ld rules and allows proper term expansion 
        (see json-ld documentation for more details and examples on contexts, expansion and term mapping)
    relationships : dict
        a dictionary specifying the relationships this Thing has to other things 
        e.g. for PlexiformNeurofibromatosis we could have
        {
            isSubclassOf:Neurofibromatosis,
            isRelatedTo:CutaneousNeurofibromatosis
        }

        see class Relationships for possible relationships

    Methods
    -------
    getSourceSchema()
        get source schema name and IRI
    getThingType()
        get this Thing's type
    getName()
        get this Thing's name
    getRelationships()
        get this Thing's relationships
    setSourceSchema(sourceSchema)
        set source schema name and IRI
    setThingType(thingType)
        set this Thing's type
    setName(name)
        set this Thing's name
    setRelationships(relationships)
        set this Thing's relationships
    generateID()
        generate a JSON-LD "@id" string to use in JSON-LD context creation for instance;
        see JSON-LD documentation for more details.
        For Sage meta-data purposes "@id" typically expands to IRI of a term 
        (via the JSON-LD schema_name:Term mapping syntax in context)
    generateType()
        generate a JSON-LD "@type" string to use in JSON-LD context creation for instance;
        see JSON-LD documentation for more details.

        For Sage meta-data purposes "@type" typically refers to the type of Thing this Thing
        belongs (could be used for JSON-LD expansion or definitions constructions (e.g. see the Definition class).

    """     

    def __init__(self, sourceSchema, name, thingType = None, relationships = None):
        """
        Parameters
        ----------
        sourceSchema : dict, required
            a dictionary indicating the source schema name (e.g. unique name of the resource containing the definition of this thing) 
            and corresponding schema IRI prefix (e.g. http://schema.org/)
        name : str, required
            a string indicating the name of this Thing (i.e. what is this thing more precisely - Chair, Table, Melanoma, ...)
            note: references to existing schema can be added to the name like so: 'sage.cancer:Melanoma' is the name of Melanoma 
            defined in the sage.cancer schema; the name follows json-ld rules and allows proper term expansion 
            (see json-ld documentation for more details and examples on contexts, expansion and term mapping)
        thingType : str, optional
            a string indicating the type of Thing (e.g. another Thing defined in a schema)
            additional types could be added via the additionalType relationship (see. class Relationships)
        relationships : dict, optional
            a dictionary specifying the relationships this Thing has to other things 
            e.g. for PlexiformNeurofibromatosis we could have
            {
                isSubclassOf:Neurofibromatosis,
                isRelatedTo:CutaneousNeurofibromatosis
            }

            see class Relationships for possible relationships
        """
        
        self.sourceSchema = sourceSchem
        self.name = name
        self.thingType = thingType
        self.relationships = relationships

    ### 
    # Accessors 
    ###
    def getSourceSchema(self) -> dict:
        """
        Raises
        ------
        NotImplementedError 
            If no sourceSchema has been defined. 
        """

        if self.sourceSchema is None:
            raise NotImplementedError("Things without a source schema for definiton are not supported!")

        return self.sourceSchema
    
    
    def getName(self) -> str:
        """
        Raises
        ------
        NotImplementedError 
            If no name has been defined. 
        """

        if self.name is None:
            raise NotImplementedError("Things without a name are not supported!")

        return self.name


    def getThingType(self) -> Union[str, None]:

        return self.thingType # could be None


    def getRelationships(self) -> Union[list, None]:

        return self.relationships # could be None


    ### 
    # Mutators 
    ###
    
    def setSourceSchema(self, sourceSchema: dict) -> dict:
        """
        Raises
        ------
        NotImplementedError 
            If no sourceSchema is provided. 
        """
        
        self.sourceSchema = sourceSchema
        
        if self.name is None:
            raise NotImplementedError("Need to pass sourceSchema!")

        return self.sourceSchema


    def setName(self, name: str) -> str:
        """
        Raises
        ------
        NotImplementedError 
            If no name is provided. 
        """
        
        self.name = name
        
        if self.name is None:
            raise NotImplementedError("Need to pass name!")

        return self.name
    
    
    def setThingType(self, thingType: str) -> Union[str, None]:

        return self.thingType # could be None


    def setRelationships(self, relationships: list) -> Union[list, None]:
        
        self.relationships = relationships
        
        return self.relationships


    ###
    # Generators
    ###

    def generateID(self) -> str:

        return self.sourceSchema["name"] + ":" + self.name
   

    def generateType(self) -> Union[str, None]:

        if thingType is None:
            return None
        
        return self.sourceSchema["name"] + ":" + self.name


    def __eq__(self, other:Thing) -> bool:
        """overriding equality; assume two things with the same name refer to the same Thing!
        """
        return self.name == other.getName()
