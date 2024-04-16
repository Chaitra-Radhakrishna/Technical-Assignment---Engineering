import argparse
import mysql.connector      #install mysql-connector

def execute_query(query_name, time_window_start, time_window_end, category):
    cursor = None
    connection = None
    #connect to database
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="user_name",
            password="password",
            database="db_name"
        )
        #create cursor
        cursor = connection.cursor()
        
        #check if the query name exists
        if query_name not in SQL_QUERIES:
            print(f"Error: Query '{query_name}' not found.")
            cursor.close()
            connection.close()
            return

        query = SQL_QUERIES[query_name]
        cursor.execute(query, (category, time_window_start, time_window_end))
        
        #fetch results
        result = cursor.fetchall()
        
        print("Query executed successfully!")
        print("Results:")
        for row in result:
            print(row)
            
    except mysql.connector.Error as err:
        print("Error executing query:", err)
    finally:
        #close cursor and connection
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()

def post_res(result):
    filtered_results = [row for row in result if row['UnitPrice'] < 5.0]
    
    return filtered_results

#define your queries here
SQL_QUERIES = {
    'demand': "SELECT * FROM ecommerce_data WHERE Country = %s AND date BETWEEN %s AND %s;",
}

def main():
    #define CLI arguments
    parser = argparse.ArgumentParser(description='CLI tool to execute SQL queries')
    parser.add_argument('query_name', type=str, help='Name of the SQL query')
    parser.add_argument('time_window_start', type=str, help='Start of the time window (YYYY-MM-DD)')
    parser.add_argument('time_window_end', type=str, help='End of the time window (YYYY-MM-DD)')
    parser.add_argument('country', type=str, help='country for the query')

    args = parser.parse_args()

    #executing the query
    execute_query(args.query_name, args.time_window_start, args.time_window_end, args.category)

if __name__ == "__main__":
    main()