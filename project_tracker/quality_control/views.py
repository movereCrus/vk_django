from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView
from quality_control.models import BugReport, FeatureRequest

def index(request):
    return render(request, 'quality_control/index.html')

# def bug_list(request):
#     bugs = BugReport.objects.all()
#     bug_reports_html = "<h1>Cписок отчетов об ошибках</h1><ul>"
#     for report in bugs:
#         bug_reports_html += f'<li><a href="{report.id}/">{report.title} - статус "{report.status}"</a></li>'
#     bug_reports_html += '</ul>'
#     return HttpResponse(bug_reports_html)

def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bug_list.html', {'bugs_list': bugs})

# class BugDetailView(DetailView):
#     model = BugReport
#     pk_url_kwarg = 'bug_id'
    
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         bug = self.object
#         task = bug.task
#         project = bug.project
#         response_html = f"""<h1>Детали бага {bug.title} ({bug.id})</h1>
#             <p>
#                 Описание: {bug.description}
#             </p>
#             <ul>
#                 <li>Статус: {bug.status}</li>
#                 <li>Приоритет: {bug.priority}</li>
#                 <li>Проект: {project.name}</li>
#                 <li>Задача: {task.name}</li>
#             </ul>"""
#         return HttpResponse(response_html)

class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_detail.html'

def feature_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {'features_list': features})
    # feature_requests_html = "<h1>Cписок запросов на улучшение</h1><ul>"
    # for feature_request in features:
    #     feature_requests_html += f'<li><a href="{feature_request.id}/">{feature_request.title} - статус "{feature_request.status}"</a></li>'
    # feature_requests_html += '</ul>'
    # return HttpResponse(feature_requests_html)

class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    template_name = 'quality_control/feature_detail.html'
    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     feature = self.object
    #     task = feature.task
    #     project = feature.project
    #     response_html = f"""<h1>Детали запроса на улучшение {feature.title} ({feature.id})</h1>
    #         <p>
    #             Описание: {feature.description}
    #         </p>
    #         <ul>
    #             <li>Статус: {feature.status}</li>
    #             <li>Приоритет: {feature.priority}</li>
    #             <li>Проект: {project.name}</li>
    #             <li>Задача: {task.name}</li>
    #         </ul>"""
    #     return HttpResponse(response_html)