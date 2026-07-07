# Nimbus - Database Design

## Why Database Design Matters

Before building APIs, we need to decide what data the system stores and how different pieces of data connect.

## Main Tables

### 1. users

Stores people who can log in to Nimbus.

Fields:
- id
- full_name
- email
- password_hash
- role
- created_at

### 2. products

Stores retail products.

Fields:
- id
- name
- category
- unit_price
- is_active
- created_at

### 3. inventory

Stores current stock levels for each product.

Fields:
- id
- product_id
- current_stock
- minimum_stock
- updated_at

### 4. sales

Stores sales transactions.

Fields:
- id
- product_id
- quantity_sold
- sale_date
- total_amount
- created_at

### 5. forecasts

Stores demand prediction results.

Fields:
- id
- product_id
- forecast_date
- predicted_demand
- confidence_score
- created_at

## Relationships

- One user can create many records later.
- One product has one inventory record.
- One product can have many sales records.
- One product can have many forecast records.

## First Database Version

For version 1, Nimbus will start with:

- products
- inventory
- sales

Users and authentication will come later.