from django.shortcuts import render, redirect
from app.models import *

def Home(request):
    return render(request, 'Staff/staff_home.html')

def Notification(request):
    # Get the staff object for the current user
    staff = Staff.objects.filter(admin=request.user).first()
    
    if staff:
        notifications = StaffNotification.objects.filter(staff_id=staff).order_by('-id')  
       
        unread_notifications_count = notifications.filter(status=0).count()
        
        context = {
            'notification': notifications,  # All notifications (read and unread)
            'unread_notifications_count': unread_notifications_count  
        }
        
        return render(request, 'Staff/notification.html', context)
    else:
        return redirect('notification')


    
def Notification_Mark_Read(request, status):
    notification = StaffNotification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('notification')