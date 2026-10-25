# horovod_tf_training.py
import tensorflow as tf
import horovod.tensorflow as hvd
import time

# 1. Initialize Horovod
hvd.init()
print(f"[Worker Rank {hvd.rank()}/{hvd.size()}] Initialized Horovod process.")

# 2. Pin to CPU/GPU threads
tf.config.threading.set_inter_op_parallelism_threads(2)
tf.config.threading.set_intra_op_parallelism_threads(4)

# 3. Create Synthetic Dataset
(x_train, y_train), _ = tf.keras.datasets.mnist.load_data()
x_train = x_train[..., tf.newaxis] / 255.0

# Partition dataset shards across workers
dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))
dataset = dataset.shard(num_shards=hvd.size(), index=hvd.rank())
dataset = dataset.shuffle(1000).batch(64)

# 4. Define Deep Learning Model
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, 3, activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10)
])

# 5. Scale learning rate with cluster worker count
scaled_lr = 0.001 * hvd.size()
opt = tf.keras.optimizers.Adam(scaled_lr)

# 6. Wrap with DistributedOptimizer (Performs Ring-AllReduce)
opt = hvd.DistributedOptimizer(opt)

model.compile(
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=opt,
    metrics=['accuracy'],
    experimental_run_tf_function=False
)

# 7. Broadcast initial random weights from Rank 0
callbacks = [
    hvd.callbacks.BroadcastGlobalVariablesCallback(0),
    hvd.callbacks.MetricAverageCallback()
]

# Only Rank 0 saves checkpoints and prints progress
verbose = 1 if hvd.rank() == 0 else 0

t0 = time.time()
model.fit(dataset.take(50), epochs=1, callbacks=callbacks, verbose=verbose)
if hvd.rank() == 0:
    print(f"[Master Rank 0] Distributed Training Step Completed in: {time.time() - t0:.2f}s")
