from django.contrib import admin
from .models import TaskManager, Category, Priority, Completed, Favourite

class TaskManagerAdmin(admin.ModelAdmin):
    # def save_model(self, request, obj, form, change):
    #     if not change:
    #         obj.user = request.user
    #
    #     super(TaskManagerAdmin, self).save_model(
    #         request=request,
    #         obj=obj,
    #         form=form,
    #         change=change
    #     )
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)

    # def save_model(self, request, obj, form, change):
    #     obj.user = request.user
    #     super().save_model(request, obj, form, change)

    list_display = ('id', 'title', 'category', 'priority', 'completed', 'favourite', 'completed_at', 'user')
    list_display_links = ('id', 'title', 'user')
    search_fields = ('title',)
    list_editable = ('completed', 'priority', 'favourite')
    list_filter = ('category', 'favourite')


# class User(admin.ModelAdmin):
#     list_display = ('id', 'task', 'is_author')
#     list_display_links = ('id', 'task')
#     search_fields = ('task',)
#     list_editable = ('task',)
#     list_filter = ('task', 'is_author')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    # prepopulated_fields = {'slug': ('title',)}


class PriorityAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class CompletedAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

# class CompletedAtAdmin(admin.ModelAdmin):
#     list_display = ('id', 'completed_at')
#     list_display_links = ('id',)
#     # search_fields = ('completed',)

class FavouriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'mark')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(TaskManager, TaskManagerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Priority, PriorityAdmin)
admin.site.register(Completed, CompletedAdmin)
admin.site.register(Favourite, FavouriteAdmin)



