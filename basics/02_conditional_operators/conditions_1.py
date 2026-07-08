#Create a work tracker that checks whether you worked today.
#The option with capital letters or abbreviated (y, n) should also be taken into account
work_track = input('you work today?: ')
if work_track.lower() == 'yes' or work_track.lower() == 'y':
    print('✓')
elif work_track.lower() == 'no' or work_track.lower() == 'n':
    print('✗')
