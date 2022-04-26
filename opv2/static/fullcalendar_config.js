document.addEventListener('DOMContentLoaded', function() {
    const calendarEl = document.getElementById('calendar');
    const calendar = new FullCalendar.Calendar(calendarEl, {
        fixedWeekCount: true,
        themeSystem: 'bootstrap5',
        locale: 'cs',
        initialView: 'dayGridMonth',
        firstDay: 1,
        height: "auto",
        headerToolbar: {
            left: 'prev,next',
            center: '',
            right: 'title',
        },
        events: {
            url: "fetch_calendar",
            method: "GET",
            format: "json"
        },
        eventSourceSuccess: function (c, x) {
            const stArr = [];
            c.forEach(element => {
                stArr.push(Date.parse(element.start));
                stArr.push(Date.parse(element.end));
            });
            const maxDate = new Date(Math.max.apply(null, stArr));
            const minDate = new Date(Math.min.apply(null, stArr));
            maxDate.setDate(maxDate.getDate() - 1);
            calendar.setOption("validRange", {
                start: minDate,
                end: maxDate
            })
        },
        eventSourceFailure: function (error) {
            console.log(error)
            calendar.refetchEvents()
        }
    });
    calendar.render();
});
