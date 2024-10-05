def generate_create_database_sql():
    # Get user input for entity name
    entity_name = input("Enter the entity name: ").strip()
    
    # Get user input for environment, defaulting to "prod"
    environment = input("Enter the environment (dev/staging/prod, default is 'prod'): ").strip()
    if not environment:
        environment = "prod"
    
    # Ask the user for their preferred separator
    separator = input("Do you want to use hyphen (-) or underscore (_) seperators? (default is '_'): ").strip()
    if separator not in ['-', '_']:
        separator = '_'

    # Create the database name
    database_name = f"{entity_name}{separator}{environment}"
    
    # Generate the SQL statement
    create_database_sql = f"CREATE DATABASE {database_name};"
    
    return create_database_sql

# Output the generated SQL
if __name__ == "__main__":
    sql_statement = generate_create_database_sql()
    print(sql_statement)

