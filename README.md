# Region Based Rotation

# Problem Statement

The objective of this project is to design a Dynamic Question Assignment System that assigns region-specific questions to users on a weekly cycle. Each cycle spans one week, after which a new question is assigned based on the configured cycle duration. Users from different regions (e.g., Singapore and the US) will receive distinct sets of questions, ensuring that all users within the same region are assigned the same question.

Question Sets
Singapore: [1, 2, 3, 4, 5, ..., N]
Cycle 1 (Week 1): Assign question 1
Cycle 2 (Week 2): Assign question 2
...
Cycle N (Week N): Assign question N
US: [6, 7, 8, 9, 10, ..., N]
Cycle 1 (Week 1): Assign question 6
Cycle 2 (Week 2): Assign question 7
...
Cycle N (Week N): Assign question N

# Solution Architecture

To implement the solution, we chose a Flask-based API that will serve as the backend for handling question assignments. The architecture is designed to accommodate the following requirements:

API Endpoints: Create endpoints to fetch questions based on the user’s region.
Dynamic Assignment: Implement logic to dynamically assign questions based on the current cycle and region.
Caching: Utilize caching mechanisms to improve performance and response times, particularly for frequently accessed data.
Technology Stack
Framework: Flask for building the RESTful API.
Database: A simple in-memory structure for this implementation, with future potential for a more robust database solution (e.g., PostgreSQL, MongoDB).
Caching: Flask-Caching for temporary storage of frequently requested data.

# Implementation

The implementation includes the following steps:

API Development: Developed endpoints to handle GET requests for questions based on region.
Cycle Management: Built logic to determine which question to assign based on the current date and time, ensuring that assignments align with the weekly cycle.
Testing: Conducted tests on the API endpoints to verify functionality, including checking for valid and invalid regions.
Example Endpoint
GET /api/v1/question/<region>
Parameters: region (e.g., Singapore, US)
Response: Returns the question assigned for the current cycle in the specified region.

# Scalability Considerations

To meet the scalability requirement of handling 100,000 daily active users and supporting millions globally, we implemented several strategies:

Caching: The use of Flask-Caching helps reduce server load by storing frequently accessed data, which can significantly enhance performance during peak usage times.
Load Balancing: In a production environment, using load balancers would distribute incoming requests across multiple server instances, allowing for better resource management and reliability.
Database Optimization: Future plans involve integrating a scalable database solution to manage a larger question set and provide more complex query capabilities.
Horizontal Scaling: The architecture allows for horizontal scaling, where additional instances of the application can be deployed to handle increased load.

# Pros and Cons
Pros:

Modular Design: Easy to extend with additional regions or cycle configurations.
Scalability: Suitable for a high number of users by leveraging caching and database partitioning.
Flexibility: Cycle duration and start time are configurable.

Cons:

Database Complexity: Requires careful management of regional data partitions.
Cache Invalidation: Cache updates during cycle changes can be tricky, needing careful synchronization.
Timezone Handling: Accurate cycle management requires careful handling of timezones.

# Conclusion

The Dynamic Question Assignment System provides a robust framework for region-specific question assignments, adhering to the requirements outlined in the task description. While the current implementation meets the basic functionality, further enhancements can be made to ensure scalability and efficiency in handling large user bases. This write-up serves as a comprehensive overview of the project, detailing the architecture, implementation, and considerations for future growth.