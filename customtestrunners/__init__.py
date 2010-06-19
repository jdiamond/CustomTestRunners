import os
import unittest

APP_NAME = 'pyautotest'

PASSED_TYPE = 'Passed'
FAILED_TYPE = 'Failed'

PASSED_IMAGE = 'pass.png'
FAILED_IMAGE = 'fail.png'

class GrowlTestRunner(unittest.TextTestRunner):

    def run(self, test):
        result = unittest.TextTestRunner.run(self, test)
        self._notify(result)
        return result

    def _notify(self, result):
        failed = len(result.failures) + len(result.errors)
        passed = result.testsRun - failed

        values = {
            'app': APP_NAME,
            'passed': PASSED_TYPE,
            'failed': FAILED_TYPE,
            'type': PASSED_TYPE if result.wasSuccessful() else FAILED_TYPE,
            'icon': PASSED_IMAGE if result.wasSuccessful() else FAILED_IMAGE,
            'msg': '%d passed, %d failed!' % (passed, failed)
        }

        values['icon'] = os.path.join(
                os.path.dirname(__file__),
                values['icon'])

        cmd = ('growlnotify ' +
               '/a:"%(app)s" ' +
               '/r:"%(passed)s","%(failed)s" ' +
               '/n:"%(type)s" ' +
               '/t:"%(type)s" ' +
               '/i:"%(icon)s" ' +
               '"%(msg)s"') % values

        os.system(cmd)
