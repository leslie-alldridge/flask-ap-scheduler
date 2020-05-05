# flask-ap-scheduler
flask ap scheduler example

You can also use things like:

- app.apscheduler.remove_job('inv_script')

- for job in app.apscheduler.get_jobs():
        print(job)
        
- app.apscheduler.add_listener(my_listener)

- def my_listener(event):
    //Removes job from queue regardless, we can check logs for result if required
    if event.exception:
        print('Error: The job crashed!')
        app.apscheduler.remove_job('inv_script')
    else:
        print('The job worked!')
        app.apscheduler.remove_job('inv_script')
