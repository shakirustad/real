<!DOCTYPE html>
<?php
$db = new SQLite3('sqlite3db.db');

// use $db;


// include('connector.php');
// include('logincode.php');
// require_once('connector.php');

// // Create a table (if not exists)
// $queryCreateTable = "
//     CREATE TABLE IF NOT EXISTS users (
//         id INTEGER PRIMARY KEY AUTOINCREMENT,
//         username TEXT NOT NULL,
//         email TEXT NOT NULL
//     )
// ";
// $db->exec($queryCreateTable);

// // Insert some sample data (if not exists)
// $queryInsertData = "
//     INSERT INTO users (username, email)
//     VALUES
//         ('john_doe', 'john@example.com'),
//         ('jane_doe', 'jane@example.com')
// ";
// $db->exec($queryInsertData);

$results = $db->query('select * from users');
while ($row = $results->fetchArray()) {
var_dump($row);
}

// // Close the database connection
// $db->close();
?>
</html>