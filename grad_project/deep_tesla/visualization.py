from keras.utils import plot_model
import utils
import params

models = ['benchmark_model', 'my_model', 'my_refined_model']
for model_name in models:
    model_path = utils.join_dir(params.model_dir, '{}.json'.format(model_name))
    with open(model_path, 'r') as in_file:
        json_model = in_file.read()
        model = utils.model_from_json(json_model)
    plot_model(model, to_file='./graphs/{}.png'.format(model_name))
