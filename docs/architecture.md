# Nimbus - Architecture

## Project Goal

Build a full-stack software platform that helps small retail/dessert stores manage inventory, track sales, predict demand, and generate restocking suggestions.

## Main Users

1. Store Manager
2. Store Staff
3. Business Owner

## Core Modules

### 1. Product Management
- Add products
- Update product details
- Track product category
- Track unit price

### 2. Inventory Management
- Track current stock
- Track minimum stock level
- Generate low-stock alerts

### 3. Sales Tracking
- Add daily sales
- Track quantity sold
- Track revenue
- View sales history

### 4. Forecasting Engine
- Use historical sales data
- Predict future demand
- Identify high-demand products

### 5. Restocking Engine
- Compare forecasted demand with inventory
- Suggest restocking quantity
- Flag wastage risk

### 6. Dashboard
- Total revenue
- Top-selling products
- Low-stock alerts
- Demand forecast
- Restocking suggestions

## Tech Stack

- Frontend: React
- Backend: FastAPI
- Database: PostgreSQL
- Machine Learning: Python, pandas, scikit-learn
- Containerization: Docker
- Version Control: Git and GitHub

## System Flow

1. User adds products.
2. User updates inventory.
3. User records sales.
4. Forecasting engine analyses historical sales.
5. Restocking engine compares forecast with current stock.
6. Dashboard displays insights.