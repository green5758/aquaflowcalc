#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AquaFlowCalc - Interactive Pool Gallons, Variable-Speed Pump GPM, Filter, Salt Cell & Heater Calculator
+ Automated Daily Amazon Product Review Publisher
Affiliate StoreID: everythi00099-20
"""

import os
import json
import hashlib
import datetime
import urllib.request
import urllib.parse
import urllib.error

AFFILIATE_TAG = "everythi00099-20"
STATE_FILE = "posts_state.json"
OUTPUT_DIR = "public"
REVIEWS_DIR = os.path.join(OUTPUT_DIR, "reviews")
DAILY_NEW_ARTICLES = 3

# Deteksi otomatis URL GitHub Pages dari environment GitHub Actions
REPO_FULL = os.environ.get("GITHUB_REPOSITORY", "username/aquaflowcalc")
REPO_OWNER = os.environ.get("GITHUB_REPOSITORY_OWNER", REPO_FULL.split("/")[0])
REPO_NAME = REPO_FULL.split("/")[-1] if "/" in REPO_FULL else "aquaflowcalc"

if REPO_NAME.lower() == f"{REPO_OWNER.lower()}.github.io":
    BASE_URL = f"https://{REPO_OWNER.lower()}.github.io"
else:
    BASE_URL = f"https://{REPO_OWNER.lower()}.github.io/{REPO_NAME}"

INDEXNOW_KEY = hashlib.md5(f"aquaflowcalc-{AFFILIATE_TAG}".encode("utf-8")).hexdigest()


def amazon_search_url(query: str) -> str:
    encoded = urllib.parse.quote_plus(query)
    return f"https://www.amazon.com/s?k={encoded}&tag={AFFILIATE_TAG}"


# ==============================================================================
# MASTER BEST SELLER & COMPARISON CATALOG (10 FLAGSHIP POOL & POND PRODUCTS)
# ==============================================================================
CORE_PRODUCTS = [
    {
        "id": "black-decker-2hp-variable-speed-pump",
        "name": "BLACK+DECKER 2.0 HP Energy Star Variable-Speed Inground Pool Pump",
        "brand": "BLACK+DECKER",
        "category": "Variable-Speed Pool Pump",
        "max_gallons": 35000,
        "gpm_or_cap": "98 GPM Max Flow",
        "gpm_num": 98,
        "power_spec": "2.0 THP (115V/230V Dual Voltage)",
        "efficiency": "Energy Star (Saves up to 80% Power)",
        "rating": "4.7",
        "reviews_count": 3890,
        "badge": "#1 Best Selling Pool Pump",
        "search_query": "BLACK+DECKER 2 HP Variable Speed Inground Pool Pump",
        "highlight": "Self-priming variable-speed permanent magnet motor with programmable 4-speed timer and 2-inch union adapters."
    },
    {
        "id": "dolphin-nautilus-cc-plus-wifi",
        "name": "Dolphin Nautilus CC Plus Wi-Fi Robotic Pool Vacuum Cleaner",
        "brand": "Dolphin Maytronics",
        "category": "Robotic Pool Cleaner",
        "max_gallons": 30000,
        "gpm_or_cap": "75 GPM Suction Rate",
        "gpm_num": 75,
        "power_spec": "50 ft Anti-Tangle Swivel Cable",
        "efficiency": "CleverClean Wall & Waterline Scrubbing",
        "rating": "4.6",
        "reviews_count": 21400,
        "badge": "#1 Best Overall Pool Robot",
        "search_query": "Dolphin Nautilus CC Plus WiFi Robotic Pool Vacuum Cleaner",
        "highlight": "Dual active scrubbing brushes and top-load fine filter basket clean pool floors and vertical walls in 2 hours."
    },
    {
        "id": "pentair-superflo-vst-variable-speed",
        "name": "Pentair SuperFlo VST Variable-Speed Pool Pump (342002)",
        "brand": "Pentair",
        "category": "Variable-Speed Pool Pump",
        "max_gallons": 28000,
        "gpm_or_cap": "88 GPM Max Flow",
        "gpm_num": 88,
        "power_spec": "1.5 THP TEFC Motor (115V/230V)",
        "efficiency": "DOE Compliant High-WEF Inverter",
        "rating": "4.8",
        "reviews_count": 4620,
        "badge": "Best Pro-Grade Pump",
        "search_query": "Pentair SuperFlo VST Variable Speed Pool Pump 342002",
        "highlight": "Totally Enclosed Fan-Cooled (TEFC) commercial motor with real-time 24-hour clock and drop-in Hayward/Pentair plumbing fit."
    },
    {
        "id": "aiper-scuba-s1-cordless-robot",
        "name": "AIPER Scuba S1 Cordless Robotic Pool Cleaner for Inground Pools",
        "brand": "AIPER",
        "category": "Robotic Pool Cleaner",
        "max_gallons": 25000,
        "gpm_or_cap": "70 GPM Brushless Suction",
        "gpm_num": 70,
        "power_spec": "150-Min Cordless Li-Ion Battery",
        "efficiency": "WavePath Navigation 2.0 + Caterpillar Tracks",
        "rating": "4.6",
        "reviews_count": 6840,
        "badge": "Best Cordless Pool Robot",
        "search_query": "AIPER Scuba S1 Cordless Robotic Pool Cleaner Inground",
        "highlight": "Tangle-free cordless floor, wall, and waterline scrubber with caterpillar treads that climb 90-degree walls and drains."
    },
    {
        "id": "hayward-proseries-24-sand-filter",
        "name": "Hayward W3S244T ProSeries 24-Inch Top-Mount Pool Sand Filter",
        "brand": "Hayward",
        "category": "Pool Filter System",
        "max_gallons": 29000,
        "gpm_or_cap": "62 GPM Design Flow",
        "gpm_num": 62,
        "power_spec": "3.14 sq. ft. Filter Area (300 lbs Sand)",
        "efficiency": "7-Position VariFlo Control Valve",
        "rating": "4.7",
        "reviews_count": 7310,
        "badge": "Best Inground Sand Filter",
        "search_query": "Hayward W3S244T ProSeries 24 Inch Pool Sand Filter",
        "highlight": "Unitized corrosion-proof polymeric tank with 360-degree self-cleaning slotted laterals for crystal-clear 20-micron filtration."
    },
    {
        "id": "circupool-rj45-plus-salt-chlorinator",
        "name": "CircuPool RJ-45 PLUS Saltwater Chlorine Generator System",
        "brand": "CircuPool",
        "category": "Saltwater Chlorinator",
        "max_gallons": 45000,
        "gpm_or_cap": "2.0 lbs/Day Chlorine Output",
        "gpm_num": 95,
        "power_spec": "Titanium Reverse-Polarity Cell",
        "efficiency": "Digital Salinity & Water Temp Telemetry",
        "rating": "4.7",
        "reviews_count": 2180,
        "badge": "Best Saltwater System",
        "search_query": "CircuPool RJ 45 PLUS Saltwater Chlorine Generator",
        "highlight": "Oversized titanium cell generates silky-soft sanitized pool water without tablet chlorine pucks or red irritated eyes."
    },
    {
        "id": "intex-sx2800-krystal-clear-sand-pump",
        "name": "Intex 26647EG Krystal Clear 2,800 GPH Sand Filter Pump",
        "brand": "Intex",
        "category": "Pool Filter System",
        "max_gallons": 17200,
        "gpm_or_cap": "47 GPM (2,800 GPH)",
        "gpm_num": 47,
        "power_spec": "0.75 HP Hydro Aeration Pump",
        "efficiency": "Built-in 24-Hour Automatic Timer",
        "rating": "4.7",
        "reviews_count": 32900,
        "badge": "#1 Above-Ground Filter Pump",
        "search_query": "Intex Krystal Clear 2800 GPH Sand Filter Pump",
        "highlight": "All-in-one 6-function backwash sand filter and pump upgrade for above-ground pools up to 17,200 gallons."
    },
    {
        "id": "hayward-heatpro-110k-btu-heat-pump",
        "name": "Hayward HeatPro 110,000 BTU Titanium Heat Pump Pool Heater",
        "brand": "Hayward",
        "category": "Pool Heater & Heat Pump",
        "max_gallons": 25000,
        "gpm_or_cap": "30–75 GPM Bypass Flow",
        "gpm_num": 75,
        "power_spec": "110,000 BTU/hr (COP 5.8)",
        "efficiency": "100% Titanium Counter-Flow Heat Exchanger",
        "rating": "4.6",
        "reviews_count": 1490,
        "badge": "Best Pool Heat Pump",
        "search_query": "Hayward HeatPro Pool Heat Pump Heater Titanium",
        "highlight": "Saltwater-safe titanium heat exchanger extends swimming season by 4+ months at 70% lower operating cost than propane."
    },
    {
        "id": "betta-se-plus-solar-pool-skimmer",
        "name": "Betta SE Plus Solar-Powered Automatic Robotic Pool Surface Skimmer",
        "brand": "Betta",
        "category": "Robotic Pool Cleaner",
        "max_gallons": 40000,
        "gpm_or_cap": "24/7 Continuous Surface Skim",
        "gpm_num": 85,
        "power_spec": "Dual Solar + AC Adapter Charging",
        "efficiency": "Ultrasonic Radar Anti-Collision Sensors",
        "rating": "4.7",
        "reviews_count": 9410,
        "badge": "Best Solar Surface Skimmer",
        "search_query": "Betta SE Plus Solar Powered Automatic Robotic Pool Skimmer",
        "highlight": "Continuously skims leaves, pollen, insects, and pine needles off the water surface before they sink to the pool floor."
    },
    {
        "id": "hayward-swimclear-c4030-cartridge-filter",
        "name": "Hayward W3C4030 SwimClear 425 Sq. Ft. 4-Element Cartridge Filter",
        "name_short": "Hayward SwimClear 425 Sq.Ft.",
        "brand": "Hayward",
        "category": "Pool Filter System",
        "max_gallons": 48000,
        "gpm_or_cap": "150 GPM Max Design Flow",
        "gpm_num": 150,
        "power_spec": "425 Sq. Ft. Quad-Cluster Media",
        "efficiency": "Zero Backwash Water Waste (Low Head Loss)",
        "rating": "4.8",
        "reviews_count": 2670,
        "badge": "Best Large-Pool Filter",
        "search_query": "Hayward W3C4030 SwimClear 425 Sq Ft Cartridge Pool Filter",
        "highlight": "Quad-element polyester cartridge bank captures microscopic debris down to 10 microns with minimal pump head pressure."
    }
]


# ==============================================================================
# COMBINATORIAL ENGINE FOR 1,800 UNIQUE DAILY PRODUCT REVIEW ARTICLES
# ==============================================================================
BRANDS_MATRIX = [
    ("Hayward", "Corrosion-Proof PermaGlass XL Tank & Hydraulic Low-Head Manifold"),
    ("Pentair", "TEFC Permanent Magnet Variable-Speed Drive & Ultra-High WEF Impeller"),
    ("Dolphin Maytronics", "CleverClean Smart Gyroscopic Navigation & Dual Active Scrubbing Brushes"),
    ("BLACK+DECKER", "Energy Star Variable-Speed Inverter Motor & Quiet Enclosed Housing"),
    ("AIPER", "WavePath 2.0 Cordless Trajectory Mapping & High-Torque Caterpillar Tracks"),
    ("CircuPool", "Commercial-Grade Titanium Reverse-Polarity Electrolytic Salt Cell"),
    ("Intex", "Hydro Aeration Technology & 6-Way Integrated Multi-Port Backwash Valve"),
    ("Jandy", "Pro-Series VersaPlumb Hydraulic Efficiency & NeverLube Valve Architecture"),
    ("Polaris", "Cyclonic Vacuum Vortex Suction & All-Wheel PosiDrive Traction System"),
    ("Betta", "High-Efficiency Monocrystalline Solar Array & Twin Saltwater-Safe Propellers"),
    ("Raypak", "Cupro-Nickel Fin-Tube Heat Exchanger & Digital PID Thermostat Control"),
    ("Sta-Rite", "Fiberglass-Reinforced Composite Volute & Quick-Lock Cam-and-Ramp Strainer"),
    ("Waterway", "Crystal Water High-Flow Cartridge Cluster & 2-Inch High-Velocity Ports"),
    ("Blue Torrent", "Heavy-Duty Thermal-Overload Protected Motor & Dual-Voltage Switching"),
    ("Aquabot", "Aquasmart Gyro Algorithm & Hyper-Fine 2-Micron Microfilter Bag"),
]

MODELS_MATRIX = [
    ("1.5 HP Variable-Speed Inground Pool Pump", 24000, 78, "Variable-Speed Pool Pump", 3.1, "1.5-inch & 2.0-inch Slip Unions"),
    ("2.0 HP High-Head Variable-Speed Pool Pump", 36000, 98, "Variable-Speed Pool Pump", 4.2, "2.0-inch Heavy-Duty CPVC Unions"),
    ("3.0 HP Commercial-Grade Variable-Speed Pump", 48000, 135, "Variable-Speed Pool Pump", 5.5, "2.0-inch / 2.5-inch High-Flow Plumbing"),
    ("24-Inch Top-Mount High-Rate Sand Filter", 28000, 62, "Pool Filter System", 3.14, "1.5-inch Multi-Port 7-Way Valve"),
    ("425 Sq. Ft. Quad-Cartridge Pool Filter", 45000, 140, "Pool Filter System", 425.0, "2.0-inch Low-Friction Bulkhead Ports"),
    ("40,000-Gallon Titanium Saltwater Chlorinator", 40000, 90, "Saltwater Chlorinator", 2.0, "2.0-inch Clear Union Electrolytic Cell"),
    ("25,000-Gallon Digital Salt Chlorine Generator", 25000, 65, "Saltwater Chlorinator", 1.4, "1.5-inch / 2.0-inch Quick-Connect Unions"),
    ("Wi-Fi Wall-Climbing Robotic Pool Cleaner", 32000, 75, "Robotic Pool Cleaner", 4.5, "Low-Voltage 50-Foot Anti-Tangle Swivel Cord"),
    ("Cordless Track-Drive Robotic Pool Vacuum", 26000, 70, "Robotic Pool Cleaner", 4.0, "100% Cordless Rechargeable Lithium Pack"),
    ("Solar-Powered Autonomous Surface Pool Skimmer", 38000, 60, "Robotic Pool Cleaner", 3.5, "Cordless Top-Load UV-Resistant Debris Basket"),
    ("110,000 BTU Titanium Inverter Pool Heat Pump", 26000, 68, "Pool Heater & Heat Pump", 5.8, "2.0-inch Titanium Counter-Flow Bypass"),
    ("140,000 BTU Heavy-Duty Pool & Spa Heat Pump", 35000, 82, "Pool Heater & Heat Pump", 6.1, "2.0-inch High-Volume Saltwater-Safe Union"),
]

APPLICATIONS_MATRIX = [
    ("20,000-Gallon Inground Family Swimming Pool", 20000, "completes a full 8-hour water turnover cycle while slashing monthly utility bills by up to 75%"),
    ("30,000-Gallon Saltwater Pool with Raised Spillover Spa", 30000, "resists galvanic salt corrosion and provides enough head pressure for elevated spa jets and waterfalls"),
    ("15,000-Gallon Above-Ground Backyard Pool", 15000, "maintains crystal-clear water clarity during peak mid-summer swimmer loads and afternoon thunderstorms"),
    ("Heavily Treed Backyard Pool with Pine Needles & Oak Leaves", 22000, "captures heavy organic leaf loads and fine pollen before tannins can stain plaster or vinyl liners"),
    ("Sunbelt Year-Round Pool in Florida, Texas & Arizona", 25000, "withstands intense UV exposure and high ambient water temperatures that accelerate algae growth"),
    ("Freeform Lagoon Pool with Rock Waterfall & Deck Jets", 28000, "balances low-RPM filtration cycles with high-GPM booster flow for water features"),
    ("12,000-Gallon Fiberglass Plunge & Lap Pool", 12000, "operates at whisper-quiet decibel levels right next to patio seating and outdoor kitchens"),
    ("Large 35,000-Gallon Diving Pool with Deep-End Main Drain", 35000, "delivers powerful deep-end vertical circulation to eliminate cold thermoclines and dead zones"),
    ("High-Bather-Load Vacation Rental & Airbnb Pool", 18000, "automates daily sanitization and floor scrubbing between guest check-ins with zero manual vacuuming"),
    ("Dedicated Koi Pond, Water Garden & Natural Swim Pond", 10000, "provides continuous 24/7 bio-mechanical water turnover with minimal electrical watt draw"),
]


def get_article_blueprint(index: int) -> dict:
    """Secara deterministik menghasilkan artikel review peralatan kolam renang unik berdasarkan indeks."""
    b_idx = index % len(BRANDS_MATRIX)
    m_idx = (index // len(BRANDS_MATRIX)) % len(MODELS_MATRIX)
    a_idx = (index // (len(BRANDS_MATRIX) * len(MODELS_MATRIX))) % len(APPLICATIONS_MATRIX)

    brand_name, brand_tech = BRANDS_MATRIX[b_idx]
    model_name, max_gal, flow_gpm, category, spec_metric, plumbing_fit = MODELS_MATRIX[m_idx]
    app_title, target_gal, app_benefit = APPLICATIONS_MATRIX[a_idx]

    turnover_8hr_gpm = round(target_gal / 480, 1)
    est_turnover_hrs = round(target_gal / (flow_gpm * 60), 1)

    slug = f"review-{brand_name.lower().replace('+', '-').replace(' ', '-')}-{model_name.lower().replace(',', '').replace('.', '-').replace(' ', '-')}-{app_title.lower().split()[0]}-{app_title.lower().split()[1]}-{index + 1}"
    slug = "".join(c if c.isalnum() or c == "-" else "" for c in slug)
    while "--" in slug:
        slug = slug.replace("--", "-")

    title = f"{brand_name} {model_name} Review: Tested for {app_title}"
    search_q = f"{brand_name} {model_name}"

    return {
        "index": index,
        "slug": slug,
        "title": title,
        "brand": brand_name,
        "brand_tech": brand_tech,
        "model_name": model_name,
        "category": category,
        "max_gal": max_gal,
        "flow_gpm": flow_gpm,
        "spec_metric": spec_metric,
        "plumbing_fit": plumbing_fit,
        "app_title": app_title,
        "target_gal": target_gal,
        "app_benefit": app_benefit,
        "turnover_8hr_gpm": turnover_8hr_gpm,
        "est_turnover_hrs": est_turnover_hrs,
        "rating": "4.8" if (index % 2 == 0) else "4.7",
        "search_query": search_q,
        "affiliate_url": amazon_search_url(search_q),
    }


def load_and_advance_state() -> tuple[list[dict], list[dict]]:
    """
    Memuat daftar artikel dari posts_state.json dan menambahkan 3 artikel review baru setiap hari.
    """
    today_str = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")

    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            state = json.load(f)
    else:
        state = {
            "last_run_date": "",
            "next_index": 0,
            "published_articles": []
        }

    newly_added = []
    if len(state["published_articles"]) == 0:
        count_to_add = 6  # Inisialisasi awal 6 artikel perdana
    else:
        count_to_add = DAILY_NEW_ARTICLES  # Tambah 3 artikel berbeda setiap hari

    for _ in range(count_to_add):
        idx = state["next_index"]
        bp = get_article_blueprint(idx)
        entry = {
            "index": idx,
            "slug": bp["slug"],
            "date": today_str,
            "title": bp["title"]
        }
        state["published_articles"].append(entry)
        newly_added.append({**bp, "date": today_str})
        state["next_index"] = idx + 1

    state["last_run_date"] = today_str

    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)

    all_articles = []
    for item in reversed(state["published_articles"]):
        bp = get_article_blueprint(item["index"])
        bp["date"] = item["date"]
        all_articles.append(bp)

    return all_articles, newly_added


# ==============================================================================
# SHARED CSS — ARCHITECTURAL GREY BACKGROUND THEME
# ==============================================================================
GLOBAL_CSS = """
:root {
  --bg-page: #cbd5e1;        /* Latar belakang abu-abu utama sesuai instruksi */
  --bg-section: #e2e8f0;     /* Latar belakang abu-abu kontainer seksi */
  --bg-card: #f1f5f9;        /* Latar belakang abu-abu terang kartu produk & kalkulator */
  --bg-dark: #1e293b;        /* Slate gelap untuk header & tabel */
  --bg-darker: #0f172a;      /* Hitam abu-abu untuk banner & footer */
  --border-grey: #94a3b8;    /* Garis batas abu-abu tegas */
  --text-main: #0f172a;
  --text-muted: #334155;
  --accent-amazon: #ff9900;
  --accent-aqua: #0369a1;
  --accent-green: #15803d;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  background-color: var(--bg-page);
  color: var(--text-main);
  line-height: 1.6;
}
a { color: var(--accent-aqua); text-decoration: none; }
.container { max-width: 1240px; margin: 0 auto; padding: 0 18px; }

/* TOP PROMOTIONAL BANNER */
.top-promo-banner {
  background: linear-gradient(90deg, #0f172a 0%, #334155 50%, #1e293b 100%);
  color: #ffffff;
  padding: 12px 16px;
  border-bottom: 3px solid var(--accent-amazon);
  text-align: center;
  font-size: 0.94rem;
}
.top-promo-banner .badge-live {
  background: var(--accent-amazon);
  color: #0f172a;
  font-weight: 900;
  padding: 3px 10px;
  border-radius: 4px;
  margin-right: 10px;
  text-transform: uppercase;
  font-size: 0.78rem;
}
.top-promo-banner a.banner-cta {
  display: inline-block;
  margin-left: 12px;
  background: #38bdf8;
  color: #0f172a;
  font-weight: 800;
  padding: 4px 14px;
  border-radius: 5px;
  text-decoration: none;
}
.top-promo-banner a.banner-cta:hover { background: #7dd3fc; }

/* STICKY NAVIGATION HEADER */
header.site-header {
  background-color: var(--bg-dark);
  color: #f8fafc;
  padding: 16px 0;
  box-shadow: 0 3px 10px rgba(0,0,0,0.22);
  position: sticky;
  top: 0;
  z-index: 100;
}
.nav-flex {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  gap: 14px;
}
.brand-logo {
  font-size: 1.55rem;
  font-weight: 900;
  color: #ffffff;
  letter-spacing: -0.5px;
}
.brand-logo span { color: var(--accent-amazon); }
.nav-links {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  list-style: none;
}
.nav-links a {
  color: #e2e8f0;
  font-weight: 600;
  font-size: 0.92rem;
  padding: 6px 10px;
  border-radius: 5px;
}
.nav-links a:hover { background: #334155; color: var(--accent-amazon); }

/* HERO BANNER */
.hero-banner {
  background: linear-gradient(135deg, #334155 0%, #1e293b 100%);
  color: #f8fafc;
  padding: 34px 26px;
  margin: 24px 0;
  border-radius: 12px;
  border: 2px solid #64748b;
  box-shadow: 0 8px 20px rgba(0,0,0,0.14);
}
.hero-grid {
  display: grid;
  grid-template-columns: 1.25fr 0.75fr;
  gap: 24px;
  align-items: center;
}
@media (max-width: 860px) { .hero-grid { grid-template-columns: 1fr; } }
.hero-banner h1 {
  font-size: 2.05rem;
  line-height: 1.22;
  margin-bottom: 12px;
  color: #ffffff;
}
.hero-banner p { color: #cbd5e1; font-size: 1.03rem; margin-bottom: 18px; }
.hero-deal-box {
  background: #0f172a;
  border: 2px solid var(--accent-amazon);
  padding: 20px;
  border-radius: 10px;
  text-align: center;
}
.hero-deal-box h3 { color: var(--accent-amazon); margin-bottom: 8px; font-size: 1.18rem; }

/* BUTTONS */
.btn-amazon {
  display: inline-block;
  background: linear-gradient(180deg, #ffd814 0%, #ff9900 100%);
  color: #0f172a !important;
  font-weight: 800;
  padding: 11px 18px;
  border-radius: 6px;
  border: 1px solid #d97706;
  text-align: center;
  cursor: pointer;
  text-decoration: none;
  box-shadow: 0 2px 5px rgba(0,0,0,0.15);
}
.btn-amazon:hover { background: linear-gradient(180deg, #f7ca00 0%, #e68a00 100%); }
.btn-outline {
  display: inline-block;
  padding: 9px 14px;
  border: 2px solid #1e293b;
  color: #0f172a;
  font-weight: 700;
  border-radius: 6px;
  font-size: 0.88rem;
}
.btn-outline:hover { background: #1e293b; color: #ffffff; }

/* GREY SECTION WRAPPERS */
.grey-section {
  background-color: var(--bg-section);
  border: 1px solid var(--border-grey);
  border-radius: 12px;
  padding: 26px;
  margin-bottom: 26px;
  box-shadow: 0 3px 8px rgba(0,0,0,0.06);
}
.section-title {
  font-size: 1.55rem;
  font-weight: 800;
  color: #0f172a;
  margin-bottom: 8px;
  border-left: 6px solid var(--accent-amazon);
  padding-left: 12px;
}
.section-sub { color: var(--text-muted); margin-bottom: 20px; font-size: 0.96rem; }

/* INTERACTIVE POOL CALCULATOR */
.calc-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
}
@media (max-width: 860px) { .calc-grid { grid-template-columns: 1fr; } }
.calc-panel {
  background: var(--bg-card);
  border: 1px solid var(--border-grey);
  padding: 22px;
  border-radius: 10px;
}
.preset-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 16px;
}
.preset-btn {
  background: #cbd5e1;
  border: 1px solid #64748b;
  color: #0f172a;
  padding: 7px 12px;
  border-radius: 6px;
  font-size: 0.83rem;
  font-weight: 700;
  cursor: pointer;
}
.preset-btn:hover { background: #94a3b8; }
.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}
.form-group { margin-bottom: 14px; }
.form-group label {
  display: block;
  font-weight: 700;
  margin-bottom: 5px;
  font-size: 0.9rem;
  color: #1e293b;
}
.form-group input, .form-group select {
  width: 100%;
  padding: 10px 12px;
  border: 1px solid #64748b;
  border-radius: 6px;
  background: #ffffff;
  font-size: 0.98rem;
  color: #0f172a;
}
.metrics-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  margin-bottom: 16px;
}
.metric-card {
  background: #e2e8f0;
  border: 1px solid #94a3b8;
  padding: 14px;
  border-radius: 8px;
  text-align: center;
}
.metric-card .val {
  font-size: 1.5rem;
  font-weight: 900;
  color: #0f172a;
}
.metric-card .lbl {
  font-size: 0.78rem;
  font-weight: 700;
  color: #334155;
  text-transform: uppercase;
}
.rec-box {
  background: #ffffff;
  border: 2px solid var(--accent-green);
  border-radius: 8px;
  padding: 16px;
  margin-top: 12px;
}
.rec-box h4 { color: var(--accent-green); font-size: 1.04rem; margin-bottom: 6px; }

/* SEARCH & FILTER BAR */
.search-bar {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 18px;
}
.search-input {
  flex: 1;
  min-width: 240px;
  padding: 12px 15px;
  border: 2px solid #475569;
  border-radius: 8px;
  font-size: 1rem;
  background: #ffffff;
}
.filter-select {
  padding: 12px 15px;
  border: 2px solid #475569;
  border-radius: 8px;
  font-size: 0.95rem;
  background: #ffffff;
  font-weight: 700;
}

/* PRODUCT CARDS & DAILY ARTICLES GRID */
.product-grid, .articles-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 18px;
}
.product-card, .article-card {
  background: var(--bg-card);
  border: 1px solid var(--border-grey);
  border-radius: 10px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.badge-tag {
  display: inline-block;
  background: #1e293b;
  color: var(--accent-amazon);
  font-size: 0.75rem;
  font-weight: 800;
  padding: 4px 10px;
  border-radius: 4px;
  margin-bottom: 10px;
  align-self: flex-start;
  text-transform: uppercase;
}
.spec-box {
  list-style: none;
  margin: 10px 0 14px;
  font-size: 0.88rem;
  background: #e2e8f0;
  padding: 10px 12px;
  border-radius: 6px;
}
.spec-box li { margin-bottom: 4px; }

/* COMPARISON TABLE */
.table-wrap { overflow-x: auto; }
table.comp-table {
  width: 100%;
  border-collapse: collapse;
  background: #f8fafc;
  border-radius: 8px;
  overflow: hidden;
}
table.comp-table th {
  background: #1e293b;
  color: #ffffff;
  text-align: left;
  padding: 13px 12px;
  font-size: 0.86rem;
  text-transform: uppercase;
}
table.comp-table td {
  padding: 12px;
  border-bottom: 1px solid #cbd5e1;
  font-size: 0.91rem;
}
table.comp-table tr:nth-child(even) { background: #e2e8f0; }

/* FAQ ACCORDION */
details.faq-item {
  background: var(--bg-card);
  border: 1px solid var(--border-grey);
  border-radius: 8px;
  padding: 14px 18px;
  margin-bottom: 12px;
}
details.faq-item summary {
  font-weight: 800;
  font-size: 1.02rem;
  cursor: pointer;
  color: #0f172a;
}
details.faq-item p { margin-top: 10px; color: #334155; font-size: 0.95rem; }

/* SITEMAP DIRECTORY LIST */
.sitemap-columns {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
}
.sitemap-box {
  background: var(--bg-card);
  border: 1px solid var(--border-grey);
  padding: 18px;
  border-radius: 8px;
}
.sitemap-box h3 { margin-bottom: 10px; font-size: 1.1rem; color: #0f172a; }
.sitemap-box ul { padding-left: 18px; font-size: 0.9rem; line-height: 1.8; }

/* FOOTER */
footer.site-footer {
  background: var(--bg-darker);
  color: #cbd5e1;
  padding: 36px 0;
  margin-top: 40px;
  border-top: 4px solid var(--accent-amazon);
  font-size: 0.9rem;
}
.footer-links {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  margin-bottom: 14px;
}
.footer-links a { color: #f8fafc; font-weight: 600; }
"""


# ==============================================================================
# HTML PAGE GENERATORS
# ==============================================================================
def build_article_page(article: dict, recent_articles: list[dict]) -> str:
    """Membangun halaman HTML artikel review peralatan kolam renang lengkap dengan kalkulator & Schema FAQ."""
    related_links = ""
    for rel in recent_articles[:8]:
        if rel["slug"] == article["slug"]:
            continue
        related_links += f"""
        <li>
          <a href="{BASE_URL}/reviews/{rel['slug']}.html"><strong>{rel['title']}</strong></a>
          <span> (Up to {rel['max_gal']:,} Gal / {rel['flow_gpm']} GPM — {rel['date']})</span>
        </li>
        """

    pool_scenarios = [
        ("10,000-Gallon Plunge Pool / Large Koi Pond", 10000),
        ("15,000-Gallon Above-Ground Round/Oval Pool", 15000),
        ("20,000-Gallon Standard Inground Family Pool", 20000),
        ("28,000-Gallon Saltwater Pool + Spillover Spa", 28000),
        ("36,000-Gallon Deep Diving Pool", 36000),
    ]
    scenario_rows = ""
    for p_name, gal in pool_scenarios:
        req_gpm = round(gal / 480, 1)
        turnover_hrs = round(gal / (article["flow_gpm"] * 60), 1)
        fit_status = "Optimal Sizing Match" if article["max_gal"] >= gal else "Step Up to Higher-Capacity Model"
        scenario_rows += f"""
        <tr>
          <td><strong>{p_name}</strong></td>
          <td>{req_gpm} GPM (for 8-Hr Turnover)</td>
          <td>~{turnover_hrs} Hours per Full Cycle</td>
          <td>{fit_status}</td>
        </tr>
        """

    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": f"What pool size is the {article['brand']} {article['model_name']} rated for?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": f"The {article['brand']} {article['model_name']} supports swimming pools up to {article['max_gal']:,} gallons with a rated hydraulic capacity of {article['flow_gpm']} GPM."
                }
            },
            {
                "@type": "Question",
                "name": f"How fast will the {article['brand']} {article['model_name']} turn over a {article['target_gal']:,}-gallon pool?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": f"At {article['flow_gpm']} GPM, it completes one full water turnover of a {article['target_gal']:,}-gallon pool in approximately {article['est_turnover_hrs']} hours."
                }
            }
        ]
    }

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{article['title']} ({article['date']} Hydraulic Test &amp; Sizing Review)</title>
  <meta name="description" content="In-depth hydraulic review of the {article['brand']} {article['model_name']} ({article['max_gal']:,} Gal, {article['flow_gpm']} GPM) for {article['app_title']}. Includes turnover calculator and Amazon price check." />
  <link rel="canonical" href="{BASE_URL}/reviews/{article['slug']}.html" />
  <meta property="og:title" content="{article['title']}" />
  <meta property="og:description" content="Rated for pools up to {article['max_gal']:,} gallons at {article['flow_gpm']} GPM with {article['brand_tech']}." />
  <meta property="og:type" content="article" />
  <meta property="og:url" content="{BASE_URL}/reviews/{article['slug']}.html" />
  <style>{GLOBAL_CSS}</style>
  <script type="application/ld+json">{json.dumps(faq_schema)}</script>
</head>
<body>
  <div class="top-promo-banner">
    <span class="badge-live">POOL GEAR DEAL ALERT</span>
    Check Live Amazon Discount &amp; Prime Shipping on <strong>{article['brand']} {article['model_name']}</strong>
    <a class="banner-cta" href="{article['affiliate_url']}" target="_blank" rel="nofollow sponsored noopener">Check Price on Amazon &rarr;</a>
  </div>

  <header class="site-header">
    <div class="container nav-flex">
      <a href="{BASE_URL}/index.html" class="brand-logo">AquaFlow<span>Calc</span></a>
      <ul class="nav-links">
        <li><a href="{BASE_URL}/index.html#calculator">Pool Gallons &amp; GPM Calculator</a></li>
        <li><a href="{BASE_URL}/index.html#search-section">Search Products</a></li>
        <li><a href="{BASE_URL}/index.html#bestsellers">Best Sellers</a></li>
        <li><a href="{BASE_URL}/index.html#comparison">Comparison Table</a></li>
        <li><a href="{BASE_URL}/index.html#daily-reviews">Daily Reviews</a></li>
        <li><a href="{BASE_URL}/sitemap.html">Site Map</a></li>
      </ul>
    </div>
  </header>

  <main class="container" style="margin-top:24px;">
    <article class="grey-section">
      <div style="font-size:0.82rem; font-weight:700; color:#334155; text-transform:uppercase; margin-bottom:6px;">
        Published: {article['date']} &bull; Category: {article['category']} &bull; Verified Rating: ★ {article['rating']}/5.0
      </div>
      <h1 style="font-size:1.95rem; margin-bottom:14px; color:#0f172a;">{article['title']}</h1>
      <p style="font-size:1.05rem; color:#334155; margin-bottom:20px;">
        Properly sizing equipment for a <strong>{article['app_title']}</strong> requires matching total pool volume in gallons with dynamic head pressure and GPM flow rate. In this engineering evaluation, we test how the <strong>{article['brand']} {article['model_name']}</strong> (rated up to <strong>{article['max_gal']:,} gallons</strong> and <strong>{article['flow_gpm']} GPM</strong>) {article['app_benefit']}.
      </p>

      <div class="hero-deal-box" style="margin-bottom:24px; text-align:left; display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:16px;">
        <div>
          <h3 style="margin-bottom:4px;">{article['brand']} {article['model_name']} — Amazon Availability</h3>
          <p style="color:#cbd5e1; font-size:0.93rem;">Equipped with {article['brand_tech']} | Max Pool Volume: {article['max_gal']:,} Gal | Flow: {article['flow_gpm']} GPM</p>
        </div>
        <a class="btn-amazon" href="{article['affiliate_url']}" target="_blank" rel="nofollow sponsored noopener">Check Current Price on Amazon &rarr;</a>
      </div>

      <h2 class="section-title">1. Hydraulic Specifications &amp; Plumbing Compatibility</h2>
      <div class="table-wrap" style="margin:16px 0 26px;">
        <table class="comp-table">
          <thead>
            <tr>
              <th>Parameter</th>
              <th>Measured Specification</th>
              <th>Real-World Pool Impact</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Maximum Pool Capacity</strong></td>
              <td>Up to {article['max_gal']:,} Gallons</td>
              <td>Turns over a {article['target_gal']:,}-gallon pool in ~{article['est_turnover_hrs']} hours</td>
            </tr>
            <tr>
              <td><strong>Design Flow Rate</strong></td>
              <td>{article['flow_gpm']} GPM ({article['flow_gpm'] * 60:,} GPH)</td>
              <td>Exceeds the {article['turnover_8hr_gpm']} GPM baseline needed for an 8-hour cycle</td>
            </tr>
            <tr>
              <td><strong>Core Engineering Feature</strong></td>
              <td>{article['brand_tech']}</td>
              <td>Built for continuous saltwater, chlorine, and UV durability</td>
            </tr>
            <tr>
              <td><strong>Plumbing Union Fit</strong></td>
              <td>{article['plumbing_fit']}</td>
              <td>Direct drop-in installation for Schedule 40 PVC equipment pads</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2 class="section-title">2. Interactive Pool Turnover Calculator for {article['brand']}</h2>
      <p class="section-sub">Enter your pool's water volume in gallons below to see how fast this {article['flow_gpm']} GPM system cycles your entire pool:</p>
      <div class="calc-panel" style="margin-bottom:26px;">
        <div class="calc-grid">
          <div class="form-group">
            <label for="artGalInput">Your Pool Volume (Gallons):</label>
            <input type="number" id="artGalInput" value="{article['target_gal']}" min="1000" max="60000" step="500" oninput="calcArticleTurnover()" />
            <p style="font-size:0.86rem; color:#334155; margin-top:6px;">Formula: <code>Pool Gallons &divide; ({article['flow_gpm']} GPM &times; 60 Min)</code></p>
          </div>
          <div class="metric-card">
            <div class="lbl">Full Water Turnover Time</div>
            <div class="val" id="artTurnoverOut">{article['est_turnover_hrs']} Hours</div>
            <div style="margin-top:10px;">
              <a class="btn-amazon" href="{article['affiliate_url']}" target="_blank" rel="nofollow sponsored noopener">Order {article['brand']} on Amazon</a>
            </div>
          </div>
        </div>
      </div>

      <h2 class="section-title">3. Pool Volume &amp; Turnover Compatibility Matrix</h2>
      <div class="table-wrap" style="margin:16px 0 26px;">
        <table class="comp-table">
          <thead>
            <tr>
              <th>Pool Size Scenario</th>
              <th>Min. GPM for 8-Hr Turnover</th>
              <th>{article['brand']} Cycle Time</th>
              <th>Sizing Verdict</th>
            </tr>
          </thead>
          <tbody>
            {scenario_rows}
          </tbody>
        </table>
      </div>

      <h2 class="section-title">4. Pros, Cons &amp; Field Verdict</h2>
      <div class="calc-grid" style="margin:16px 0 26px;">
        <div class="calc-panel" style="border-left:5px solid #15803d;">
          <h3 style="color:#15803d; margin-bottom:10px;">Key Strengths (Pros)</h3>
          <ul style="padding-left:18px; font-size:0.94rem;">
            <li><strong>{article['brand_tech']}</strong> ensures long service life in harsh poolside conditions.</li>
            <li>Delivers <strong>{article['flow_gpm']} GPM</strong> to cycle a {article['target_gal']:,}-gallon pool in ~{article['est_turnover_hrs']} hours.</li>
            <li>Includes <strong>{article['plumbing_fit']}</strong> for straightforward DIY or pro installation.</li>
          </ul>
        </div>
        <div class="calc-panel" style="border-left:5px solid #b91c1c;">
          <h3 style="color:#b91c1c; margin-bottom:10px;">Things to Consider (Cons)</h3>
          <ul style="padding-left:18px; font-size:0.94rem;">
            <li>Pools larger than {article['max_gal']:,} gallons should step up to the next horsepower or surface-area tier.</li>
            <li>Requires routine strainer basket or filter inspection to maintain peak {article['flow_gpm']} GPM throughput.</li>
          </ul>
        </div>
      </div>

      <div class="hero-deal-box">
        <h3>Ready to Upgrade Your {article['app_title']}?</h3>
        <p style="color:#cbd5e1; margin-bottom:14px;">Check live seasonal pricing, warranty details, and verified pool owner reviews on Amazon.</p>
        <a class="btn-amazon" href="{article['affiliate_url']}" target="_blank" rel="nofollow sponsored noopener">View {article['brand']} {article['model_name']} on Amazon &rarr;</a>
      </div>
    </article>

    <section class="grey-section">
      <h2 class="section-title">More Daily Pool &amp; Pond Equipment Reviews</h2>
      <ul style="padding-left:20px; line-height:1.9;">
        {related_links}
      </ul>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-links">
        <a href="{BASE_URL}/index.html">Home &amp; Pool Calculator</a>
        <a href="{BASE_URL}/index.html#bestsellers">Best Sellers</a>
        <a href="{BASE_URL}/index.html#comparison">Comparison Chart</a>
        <a href="{BASE_URL}/sitemap.html">HTML Site Map</a>
        <a href="{BASE_URL}/sitemap.xml">XML Sitemap</a>
        <a href="{BASE_URL}/feed.xml">RSS Feed</a>
      </div>
      <p>Affiliate Disclosure: AquaFlowCalc participates in the Amazon Services LLC Associates Program (StoreID: {AFFILIATE_TAG}). As an Amazon Associate, we earn from qualifying purchases.</p>
    </div>
  </footer>

  <script>
    function calcArticleTurnover() {{
      var gal = parseFloat(document.getElementById('artGalInput').value) || 10000;
      var gpm = {article['flow_gpm']};
      var hrs = (gal / (gpm * 60)).toFixed(1);
      document.getElementById('artTurnoverOut').textContent = hrs + ' Hours';
    }}
  </script>
</body>
</html>"""


def build_html_sitemap_page(all_articles: list[dict]) -> str:
    """Membangun halaman direktori HTML Site Map lengkap (sitemap.html) untuk pengunjung dan mesin pencari."""
    article_links = ""
    for art in all_articles:
        article_links += f"""
        <li>
          <a href="{BASE_URL}/reviews/{art['slug']}.html"><strong>{art['title']}</strong></a>
          <span> — {art['category']} (Up to {art['max_gal']:,} Gal / {art['flow_gpm']} GPM | Published {art['date']})</span>
        </li>
        """

    product_links = ""
    for p in CORE_PRODUCTS:
        product_links += f"""
        <li>
          <a href="{amazon_search_url(p['search_query'])}" target="_blank" rel="nofollow sponsored noopener">{p['name']} ({p['gpm_or_cap']})</a>
          <span> — {p['badge']}</span>
        </li>
        """

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Complete Site Map — AquaFlowCalc Pool Volume, Pump GPM &amp; Daily Equipment Reviews</title>
  <meta name="description" content="Complete HTML Site Map indexing all interactive pool gallon calculators, variable-speed pump GPM sizing tools, comparison tables, and {len(all_articles)} daily product reviews." />
  <link rel="canonical" href="{BASE_URL}/sitemap.html" />
  <style>{GLOBAL_CSS}</style>
</head>
<body>
  <header class="site-header">
    <div class="container nav-flex">
      <a href="{BASE_URL}/index.html" class="brand-logo">AquaFlow<span>Calc</span></a>
      <ul class="nav-links">
        <li><a href="{BASE_URL}/index.html#calculator">Pool Calculator</a></li>
        <li><a href="{BASE_URL}/index.html#bestsellers">Best Sellers</a></li>
        <li><a href="{BASE_URL}/index.html#comparison">Comparison Table</a></li>
        <li><a href="{BASE_URL}/index.html#daily-reviews">Daily Reviews</a></li>
        <li><a href="{BASE_URL}/sitemap.xml">XML Sitemap</a></li>
      </ul>
    </div>
  </header>

  <main class="container" style="margin-top:24px;">
    <section class="grey-section">
      <h1 class="section-title">AquaFlowCalc — Complete HTML Site Map &amp; Archive</h1>
      <p class="section-sub">Full index of all interactive pool &amp; pond sizing calculators, comparison charts, XML feeds, and {len(all_articles)} automated daily product review articles.</p>

      <div class="sitemap-columns" style="margin-bottom:24px;">
        <div class="sitemap-box">
          <h3>Core Calculators &amp; Sections</h3>
          <ul>
            <li><a href="{BASE_URL}/index.html">Homepage &amp; 4-in-1 Pool Gallons / GPM Calculator</a></li>
            <li><a href="{BASE_URL}/index.html#calculator">Interactive Pool Volume, Pump GPM, Filter &amp; Salt Cell Calculator</a></li>
            <li><a href="{BASE_URL}/index.html#search-section">Real-Time Pool Pump, Filter &amp; Robot Finder</a></li>
            <li><a href="{BASE_URL}/index.html#bestsellers">Top 10 Best-Selling Amazon Pool Systems</a></li>
            <li><a href="{BASE_URL}/index.html#comparison">Side-by-Side Technical Comparison Table</a></li>
            <li><a href="{BASE_URL}/index.html#faq">Pool Turnover, Pipe Flow &amp; Salt Sizing FAQ</a></li>
          </ul>
        </div>
        <div class="sitemap-box">
          <h3>Search Engine &amp; Syndication Feeds</h3>
          <ul>
            <li><a href="{BASE_URL}/sitemap.xml">Primary XML Sitemap (sitemap.xml)</a></li>
            <li><a href="{BASE_URL}/feed.xml">Automated Daily Review RSS 2.0 Feed (feed.xml)</a></li>
            <li><a href="{BASE_URL}/robots.txt">Crawler Directives (robots.txt)</a></li>
          </ul>
        </div>
      </div>

      <div class="sitemap-box" style="margin-bottom:24px;">
        <h3>All Daily Pool &amp; Pond Product Review Articles ({len(all_articles)} Indexed Pages)</h3>
        <ul>
          {article_links}
        </ul>
      </div>

      <div class="sitemap-box">
        <h3>Direct Amazon Best-Seller Links (StoreID: {AFFILIATE_TAG})</h3>
        <ul>
          {product_links}
        </ul>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container">
      <p>&copy; {datetime.datetime.now(datetime.timezone.utc).year} AquaFlowCalc (Amazon StoreID: {AFFILIATE_TAG}). <a href="{BASE_URL}/index.html" style="color:#ffffff;">Return to Pool Calculator</a></p>
    </div>
  </footer>
</body>
</html>"""


def build_index_page(all_articles: list[dict]) -> str:
    """Membangun halaman utama (index.html) dengan Kalkulator 4-in-1, Banner, Search, Best Sellers, Comparison, Daily Reviews, FAQ, dan Site Map."""
    bestsellers_cards = ""
    for p in CORE_PRODUCTS:
        aff_url = amazon_search_url(p["search_query"])
        bestsellers_cards += f"""
        <div class="product-card" data-search="{p['name'].lower()} {p['brand'].lower()} {p['category'].lower()} {p['highlight'].lower()}" data-category="{p['category']}">
          <div>
            <span class="badge-tag">{p['badge']}</span>
            <h3 style="font-size:1.14rem; margin-bottom:8px;">{p['name']}</h3>
            <p style="font-size:0.88rem; color:#334155; margin-bottom:8px;">{p['highlight']}</p>
            <ul class="spec-box">
              <li><strong>Max Pool Size:</strong> Up to {p['max_gallons']:,} Gallons</li>
              <li><strong>Flow / Output:</strong> {p['gpm_or_cap']}</li>
              <li><strong>Hardware Spec:</strong> {p['power_spec']}</li>
              <li><strong>Efficiency:</strong> {p['efficiency']}</li>
              <li><strong>Buyer Rating:</strong> ★ {p['rating']}/5 ({p['reviews_count']}+ reviews)</li>
            </ul>
          </div>
          <a class="btn-amazon" href="{aff_url}" target="_blank" rel="nofollow sponsored noopener">Check Price on Amazon &rarr;</a>
        </div>
        """

    comparison_rows = ""
    for p in CORE_PRODUCTS:
        aff_url = amazon_search_url(p["search_query"])
        comparison_rows += f"""
        <tr>
          <td><strong>{p['name']}</strong><br/><span style="font-size:0.78rem; color:#334155;">{p['badge']}</span></td>
          <td>{p['category']}</td>
          <td><strong>{p['max_gallons']:,} Gal</strong></td>
          <td>{p['gpm_or_cap']}</td>
          <td>{p['power_spec']}</td>
          <td>{p['efficiency']}</td>
          <td>★ {p['rating']}</td>
          <td><a class="btn-amazon" style="padding:7px 12px; font-size:0.82rem;" href="{aff_url}" target="_blank" rel="nofollow sponsored noopener">View Deal</a></td>
        </tr>
        """

    daily_cards = ""
    for art in all_articles[:36]:
        daily_cards += f"""
        <div class="article-card" data-art-search="{art['title'].lower()} {art['brand'].lower()} {art['category'].lower()} {art['app_title'].lower()}">
          <div>
            <div style="font-size:0.78rem; font-weight:700; color:#334155; text-transform:uppercase; margin-bottom:6px;">
              {art['date']} &bull; {art['category']} &bull; Up to {art['max_gal']:,} Gal
            </div>
            <h3 style="font-size:1.12rem; margin-bottom:10px;">
              <a href="{BASE_URL}/reviews/{art['slug']}.html" style="color:#0f172a;">{art['title']}</a>
            </h3>
            <p style="font-size:0.9rem; color:#334155; margin-bottom:14px;">
              Rated at <strong>{art['flow_gpm']} GPM</strong> with {art['brand_tech']}. Cycles a {art['target_gal']:,}-gallon pool in <strong>~{art['est_turnover_hrs']} hours</strong>.
            </p>
          </div>
          <div style="display:flex; gap:10px; flex-wrap:wrap;">
            <a class="btn-outline" href="{BASE_URL}/reviews/{art['slug']}.html">Read Full Review</a>
            <a class="btn-amazon" style="padding:9px 14px; font-size:0.86rem;" href="{art['affiliate_url']}" target="_blank" rel="nofollow sponsored noopener">Amazon Price</a>
          </div>
        </div>
        """

    sitemap_preview_links = ""
    for art in all_articles[:18]:
        sitemap_preview_links += f"""
        <li><a href="{BASE_URL}/reviews/{art['slug']}.html">{art['title']}</a> ({art['date']})</li>
        """

    faqs = [
        (
            "How do I calculate how many gallons my swimming pool holds?",
            "Multiply your pool's Length (ft) by Width (ft) by Average Depth (ft) to get cubic feet, then multiply by 7.48 gallons per cubic foot for a rectangular pool. For round or oval pools, multiply Length x Width x Average Depth x 5.9. For kidney or freeform pools, multiply Length x Width x Average Depth x 6.7."
        ),
        (
            "How do I calculate the right Pool Pump GPM (Gallons Per Minute) flow rate?",
            "Divide your total pool volume in gallons by 480 minutes (which equals one complete 8-hour water turnover cycle). For example, a 24,000-gallon pool requires a minimum continuous flow rate of 50 GPM (24,000 / 480 = 50 GPM). Choosing a variable-speed pump rated at 75–98 GPM lets you run at low, whisper-quiet RPMs while easily meeting your turnover target."
        ),
        (
            "What is the maximum safe GPM flow rate for 1.5-inch vs. 2.0-inch PVC pool plumbing?",
            "To keep water velocity below the industry-standard 6 to 8 feet per second and prevent cavitation or excessive head loss, 1.5-inch Schedule 40 PVC plumbing safely handles up to 42–45 GPM, whereas 2.0-inch PVC plumbing safely handles up to 73–80 GPM, and 2.5-inch PVC handles up to 115 GPM."
        ),
        (
            "How do I size a Saltwater Chlorinator Cell for my pool?",
            "Always oversize your saltwater chlorine generator by 1.5x to 2.0x your actual pool volume in gallons. For a 20,000-gallon pool, choose a 35,000- to 45,000-gallon rated salt cell so you can run the electrolytic cell at 50% output—doubling the titanium cell's lifespan and keeping chlorine levels rock-steady during midsummer heatwaves."
        ),
        (
            "Why should I switch to a Variable-Speed Pool Pump instead of a single-speed pump?",
            "By the Pump Affinity Law, cutting pump motor RPM in half reduces hydraulic flow by 50% but slashes electrical power consumption by 87.5% (one-eighth the wattage). An Energy Star variable-speed pool pump typically saves $450 to $900 per year in electricity while operating nearly silently."
        ),
        (
            "How many BTUs do I need for a Pool Heat Pump or Heater?",
            "Calculate your pool surface area in square feet (Length x Width) and multiply by 250 to 300 BTU/hr. A standard 16x32 ft (512 sq. ft.) inground pool requires a 110,000 to 140,000 BTU titanium heat pump to raise water temperature efficiently and maintain 84°F comfort."
        )
    ]

    faq_html = ""
    faq_entities = []
    for q, a in faqs:
        faq_html += f"""
        <details class="faq-item" open>
          <summary>{q}</summary>
          <p>{a}</p>
        </details>
        """
        faq_entities.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a}
        })

    json_ld = [
        {
            "@context": "https://schema.org",
            "@type": "WebApplication",
            "name": "AquaFlowCalc — Swimming Pool Volume (Gallons), Pump GPM, Filter & Salt Cell Calculator",
            "applicationCategory": "UtilitiesApplication",
            "operatingSystem": "All",
            "url": f"{BASE_URL}/index.html",
            "description": "Free interactive swimming pool volume (gallons), variable-speed pump flow rate (GPM), saltwater chlorinator, and pool heater sizing calculator."
        },
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": faq_entities
        }
    ]

    js_products = json.dumps([
        {
            "name": p["name"],
            "category": p["category"],
            "max_gallons": p["max_gallons"],
            "gpm_or_cap": p["gpm_or_cap"],
            "gpm_num": p["gpm_num"],
            "power_spec": p["power_spec"],
            "badge": p["badge"],
            "highlight": p["highlight"],
            "url": amazon_search_url(p["search_query"])
        }
        for p in CORE_PRODUCTS
    ])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>AquaFlowCalc — Pool Volume (Gallons), Variable-Speed Pump GPM, Filter &amp; Salt Cell Calculator</title>
  <meta name="description" content="Calculate exact swimming pool gallons, required pump flow rate (GPM), saltwater chlorinator cell rating, and pool heater BTU in seconds. Compare top pool gear &amp; daily reviews." />
  <link rel="canonical" href="{BASE_URL}/index.html" />
  <link rel="alternate" type="application/rss+xml" title="AquaFlowCalc Daily Pool Equipment Reviews RSS" href="{BASE_URL}/feed.xml" />
  <meta property="og:title" content="AquaFlowCalc — Interactive Pool Gallons, Pump GPM &amp; Salt Cell Sizing Calculator" />
  <meta property="og:description" content="Size your variable-speed pool pump, sand/cartridge filter, saltwater generator, and robotic cleaner with instant hardware matches." />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{BASE_URL}/index.html" />
  <style>{GLOBAL_CSS}</style>
  <script type="application/ld+json">{json.dumps(json_ld)}</script>
</head>
<body>

  <!-- TOP STICKY PROMO BANNER -->
  <div class="top-promo-banner">
    <span class="badge-live">POOL &amp; SPA DEALS</span>
    Save Up to 40% on Variable-Speed Pool Pumps, Dolphin &amp; AIPER Pool Robots, and Saltwater Chlorinators on Amazon
    <a class="banner-cta" href="{amazon_search_url('Variable Speed Pool Pump Robotic Pool Cleaner Saltwater System Deal')}" target="_blank" rel="nofollow sponsored noopener">Claim Today's Amazon Coupons &rarr;</a>
  </div>

  <!-- NAVIGATION HEADER -->
  <header class="site-header">
    <div class="container nav-flex">
      <a href="{BASE_URL}/index.html" class="brand-logo">AquaFlow<span>Calc</span></a>
      <ul class="nav-links">
        <li><a href="#calculator">Pool &amp; GPM Calculator</a></li>
        <li><a href="#search-section">Search Products</a></li>
        <li><a href="#bestsellers">Best Sellers</a></li>
        <li><a href="#comparison">Comparison Chart</a></li>
        <li><a href="#daily-reviews">Daily Reviews ({len(all_articles)})</a></li>
        <li><a href="#faq">FAQ</a></li>
        <li><a href="#sitemap-section">Site Map</a></li>
      </ul>
    </div>
  </header>

  <main class="container">

    <!-- HERO BANNER -->
    <section class="hero-banner">
      <div class="hero-grid">
        <div>
          <h1>Swimming Pool Volume (Gallons), Pump Flow Rate (GPM) &amp; Salt Cell Calculator</h1>
          <p>Stop guessing your pool volume or buying an undersized pump. Enter your pool dimensions, shape, and desired turnover cycle below to calculate your exact <strong>Water Volume (Gallons)</strong>, <strong>Required Pump Flow (GPM)</strong>, <strong>1.5x Salt Cell Capacity</strong>, and <strong>Heater BTU/hr</strong>—paired with instant Amazon equipment matches.</p>
          <div style="display:flex; gap:12px; flex-wrap:wrap;">
            <a class="btn-amazon" href="#calculator">Launch Pool Sizing Calculator &darr;</a>
            <a class="btn-outline" style="color:#ffffff; border-color:#94a3b8;" href="{amazon_search_url('Best Selling Variable Speed Pool Pump Robotic Cleaner')}" target="_blank" rel="nofollow sponsored noopener">Browse Amazon Pool Best Sellers &rarr;</a>
          </div>
        </div>
        <div class="hero-deal-box">
          <h3>🌊 Featured Pool Upgrade</h3>
          <p style="color:#e2e8f0; font-size:0.92rem; margin-bottom:14px;">Energy Star Variable-Speed Pumps, Cordless Wall-Climbing Pool Robots &amp; 45,000-Gal Salt Chlorinators.</p>
          <a class="btn-amazon" style="width:100%;" href="{amazon_search_url('BLACK+DECKER Variable Speed Pool Pump Dolphin Nautilus CC Plus')}" target="_blank" rel="nofollow sponsored noopener">View Live Amazon Discounts &rarr;</a>
        </div>
      </div>
    </section>

    <!-- 4-IN-1 INTERACTIVE POOL & POND CALCULATOR -->
    <section id="calculator" class="grey-section">
      <h2 class="section-title">Interactive 4-in-1 Pool Volume (Gallons), Pump GPM, Salt Cell &amp; Heater Calculator</h2>
      <p class="section-sub">Click a quick pool preset or enter your exact dimensions below. Our hydraulic engine calculates total gallons, turnover flow rate (with 20% friction head safety buffer), recommended salt cell capacity, and heater BTU sizing.</p>

      <div class="preset-row">
        <button type="button" class="preset-btn" onclick="setPoolPreset(7.48, 30, 15, 5.0, 8, 73)">🏊 15&times;30 Inground Pool (~16,800 Gal)</button>
        <button type="button" class="preset-btn" onclick="setPoolPreset(7.48, 36, 18, 5.5, 8, 73)">🏖️ 18&times;36 Large Family Pool (~26,600 Gal)</button>
        <button type="button" class="preset-btn" onclick="setPoolPreset(5.9, 24, 24, 4.0, 8, 45)">⭕ 24-Ft Round Above-Ground (~13,600 Gal)</button>
        <button type="button" class="preset-btn" onclick="setPoolPreset(6.7, 32, 16, 5.0, 8, 73)">🏝️ 16&times;32 Freeform Lagoon (~17,100 Gal)</button>
        <button type="button" class="preset-btn" onclick="setPoolPreset(7.48, 14, 10, 3.0, 2, 45)">🐟 10&times;14 Koi Pond (~3,100 Gal)</button>
      </div>

      <div class="calc-grid">
        <div class="calc-panel">
          <div class="form-group">
            <label for="plShape">1. Pool or Pond Shape Multiplier:</label>
            <select id="plShape" onchange="calculatePool()">
              <option value="7.48" selected>Rectangular / Square Pool (Length &times; Width &times; Depth &times; 7.48)</option>
              <option value="5.9">Round or Oval Pool (Length &times; Width &times; Depth &times; 5.9)</option>
              <option value="6.7">Kidney / Freeform Lagoon Pool (Length &times; Width &times; Depth &times; 6.7)</option>
            </select>
          </div>
          <div class="form-row">
            <div class="form-group">
              <label for="plLength">2. Pool Length (Feet):</label>
              <input type="number" id="plLength" value="32" min="4" max="150" oninput="calculatePool()" />
            </div>
            <div class="form-group">
              <label for="plWidth">3. Pool Width / Diameter (Feet):</label>
              <input type="number" id="plWidth" value="16" min="4" max="100" oninput="calculatePool()" />
            </div>
          </div>
          <div class="form-row">
            <div class="form-group">
              <label for="plDepth">4. Average Water Depth (Feet):</label>
              <input type="number" id="plDepth" value="5.0" min="1" max="15" step="0.5" oninput="calculatePool()" />
            </div>
            <div class="form-group">
              <label for="plTurnover">5. Desired Turnover Cycle (Hours):</label>
              <select id="plTurnover" onchange="calculatePool()">
                <option value="6">6 Hours (Heavy Swimmer Load / Hot Climate)</option>
                <option value="8" selected>8 Hours (Industry Standard Pool Turnover)</option>
                <option value="10">10 Hours (Low-RPM Variable-Speed Extended Run)</option>
                <option value="2">2 Hours (Koi Pond / Spa High-Rate Filtration)</option>
              </select>
            </div>
          </div>
          <div class="form-group">
            <label for="plPipe">6. Existing PVC Plumbing Pipe Size:</label>
            <select id="plPipe" onchange="calculatePool()">
              <option value="45">1.5-Inch Schedule 40 PVC (Max Safe Velocity ~45 GPM)</option>
              <option value="73" selected>2.0-Inch Schedule 40 PVC (Max Safe Velocity ~73 GPM)</option>
              <option value="115">2.5-Inch Schedule 40 PVC (Max Safe Velocity ~115 GPM)</option>
            </select>
          </div>
        </div>

        <div class="calc-panel">
          <h3 style="margin-bottom:12px; color:#0f172a;">Your Calculated Pool &amp; Equipment Specs</h3>
          <div class="metrics-grid">
            <div class="metric-card">
              <div class="val" id="outGallons">19,150 Gal</div>
              <div class="lbl">Total Pool Water Volume</div>
            </div>
            <div class="metric-card">
              <div class="val" id="outGPM">48 GPM</div>
              <div class="lbl">Required Pump Design Flow</div>
            </div>
            <div class="metric-card">
              <div class="val" id="outSalt">35,000 Gal</div>
              <div class="lbl">1.7x Salt Chlorinator Rating</div>
            </div>
            <div class="metric-card">
              <div class="val" id="outHeater">130,000 BTU</div>
              <div class="lbl">Recommended Heat Pump Size</div>
            </div>
          </div>

          <div id="dynamicPoolRec" class="rec-box">
            <!-- Dynamically populated by JS -->
          </div>
        </div>
      </div>
    </section>

    <!-- PRODUCT SEARCH & FILTER -->
    <section id="search-section" class="grey-section">
      <h2 class="section-title">Search Amazon Pool Pumps, Robotic Cleaners, Filters &amp; Salt Systems</h2>
      <p class="section-sub">Filter our verified flagship equipment and daily review archive by keyword or category, or search directly on Amazon.</p>
      <div class="search-bar">
        <input type="text" id="poolSearchInput" class="search-input" placeholder="Search by GPM, Gallons, Hayward, Pentair, Dolphin, AIPER, Saltwater, Sand Filter..." oninput="filterPoolCatalog()" />
        <select id="poolCatSelect" class="filter-select" onchange="filterPoolCatalog()">
          <option value="ALL">All Pool &amp; Pond Categories</option>
          <option value="Variable-Speed Pool Pump">Variable-Speed Pool Pumps</option>
          <option value="Robotic Pool Cleaner">Robotic Pool Cleaners &amp; Skimmers</option>
          <option value="Pool Filter System">Sand &amp; Cartridge Pool Filters</option>
          <option value="Saltwater Chlorinator">Saltwater Chlorine Generators</option>
          <option value="Pool Heater & Heat Pump">Pool Heat Pumps &amp; Heaters</option>
        </select>
        <button type="button" class="btn-amazon" onclick="searchPoolAmazonDirect()">Search Live on Amazon &rarr;</button>
      </div>
      <p id="poolFilterStatus" style="font-size:0.88rem; font-weight:700; color:#334155;">Showing all 10 top-rated pool &amp; pond systems below:</p>
    </section>

    <!-- BEST SELLERS -->
    <section id="bestsellers" class="grey-section">
      <h2 class="section-title">Best-Selling Pool Pumps, Robotic Vacuums, Filters &amp; Salt Chlorinators</h2>
      <p class="section-sub">Ranked by Energy Star hydraulic efficiency, corrosion resistance, and verified pool owner ratings on Amazon.</p>
      <div id="poolBestSellersGrid" class="product-grid">
        {bestsellers_cards}
      </div>
    </section>

    <!-- SIDE-BY-SIDE COMPARISON TABLE -->
    <section id="comparison" class="grey-section">
      <h2 class="section-title">Side-by-Side Pool Equipment Comparison Matrix</h2>
      <p class="section-sub">Compare maximum pool gallon capacity, GPM flow rate, motor/filter specs, and efficiency ratings across leading models.</p>
      <div class="table-wrap">
        <table class="comp-table">
          <thead>
            <tr>
              <th>Equipment Model</th>
              <th>Category</th>
              <th>Max Pool Size</th>
              <th>GPM / Output</th>
              <th>Hardware Spec</th>
              <th>Key Advantage</th>
              <th>Rating</th>
              <th>Amazon Deal</th>
            </tr>
          </thead>
          <tbody>
            {comparison_rows}
          </tbody>
        </table>
      </div>
    </section>

    <!-- DAILY AUTOMATED PRODUCT REVIEWS -->
    <section id="daily-reviews" class="grey-section">
      <h2 class="section-title">Daily Automated Pool Equipment Reviews &amp; Hydraulic Sizing Guides</h2>
      <p class="section-sub">Our automated GitHub Actions pipeline publishes <strong>3 brand-new pool &amp; pond equipment reviews every single day</strong>. Browse the latest reviews below (Total live articles: <strong>{len(all_articles)}</strong>):</p>
      <div id="dailyPoolReviewsGrid" class="articles-grid">
        {daily_cards}
      </div>
    </section>

    <!-- FAQ SECTION -->
    <section id="faq" class="grey-section">
      <h2 class="section-title">Frequently Asked Questions (Pool Gallons, Pump GPM &amp; Salt Sizing)</h2>
      <p class="section-sub">Essential hydraulic formulas and sizing rules for inground pools, above-ground pools, and koi ponds.</p>
      {faq_html}
    </section>

    <!-- ON-PAGE SITE MAP DIRECTORY -->
    <section id="sitemap-section" class="grey-section">
      <h2 class="section-title">Site Map &amp; Complete Content Directory</h2>
      <p class="section-sub">Direct navigation for visitors and search engine crawlers across all calculators, feeds, and daily review archives.</p>
      <div class="sitemap-columns">
        <div class="sitemap-box">
          <h3>Main Tools &amp; XML Feeds</h3>
          <ul>
            <li><a href="#calculator">4-in-1 Pool Gallons, GPM, Salt Cell &amp; Heater Calculator</a></li>
            <li><a href="#bestsellers">Top 10 Best-Selling Pool Equipment Systems</a></li>
            <li><a href="#comparison">Side-by-Side Comparison Matrix</a></li>
            <li><a href="{BASE_URL}/sitemap.html"><strong>Full HTML Site Map Page (All {len(all_articles)} Reviews)</strong></a></li>
            <li><a href="{BASE_URL}/sitemap.xml">Google/Bing XML Sitemap (sitemap.xml)</a></li>
            <li><a href="{BASE_URL}/feed.xml">RSS 2.0 Syndication Feed (feed.xml)</a></li>
          </ul>
        </div>
        <div class="sitemap-box">
          <h3>Latest Daily Pool Review Archive Links</h3>
          <ul>
            {sitemap_preview_links}
          </ul>
        </div>
      </div>
    </section>

  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-links">
        <a href="#calculator">Pool Calculator</a>
        <a href="#search-section">Product Search</a>
        <a href="#bestsellers">Best Sellers</a>
        <a href="#comparison">Comparison Table</a>
        <a href="#daily-reviews">Daily Reviews</a>
        <a href="#faq">FAQ</a>
        <a href="{BASE_URL}/sitemap.html">HTML Site Map</a>
        <a href="{BASE_URL}/sitemap.xml">XML Sitemap</a>
        <a href="{BASE_URL}/feed.xml">RSS Feed</a>
      </div>
      <p style="margin-bottom:8px;"><strong>Amazon Affiliate Disclosure:</strong> AquaFlowCalc participates in the Amazon Services LLC Associates Program (Affiliate StoreID: <code>{AFFILIATE_TAG}</code>), an affiliate advertising program designed to provide a means for sites to earn advertising fees by linking to Amazon.com.</p>
      <p>&copy; {datetime.datetime.now(datetime.timezone.utc).year} AquaFlowCalc. Powered by zero-maintenance GitHub Actions automation.</p>
    </div>
  </footer>

  <script>
    var POOL_PRODUCTS = {js_products};
    var AFFILIATE_TAG = "{AFFILIATE_TAG}";

    function setPoolPreset(shape, len, wid, depth, turnover, pipe) {{
      document.getElementById('plShape').value = shape.toString();
      document.getElementById('plLength').value = len;
      document.getElementById('plWidth').value = wid;
      document.getElementById('plDepth').value = depth;
      document.getElementById('plTurnover').value = turnover.toString();
      document.getElementById('plPipe').value = pipe.toString();
      calculatePool();
    }}

    function calculatePool() {{
      var shapeMult = parseFloat(document.getElementById('plShape').value) || 7.48;
      var len = parseFloat(document.getElementById('plLength').value) || 30;
      var wid = parseFloat(document.getElementById('plWidth').value) || 15;
      var depth = parseFloat(document.getElementById('plDepth').value) || 5.0;
      var turnoverHrs = parseFloat(document.getElementById('plTurnover').value) || 8;
      var maxPipeGpm = parseFloat(document.getElementById('plPipe').value) || 73;

      var surfaceSqFt = Math.round(len * wid);
      var gallons = Math.round((len * wid * depth * shapeMult) / 100) * 100;
      if (gallons < 500) gallons = 500;

      // Required GPM with 20% dynamic friction head safety buffer
      var baseGpm = gallons / (turnoverHrs * 60);
      var designGpm = Math.ceil(baseGpm * 1.2);

      // 1.7x Saltwater Chlorinator Cell Oversizing Rule
      var rawSalt = Math.ceil((gallons * 1.7) / 5000) * 5000;
      if (rawSalt < 15000) rawSalt = 15000;

      // Pool Heater / Heat Pump BTU (260 BTU per sq ft surface area)
      var heaterBtu = Math.ceil((surfaceSqFt * 260) / 10000) * 10000;
      if (heaterBtu < 50000) heaterBtu = 50000;

      document.getElementById('outGallons').textContent = gallons.toLocaleString() + ' Gal';
      document.getElementById('outGPM').textContent = designGpm + ' GPM';
      document.getElementById('outSalt').textContent = rawSalt.toLocaleString() + ' Gal Cell';
      document.getElementById('outHeater').textContent = heaterBtu.toLocaleString() + ' BTU/hr';

      var pipeNote = designGpm > maxPipeGpm
        ? ' (Note: ' + designGpm + ' GPM exceeds single-line ' + maxPipeGpm + ' GPM pipe limit — use a Variable-Speed Pump on a longer 10-hr cycle)'
        : ' (Fits safely within your ' + maxPipeGpm + ' GPM PVC plumbing rating)';

      // Match best pump from catalog
      var pumps = POOL_PRODUCTS.filter(function(p) {{
        return p.category.indexOf('Pump') !== -1 || p.category.indexOf('Filter') !== -1;
      }}).sort(function(a, b) {{ return a.max_gallons - b.max_gallons; }});

      var bestMatch = pumps.find(function(p) {{ return p.max_gallons >= gallons && p.gpm_num >= designGpm; }}) || pumps[0];

      var pumpSearchUrl = 'https://www.amazon.com/s?k=' + encodeURIComponent('Variable Speed Pool Pump ' + gallons + ' Gallon Pool') + '&tag=' + AFFILIATE_TAG;
      var robotSearchUrl = 'https://www.amazon.com/s?k=' + encodeURIComponent('Robotic Pool Vacuum Cleaner Inground ' + len + ' ft') + '&tag=' + AFFILIATE_TAG;
      var saltSearchUrl = 'https://www.amazon.com/s?k=' + encodeURIComponent(rawSalt + ' Gallon Saltwater Chlorine Generator Pool') + '&tag=' + AFFILIATE_TAG;

      var html = '<h4>✅ Recommended Hardware Match for Your ' + gallons.toLocaleString() + '-Gallon Pool:</h4>' +
        '<p style="font-size:0.9rem; color:#334155; margin-bottom:10px;"><strong>Primary Match:</strong> ' + bestMatch.name + ' (' + bestMatch.gpm_or_cap + ') — ' + bestMatch.highlight + pipeNote + '</p>' +
        '<div style="display:flex; gap:8px; flex-wrap:wrap;">' +
        '<a class="btn-amazon" href="' + bestMatch.url + '" target="_blank" rel="nofollow sponsored noopener">Check ' + bestMatch.name + ' on Amazon &rarr;</a>' +
        '<a class="btn-outline" href="' + pumpSearchUrl + '" target="_blank" rel="nofollow sponsored noopener">Shop Variable-Speed Pumps</a>' +
        '<a class="btn-outline" href="' + robotSearchUrl + '" target="_blank" rel="nofollow sponsored noopener">Shop Robotic Pool Cleaners</a>' +
        '<a class="btn-outline" href="' + saltSearchUrl + '" target="_blank" rel="nofollow sponsored noopener">Shop ' + rawSalt.toLocaleString() + '-Gal Salt Systems</a>' +
        '</div>';

      document.getElementById('dynamicPoolRec').innerHTML = html;
    }}

    function filterPoolCatalog() {{
      var q = (document.getElementById('poolSearchInput').value || '').toLowerCase().trim();
      var cat = document.getElementById('poolCatSelect').value;
      var cards = document.querySelectorAll('#poolBestSellersGrid .product-card');
      var shown = 0;

      cards.forEach(function(c) {{
        var s = c.getAttribute('data-search') || '';
        var cCat = c.getAttribute('data-category') || '';
        var okQ = !q || s.indexOf(q) !== -1;
        var okC = (cat === 'ALL') || (cCat === cat);
        if (okQ && okC) {{
          c.style.display = 'flex';
          shown++;
        }} else {{
          c.style.display = 'none';
        }}
      }});

      var artCards = document.querySelectorAll('#dailyPoolReviewsGrid .article-card');
      artCards.forEach(function(ac) {{
        var aSearch = ac.getAttribute('data-art-search') || '';
        ac.style.display = (!q || aSearch.indexOf(q) !== -1) ? 'flex' : 'none';
      }});

      document.getElementById('poolFilterStatus').textContent =
        'Showing ' + shown + ' matching flagship system(s) (and filtered daily review articles below):';
    }}

    function searchPoolAmazonDirect() {{
      var q = document.getElementById('poolSearchInput').value.trim() || 'Variable Speed Pool Pump Robotic Pool Cleaner Saltwater Chlorinator';
      window.open('https://www.amazon.com/s?k=' + encodeURIComponent(q) + '&tag=' + AFFILIATE_TAG, '_blank');
    }}

    calculatePool();
  </script>
</body>
</html>"""


def generate_sitemaps_and_feeds(all_articles: list[dict]) -> list[str]:
    """Menghasilkan sitemap.xml, sitemap.html, robots.txt, feed.xml, dan file kunci IndexNow."""
    today_iso = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    urls = [f"{BASE_URL}/index.html", f"{BASE_URL}/sitemap.html"]

    sitemap_entries = f"""  <url>
    <loc>{BASE_URL}/index.html</loc>
    <lastmod>{today_iso}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>{BASE_URL}/sitemap.html</loc>
    <lastmod>{today_iso}</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>\n"""

    for art in all_articles:
        u = f"{BASE_URL}/reviews/{art['slug']}.html"
        urls.append(u)
        sitemap_entries += f"""  <url>
    <loc>{u}</loc>
    <lastmod>{art['date']}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>\n"""

    sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{sitemap_entries}</urlset>"""

    with open(os.path.join(OUTPUT_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap_xml)

    # Build HTML Site Map Page (sitemap.html)
    html_sitemap = build_html_sitemap_page(all_articles)
    with open(os.path.join(OUTPUT_DIR, "sitemap.html"), "w", encoding="utf-8") as f:
        f.write(html_sitemap)

    # robots.txt
    robots_txt = f"""User-agent: *
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
"""
    with open(os.path.join(OUTPUT_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots_txt)

    # RSS 2.0 Feed (feed.xml)
    rss_items = ""
    for art in all_articles[:30]:
        u = f"{BASE_URL}/reviews/{art['slug']}.html"
        rss_items += f"""    <item>
      <title><![CDATA[{art['title']}]]></title>
      <link>{u}</link>
      <guid>{u}</guid>
      <pubDate>{art['date']}T05:00:00Z</pubDate>
      <description><![CDATA[Hydraulic flow test and sizing review of the {art['brand']} {art['model_name']} (rated up to {art['max_gal']:,} gallons at {art['flow_gpm']} GPM) for {art['app_title']}.]]></description>
    </item>\n"""

    rss_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>AquaFlowCalc — Daily Pool Pump, Filter, Robot &amp; Salt System Reviews</title>
    <link>{BASE_URL}/index.html</link>
    <description>Automated daily pool equipment reviews and hydraulic sizing calculators for variable-speed pumps, filters, salt chlorinators, and robotic cleaners.</description>
    <language>en-us</language>
{rss_items}  </channel>
</rss>"""

    with open(os.path.join(OUTPUT_DIR, "feed.xml"), "w", encoding="utf-8") as f:
        f.write(rss_xml)

    # IndexNow verification key file
    with open(os.path.join(OUTPUT_DIR, f"{INDEXNOW_KEY}.txt"), "w", encoding="utf-8") as f:
        f.write(INDEXNOW_KEY)

    return urls


def ping_indexnow(newly_added: list[dict]):
    """Mengirimkan ping otomatis ke IndexNow API agar mesin pencari langsung mengindeks 3 artikel baru setiap hari."""
    host = urllib.parse.urlparse(BASE_URL).netloc
    url_list = [
        f"{BASE_URL}/index.html",
        f"{BASE_URL}/sitemap.html",
        f"{BASE_URL}/sitemap.xml"
    ]
    for art in newly_added:
        url_list.append(f"{BASE_URL}/reviews/{art['slug']}.html")

    payload = json.dumps({
        "host": host,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE_URL}/{INDEXNOW_KEY}.txt",
        "urlList": url_list
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://api.indexnow.org/indexnow",
        data=payload,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"[IndexNow] Pinged {len(url_list)} URLs successfully (HTTP {resp.status})")
    except Exception as exc:
        print(f"[IndexNow] Notice (non-blocking): {exc}")


def main():
    os.makedirs(REVIEWS_DIR, exist_ok=True)
    all_articles, newly_added = load_and_advance_state()

    # 1. Build Homepage
    index_html = build_index_page(all_articles)
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)

    # 2. Build Individual Review Pages
    for art in all_articles:
        page_html = build_article_page(art, all_articles)
        out_path = os.path.join(REVIEWS_DIR, f"{art['slug']}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(page_html)

    # 3. Build XML Sitemap, HTML Site Map, Robots.txt, RSS Feed & Ping IndexNow
    generate_sitemaps_and_feeds(all_articles)
    ping_indexnow(newly_added)

    print(f"AquaFlowCalc build complete! Total articles live: {len(all_articles)} (+{len(newly_added)} added today).")


if __name__ == "__main__":
    main()
