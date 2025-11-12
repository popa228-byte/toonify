"""
Sample datasets for benchmarking TOON vs JSON.
50 diverse datasets representing common data structures used in LLM applications.
"""

# 1. E-commerce product catalog (tabular data)
ECOMMERCE_PRODUCTS = {
    "products": [
        {"id": 1001, "sku": "LAP-001", "name": "Gaming Laptop", "price": 1299.99, "stock": 45, "category": "Electronics"},
        {"id": 1002, "sku": "MOU-042", "name": "Wireless Mouse", "price": 29.99, "stock": 234, "category": "Accessories"},
        {"id": 1003, "sku": "KEY-089", "name": "Mechanical Keyboard", "price": 149.99, "stock": 67, "category": "Accessories"},
        {"id": 1004, "sku": "MON-156", "name": "4K Monitor", "price": 499.99, "stock": 23, "category": "Electronics"},
        {"id": 1005, "sku": "HED-234", "name": "USB Headset", "price": 79.99, "stock": 156, "category": "Accessories"},
        {"id": 1006, "sku": "CAM-445", "name": "Webcam HD", "price": 89.99, "stock": 89, "category": "Electronics"},
        {"id": 1007, "sku": "CHA-778", "name": "Office Chair", "price": 299.99, "stock": 34, "category": "Furniture"},
        {"id": 1008, "sku": "DES-992", "name": "Standing Desk", "price": 599.99, "stock": 12, "category": "Furniture"},
        {"id": 1009, "sku": "LAM-334", "name": "Desk Lamp", "price": 45.99, "stock": 178, "category": "Accessories"},
        {"id": 1010, "sku": "HUB-667", "name": "USB-C Hub", "price": 69.99, "stock": 203, "category": "Electronics"},
    ]
}

# 2. API response with nested structure
API_RESPONSE = {
    "status": "success",
    "timestamp": "2024-01-15T10:30:00Z",
    "data": {
        "user": {
            "id": 12345,
            "username": "john_doe",
            "email": "john@example.com",
            "profile": {
                "first_name": "John",
                "last_name": "Doe",
                "age": 32,
                "location": "San Francisco"
            }
        },
        "orders": [
            {"order_id": "ORD-2024-001", "date": "2024-01-10", "total": 599.99, "status": "shipped", "items": 3},
            {"order_id": "ORD-2024-002", "date": "2024-01-12", "total": 129.99, "status": "processing", "items": 1},
            {"order_id": "ORD-2024-003", "date": "2024-01-14", "total": 349.50, "status": "delivered", "items": 2}
        ]
    },
    "metadata": {
        "request_id": "req_abc123def456",
        "processing_time_ms": 45,
        "api_version": "v2.1"
    }
}

# 3. Database query results (highly tabular)
DATABASE_RESULTS = {
    "query": "SELECT * FROM employees WHERE department = 'Engineering'",
    "rows": [
        {"emp_id": 1001, "name": "Alice Johnson", "department": "Engineering", "salary": 95000, "start_date": "2020-03-15", "remote": True},
        {"emp_id": 1002, "name": "Bob Smith", "department": "Engineering", "salary": 105000, "start_date": "2019-07-22", "remote": False},
        {"emp_id": 1003, "name": "Carol White", "department": "Engineering", "salary": 98000, "start_date": "2021-01-10", "remote": True},
        {"emp_id": 1004, "name": "David Brown", "department": "Engineering", "salary": 110000, "start_date": "2018-11-05", "remote": False},
        {"emp_id": 1005, "name": "Eve Davis", "department": "Engineering", "salary": 92000, "start_date": "2022-02-28", "remote": True},
        {"emp_id": 1006, "name": "Frank Miller", "department": "Engineering", "salary": 115000, "start_date": "2017-09-14", "remote": False},
        {"emp_id": 1007, "name": "Grace Lee", "department": "Engineering", "salary": 88000, "start_date": "2023-05-20", "remote": True},
        {"emp_id": 1008, "name": "Henry Wilson", "department": "Engineering", "salary": 120000, "start_date": "2016-04-03", "remote": False},
    ],
    "count": 8,
    "execution_time_ms": 12
}

# 4. Machine learning training data
ML_TRAINING_DATA = {
    "dataset": "customer_churn",
    "features": ["age", "tenure", "monthly_charges", "total_charges", "num_services"],
    "samples": [
        {"age": 45, "tenure": 24, "monthly_charges": 89.99, "total_charges": 2159.76, "num_services": 4, "churned": False},
        {"age": 32, "tenure": 6, "monthly_charges": 65.50, "total_charges": 393.00, "num_services": 2, "churned": True},
        {"age": 28, "tenure": 36, "monthly_charges": 120.00, "total_charges": 4320.00, "num_services": 6, "churned": False},
        {"age": 55, "tenure": 12, "monthly_charges": 45.25, "total_charges": 543.00, "num_services": 1, "churned": True},
        {"age": 41, "tenure": 48, "monthly_charges": 95.75, "total_charges": 4596.00, "num_services": 5, "churned": False},
        {"age": 29, "tenure": 3, "monthly_charges": 55.00, "total_charges": 165.00, "num_services": 2, "churned": True},
        {"age": 38, "tenure": 60, "monthly_charges": 110.50, "total_charges": 6630.00, "num_services": 7, "churned": False},
        {"age": 52, "tenure": 18, "monthly_charges": 75.25, "total_charges": 1354.50, "num_services": 3, "churned": False},
        {"age": 26, "tenure": 9, "monthly_charges": 50.00, "total_charges": 450.00, "num_services": 1, "churned": True},
        {"age": 47, "tenure": 42, "monthly_charges": 105.00, "total_charges": 4410.00, "num_services": 6, "churned": False},
    ],
    "metadata": {"total_samples": 10, "positive_samples": 4, "negative_samples": 6, "date_collected": "2024-01-15"}
}

# 5. Server configuration (nested objects)
SERVER_CONFIG = {
    "application": {"name": "production-api", "version": "2.3.1", "environment": "production"},
    "server": {"host": "0.0.0.0", "port": 8080, "workers": 4, "timeout": 30, "keepalive": 65},
    "database": {
        "primary": {"host": "db-primary.example.com", "port": 5432, "name": "production_db", "pool_size": 20, "max_overflow": 10},
        "replica": {"host": "db-replica.example.com", "port": 5432, "name": "production_db", "pool_size": 10, "max_overflow": 5}
    },
    "cache": {"redis": {"host": "redis.example.com", "port": 6379, "db": 0, "password": "secret", "max_connections": 50}},
    "logging": {"level": "info", "format": "json", "output": "stdout", "rotation": {"max_bytes": 10485760, "backup_count": 5}},
    "features": {"rate_limiting": True, "caching": True, "monitoring": True, "metrics": True}
}

# 6. Analytics/metrics data
ANALYTICS_DATA = {
    "report": "weekly_metrics",
    "period": {"start": "2024-01-08", "end": "2024-01-14"},
    "metrics": [
        {"date": "2024-01-08", "users": 1234, "sessions": 3456, "pageviews": 12345, "bounce_rate": 42.5, "avg_duration": 185},
        {"date": "2024-01-09", "users": 1456, "sessions": 3789, "pageviews": 13456, "bounce_rate": 41.2, "avg_duration": 192},
        {"date": "2024-01-10", "users": 1567, "sessions": 4012, "pageviews": 14567, "bounce_rate": 40.8, "avg_duration": 198},
        {"date": "2024-01-11", "users": 1678, "sessions": 4234, "pageviews": 15678, "bounce_rate": 39.5, "avg_duration": 205},
        {"date": "2024-01-12", "users": 1789, "sessions": 4456, "pageviews": 16789, "bounce_rate": 38.9, "avg_duration": 212},
        {"date": "2024-01-13", "users": 1345, "sessions": 3678, "pageviews": 13234, "bounce_rate": 43.1, "avg_duration": 178},
        {"date": "2024-01-14", "users": 1456, "sessions": 3890, "pageviews": 14123, "bounce_rate": 42.3, "avg_duration": 183},
    ],
    "summary": {"total_users": 10525, "total_sessions": 27515, "total_pageviews": 100192, "avg_bounce_rate": 41.2, "avg_duration": 193}
}

# 7. Large inventory dataset
LARGE_INVENTORY = {
    "warehouse": "WH-CENTRAL-01",
    "inventory": [
        {"sku": f"PROD-{i:04d}", "name": f"Product {i}", "quantity": (i * 7) % 500, "price": round(10 + (i * 3.14) % 1000, 2), "location": f"A{(i % 10) + 1}-B{(i % 5) + 1}"}
        for i in range(100)
    ]
}

# 8. Customer reviews
CUSTOMER_REVIEWS = {
    "product_id": "LAP-001",
    "reviews": [
        {"review_id": "R001", "user": "user123", "rating": 5, "date": "2024-01-10", "verified": True, "helpful": 45},
        {"review_id": "R002", "user": "user456", "rating": 4, "date": "2024-01-11", "verified": True, "helpful": 23},
        {"review_id": "R003", "user": "user789", "rating": 5, "date": "2024-01-12", "verified": False, "helpful": 12},
        {"review_id": "R004", "user": "user234", "rating": 3, "date": "2024-01-13", "verified": True, "helpful": 8},
        {"review_id": "R005", "user": "user567", "rating": 4, "date": "2024-01-14", "verified": True, "helpful": 34},
    ]
}

# 9. Social media posts
SOCIAL_MEDIA_POSTS = {
    "posts": [
        {"post_id": "P001", "author": "alice", "likes": 245, "comments": 12, "shares": 34, "timestamp": "2024-01-15T09:00:00Z"},
        {"post_id": "P002", "author": "bob", "likes": 156, "comments": 8, "shares": 21, "timestamp": "2024-01-15T10:15:00Z"},
        {"post_id": "P003", "author": "carol", "likes": 489, "comments": 56, "shares": 78, "timestamp": "2024-01-15T11:30:00Z"},
        {"post_id": "P004", "author": "david", "likes": 123, "comments": 5, "shares": 12, "timestamp": "2024-01-15T12:45:00Z"},
        {"post_id": "P005", "author": "eve", "likes": 678, "comments": 89, "shares": 123, "timestamp": "2024-01-15T14:00:00Z"},
    ]
}

# 10. Weather forecast
WEATHER_FORECAST = {
    "location": "San Francisco, CA",
    "forecast": [
        {"date": "2024-01-16", "high": 65, "low": 52, "condition": "Partly Cloudy", "humidity": 72, "wind": 8},
        {"date": "2024-01-17", "high": 68, "low": 54, "condition": "Sunny", "humidity": 65, "wind": 6},
        {"date": "2024-01-18", "high": 62, "low": 50, "condition": "Rainy", "humidity": 85, "wind": 12},
        {"date": "2024-01-19", "high": 64, "low": 51, "condition": "Cloudy", "humidity": 70, "wind": 9},
        {"date": "2024-01-20", "high": 66, "low": 53, "condition": "Sunny", "humidity": 68, "wind": 7},
    ]
}

# 11. Stock market data
STOCK_MARKET_DATA = {
    "symbol": "TECH",
    "quotes": [
        {"timestamp": "2024-01-15T09:30:00Z", "open": 150.25, "high": 152.10, "low": 149.80, "close": 151.50, "volume": 1250000},
        {"timestamp": "2024-01-15T10:30:00Z", "open": 151.50, "high": 153.25, "low": 151.20, "close": 152.80, "volume": 980000},
        {"timestamp": "2024-01-15T11:30:00Z", "open": 152.80, "high": 154.00, "low": 152.50, "close": 153.60, "volume": 1120000},
        {"timestamp": "2024-01-15T12:30:00Z", "open": 153.60, "high": 154.50, "low": 152.90, "close": 153.20, "volume": 890000},
        {"timestamp": "2024-01-15T13:30:00Z", "open": 153.20, "high": 154.80, "low": 153.00, "close": 154.40, "volume": 1050000},
    ]
}

# 12. Restaurant menu
RESTAURANT_MENU = {
    "restaurant": "Bella Italia",
    "menu_items": [
        {"item_id": "M001", "name": "Margherita Pizza", "category": "Pizza", "price": 14.99, "calories": 800, "vegetarian": True},
        {"item_id": "M002", "name": "Spaghetti Carbonara", "category": "Pasta", "price": 16.99, "calories": 950, "vegetarian": False},
        {"item_id": "M003", "name": "Caesar Salad", "category": "Salad", "price": 9.99, "calories": 350, "vegetarian": True},
        {"item_id": "M004", "name": "Lasagna", "category": "Pasta", "price": 18.99, "calories": 1100, "vegetarian": False},
        {"item_id": "M005", "name": "Tiramisu", "category": "Dessert", "price": 7.99, "calories": 450, "vegetarian": True},
    ]
}

# 13. Hotel bookings
HOTEL_BOOKINGS = {
    "hotel": "Grand Plaza Hotel",
    "bookings": [
        {"booking_id": "B001", "guest": "John Smith", "room": "201", "check_in": "2024-01-20", "check_out": "2024-01-23", "rate": 199.00, "guests": 2},
        {"booking_id": "B002", "guest": "Jane Doe", "room": "305", "check_in": "2024-01-21", "check_out": "2024-01-25", "rate": 249.00, "guests": 1},
        {"booking_id": "B003", "guest": "Bob Wilson", "room": "412", "check_in": "2024-01-22", "check_out": "2024-01-24", "rate": 299.00, "guests": 3},
        {"booking_id": "B004", "guest": "Alice Brown", "room": "108", "check_in": "2024-01-23", "check_out": "2024-01-27", "rate": 189.00, "guests": 2},
    ]
}

# 14. Flight schedule
FLIGHT_SCHEDULE = {
    "airport": "SFO",
    "flights": [
        {"flight_num": "UA123", "destination": "LAX", "departure": "09:00", "arrival": "10:30", "status": "On Time", "gate": "A12"},
        {"flight_num": "DL456", "destination": "JFK", "departure": "10:15", "arrival": "18:45", "status": "Delayed", "gate": "B05"},
        {"flight_num": "AA789", "destination": "ORD", "departure": "11:30", "arrival": "17:20", "status": "On Time", "gate": "C23"},
        {"flight_num": "SW234", "destination": "LAS", "departure": "12:00", "arrival": "13:20", "status": "Boarding", "gate": "D18"},
        {"flight_num": "UA567", "destination": "SEA", "departure": "13:45", "arrival": "16:00", "status": "On Time", "gate": "A08"},
    ]
}

# 15. Medical records
MEDICAL_RECORDS = {
    "patient_id": "P12345",
    "visits": [
        {"visit_id": "V001", "date": "2024-01-05", "diagnosis": "Common Cold", "prescribed": "Rest", "cost": 75.00},
        {"visit_id": "V002", "date": "2024-01-10", "diagnosis": "Annual Checkup", "prescribed": "None", "cost": 150.00},
        {"visit_id": "V003", "date": "2024-01-12", "diagnosis": "Sprained Ankle", "prescribed": "Ice and Rest", "cost": 120.00},
    ]
}

# 16. Student grades
STUDENT_GRADES = {
    "semester": "Fall 2024",
    "students": [
        {"student_id": "S001", "name": "Alice Chen", "math": 95, "science": 92, "english": 88, "history": 90, "gpa": 3.85},
        {"student_id": "S002", "name": "Bob Lee", "math": 88, "science": 85, "english": 92, "history": 87, "gpa": 3.55},
        {"student_id": "S003", "name": "Carol Martinez", "math": 92, "science": 94, "english": 90, "history": 93, "gpa": 3.92},
        {"student_id": "S004", "name": "David Kim", "math": 85, "science": 88, "english": 86, "history": 84, "gpa": 3.45},
        {"student_id": "S005", "name": "Eve Patel", "math": 98, "science": 96, "english": 94, "history": 95, "gpa": 3.98},
    ]
}

# 17. Sports statistics
SPORTS_STATISTICS = {
    "league": "NBA",
    "season": "2023-2024",
    "players": [
        {"player_id": "P001", "name": "LeBron James", "team": "LAL", "points": 25.4, "rebounds": 7.2, "assists": 8.1, "games": 45},
        {"player_id": "P002", "name": "Stephen Curry", "team": "GSW", "points": 28.7, "rebounds": 5.1, "assists": 6.3, "games": 48},
        {"player_id": "P003", "name": "Kevin Durant", "team": "PHX", "points": 29.1, "rebounds": 6.8, "assists": 5.4, "games": 42},
        {"player_id": "P004", "name": "Giannis Antetokounmpo", "team": "MIL", "points": 31.2, "rebounds": 11.5, "assists": 5.8, "games": 50},
    ]
}

# 18. Movie catalog
MOVIE_CATALOG = {
    "movies": [
        {"movie_id": "M001", "title": "The Matrix", "year": 1999, "genre": "Sci-Fi", "rating": 8.7, "runtime": 136, "director": "Wachowski"},
        {"movie_id": "M002", "title": "Inception", "year": 2010, "genre": "Sci-Fi", "rating": 8.8, "runtime": 148, "director": "Nolan"},
        {"movie_id": "M003", "title": "The Godfather", "year": 1972, "genre": "Crime", "rating": 9.2, "runtime": 175, "director": "Coppola"},
        {"movie_id": "M004", "title": "Pulp Fiction", "year": 1994, "genre": "Crime", "rating": 8.9, "runtime": 154, "director": "Tarantino"},
        {"movie_id": "M005", "title": "The Dark Knight", "year": 2008, "genre": "Action", "rating": 9.0, "runtime": 152, "director": "Nolan"},
    ]
}

# 19. Music playlist
MUSIC_PLAYLIST = {
    "playlist": "Top Hits 2024",
    "tracks": [
        {"track_id": "T001", "title": "Blinding Lights", "artist": "The Weeknd", "album": "After Hours", "duration": 200, "plays": 2450000},
        {"track_id": "T002", "title": "Levitating", "artist": "Dua Lipa", "album": "Future Nostalgia", "duration": 203, "plays": 1980000},
        {"track_id": "T003", "title": "Save Your Tears", "artist": "The Weeknd", "album": "After Hours", "duration": 215, "plays": 1750000},
        {"track_id": "T004", "title": "Peaches", "artist": "Justin Bieber", "album": "Justice", "duration": 198, "plays": 1650000},
        {"track_id": "T005", "title": "Good 4 U", "artist": "Olivia Rodrigo", "album": "Sour", "duration": 178, "plays": 2100000},
    ]
}

# 20. Real estate listings
REAL_ESTATE_LISTINGS = {
    "city": "San Francisco",
    "listings": [
        {"listing_id": "L001", "address": "123 Market St", "price": 1250000, "bedrooms": 2, "bathrooms": 2, "sqft": 1200, "year_built": 2015},
        {"listing_id": "L002", "address": "456 Mission St", "price": 2100000, "bedrooms": 3, "bathrooms": 2.5, "sqft": 1800, "year_built": 2018},
        {"listing_id": "L003", "address": "789 Valencia St", "price": 950000, "bedrooms": 1, "bathrooms": 1, "sqft": 850, "year_built": 2010},
        {"listing_id": "L004", "address": "321 Folsom St", "price": 1650000, "bedrooms": 2, "bathrooms": 2, "sqft": 1400, "year_built": 2020},
    ]
}

# 21. Job postings
JOB_POSTINGS = {
    "company": "TechCorp Inc",
    "positions": [
        {"job_id": "J001", "title": "Software Engineer", "department": "Engineering", "location": "Remote", "salary_min": 120000, "salary_max": 180000, "level": "Senior"},
        {"job_id": "J002", "title": "Product Manager", "department": "Product", "location": "San Francisco", "salary_min": 140000, "salary_max": 200000, "level": "Lead"},
        {"job_id": "J003", "title": "Data Scientist", "department": "Data", "location": "New York", "salary_min": 130000, "salary_max": 190000, "level": "Senior"},
        {"job_id": "J004", "title": "UX Designer", "department": "Design", "location": "Remote", "salary_min": 100000, "salary_max": 150000, "level": "Mid"},
    ]
}

# 22. Event calendar
EVENT_CALENDAR = {
    "month": "January 2024",
    "events": [
        {"event_id": "E001", "title": "Team Meeting", "date": "2024-01-16", "time": "10:00", "duration": 60, "attendees": 12, "location": "Conf Room A"},
        {"event_id": "E002", "title": "Product Launch", "date": "2024-01-18", "time": "14:00", "duration": 120, "attendees": 50, "location": "Main Hall"},
        {"event_id": "E003", "title": "Training Session", "date": "2024-01-22", "time": "09:00", "duration": 180, "attendees": 25, "location": "Training Room"},
        {"event_id": "E004", "title": "Client Presentation", "date": "2024-01-25", "time": "15:00", "duration": 90, "attendees": 8, "location": "Virtual"},
    ]
}

# 23. IoT sensor data
IOT_SENSOR_DATA = {
    "device_id": "SENSOR-001",
    "location": "Building A - Floor 3",
    "readings": [
        {"timestamp": "2024-01-15T09:00:00Z", "temperature": 72.5, "humidity": 45, "pressure": 1013.25, "air_quality": 85},
        {"timestamp": "2024-01-15T09:15:00Z", "temperature": 73.1, "humidity": 46, "pressure": 1013.30, "air_quality": 84},
        {"timestamp": "2024-01-15T09:30:00Z", "temperature": 73.8, "humidity": 47, "pressure": 1013.35, "air_quality": 83},
        {"timestamp": "2024-01-15T09:45:00Z", "temperature": 74.2, "humidity": 48, "pressure": 1013.40, "air_quality": 82},
        {"timestamp": "2024-01-15T10:00:00Z", "temperature": 74.6, "humidity": 49, "pressure": 1013.45, "air_quality": 81},
    ]
}

# 24. Network logs
NETWORK_LOGS = {
    "server": "web-prod-01",
    "logs": [
        {"timestamp": "2024-01-15T10:00:01Z", "ip": "192.168.1.100", "method": "GET", "path": "/api/users", "status": 200, "response_time": 45},
        {"timestamp": "2024-01-15T10:00:02Z", "ip": "192.168.1.101", "method": "POST", "path": "/api/orders", "status": 201, "response_time": 120},
        {"timestamp": "2024-01-15T10:00:03Z", "ip": "192.168.1.102", "method": "GET", "path": "/api/products", "status": 200, "response_time": 35},
        {"timestamp": "2024-01-15T10:00:04Z", "ip": "192.168.1.103", "method": "PUT", "path": "/api/users/123", "status": 200, "response_time": 85},
        {"timestamp": "2024-01-15T10:00:05Z", "ip": "192.168.1.104", "method": "DELETE", "path": "/api/sessions", "status": 204, "response_time": 25},
    ]
}

# 25. Payment transactions
PAYMENT_TRANSACTIONS = {
    "merchant_id": "MERCH-12345",
    "transactions": [
        {"txn_id": "T001", "amount": 49.99, "currency": "USD", "method": "credit_card", "status": "completed", "timestamp": "2024-01-15T10:15:00Z"},
        {"txn_id": "T002", "amount": 129.50, "currency": "USD", "method": "paypal", "status": "completed", "timestamp": "2024-01-15T10:18:00Z"},
        {"txn_id": "T003", "amount": 79.99, "currency": "USD", "method": "credit_card", "status": "pending", "timestamp": "2024-01-15T10:20:00Z"},
        {"txn_id": "T004", "amount": 199.00, "currency": "USD", "method": "apple_pay", "status": "completed", "timestamp": "2024-01-15T10:25:00Z"},
        {"txn_id": "T005", "amount": 29.99, "currency": "USD", "method": "credit_card", "status": "failed", "timestamp": "2024-01-15T10:30:00Z"},
    ]
}

# 26. User activity logs
USER_ACTIVITY_LOGS = {
    "user_id": "U12345",
    "activities": [
        {"activity_id": "A001", "action": "login", "timestamp": "2024-01-15T08:00:00Z", "ip": "192.168.1.50", "device": "iPhone", "success": True},
        {"activity_id": "A002", "action": "view_product", "timestamp": "2024-01-15T08:05:00Z", "ip": "192.168.1.50", "device": "iPhone", "success": True},
        {"activity_id": "A003", "action": "add_to_cart", "timestamp": "2024-01-15T08:10:00Z", "ip": "192.168.1.50", "device": "iPhone", "success": True},
        {"activity_id": "A004", "action": "checkout", "timestamp": "2024-01-15T08:15:00Z", "ip": "192.168.1.50", "device": "iPhone", "success": True},
        {"activity_id": "A005", "action": "logout", "timestamp": "2024-01-15T08:20:00Z", "ip": "192.168.1.50", "device": "iPhone", "success": True},
    ]
}

# 27. Email metadata
EMAIL_METADATA = {
    "mailbox": "inbox",
    "emails": [
        {"email_id": "E001", "from": "alice@example.com", "subject": "Project Update", "date": "2024-01-15T09:00:00Z", "size": 15840, "read": True, "flagged": False},
        {"email_id": "E002", "from": "bob@example.com", "subject": "Meeting Reminder", "date": "2024-01-15T10:30:00Z", "size": 8920, "read": True, "flagged": True},
        {"email_id": "E003", "from": "carol@example.com", "subject": "Q4 Report", "date": "2024-01-15T11:45:00Z", "size": 245600, "read": False, "flagged": False},
        {"email_id": "E004", "from": "david@example.com", "subject": "Lunch Plans", "date": "2024-01-15T12:15:00Z", "size": 5120, "read": True, "flagged": False},
    ]
}

# 28. Sales pipeline
SALES_PIPELINE = {
    "quarter": "Q1 2024",
    "opportunities": [
        {"opp_id": "O001", "company": "Acme Corp", "value": 50000, "stage": "Proposal", "probability": 60, "close_date": "2024-02-15"},
        {"opp_id": "O002", "company": "TechStart Inc", "value": 125000, "stage": "Negotiation", "probability": 80, "close_date": "2024-02-20"},
        {"opp_id": "O003", "company": "Global Solutions", "value": 75000, "stage": "Discovery", "probability": 40, "close_date": "2024-03-10"},
        {"opp_id": "O004", "company": "Enterprise LLC", "value": 200000, "stage": "Closed Won", "probability": 100, "close_date": "2024-01-30"},
    ]
}

# 29. Support tickets
SUPPORT_TICKETS = {
    "queue": "technical_support",
    "tickets": [
        {"ticket_id": "T001", "customer": "John Doe", "subject": "Login Issue", "priority": "High", "status": "Open", "created": "2024-01-15T08:00:00Z"},
        {"ticket_id": "T002", "customer": "Jane Smith", "subject": "Payment Failed", "priority": "Critical", "status": "In Progress", "created": "2024-01-15T09:15:00Z"},
        {"ticket_id": "T003", "customer": "Bob Wilson", "subject": "Feature Request", "priority": "Low", "status": "Open", "created": "2024-01-15T10:30:00Z"},
        {"ticket_id": "T004", "customer": "Alice Brown", "subject": "Bug Report", "priority": "Medium", "status": "Resolved", "created": "2024-01-15T11:45:00Z"},
    ]
}

# 30. Project tasks
PROJECT_TASKS = {
    "project": "Website Redesign",
    "tasks": [
        {"task_id": "T001", "title": "Design Homepage", "assignee": "Alice", "status": "Completed", "priority": "High", "estimated_hours": 16, "actual_hours": 14},
        {"task_id": "T002", "title": "Implement Navigation", "assignee": "Bob", "status": "In Progress", "priority": "High", "estimated_hours": 8, "actual_hours": 6},
        {"task_id": "T003", "title": "Create Content", "assignee": "Carol", "status": "Not Started", "priority": "Medium", "estimated_hours": 12, "actual_hours": 0},
        {"task_id": "T004", "title": "Test Responsive Design", "assignee": "David", "status": "Not Started", "priority": "Medium", "estimated_hours": 6, "actual_hours": 0},
    ]
}

# 31. Time series metrics
TIME_SERIES_METRICS = {
    "metric": "cpu_usage",
    "host": "server-01",
    "data_points": [
        {"timestamp": "2024-01-15T10:00:00Z", "value": 45.2, "min": 42.1, "max": 48.5, "avg": 45.0},
        {"timestamp": "2024-01-15T10:01:00Z", "value": 46.8, "min": 43.2, "max": 49.1, "avg": 46.5},
        {"timestamp": "2024-01-15T10:02:00Z", "value": 44.5, "min": 41.8, "max": 47.2, "avg": 44.3},
        {"timestamp": "2024-01-15T10:03:00Z", "value": 48.1, "min": 44.5, "max": 51.0, "avg": 47.8},
        {"timestamp": "2024-01-15T10:04:00Z", "value": 43.9, "min": 40.5, "max": 46.8, "avg": 43.7},
    ]
}

# 32. A/B test results
AB_TEST_RESULTS = {
    "experiment": "Homepage CTA Button Color",
    "variants": [
        {"variant": "Control", "impressions": 10000, "clicks": 320, "conversions": 45, "ctr": 3.2, "cvr": 0.45, "revenue": 4500.00},
        {"variant": "Blue Button", "impressions": 10200, "clicks": 385, "conversions": 58, "ctr": 3.77, "cvr": 0.57, "revenue": 5800.00},
        {"variant": "Green Button", "impressions": 9900, "clicks": 350, "conversions": 52, "ctr": 3.54, "cvr": 0.53, "revenue": 5200.00},
    ]
}

# 33. Survey responses
SURVEY_RESPONSES = {
    "survey": "Customer Satisfaction Q1 2024",
    "responses": [
        {"response_id": "R001", "age_group": "25-34", "satisfaction": 8, "recommend": True, "support_rating": 9, "product_rating": 8},
        {"response_id": "R002", "age_group": "35-44", "satisfaction": 7, "recommend": True, "support_rating": 7, "product_rating": 8},
        {"response_id": "R003", "age_group": "18-24", "satisfaction": 9, "recommend": True, "support_rating": 10, "product_rating": 9},
        {"response_id": "R004", "age_group": "45-54", "satisfaction": 6, "recommend": False, "support_rating": 6, "product_rating": 7},
        {"response_id": "R005", "age_group": "25-34", "satisfaction": 8, "recommend": True, "support_rating": 8, "product_rating": 9},
    ]
}

# 34. Geographic data
GEOGRAPHIC_DATA = {
    "region": "West Coast",
    "cities": [
        {"city": "San Francisco", "state": "CA", "population": 873965, "area_sqmi": 46.9, "density": 18633, "elevation": 52},
        {"city": "Los Angeles", "state": "CA", "population": 3979576, "area_sqmi": 468.7, "density": 8485, "elevation": 305},
        {"city": "Seattle", "state": "WA", "population": 753675, "area_sqmi": 83.8, "density": 8995, "elevation": 175},
        {"city": "Portland", "state": "OR", "population": 652503, "area_sqmi": 133.4, "density": 4890, "elevation": 50},
        {"city": "San Diego", "state": "CA", "population": 1423851, "area_sqmi": 325.2, "density": 4378, "elevation": 62},
    ]
}

# 35. Product recommendations
PRODUCT_RECOMMENDATIONS = {
    "user_id": "U54321",
    "recommendations": [
        {"product_id": "P001", "name": "Wireless Earbuds", "score": 0.92, "reason": "Based on purchase history", "price": 79.99},
        {"product_id": "P002", "name": "Phone Case", "score": 0.87, "reason": "Frequently bought together", "price": 19.99},
        {"product_id": "P003", "name": "Screen Protector", "score": 0.85, "reason": "Customers also viewed", "price": 12.99},
        {"product_id": "P004", "name": "Charging Cable", "score": 0.82, "reason": "Based on browsing history", "price": 14.99},
    ]
}

# 36. Search results
SEARCH_RESULTS = {
    "query": "wireless keyboard",
    "total_results": 1247,
    "results": [
        {"result_id": "R001", "title": "Logitech Wireless Keyboard", "price": 49.99, "rating": 4.5, "reviews": 2340, "in_stock": True},
        {"result_id": "R002", "title": "Apple Magic Keyboard", "price": 99.00, "rating": 4.8, "reviews": 5670, "in_stock": True},
        {"result_id": "R003", "title": "Microsoft Wireless Keyboard", "price": 59.99, "rating": 4.3, "reviews": 1890, "in_stock": False},
        {"result_id": "R004", "title": "Razer Wireless Gaming Keyboard", "price": 149.99, "rating": 4.6, "reviews": 3210, "in_stock": True},
    ]
}

# 37. Shopping cart
SHOPPING_CART = {
    "cart_id": "CART-12345",
    "user_id": "U98765",
    "items": [
        {"item_id": "I001", "product_id": "P123", "name": "Laptop", "quantity": 1, "unit_price": 1299.99, "total": 1299.99},
        {"item_id": "I002", "product_id": "P456", "name": "Mouse", "quantity": 2, "unit_price": 29.99, "total": 59.98},
        {"item_id": "I003", "product_id": "P789", "name": "Keyboard", "quantity": 1, "unit_price": 149.99, "total": 149.99},
    ],
    "subtotal": 1509.96,
    "tax": 120.80,
    "shipping": 0.00,
    "total": 1630.76
}

# 38. Order history
ORDER_HISTORY = {
    "customer_id": "C45678",
    "orders": [
        {"order_id": "O001", "date": "2024-01-10", "items": 3, "total": 249.97, "status": "Delivered", "tracking": "TRK123456"},
        {"order_id": "O002", "date": "2024-01-05", "items": 1, "total": 1299.99, "status": "Delivered", "tracking": "TRK234567"},
        {"order_id": "O003", "date": "2023-12-28", "items": 5, "total": 459.95, "status": "Delivered", "tracking": "TRK345678"},
        {"order_id": "O004", "date": "2023-12-15", "items": 2, "total": 179.98, "status": "Returned", "tracking": "TRK456789"},
    ]
}

# 39. Shipping tracking
SHIPPING_TRACKING = {
    "tracking_number": "TRK123456789",
    "carrier": "FedEx",
    "status": "In Transit",
    "events": [
        {"timestamp": "2024-01-15T08:00:00Z", "location": "San Francisco, CA", "status": "Picked Up", "description": "Package picked up by carrier"},
        {"timestamp": "2024-01-15T12:00:00Z", "location": "Oakland, CA", "status": "In Transit", "description": "Arrived at sorting facility"},
        {"timestamp": "2024-01-15T18:00:00Z", "location": "Sacramento, CA", "status": "In Transit", "description": "Departed sorting facility"},
        {"timestamp": "2024-01-16T06:00:00Z", "location": "Reno, NV", "status": "In Transit", "description": "In transit to next facility"},
    ]
}

# 40. Inventory alerts
INVENTORY_ALERTS = {
    "warehouse": "WH-WEST-01",
    "alerts": [
        {"alert_id": "A001", "sku": "PROD-1234", "name": "Wireless Mouse", "current_stock": 5, "threshold": 20, "severity": "High", "action": "Reorder"},
        {"alert_id": "A002", "sku": "PROD-5678", "name": "USB Cable", "current_stock": 12, "threshold": 50, "severity": "Medium", "action": "Review"},
        {"alert_id": "A003", "sku": "PROD-9012", "name": "Keyboard", "current_stock": 2, "threshold": 15, "severity": "Critical", "action": "Urgent Reorder"},
    ]
}

# 41. Performance metrics
PERFORMANCE_METRICS = {
    "service": "api-gateway",
    "period": "last_hour",
    "metrics": [
        {"metric": "requests_per_second", "current": 1250, "average": 1180, "peak": 1580, "threshold": 2000},
        {"metric": "latency_ms", "current": 45, "average": 42, "peak": 89, "threshold": 100},
        {"metric": "error_rate", "current": 0.12, "average": 0.15, "peak": 0.45, "threshold": 1.0},
        {"metric": "cpu_usage", "current": 65, "average": 62, "peak": 78, "threshold": 85},
        {"metric": "memory_usage", "current": 72, "average": 70, "peak": 82, "threshold": 90},
    ]
}

# 42. Error logs
ERROR_LOGS = {
    "application": "web-app",
    "timeframe": "last_24_hours",
    "errors": [
        {"error_id": "E001", "timestamp": "2024-01-15T10:15:23Z", "level": "ERROR", "message": "Database connection timeout", "count": 3, "first_seen": "2024-01-15T08:00:00Z"},
        {"error_id": "E002", "timestamp": "2024-01-15T11:30:45Z", "level": "WARNING", "message": "High memory usage detected", "count": 12, "first_seen": "2024-01-15T09:30:00Z"},
        {"error_id": "E003", "timestamp": "2024-01-15T12:45:12Z", "level": "CRITICAL", "message": "Service unavailable", "count": 1, "first_seen": "2024-01-15T12:45:12Z"},
    ]
}

# 43. Audit trail
AUDIT_TRAIL = {
    "resource": "user_accounts",
    "entries": [
        {"audit_id": "A001", "timestamp": "2024-01-15T09:00:00Z", "user": "admin", "action": "CREATE", "resource_id": "U123", "ip": "192.168.1.1"},
        {"audit_id": "A002", "timestamp": "2024-01-15T10:15:00Z", "user": "manager", "action": "UPDATE", "resource_id": "U456", "ip": "192.168.1.2"},
        {"audit_id": "A003", "timestamp": "2024-01-15T11:30:00Z", "user": "admin", "action": "DELETE", "resource_id": "U789", "ip": "192.168.1.1"},
        {"audit_id": "A004", "timestamp": "2024-01-15T12:45:00Z", "user": "operator", "action": "UPDATE", "resource_id": "U234", "ip": "192.168.1.3"},
    ]
}

# 44. Notification queue
NOTIFICATION_QUEUE = {
    "queue_name": "email_notifications",
    "notifications": [
        {"notif_id": "N001", "user_id": "U123", "type": "order_confirmation", "priority": "Normal", "status": "Pending", "created": "2024-01-15T10:00:00Z"},
        {"notif_id": "N002", "user_id": "U456", "type": "password_reset", "priority": "High", "status": "Sent", "created": "2024-01-15T10:15:00Z"},
        {"notif_id": "N003", "user_id": "U789", "type": "promotional", "priority": "Low", "status": "Pending", "created": "2024-01-15T10:30:00Z"},
        {"notif_id": "N004", "user_id": "U234", "type": "security_alert", "priority": "Critical", "status": "Sent", "created": "2024-01-15T10:45:00Z"},
    ]
}

# 45. Chat messages
CHAT_MESSAGES = {
    "conversation_id": "CONV-12345",
    "participants": ["alice", "bob"],
    "messages": [
        {"msg_id": "M001", "sender": "alice", "timestamp": "2024-01-15T10:00:00Z", "text": "Hey, did you finish the report?", "read": True},
        {"msg_id": "M002", "sender": "bob", "timestamp": "2024-01-15T10:02:00Z", "text": "Almost done, just reviewing it now", "read": True},
        {"msg_id": "M003", "sender": "alice", "timestamp": "2024-01-15T10:03:00Z", "text": "Great, can you send it by 2pm?", "read": True},
        {"msg_id": "M004", "sender": "bob", "timestamp": "2024-01-15T10:05:00Z", "text": "Sure, will do!", "read": False},
    ]
}

# 46. Video metadata
VIDEO_METADATA = {
    "channel": "TechReviews",
    "videos": [
        {"video_id": "V001", "title": "iPhone 15 Review", "duration": 720, "views": 1250000, "likes": 45000, "published": "2024-01-10", "resolution": "4K"},
        {"video_id": "V002", "title": "Best Laptops 2024", "duration": 900, "views": 890000, "likes": 32000, "published": "2024-01-12", "resolution": "1080p"},
        {"video_id": "V003", "title": "Samsung Galaxy Review", "duration": 680, "views": 1100000, "likes": 38000, "published": "2024-01-14", "resolution": "4K"},
    ]
}

# 47. Blog posts
BLOG_POSTS = {
    "blog": "Tech Insights",
    "posts": [
        {"post_id": "P001", "title": "The Future of AI", "author": "Jane Doe", "date": "2024-01-10", "views": 5600, "comments": 45, "category": "AI"},
        {"post_id": "P002", "title": "Web Development Trends", "author": "John Smith", "date": "2024-01-12", "views": 4200, "comments": 32, "category": "WebDev"},
        {"post_id": "P003", "title": "Cloud Computing Best Practices", "author": "Alice Johnson", "date": "2024-01-14", "views": 3800, "comments": 28, "category": "Cloud"},
    ]
}

# 48. Comments thread
COMMENTS_THREAD = {
    "post_id": "P001",
    "comments": [
        {"comment_id": "C001", "author": "user123", "timestamp": "2024-01-11T10:00:00Z", "text": "Great article!", "upvotes": 12, "downvotes": 0},
        {"comment_id": "C002", "author": "user456", "timestamp": "2024-01-11T11:30:00Z", "text": "Very informative, thanks!", "upvotes": 8, "downvotes": 1},
        {"comment_id": "C003", "author": "user789", "timestamp": "2024-01-11T13:15:00Z", "text": "Could you elaborate on section 3?", "upvotes": 5, "downvotes": 0},
        {"comment_id": "C004", "author": "user234", "timestamp": "2024-01-11T15:45:00Z", "text": "I disagree with this point", "upvotes": 2, "downvotes": 4},
    ]
}

# 49. User profiles
USER_PROFILES = {
    "platform": "SocialNet",
    "profiles": [
        {"user_id": "U001", "username": "alice_tech", "followers": 15400, "following": 342, "posts": 1250, "verified": True, "joined": "2020-03-15"},
        {"user_id": "U002", "username": "bob_dev", "followers": 8900, "following": 567, "posts": 890, "verified": False, "joined": "2021-07-22"},
        {"user_id": "U003", "username": "carol_design", "followers": 23500, "following": 234, "posts": 1890, "verified": True, "joined": "2019-11-05"},
        {"user_id": "U004", "username": "david_writer", "followers": 12300, "following": 456, "posts": 2340, "verified": True, "joined": "2020-08-18"},
    ]
}

# 50. API request log
API_REQUEST_LOG = {
    "api": "public-api-v2",
    "date": "2024-01-15",
    "requests": [
        {"request_id": "R001", "endpoint": "/api/users", "method": "GET", "status": 200, "duration_ms": 45, "client_id": "client_123", "timestamp": "10:00:00"},
        {"request_id": "R002", "endpoint": "/api/products", "method": "GET", "status": 200, "duration_ms": 32, "client_id": "client_456", "timestamp": "10:01:15"},
        {"request_id": "R003", "endpoint": "/api/orders", "method": "POST", "status": 201, "duration_ms": 120, "client_id": "client_123", "timestamp": "10:02:30"},
        {"request_id": "R004", "endpoint": "/api/users/123", "method": "PUT", "status": 200, "duration_ms": 78, "client_id": "client_789", "timestamp": "10:03:45"},
        {"request_id": "R005", "endpoint": "/api/analytics", "method": "GET", "status": 200, "duration_ms": 156, "client_id": "client_456", "timestamp": "10:05:00"},
    ]
}

# All 50 datasets
DATASETS = {
    "01. E-commerce Products": ECOMMERCE_PRODUCTS,
    "02. API Response": API_RESPONSE,
    "03. Database Results": DATABASE_RESULTS,
    "04. ML Training Data": ML_TRAINING_DATA,
    "05. Server Configuration": SERVER_CONFIG,
    "06. Analytics Data": ANALYTICS_DATA,
    "07. Large Inventory (100 items)": LARGE_INVENTORY,
    "08. Customer Reviews": CUSTOMER_REVIEWS,
    "09. Social Media Posts": SOCIAL_MEDIA_POSTS,
    "10. Weather Forecast": WEATHER_FORECAST,
    "11. Stock Market Data": STOCK_MARKET_DATA,
    "12. Restaurant Menu": RESTAURANT_MENU,
    "13. Hotel Bookings": HOTEL_BOOKINGS,
    "14. Flight Schedule": FLIGHT_SCHEDULE,
    "15. Medical Records": MEDICAL_RECORDS,
    "16. Student Grades": STUDENT_GRADES,
    "17. Sports Statistics": SPORTS_STATISTICS,
    "18. Movie Catalog": MOVIE_CATALOG,
    "19. Music Playlist": MUSIC_PLAYLIST,
    "20. Real Estate Listings": REAL_ESTATE_LISTINGS,
    "21. Job Postings": JOB_POSTINGS,
    "22. Event Calendar": EVENT_CALENDAR,
    "23. IoT Sensor Data": IOT_SENSOR_DATA,
    "24. Network Logs": NETWORK_LOGS,
    "25. Payment Transactions": PAYMENT_TRANSACTIONS,
    "26. User Activity Logs": USER_ACTIVITY_LOGS,
    "27. Email Metadata": EMAIL_METADATA,
    "28. Sales Pipeline": SALES_PIPELINE,
    "29. Support Tickets": SUPPORT_TICKETS,
    "30. Project Tasks": PROJECT_TASKS,
    "31. Time Series Metrics": TIME_SERIES_METRICS,
    "32. A/B Test Results": AB_TEST_RESULTS,
    "33. Survey Responses": SURVEY_RESPONSES,
    "34. Geographic Data": GEOGRAPHIC_DATA,
    "35. Product Recommendations": PRODUCT_RECOMMENDATIONS,
    "36. Search Results": SEARCH_RESULTS,
    "37. Shopping Cart": SHOPPING_CART,
    "38. Order History": ORDER_HISTORY,
    "39. Shipping Tracking": SHIPPING_TRACKING,
    "40. Inventory Alerts": INVENTORY_ALERTS,
    "41. Performance Metrics": PERFORMANCE_METRICS,
    "42. Error Logs": ERROR_LOGS,
    "43. Audit Trail": AUDIT_TRAIL,
    "44. Notification Queue": NOTIFICATION_QUEUE,
    "45. Chat Messages": CHAT_MESSAGES,
    "46. Video Metadata": VIDEO_METADATA,
    "47. Blog Posts": BLOG_POSTS,
    "48. Comments Thread": COMMENTS_THREAD,
    "49. User Profiles": USER_PROFILES,
    "50. API Request Log": API_REQUEST_LOG,
}
