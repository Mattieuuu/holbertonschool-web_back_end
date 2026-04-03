-- Create users table with unique email and primary key id
-- Ensure table creation succeeds even if it already exists
IF NOT EXISTS (
    SELECT 1
    FROM sys.objects
    WHERE object_id = OBJECT_ID(N'dbo.users')
      AND type = N'U'
)
BEGIN
    CREATE TABLE dbo.users (
        id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
        email NVARCHAR(255) NOT NULL UNIQUE,
        name NVARCHAR(255)
    );
END;
