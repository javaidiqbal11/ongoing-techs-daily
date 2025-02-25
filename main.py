from pymilvus import Collection, CollectionSchema, FieldSchema, DataType, connections
import random
import numpy as np

# Step 1: Connect to Milvus
connections.connect("default", host="localhost", port="19530")  # Adjust host/port if needed

# Step 2: Define Collection Schema
collection_name = "test_collection"
id_field = FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True)
vector_field = FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=128)

schema = CollectionSchema(fields=[id_field, vector_field], description="Test vector collection")

# Step 3: Create Collection
if collection_name in [col.name for col in Collection.list()]:
    Collection(name=collection_name).drop()  # Drop existing collection for a clean start

collection = Collection(name=collection_name, schema=schema)

# Step 4: Insert Sample Data
num_vectors = 100
vectors = np.random.rand(num_vectors, 128).tolist()  # Generate 100 random 128-dimensional vectors

collection.insert([vectors])  # Insert vectors
collection.load()  # Load the collection for querying

# Step 5: Create Index
collection.create_index(
    field_name="embedding",
    index_params={
        "metric_type": "L2",  # Euclidean distance
        "index_type": "IVF_FLAT",
        "params": {"nlist": 10}
    }
)

# Step 6: Similarity Search
query_vector = np.random.rand(1, 128).tolist()  # Query with a new random vector

search_params = {"metric_type": "L2", "params": {"nprobe": 5}}
results = collection.search(
    data=query_vector,
    anns_field="embedding",
    param=search_params,
    limit=5  # Return top 5 similar vectors
)

# Step 7: Display Results
for hits in results:
    for hit in hits:
        print(f"ID: {hit.id}, Distance: {hit.distance}")
