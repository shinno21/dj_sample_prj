import glob
import json
import os

from django.http import HttpResponse
from django.template import loader

from .consts import BASE_DIR


# Create your views here.
def index(request):
    template = loader.get_template("index.html")
    context = {
        "text": "test",
    }
    return HttpResponse(template.render(context, request))


def json_data(request):
    path_list = glob.glob(os.path.join(BASE_DIR, "**"), recursive=True)
    j = __path_list_to_json(path_list)
    return HttpResponse(json.dumps(j))


def rep_words(request, words):
    return HttpResponse(words)


def cre_dir(request):
    if request.method == "POST":
        d = request.POST.get("dir", None)
        os.makedirs(BASE_DIR + d)
        return HttpResponse("create directory")


def __path_list_to_json(path_list):
    jlist = []
    flist = []
    # 最初の要素はルートなので除外
    for p in path_list[1:]:
        rpath = p.replace(BASE_DIR, "")  # ルートパス削除
        if jlist:
            if rpath.startswith(jlist[len(jlist) - 1]["text"] + "/"):
                flist.append(
                    __e_to_file_dict(
                        rpath.replace(jlist[len(jlist) - 1]["text"] + "/", "")
                    )
                )
            else:
                if flist:
                    jlist[len(jlist) - 1]["children"] = flist
                    jlist.append(__e_to_dir_dict(rpath))
                    flist = []
                else:
                    jlist.append(__e_to_dir_dict(rpath))
        # 最初の要素
        else:
            jlist.append(__e_to_dir_dict(rpath))
    return jlist


def __e_to_dir_dict(e):
    return {
        "text": e,
        "state": {"opened": True, "disabled": False},
        "a_attr": {"href": "https://qiita.com/", "target": "_blank"},
    }


def __e_to_file_dict(e):
    return {
        "text": e,
        "icon": "jstree-file",
        "state": {"opened": True, "disabled": False},
        "a_attr": {"href": "https://qiita.com/", "target": "_blank"},
    }
