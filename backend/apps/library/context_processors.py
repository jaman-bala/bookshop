from backend.apps.library.models import Category


def sidebar(request):
	categories = Category.objects.all()
	context = {
		"cat": categories
	}
	return context
