from django.shortcuts import render
from .models import SkillsCategory, Skills

def CourseView(request):
    categories = SkillsCategory.objects.all()
    skills = Skills.objects.select_related('category').all()
    
    context = {
        'categories': categories,
        'skills': skills,
    }
    return render(request , "category_skills/courses.html", context)

def CourseDetailView(request):
    return render(request , "category_skills/course-details.html")

def InstructorView(request):
    return render(request , "category_skills/instructors.html")