from model_service import ModelService


def test_transcribe(mocker):
    class MockInference:
        def __init__(self, model_dict):
            self.model_dict = model_dict

        def get_inference(self, file_name, language):
            return {'transcription': 'hello'}

    mocker.patch('model_service.InferenceService', MockInference)
    model_dict_path = 'model_dict.json'
    model = ModelService(model_dict_path)
    file_name = 'test.wav'
    language = 'hi'
    result = model.transcribe(file_name, language)
    print(result)