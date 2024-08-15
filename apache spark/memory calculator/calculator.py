from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    ram_size = float(request.form['ram_size'])
    cores_per_node = int(request.form['cores_per_node'])
    cores_per_executor = int(request.form['cores_per_executor'])
    number_of_nodes = int(request.form['number_of_nodes'])
    memory_overhead = float(request.form.get('memory_overhead', 0.1))

    total_cores = (number_of_nodes * cores_per_node) - number_of_nodes
    total_memory_overhead = ((memory_overhead / 100) * ram_size ) * number_of_nodes
    total_available_memory =  (ram_size * number_of_nodes ) - total_memory_overhead
    num_executors = round(cores_per_node / cores_per_executor) #--
    memory_per_executor = total_available_memory / (num_executors * number_of_nodes)
    total_number_of_executors= total_available_memory/memory_per_executor
    number_of_executor_pernode=round(total_number_of_executors/number_of_nodes) #--
    driver_memory = ram_size * 0.2

    parallelism = num_executors * cores_per_node
    shuffle_parallelism = int(parallelism * 1.5)


    return render_template('output.html',
                           total_cores =total_cores,
                           total_memory_overhead=total_memory_overhead,
                           total_available_memory=total_available_memory,
                           num_executors=num_executors,
                           cores_per_executor=cores_per_executor,
                           memory_per_executor=memory_per_executor,
                           total_number_of_executors=total_number_of_executors,
                           number_of_executor_pernode=number_of_executor_pernode,
                           driver_memory=driver_memory,
                           cores_per_node=cores_per_node,
                           parallelism=parallelism,
                           shuffle_parallelism=shuffle_parallelism)

if __name__ == '__main__':
    app.run(debug=True)