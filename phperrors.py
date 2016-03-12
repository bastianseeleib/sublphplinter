import sublime, sublime_plugin, os, re

class phperrors(sublime_plugin.EventListener):
	def on_post_save(self, view):

		if ".php" in view.file_name():

			view.erase_regions("phperror");

			f = os.popen("php -l "+view.file_name())
			errors = f.read()

			matchObj = re.search(r"([0-9].*)", errors, re.I|re.M)

			if matchObj:
				line = int(matchObj.group()) -1
				region = [view.line(view.text_point(line, 0))]
				view.add_regions("phperror", region, "string", "bookmark", sublime.DRAW_NO_FILL|sublime.DRAW_NO_OUTLINE|sublime.DRAW_SQUIGGLY_UNDERLINE)
