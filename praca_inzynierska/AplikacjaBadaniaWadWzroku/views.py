from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.views.i18n import get_language
from .models import *
from .dpi_calculator import calculate_dpi, calculate_pixel_ratio



def index(request):
    return render(request, 'AplikacjaBadaniaWadWzroku/index1.html')


def tests(request):
    tests_ru = {"Астигматизм": "astigmatism", "Дальтонизм": "color_blindness", "Острота зрения": "visual_acuity", "Макулодистрофия": "macular_degeneration", "Синдром сухого глаза": "dry_eye"}
    tests_pl = {"Astygmatyzm": "astigmatism", "Daltonizm": "color_blindness", "Ostrość wzroku": "visual_acuity",
                "Zwyrodnienie plamki żółtej": "macular_degeneration", "Zespół suchego oka": "dry_eye"}
    if get_language() == 'ru':
        context = {'tests': tests_ru, 'eye': 'right', 'current_result': ' '}
    elif get_language() == 'pl':
        context = {'tests': tests_pl, 'eye': 'right', 'current_result': ' '}
    return render(request, 'AplikacjaBadaniaWadWzroku/tests_menu.html', context)


def exercises(request):
    exercises_context = Exercises.objects.filter()
    context = {'exercises_context': exercises_context}
    return render(request, 'AplikacjaBadaniaWadWzroku/exercises.html', context)


def information_diseases(request):
    diseases_ru = {"Астигматизм": "astigmatism", "Дальтонизм": "color_blindness",
                "Макулодистрофия": "macular_degeneration", "Синдром сухого глаза": "dry_eye"}
    diseases_pl = {"Astygmatyzm": "astigmatism", "Daltonizm": "color_blindness",
                "Zwyrodnienie plamki żółtej": "macular_degeneration", "Zespół suchego oka": "dry_eye"}
    if get_language() == 'ru':
        context = {'diseases': diseases_ru}
    elif get_language() == 'pl':
        context = {'diseases': diseases_pl}
    return render(request, 'AplikacjaBadaniaWadWzroku/information_diseases_menu.html', context)


def information_diseases_all(request, value):
    disease_information = Information1.objects.get(disease=value)
    test_name = disease_information.disease_name
    disease_description = disease_information.disease_information
    disease_symptoms = disease_information.disease_symptoms.split(';')
    disease_treatment = disease_information.disease_treatment.split(';')
    context = {'disease_description': disease_description, 'test': test_name, 'disease_symptoms': disease_symptoms,
               'disease_treatment': disease_treatment}

    return render(request, 'AplikacjaBadaniaWadWzroku/information_diseases.html', context)


def test_visual_acuity(request, eye, current_result):
    snellen_test = Test.objects.filter(test="snellen")
    if get_language() == 'ru':
        header_text = "Тест остроты зрения"
    elif get_language() == 'pl':
        header_text = "Test ostrości wzroku"
    snellen_test_redirect = "snellen_test"
    print(calculate_dpi())
    letter_size_px_list = []
    print(calculate_pixel_ratio())
    for test in snellen_test:
        letter_size_px = calculate_dpi() * test.size / 25.4
        letter_size_px_list.append(round(letter_size_px))
    print(letter_size_px_list)
    if request.method == 'POST':
        test_result = ''
        for test in snellen_test:
            selected_option = request.POST['question-{}-answers'.format(test.question_number)]
            if selected_option == test.answer:
                test_result += '1'
            elif selected_option != test.answer:
                test_result += '0'


        print(test_result)
        current_result += test_result
        print(current_result)
        print(eye)
        if eye == 'right':
            return redirect(test_visual_acuity, eye='left', current_result=current_result)
        elif eye == 'left':
            return redirect(results, result=current_result, test=snellen_test_redirect)
    context = {'test_database': snellen_test, 'header_text': header_text, 'letter_size_px_list': letter_size_px_list}
    return render(request, 'AplikacjaBadaniaWadWzroku/tests.html', context)


def test_astigmatism(request):
    astigmatism_test = Test.objects.filter(test="astigmatism")
    if get_language() == 'ru':
        header_text = "Тест на астигматизм"
    elif get_language() == 'pl':
        header_text = "Test astygmatyzmu"
    score_list = []
    astigmatism_test_redirect = "astigmatism"
    if request.method == 'POST':
        for test in astigmatism_test:
            selected_option = request.POST['question-{}-answers'.format(test.question_number)]
            if selected_option == test.option_two:
                if get_language() == 'ru':
                    score_list.append("В Вашем случае наличие астигматизма маловероятно")
                elif get_language() == 'pl':
                    score_list.append("Masz małe prawdopodobieństwo posiadania astygmatyzmu")
            elif selected_option != test.option_two:
                if get_language() == 'ru':
                    score_list.append("У Вас большая вероятность наличия астигматизма")
                elif get_language() == 'pl':
                    score_list.append("Masz duże prawdopodobieństwo posiadania astygmatyzmu")
        if "У Вас большая вероятность наличия астигматизма" in score_list:
            test_results = "У Вас большая вероятность наличия астигматизма"
        elif "Masz duże prawdopodobieństwo posiadania astygmatyzmu" in score_list:
            test_results = "Masz duże prawdopodobieństwo posiadania astygmatyzmu"
        elif get_language() == 'pl' and "Masz duże prawdopodobieństwo posiadania astygmatyzmu" not in score_list:
            test_results = "Masz małe prawdopodobieństwo posiadania astygmatyzmu"
        else:
            test_results = "В Вашем случае наличие астигматизма маловероятно"
        return redirect(results, result=test_results, test=astigmatism_test_redirect)
    context = {'test_database': astigmatism_test, 'header_text': header_text}
    return render(request, 'AplikacjaBadaniaWadWzroku/tests.html', context)


def test_color_blindness(request):
    ishihara_test = Test.objects.filter(test="Ishihara")
    ishihara_test_redirect = "ishihara"
    if get_language() == 'ru':
        header_text = "Тест на дальтонизм"
    elif get_language() == 'pl':
        header_text = "Test daltonizmu"
    test_results = 0
    if request.method == 'POST':
        for test in ishihara_test:
            selected_option = request.POST['question-{}-answers'.format(test.question_number)]
            if selected_option == test.answer:
                test_results += 1
        print(test_results)
        return redirect(results, result=test_results, test=ishihara_test_redirect)
    context = {'test_database': ishihara_test, 'header_text': header_text}
    return render(request, 'AplikacjaBadaniaWadWzroku/tests.html', context)


def test_macular_degeneration(request):
    macular_degeneration_test = Test.objects.filter(test="macular_degeneration")
    macular_degeneration_test_redirect = "macular_degeneration"
    if get_language() == 'ru':
        header_text = "Тест на макулодистрофию"
    elif get_language() == 'pl':
        header_text = "Test plamki żółtej"
    test_results = ""
    image_size = calculate_dpi() * 100 / 25.4 / 1.5
    image_size_px = round(image_size)
    print(image_size_px)
    if request.method == 'POST':
        for test in macular_degeneration_test:
            selected_option = request.POST['question-{}-answers'.format(test.question_number)]
            if selected_option == test.option_four:
                if get_language() == 'ru':
                    test_results = "В Вашем случае наличие макулодистрофии маловероятно"
                elif get_language() == 'pl':
                    test_results = "Masz małe prawdopodobieństwo posiadania zwyrodnienia plamki żółtej"
            elif selected_option != test.option_four:
                if get_language() == 'ru':
                    test_results = "У Вас большая вероятность наличия макулодистрофии"
                elif get_language() == 'pl':
                    test_results = "Masz duże prawdopodobieństwo posiadania zwyrodnienia plamki żółtej"
        print(test_results)
        return redirect(results, result=test_results, test=macular_degeneration_test_redirect)
    context = {'test_database': macular_degeneration_test, 'header_text': header_text, 'image_size_px': image_size_px}
    return render(request, 'AplikacjaBadaniaWadWzroku/tests.html', context)


def test_dry_eye(request):
    dry_eye_test = Test.objects.filter(test = "dry eye")
    test_results = 0
    if get_language() == 'ru':
        header_text = "Тест  на сухость глаз"
    elif get_language() == 'pl':
        header_text = "Test suchego oka"
    if request.method == 'POST':
        for test in dry_eye_test:
            selected_option = request.POST['question-{}-answers'.format(test.question_number)]
            if selected_option == "Часто":
                test_results += 1
            elif selected_option == "Иногда":
                test_results += 2
            elif selected_option == "Редко":
                test_results += 3
            elif selected_option == "Никогда":
                test_results += 4
        print(test_results)
    context = {'test_database' : dry_eye_test, 'header_text': header_text}
    return render(request, 'AplikacjaBadaniaWadWzroku/tests.html', context)


def results(request, test, result):
    if test == 'dry_eye':
        if int(result) in range(24, 37):
            if get_language() == 'ru':
                result_text = "В Вашем случае наличие синдрома сухого глаза маловероятно"
            elif get_language() == 'pl':
                result_text = "Masz małe prawdopodobieństwo posiadania zespołu suchego oka"
        elif int(result) in range(13, 24):
            if get_language() == 'ru':
                result_text = "У Вас средняя вероятность наличия синдрома сухого глаза"
            elif get_language() == 'pl':
                result_text = "Masz średnie prawdopodobieństwo posiadania zespołu suchego oka"
        elif int(result) in range(13):
            if get_language() == 'ru':
                result_text = "У Вас большая вероятность наличия синдрома сухого глаза"
            elif get_language() == 'pl':
                result_text = "Masz duże prawdopodobieństwo posiadania zespołu suchego oka"
        else:
            result_text = "Some Error"
    elif test == "macular_degeneration":
        result_text = result
    elif test == "ishihara":
        right_answers = result
        if int(result) in range(13, 16):
            if get_language() == 'ru':
                result_text = "В Вашем случае наличие дальтонизма маловероятно"
            elif get_language() == 'pl':
                result_text = "Masz małe prawdopodobieństwo posiadania daltonizmu"
        elif int(result) in range(10, 13):
            if get_language() == 'ru':
                result_text = "У Вас средняя вероятность наличия дальтонизма"
            elif get_language() == 'pl':
                result_text = "Masz średnie prawdopodobieństwo posiadania daltonizmu"
        elif int(result) in range(10):
            if get_language() == 'ru':
                result_text = "У Вас большая вероятность наличия дальтонизма"
            elif get_language() == 'pl':
                result_text = "Masz duże prawdopodobieństwo posiadania daltonizmu"
        else:
            result_text = "Some Error"
    elif test == "astigmatism":
        result_text = result

    elif test == "snellen_test":
        if '0' in result.strip()[:8]:
            if result.strip()[:8].index('0') == 0:
                right_eye_result = '<1/10'
            elif result.strip()[:8].index('0') == 1:
                right_eye_result = '1/10'
            elif result.strip()[:8].index('0') == 2:
                right_eye_result = '1/8'
            elif result.strip()[:8].index('0') == 3:
                right_eye_result = '1/6'
            elif result.strip()[:8].index('0') == 4:
                right_eye_result = '1/5'
            elif result.strip()[:8].index('0') == 5:
                right_eye_result = '1/4'
            elif result.strip()[:8].index('0') == 6:
                right_eye_result = '1/3'
            elif result.strip()[:8].index('0') == 7:
                right_eye_result = '1/2'
        else:
            right_eye_result = '1/1'

        if '0' in result.strip()[8:]:
            if result.strip()[8:].index('0') == 0:
                left_eye_result = '<1/10'
            elif result.strip()[8:].index('0') == 1:
                left_eye_result = '1/10'
            elif result.strip()[8:].index('0') == 2:
                left_eye_result = '1/8'
            elif result.strip()[8:].index('0') == 3:
                left_eye_result = '1/6'
            elif result.strip()[8:].index('0') == 4:
                left_eye_result = '1/5'
            elif result.strip()[8:].index('0') == 5:
                left_eye_result = '1/4'
            elif result.strip()[8:].index('0') == 6:
                left_eye_result = '1/3'
            elif result.strip()[8:].index('0') == 7:
                left_eye_result = '1/2'
        else:
            left_eye_result = '1/1'
        if get_language() == 'pl':
            result_text = 'Ostrość wzroku prawego oka: ' + right_eye_result + '; Ostrość wzroku lewego oka: ' + left_eye_result
        elif get_language() == 'ru':
            result_text = 'Острота зрения правого глаза: ' + right_eye_result + '; Острота зрения левого глаза: ' + left_eye_result
    else:
        result_text = "No such test"

    print(result.strip())
    context = {'result_text': result_text, 'test': test, 'right_answers': right_answers}
    return render(request, 'AplikacjaBadaniaWadWzroku/results.html', context)
