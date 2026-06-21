# tests the shared base interface adapter behavior

from adapters.base_interface_adapter import BaseInterfaceAdapter


# verifies that the adapter starts disconnected
def test_adapter_starts_disconnected():
    adapter = BaseInterfaceAdapter("base")

    assert adapter.is_connected() is False


# verifies that the adapter can connect
def test_adapter_can_connect():
    adapter = BaseInterfaceAdapter("base")

    adapter.connect()

    assert adapter.is_connected() is True


# verifies that the adapter can disconnect
def test_adapter_can_disconnect():
    adapter = BaseInterfaceAdapter("base")

    adapter.connect()
    adapter.disconnect()

    assert adapter.is_connected() is False


# verifies that adapter info is returned
def test_adapter_info():
    adapter = BaseInterfaceAdapter("base")

    info = adapter.get_info()

    assert info["name"] == "base"
    assert info["connected"] is False