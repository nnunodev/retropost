# retropost

## Description

This script generates content using an AI model and scrapes news from a specified URL.

## Requirements

- Python 3.8+
- Install dependencies using `pip install -r requirements.txt`

## Environment Variables

Create a `.env` file with the following variables:

- `MISTRAL_KEY`: API key for the Mistral AI model
- `BSKY_HANDLE`: BlueSky handle
- `BSKY_PASSWORD`: BlueSky password

## Usage

```bash
python main.py --prompt "Your prompt here"
