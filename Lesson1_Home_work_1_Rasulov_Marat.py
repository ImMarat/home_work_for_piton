def naive_realisation(duration = 233234):
    second = 1
    minute = 60
    hour = minute * 60
    day = hour * 24

    add_empty_time = False

    total_days = duration // day
    duration = duration % day

    total_hours = duration // hour
    duration = duration % hour

    total_minutes = duration // minute
    total_seconds = duration % minute

    total_time = ''
    if total_days:
        total_time += f'{total_days} дн'
        add_empty_time = True
    if total_hours or add_empty_time:
        add_empty_time = True
        total_time += f' {total_hours} час'
    if total_minutes or add_empty_time:
        add_empty_time = True
        total_time += f' {total_minutes} мин'
    if total_seconds or add_empty_time:
        total_time += f' {total_seconds} сек'

    return total_time
print(naive_realisation())


def one_cycle_realisation(duration = 233234):
    second = 1
    minute = 60
    hour = minute * 60
    day = hour * 24

    add_empty_time = False

    time_items = [[day, 'дн'], [hour, 'час'], [minute, 'мин'], [second, 'сек']]
    total_time = []

    for time_element in time_items:
        current_time_element = duration // time_element[0]
        duration = duration % time_element[0]
        if current_time_element or add_empty_time:
                total_time.append(f'{current_time_element} {time_element[1]}')
                add_empty_time = True

    return  ' '.join(total_time)
print(one_cycle_realisation())


