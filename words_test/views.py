from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils.word_test_utils import Word_Utils

@csrf_exempt
def analyze_phrase(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        phrase = data.get('phrase', '')
        word_utils = Word_Utils()
        result = word_utils.to_json(phrase)
        return JsonResponse(result)
    return JsonResponse({'error': 'Invalid request method'}, status=400)
