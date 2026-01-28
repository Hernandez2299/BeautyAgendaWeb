$(document).ready(function() {
  $('#calendar').fullCalendar({
    header: {
      left: 'prev,next today',
      center: 'title',
      right: 'month,agendaWeek,agendaDay'
    },
    defaultDate: new Date(), // fecha actual
    navLinks: true,
    editable: false,
    eventLimit: true,
    events: '/citas/api',   // 👈 dinámico desde Flask
    eventRender: function(event, element) {
      element.find('.fc-title').html(
        event.title + "<br/>Empleado: " + event.extendedProps.empleado
      );
    }
  });
});

