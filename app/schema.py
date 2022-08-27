instructions= [
    'DROP TABLE IF EXISTS email;',
    """
        CREATE TABLE email(
            id INT PRIMARY KEY AUTO_INCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        )
    """
]
