from typing import Union

class Schema:

    """
    A class representing a Sage schema; a schema is characterized by name and IRI: 
    a unique name of the resource containing the definition of this thing) and corresponding 
    schema IRI prefix (e.g. http://schema.org/)

    Attributes
    ----------
    name: str
        a unique schema name (e.g. to be used as a shorthand in JSON-LD contexts
    iri: str
        a unique resource location (e.g. http://schema.org)
   
    Methods
    -------
    getName()
        get this schema name
    getIRI()
        get this schema IRI
    setName(name)
        set this schema name
    setIRI(iri)
        set this schema IRI 
    """

    def __init__(self, name, iri):
        """
        Parameters
        ----------
        name: str
            a unique schema name (e.g. to be used as a shorthand in JSON-LD contexts
        iri: str
            a unique resource location (e.g. http://schema.org)
        """

        self.name = name
        self.iri = iri

    

    ###
    # Accessors
    ###

    def getName() -> str:
        """
        Raises
        ------
        NotImplementedError 
            If no name has been defined. 
        """

        if self.name is None:
            raise NotImplementedError("A schema must have been provided with a name")
        
        return self.name
   

    def getIRI() -> str:
        """
        Raises
        ------
        NotImplementedError 
            If no IRI has been defined. 
        """

        if self.iri is None:
            raise NotImplementedError("A schema must have been provided with an IRI")
        
        return self.iri
    
    
    ###
    # Mutators
    ###

    def setName(name:str) -> str:
        """
        Raises
        ------
        NotImplementedError 
            If no name has been provided. 
        """

        if self.name is None:
            raise NotImplementedError("Nameless schema has not been implemented; need to provide a name")
        
        return self.name
   

    def setIRI(iri:str) -> str:
        """
        Raises
        ------
        NotImplementedError 
            If no IRI has been provided. 
        """

        if self.iri is None:
            raise NotImplementedError("A resourceless schema has not been implemented; need to provide an IRI")
        
        return self.iri


    def __eq__(self, other:Schema) -> bool:
        """overriding equality; assume two schemas with the same name refer to the same schema!
        """

        return self.name == other.getName()

