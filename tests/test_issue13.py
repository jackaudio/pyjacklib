import pytest

import jacklib


@pytest.mark.jack_server_required
@pytest.mark.skipif(jacklib.jlib.jack_port_rename is None, reason="libjack does not implement 'jack_port_rename'.")
@pytest.mark.parametrize("porttype,flags,name", [
    (jacklib.JACK_DEFAULT_AUDIO_TYPE, jacklib.JackPortIsOutput, "output"),
    (jacklib.JACK_DEFAULT_AUDIO_TYPE, jacklib.JackPortIsInput, "input"),
    (jacklib.JACK_DEFAULT_MIDI_TYPE, jacklib.JackPortIsOutput, "midi_output"),
    (jacklib.JACK_DEFAULT_MIDI_TYPE, jacklib.JackPortIsInput, "midi_input"),
])
def test_port_rename(jack_client, porttype, flags, name):
    port = jacklib.port_register(jack_client, name, porttype, flags, 0)

    if not port:
        raise OSError(f"Could not register port {name}.")

    assert jacklib.port_short_name(port) == name
    res = jacklib.port_rename(jack_client, port, "renamed")
    assert res == 0
    assert jacklib.port_short_name(port) == "renamed"


@pytest.mark.jack_server_required
def test_port_rename_not_supported(jack_client):
    port = jacklib.port_register(jack_client, "output", jacklib.JACK_DEFAULT_AUDIO_TYPE, jacklib.JackPortIsOutput, 0)

    if not port:
        raise OSError(f"Could not register port {name}.")

    jacklib.jlib.jack_port_rename = None
    assert jacklib.port_short_name(port) == "output"

    res = jacklib.port_rename(jack_client, port, "renamed")
    assert res == -1
    assert jacklib.port_short_name(port) == "output"
