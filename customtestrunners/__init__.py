import os
import unittest

class GrowlTestRunner(unittest.TextTestRunner):

  def run(self, test):
    result = unittest.TextTestRunner.run(self, test)
    self._notify(result)
    return result

  def _notify(self, result):
    values = {
      'type': 'Passed' if result.wasSuccessful() else 'Failed',
      'icon': 'pass.png' if result.wasSuccessful() else 'fail.png',
      'msg': '%d passed, %d failed' % (result.testsRun - len(result.failures) - len(result.errors), len(result.failures) + len(result.errors))
    }

    values['icon'] = os.path.join(os.path.dirname(__file__), values['icon'])

    cmd = 'growlnotify /a:"pyautotest" /r:Passed,Failed /n:"%(type)s" /t:%(type)s /i:"%(icon)s" "%(msg)s"' % values
    os.system(cmd)
