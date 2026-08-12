"""Tests for the GitMap application entry point."""

from gitmap.main import main


def test_main(capsys):
    """The main entry point displays GitMap."""

    main()

    output = capsys.readouterr().out

    assert output == "GitMap\n"
