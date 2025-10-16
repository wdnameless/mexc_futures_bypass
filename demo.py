"""
MEXC Futures Bypass - Demo

This demo shows how to use the MEXC Futures Bypass methods.
Replace 'your_web_token_here' with your actual MEXC WEB token.
"""

import asyncio
import httpx
import time
from typing import Dict, Optional

class MEXCWebAuth:
    """WEB Token Authentication"""
    
    def __init__(self, web_token: str):
        self.web_token = web_token
        self.base_url = "https://contract.mexc.com"
    
    def get_headers(self):
        """Get authentication headers"""
        return {
            'Authorization': f'Bearer {self.web_token}',
            'Content-Type': 'application/json',
            'User-Agent': 'MEXC-Web-Trader/1.0'
        }
    
    async def make_request(self, method: str, endpoint: str, data: dict = None):
        """Make authenticated request"""
        headers = self.get_headers()
        async with httpx.AsyncClient() as client:
            response = await client.request(
                method, f"{self.base_url}{endpoint}",
                headers=headers, json=data
            )
            return response.json()

class FastMarketOrders:
    """Fast market order execution"""
    
    def __init__(self, auth: MEXCWebAuth):
        self.auth = auth
    
    async def place_market_order(self, symbol: str, side: str, size: float):
        """Place market order with maximum speed"""
        data = {
            "symbol": symbol,
            "side": side,
            "type": "MARKET",
            "quantity": str(size),
            "leverage": "20"
        }
        
        start_time = time.time()
        result = await self.auth.make_request(
            "POST", "/api/v1/private/order/submit", data
        )
        execution_time = time.time() - start_time
        
        print(f"Order executed in {execution_time:.3f}s")
        return result

class ArbitrageDetector:
    """Arbitrage opportunity detection"""
    
    def __init__(self, auth: MEXCWebAuth):
        self.auth = auth
        self.dex_url = "https://api.dexscreener.com/latest/dex"
    
    async def get_price_difference(self, token: str):
        """Calculate price difference between MEXC and DEX"""
        try:
            # Get MEXC price
            mexc_data = await self.auth.make_request(
                "GET", f"/api/v1/private/contract/ticker?symbol={token}_USDT"
            )
            mexc_price = float(mexc_data['data']['lastPrice'])
            
            # Get DEX price
            async with httpx.AsyncClient() as client:
                dex_response = await client.get(f"{self.dex_url}/tokens/{token}")
                dex_data = dex_response.json()
                if dex_data['pairs']:
                    dex_price = float(dex_data['pairs'][0]['priceUsd'])
                else:
                    return None
            
            # Calculate difference
            difference = abs(mexc_price - dex_price) / mexc_price * 100
            
            return {
                'token': token,
                'mexc_price': mexc_price,
                'dex_price': dex_price,
                'difference_pct': difference,
                'arbitrage_opportunity': difference > 0.5
            }
        except Exception as e:
            print(f"Error getting price difference for {token}: {e}")
            return None

async def demo_basic_trading():
    """Basic trading demo"""
    print("=== Basic Trading Demo ===")
    
    # Initialize (replace with your actual token)
    auth = MEXCWebAuth("your_web_token_here")
    trader = FastMarketOrders(auth)
    
    # Place a market order
    try:
        result = await trader.place_market_order("BTC_USDT", "BUY", 0.001)
        print(f"Order result: {result}")
    except Exception as e:
        print(f"Error: {e}")

async def demo_arbitrage_detection():
    """Arbitrage detection demo"""
    print("=== Arbitrage Detection Demo ===")
    
    auth = MEXCWebAuth("your_web_token_here")
    arbitrage = ArbitrageDetector(auth)
    
    # Check for arbitrage opportunities
    tokens = ["BTC", "ETH", "BNB"]
    
    for token in tokens:
        opportunity = await arbitrage.get_price_difference(token)
        if opportunity and opportunity['arbitrage_opportunity']:
            print(f"Arbitrage found for {token}: {opportunity['difference_pct']:.2f}%")
        else:
            print(f"No arbitrage for {token}")

async def main():
    """Main demo function"""
    print("MEXC Futures Bypass - Demo")
    print("=" * 40)
    
    print("Note: Replace 'your_web_token_here' with your actual MEXC WEB token")
    print()
    
    # Run demos
    await demo_basic_trading()
    print()
    
    await demo_arbitrage_detection()
    print()
    
    print("Demo completed!")
    print("\nFor full functionality, purchase the complete methods collection.")
    print("Contact: @shitmane")

if __name__ == "__main__":
    asyncio.run(main())