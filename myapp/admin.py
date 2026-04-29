from django.contrib import admin
from .models import Device, Measurement

# Κάνουμε register τον μικροελεγκτή (Device)
@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'mac_address')  # Τι θα φαίνεται στη λίστα
    search_fields = ('name', 'mac_address') # Μπάρα αναζήτησης
    filter_horizontal = ('users',)          # Ειδικό widget για να κάνεις assign χρήστες εύκολα!

# Κάνουμε register τις Μετρήσεις (Measurement)
@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'device', 'voltage', 'current', 'temperature', 'soc', 'soh')  # Τι θα φαίνεται στη λίστα
    search_fields = ('device__name', 'device__mac_address') # Μπάρα αναζήτησης με βάση το όνομα ή το MAC της συσκευής
    list_filter = ('device',)               # Φίλτρο στα δεξιά για να βλέπεις μετρήσεις ανά ESP32
    date_hierarchy = 'timestamp'            # Μενού πλοήγησης ανά ημερομηνία/μήνα
