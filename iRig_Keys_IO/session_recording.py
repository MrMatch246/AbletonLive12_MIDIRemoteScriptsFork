# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/iRig_Keys_IO/session_recording.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 533 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.components import SessionRecordingComponent as SessionRecordingComponentBase
from ableton.v2.control_surface.control import ButtonControl

class SessionRecordingComponent(SessionRecordingComponentBase):
    record_stop_button = ButtonControl()

    @record_stop_button.pressed
    def record_stop_button(self, _):
        self.song.session_record = False
