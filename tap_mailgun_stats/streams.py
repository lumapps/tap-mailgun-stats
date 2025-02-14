"""Stream type classes for tap-mailgun-stats."""

from __future__ import annotations


from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_mailgun_stats.client import TapMailgunStatsStream

class MailgunStatsTotalStream(TapMailgunStatsStream):
    """Define custom stream."""

    name = "total"
    path = "/v3/stats/total"
    primary_keys = []
    replication_key = None
    rest_method = "GET"

    def get_url_params(self, context, next_page_token):
        return {
            "event": self.config.get("event", "accepted"),
            "start": self.config.get("start", "2025-01-01"),
            "end": self.config.get("end", "2025-01-02"),
        }

    schema = th.PropertiesList(
        th.Property("description", th.StringType),
        th.Property("start", th.StringType),
        th.Property(
            "end",
            th.StringType,
        ),
        th.Property(
            "resolution",
            th.StringType,
        ),
        th.Property(
            "tag", th.StringType
        ),
        th.Property(
            "type", th.ObjectType(
                th.Property("type", th.StringType),
                th.Property("key", th.StringType),
            )
        ),
        th.Property("stats", th.ArrayType(
            th.ObjectType(
                th.Property("time", th.StringType),
                th.Property(
                "delivered",
                th.ObjectType(
                    th.Property("smtp", th.IntegerType),
                    th.Property("http", th.IntegerType),
                    th.Property("total", th.IntegerType),
                    th.Property("optimized", th.IntegerType),
                )
            ),
                th.Property(
                "accepted",
                th.ObjectType(
                    th.Property("incoming", th.IntegerType),
                    th.Property("outgoing", th.IntegerType),
                    th.Property("total", th.IntegerType),
                )
            ),
                th.Property(
                "stored",
                th.ObjectType(
                    th.Property("total", th.IntegerType),
                )
            ),
                th.Property(
                "failed",
                th.ObjectType(
                    th.Property("temporary", th.ObjectType(
                        th.Property("espblock", th.IntegerType),
                        th.Property("total", th.IntegerType),
                    )),
                    th.Property("permanent", th.ObjectType(
                        th.Property("suppress-bounce", th.IntegerType),
                        th.Property("suppress-unsubscribe", th.IntegerType),
                        th.Property("suppress-complaint", th.IntegerType),
                        th.Property("bounce", th.IntegerType),
                        th.Property("delayed-bounce", th.IntegerType),
                        th.Property("webhook", th.IntegerType),
                        th.Property("optimized", th.IntegerType),
                        th.Property("total", th.IntegerType),                        
                    )),
                ))
        ))),
            th.Property(
                "unsubscribed",
                th.ObjectType(
                    th.Property("total", th.IntegerType),
                )
            ),
            th.Property(
                "opened",
                th.ObjectType(
                    th.Property("total", th.IntegerType),
                    th.Property("unique", th.IntegerType),
                )
            ),
            th.Property(
                "campaign",
                th.ObjectType(
                    th.Property("total", th.IntegerType),
                )
            ),
            th.Property(
                "clicked",
                th.ObjectType(
                    th.Property("total", th.IntegerType),
                    th.Property("unique", th.IntegerType),
                )
            ),
            th.Property(
                "complained",
                th.ObjectType(
                    th.Property("total", th.IntegerType),
                )
            ),
            th.Property(
                "seed_test",
                th.ObjectType(
                    th.Property("total", th.IntegerType),
                )
            ),
            th.Property(
                "email_validation",
                th.ObjectType(
                    th.Property("total", th.IntegerType),
                    th.Property("public", th.IntegerType),
                    th.Property("valid", th.IntegerType),
                    th.Property("single", th.IntegerType),
                    th.Property("bulk", th.IntegerType),
                    th.Property("list", th.IntegerType),
                    th.Property("mailgun", th.IntegerType),
                    th.Property("mailjet", th.IntegerType),
                )
            ),
            th.Property(
                "link_validation_failed", th.ObjectType(
                    th.Property("total", th.IntegerType)
                )
            ),
            th.Property(
                "link_validation", th.ObjectType(
                    th.Property("total", th.IntegerType)
                )
            ),
            th.Property(
                "email_preview", th.ObjectType(
                    th.Property("total", th.IntegerType)
                )
            ),
            th.Property("email_preview_failed", th.ObjectType(
                th.Property("total", th.IntegerType)
            )),
        ).to_dict()
