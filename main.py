from agent.planner import run_agent_loop
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    print("[*] Starting AI Strategy Analyst Agent...")
    run_agent_loop()
