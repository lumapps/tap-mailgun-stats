"""TapMailgunStats tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_mailgun_stats import streams


class TapTapMailgunStats(Tap):
    """TapMailgunStats tap class."""

    name = "tap-mailgun-stats"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "auth_token",
            th.StringType,
            required=True,
            secret=True,
            description="API key used to call Mailgun APIs",
        ),
        th.Property(
            "event",
            th.StringType,
            required=True,
            description="Name of the event(s) to receive the stats for"
        ),
        th.Property(
            "start",
            th.StringType,
            required=False,
            description="The start date in RFC 2822 format or unix epoch",
        ),
        th.Property(
            "end",
            th.StringType,
            description="The end date in RFC 2822 format or unix epoch ",
        ),
        th.Property(
            "resolution",
            th.StringType,
            description="The gregorian resolution the query is for day, month, hour ",
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.TapMailgunStatsStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.MailgunStatsTotalStream(self),
        ]


if __name__ == "__main__":
    TapTapMailgunStats.cli()
