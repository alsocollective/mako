var slider = {
	settings: {
		on: false,
		touch: false,
		main: {
			height: 50,
			width: 0
		},
		circle: {
			width: 50,
			height: 50
		},
		onmove: function() {
			return null;
		},
		onstart: function() {
			return null;
		},
		onend: function() {
			return null;
		}
	},
	location: 0,
	init: function(elementquery) {
		slider.el = {};
		slider.el.main = $(elementquery)
		if (slider.el.main.length == 0) {
			return "nothing found"
		} else {
			slider.el.main.addClass("bohdanslider")
			slider.el.main = slider.el.main[0]
		}
		slider.settings.touch = slider.actions.is_touch_device();
		slider.init_construct();
		slider.init_actions();


		return "all worked well"
	},
	init_construct: function() {
		slider.el.circle = document.createElement("div")
		slider.el.circle.className = "circle"
		slider.el.main.appendChild(slider.el.circle)
	},
	init_actions: function() {
		if (!slider.settings.touch) {
			$(slider.el.main).mousedown(slider.actions.seton_desktop);
			$(slider.el.main.parentNode).mouseup(slider.actions.setoff);
			$(slider.el.main.parentNode).mousemove(slider.actions.move_desktop);
		} else {
			$(slider.el.main).on('touchstart', slider.actions.seton_mobile);
			$(slider.el.main.parentNode).on('touchend', slider.actions.setoff);
			$(slider.el.main.parentNode).on('touchcancel', slider.actions.setoff);
			$(slider.el.main.parentNode).on('touchmove', slider.actions.move_mobile);
		}
	},
	math: {
		figureCirclLoc: function(x) {
			return slider.math.withinbar(x - (slider.settings.circle.width / 2));
		},
		figureCirclLoc_child: function(child, x) {
			return slider.math.withinbar(x + ($(child).offset().left - $(child.parentNode).offset().left));
		},
		figureCirclLocMobile: function(x) {
			return slider.math.withinbar(x - $(slider.el.main).offset().left);
		},
		withinbar: function(x) {
			if (x < 0) {
				slider.location = 0;
				return -(slider.settings.circle.width / 2);
			} else {
				var w = $(slider.el.main).width();
				if (x > w) {
					slider.location = w;
					return w - (slider.settings.circle.width / 2)
				}
				slider.location = x;
				return x - (slider.settings.circle.width / 2)
			}
		}
	},
	actions: {
		seton_desktop: function(event) {
			slider.settings.on = true;
			slider.actions.move_desktop(event);
			slider.settings.onstart();
		},
		seton_mobile: function(event) {
			slider.settings.on = true;
			slider.actions.move_mobile(event);
			slider.settings.onstart();
		},
		setoff: function(event) {
			slider.settings.on = false;
			slider.settings.onend();
		},
		move_desktop: function(event) {
			if (slider.settings.on) {
				if (event.target.className == "bohdanslider") {
					slider.el.circle.style.left = slider.math.figureCirclLoc(event.offsetX) + "px";
				} else if (event.target.className == "circle") {
					slider.el.circle.style.left = slider.math.figureCirclLoc_child(event.target, event.offsetX) + "px";
				}
				slider.settings.onmove();
			} else {
				return false;
			}
		},
		move_mobile: function(event) {
			if (slider.settings.on) {
				slider.el.circle.style.left = slider.math.figureCirclLocMobile(event.originalEvent.touches[0].pageX) + "px";
				slider.settings.onmove();
			} else {
				return false;
			}
		},
		is_touch_device: function() {
			try {
				document.createEvent("TouchEvent");
				return true;
			} catch (e) {
				return false;
			}
		}
	}

}