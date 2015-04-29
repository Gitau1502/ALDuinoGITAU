<?xml version="1.0" encoding="UTF-8" ?>
<Package name="ALDuino" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions />
    <Dialogs>
        <Dialog name="Lexicon" src="lib/butane/dialog/Lexicon/Lexicon.dlg" />
    </Dialogs>
    <Resources>
        <File name="icon" src="icon.png" />
        <File name="alduino" src="lib/alduino.py" />
        <File name="__init__" src="lib/butane/__init__.py" />
        <File name="conversation" src="lib/butane/conversation.py" />
        <File name="fuel" src="lib/butane/fuel.py" />
        <File name="language_utils" src="lib/butane/language_utils.py" />
        <File name="package_utils" src="lib/butane/package_utils.py" />
        <File name="__init__" src="lib/pyfirmata/__init__.py" />
        <File name="boards" src="lib/pyfirmata/boards.py" />
        <File name="mockup" src="lib/pyfirmata/mockup.py" />
        <File name="pyfirmata" src="lib/pyfirmata/pyfirmata.py" />
        <File name="util" src="lib/pyfirmata/util.py" />
        <File name="register" src="lib/register.py" />
    </Resources>
    <Topics>
        <Topic name="Lexicon_enu" src="lib/butane/dialog/Lexicon/Lexicon_enu.top" topicName="Lexicon" language="en_US" />
    </Topics>
    <IgnoredPaths>
        <Path src="lib/butane/tests/test_conversation.py" />
        <Path src="lib/butane/tests/test_butane.py" />
        <Path src="lib/butane/tests/conftest.py" />
        <Path src="lib/butane/tests/TestBehavior" />
        <Path src="lib/butane/tests/__init__.py" />
        <Path src="lib/butane/tests/lu_string_test.json" />
        <Path src="lib/butane/tests/TestBehavior/dialog/TestTopic/TestTopic_enu.top" />
        <Path src="lib/butane/tests/TestBehavior/Test.pml" />
        <Path src="lib/butane/tests/TestBehavior/behavior.xar" />
        <Path src="lib/butane/tests/test_language_utils.py" />
        <Path src="lib/butane/tests/TestBehavior/manifest.xml" />
        <Path src="lib/butane/.gitignore" />
        <Path src="lib/butane/.git" />
        <Path src="lib/butane/tests/TestBehavior/dialog/TestTopic/TestTopic.dlg" />
        <Path src="lib/butane/tests/test_fuel.py" />
        <Path src="lib/butane/tests/TestBehavior/.metadata" />
        <Path src="lib/butane/README" />
        <Path src="lib/butane/tests/README" />
        <Path src="lib/butane/tests/test_package_utils.py" />
    </IgnoredPaths>
</Package>
