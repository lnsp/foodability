#!/usr/bin/env python
# coding: utf-8

# # Feature Selection

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("en.openfoodfacts.org.products.csv", sep='\t')

# SPECIFY SUPERMARKETS
df["stores"] = df["stores"].str.lower().str.strip()
df = df[df["brands_tags"].isin(["lidl", "rewe", "aldi", "netto"])]


# In[5]:


head = df.sample(100)


# In[6]:


df[df["brands_tags"] == "aldi"]


# In[7]:


cols = ["code", "product_name", "quantity", "packaging", "packaging_text", "packaging_tags", "brands", 
        "categories_tags", "categories_en", "origins_en", "labels_en", "stores", "serving_size", "image_url"]


# # Feature Engineering

# In[8]:


# In[87]:


PLASTIC_TAGS = ["plastic", "plastique", "plastico", "kunststoff", "pet", "pp", "foil", "plastik"]
plastic = df["packaging_tags"].map(lambda x: any([tag in str(x).lower().split(",") for tag in PLASTIC_TAGS]))


# In[88]:


CARTON_TAGS = ["paper", "papier", "carton", "card", "karton", "tetra", "papel"]
carton = df["packaging_tags"].map(lambda x: any([tag in str(x).lower().split(",") for tag in CARTON_TAGS]))


# In[89]:


GLASS_TAGS = ["glass", "glas"]
glass = df["packaging_tags"].map(lambda x: any([tag in str(x).lower().split(",") for tag in GLASS_TAGS]))


# In[90]:


METAL_TAGS = ["metalique", "aluminium", "metal"]
metal = df["packaging_tags"].map(lambda x: any([tag in str(x).lower().split(",") for tag in METAL_TAGS]))

# ## Approximate area of packaging based on volumne

# In[14]:


from quantulum3 import parser


# In[65]:


quants = parser.parse('130 ml')
quants


# In[80]:


def get_weight(s):
    if len(s) == 0:
        return float("nan")
    quants = parser.parse(str(s))
    if len(quants) == 0:
        return float("nan")
    quant = quants[0]
    unit = quant.unit.name
    if quant.value < 0:
        return float("nan")
    if unit == "gram":
        return float(quant.value)
    if unit == "litre":
        return float(quant.value) * 1000
    if unit == "centilitre":
        return float(quant.value) * 100
    if unit == "kilogram":
        return float(quant.value) * 1000
    if unit == "ounce":
        return float(quant.value) * 28.35
    if unit == "pound-mass":
        return float(quant.value) * 453.592
    if unit == "gallon":
        return float(quant.value) * 3.78541 * 1000
    if unit == "cubic centimetre":
        return float(quant.value)
    return float("nan")


# For the sake of simplicity, we assume that the volume is equal to the weight (i.e. 750 g = 0.75l). Weights are given in gramms. Packaging area is given square cm.

# In[69]:


weight = df["quantity"].fillna("").map(lambda x: get_weight(x))

print("Finished weight computation")

# In[81]:


weight[weight > 50*1000] = float("nan")
weight[weight < 0] = float("nan")


# In[82]:


packaging_area = weight.map(lambda x: (((x/1000.0)**(1./3.))**2) * 6)


# In[85]:


packaging_area.max()


# In[86]:


df["weight"] = weight
cols.append("weight")
df["packaging area"] = packaging_area
cols.append("packaging area")


# In[92]:


df["materials"] = df["weight"].map(lambda x: [])


# In[94]:


df["glass"] = glass
df["carton"] = carton
df["metal"] = metal
df["plastic"] = plastic

def get_materials(row):
    l = []
    if row["glass"]:
        l.append("glass")
    if row["carton"]:
        l.append("carton")
    if row["metal"]:
        l.append("metal")
    if row["plastic"]:
        l.append("plastic")
    return ",".join(l)

df["materials"] = df.apply(lambda x: get_materials(x), axis=1)
print(df["materials"].unique())
print("Finished materials")

cols += ["materials"]


# In[101]:


df[cols]


# # Export data

# In[102]:


df[cols].to_csv("min_food_data.csv")

