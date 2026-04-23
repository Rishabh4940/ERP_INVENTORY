# 🏪 AI-Powered Inventory Intelligence System

A lightweight ERP-style inventory management tool built with **Python + Pandas**, integrated with **Claude AI** to query inventory data in plain English.

---

## 💡 Why I Built This

After exploring how ERP systems like ERPNext handle inventory and commerce workflows, I wanted to understand the core logic behind it — purchase orders, stock levels, sales, and reorder alerts.

I then layered Claude AI on top so instead of reading raw data tables, a business owner can just ask:
> *"Which products are running low?"*
> *"What's my best selling product this week?"*
> *"Which item is generating the most revenue?"*

And get a plain English answer instantly.

---

## ⚙️ Tech Stack

| Layer | Tool |
|-------|------|
| Data & Analysis | Python, Pandas |
| AI Layer | Claude API (Anthropic) |
| Data Storage | CSV (ERP-style flat file) |

---

## 🚀 How to Run

**1. Clone the repo**
```bash
git clone https://github.com/yourusername/erp-inventory-ai
cd erp-inventory-ai
```

**2. Install dependencies**
```bash
pip install pandas requests
```

**3. Set your API key (never hardcode it)**
```bash
export ANTHROPIC_API_KEY="your-key-here"
```

**4. Run**
```bash
python main.py
```

---

## 📊 What It Does

- Loads inventory from CSV (products, stock, price, units sold)
- Auto-detects **low stock alerts** based on reorder level
- Calculates **revenue per product**
- Identifies **best sellers** and **top revenue generators**
- Lets you **chat with Claude** about your inventory in plain English

---

## 💬 Questions You Can Ask

**Stock & Restocking**
```
Which products need restocking urgently?
What is the most critically low stock item?
Which products are below their reorder level?
What should I reorder first?
How many products are running low?
```

**Sales & Best Sellers**
```
What is my best selling product?
What are my top 3 best sellers?
Which product has the highest units sold?
Which product is selling the slowest?
```

**Revenue & Performance**
```
What is my total revenue?
Which product generates the most revenue?
Which category makes more revenue, Electronics or Stationery?
What are my top 3 revenue generating products?
How is my overall business performance?
```

**Business Insights**
```
What should I focus on to improve my business?
Which products should I promote more?
What is my biggest business risk right now?
Give me a full business summary.
```

---

## 📁 Project Structure

```
erp_inventory/
│
├── inventory.csv       # Inventory database (products, stock, sales)
├── main.py             # Core logic — Pandas analysis + Claude AI
└── README.md
```

---

## 🎯 Sample Q&A — Real Output Examples

**Q: Which products need restocking urgently?**
```
🤖 AI: Based on current inventory, 3 products are below reorder level:
- Laptop Stand: Stock at 3, reorder level is 10 — CRITICAL
- Ballpoint Pen Pack: Stock at 5, reorder level is 25 — URGENT
- USB-C Cable: Stock at 8, reorder level is 15 — URGENT
Recommend restocking Laptop Stand first as it is most critically low.
```

**Q: What is my best selling product?**
```
🤖 AI: Your best selling product is USB-C Cable with 340 units sold,
followed by Ballpoint Pen Pack at 200 units and Sticky Notes at 150 units.
USB-C Cable is driving strong volume — ensure stock levels are maintained.
```

**Q: Which category makes more revenue, Electronics or Stationery?**
```
🤖 AI: Electronics is the stronger revenue category. Top performers are
USB-C Cable (Rs 101,660), Laptop Stand (Rs 89,955), and Desk Lamp (Rs 77,940).
Stationery drives volume but at lower price points.
```

**Q: What is my biggest business risk right now?**
```
🤖 AI: Your biggest risk is stockout on high-demand items. USB-C Cable
is both your best seller AND below reorder level — a stockout here
directly impacts your top revenue line. Restock immediately.
```

**Q: Give me a full business summary.**
```
🤖 AI: Business Overview:
- Total Products: 10 | Total Revenue: Rs 496,340
- 3 products are critically low on stock and need immediate reordering
- Electronics outperforms Stationery in revenue
- USB-C Cable is your star product — highest sales and strong revenue
- Recommend focusing on restocking and promoting high-margin Electronics
```

---

## 🔮 What I'd Add Next

- Connect to a real database (PostgreSQL) instead of CSV
- Add purchase order and sales order recording
- Build a dashboard in Power BI on top of the same data
- Schedule automated low-stock email alerts

---

*Built as a hands-on exploration of ERP inventory logic + AI-assisted data querying.*
