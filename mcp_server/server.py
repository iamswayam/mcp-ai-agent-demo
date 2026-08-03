from pathlib import Path
import sqlite3

from fastmcp import FastMCP

mcp = FastMCP("EZAuto SQLite Server")

DB_PATH = Path(__file__).parent.parent / "database" / "ezauto.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


@mcp.tool
def get_total_cases() -> int:
    """Return total number of cases."""

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM cases")
        return cursor.fetchone()[0]


@mcp.tool
def get_cases_by_status(status: str) -> list:
    """
    Returns all cases having the given status.
    """

    with get_connection() as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT
                id,
                customer_name,
                city,
                status
            FROM cases
            WHERE status = ?
            ORDER BY id
            """,
            (status,),
        )

        rows = cursor.fetchall()

        return [dict(row) for row in rows]


@mcp.tool()
def get_case_status_summary() -> list[dict]:
    """
    Returns the count of cases grouped by status.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT status,
               COUNT(*)
        FROM cases
        GROUP BY status
        ORDER BY COUNT(*) DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return [
        {
            "status": status,
            "count": count
        }
        for status, count in rows
    ]


if __name__ == "__main__":
    mcp.run()


