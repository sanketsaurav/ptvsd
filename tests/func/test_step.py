# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root
# for license information.

from __future__ import absolute_import, print_function, with_statement, unicode_literals

import pytest

from tests.helpers import get_marked_line_numbers, print
from tests.helpers.session import DebugSession
from tests.helpers.timeline import Event
from tests.helpers.pattern import ANY


def test_set_next_statement(pyfile, run_as, start_method):

    @pyfile
    def code_to_debug():
        from dbgimporter import import_and_enable_debugger
        import_and_enable_debugger()

        def func():
            print(1)  # @inner1
            print(2)  # @inner2

        print(3)  # @outer3
        func()

    line_numbers = get_marked_line_numbers(code_to_debug)
    print(line_numbers)

    with DebugSession() as session:
        session.initialize(
            target=(run_as, code_to_debug),
            start_method=start_method,
            ignore_unobserved=[Event('continued')],
            client_id='vscode',
        )
        session.set_breakpoints(code_to_debug, [line_numbers['inner1']])
        session.start_debugging()

        stop = session.wait_for_thread_stopped()
        frames = stop.stacktrace.body['stackFrames']
        line = frames[0]['line']
        assert line == line_numbers['inner1']

        targets = session.send_request('gotoTargets', {
            'source': {'path': code_to_debug},
            'line': line_numbers['outer3'],
        }).wait_for_response().body['targets']

        assert targets == [{
            'id': ANY.num,
            'label': ANY.str,
            'line': line_numbers['outer3']
        }]
        outer3_target = targets[0]['id']

        with pytest.raises(Exception):
            session.send_request('goto', {
                'threadId': stop.thread_id,
                'targetId': outer3_target,
            }).wait_for_response()

        targets = session.send_request('gotoTargets', {
            'source': {'path': code_to_debug},
            'line': line_numbers['inner2'],
        }).wait_for_response().body['targets']

        assert targets == [{
            'id': ANY.num,
            'label': ANY.str,
            'line': line_numbers['inner2'],
        }]
        inner2_target = targets[0]['id']

        session.send_request('goto', {
            'threadId': stop.thread_id,
            'targetId': inner2_target,
        }).wait_for_response()

        session.wait_for_next(Event('continued'))

        stop = session.wait_for_thread_stopped(reason='goto')
        frames = stop.stacktrace.body['stackFrames']
        line = frames[0]['line']
        assert line == line_numbers['inner2']

        session.send_request('continue').wait_for_response()
        session.wait_for_exit()
