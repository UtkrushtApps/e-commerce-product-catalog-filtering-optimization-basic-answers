# Solution Steps

1. Review the current schema: The products table must have columns category_id and brand_id, but likely lacks the right indexes for efficient filtering on both.

2. Create a database migration script to add indexes. The most important is a composite index on (category_id, brand_id), as users frequently filter by both.

3. Optionally, also add single-column indexes on category_id and brand_id if not already present (but composite handles most queries for the combined filter best).

4. Implement the SQL migration file to add (and, if present, drop/recreate) these indexes.

5. Review the Python DB query logic in the repository. Make sure that both filters are applied directly in the SQL query with WHERE clauses, not in Python after fetching rows.

6. (No changes are required to the endpoint logic, as the query now uses optimized indexes automatically.)

7. Update documentation/comments in the code to note that filtering now has efficient database support.

8. After deploying the migration, ensure the query plan confirms index usage (EXPLAIN), and validate API latency has dropped to near-instant.

