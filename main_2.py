import pandas as pd
import requests
import os
from dotenv import load_dotenv

load_dotenv()
# ── Load Data ──────────────────────────────────────────────────────────────────
df = pd.read_csv("inventory.csv")
df["revenue"] = df["unit_price"] * df["units_sold"]

# ── Pandas Analysis ────────────────────────────────────────────────────────────
def get_inventory_summary():
    low_stock    = df[df["stock"] <= df["reorder_level"]][["product_name", "stock", "reorder_level"]]
    best_sellers = df.nlargest(3, "units_sold")[["product_name", "units_sold"]]
    top_revenue  = df.nlargest(3, "revenue")[["product_name", "revenue"]]
    total_rev    = df["revenue"].sum()
    total_skus   = len(df)

    summary = f"""
INVENTORY SUMMARY
=================
Total Products : {total_skus}
Total Revenue  : Rs {total_rev:,.0f}

LOW STOCK ALERTS (stock <= reorder level):
{low_stock.to_string(index=False) if not low_stock.empty else "All products are sufficiently stocked."}

TOP 3 BEST SELLERS (by units sold):
{best_sellers.to_string(index=False)}

TOP 3 REVENUE GENERATORS:
{top_revenue.to_string(index=False)}
    """
    return summary.strip()

# ── OpenRouter AI Integration ──────────────────────────────────────────────────
def ask_gemini(user_question, inventory_summary):
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        return "Error: OPENROUTER_API_KEY not set. Run: $env:OPENROUTER_API_KEY='your-key'"

    prompt = f"""You are an AI inventory analyst for a small business.
You have access to the following live inventory data:

{inventory_summary}

Answer the user's question based only on this data. Be concise and actionable.
If a product is low on stock, always flag it. Speak like a helpful business analyst.

User question: {user_question}"""

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "google/gemma-3-4b-it:free",
            "messages": [{"role": "user", "content": prompt}]
        }
    )

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"API Error {response.status_code}: {response.text}"

# ── Main App ───────────────────────────────────────────────────────────────────
def main():
    print("\n🏪  AI-Powered Inventory Intelligence System")
    print("=" * 50)

    summary = get_inventory_summary()
    print(summary)
    print("\n" + "=" * 50)
    print("💬  Ask anything about your inventory (type 'exit' to quit)")
    print("=" * 50)

    while True:
        question = input("\nYou: ").strip()
        if question.lower() in ["exit", "quit", "q"]:
            print("Goodbye!")
            break
        if not question:
            continue

        print("\n🤖 Claude: Thinking...")
        answer = ask_gemini(question, summary)
        print(f"\n🤖 Claude: {answer}")

if __name__ == "__main__":
    main()