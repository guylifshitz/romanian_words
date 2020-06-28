from django.http import HttpResponse,HttpResponseRedirect
from .models import Word
import random
import json
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.db.models import Sum
from pathlib import Path
import pandas as pd


def show_word(request, pk):
    word = get_object_or_404(Word, pk=pk)
    total_score = Word.objects.aggregate(Sum('score'))['score__sum']
    print(total_score)
    context = {
        'romanian': word.romanian,
        'english': word.english,
        "score": word.score/total_score,
        "pk": pk
    }

    return render(request, 'word.html', context=context)

def increase_score(request, pk):
    word = get_object_or_404(Word, pk=pk)
    word.score = word.score + 1 * max((word.score/2), 1)
    word.save()

    return HttpResponseRedirect(reverse('show_word', args=[pk]))

def decrease_score(request, pk):
    word = get_object_or_404(Word, pk=pk)
    word.score = max(word.score - 1 *  max((word.score / 2), 1), 1)
    word.save()

    return HttpResponseRedirect(reverse('show_word', args=[pk]))

            # try:
        # selected_choice = word.choice_set.get(pk=request.POST['choice'])
    # except (KeyError, Choice.DoesNotExist):
        # Redisplay the word voting form.
        # return render(request, 'polls/detail.html', {
            # 'word': word,
            # 'err/or_message': "You didn't select a choice.",
        # })



def create(request):
    Word.objects.all().delete()
    for path in Path("romanian_words/utils/output").glob("*"):
        print(path)
        level = int(path.name.split(".csv")[0])

        df = pd.read_csv(path)

        for idx, entry in df.iterrows():
            word = Word(romanian=entry["romanian"], english=entry["english"], score=1, level=level)
            word.save()


    return HttpResponse("Created.")

