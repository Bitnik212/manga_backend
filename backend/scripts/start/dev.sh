#!/bin/bash
cd backend
source venv/bin/activate
uvicorn bootstrap:app --reload --host=0.0.0.0
